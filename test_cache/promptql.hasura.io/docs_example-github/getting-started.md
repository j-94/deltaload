---
title: Getting Started
description: 
url: https://promptql.hasura.io/docs/example-github
timestamp: 2025-01-20T16:16:03.320Z
domain: promptql.hasura.io
path: docs_example-github
---

# Getting Started



## Content

Getting Started - Hasura PromptQL
===============

[![Image 3: QL Logo](https://promptql.hasura.io/ql-logo-dark.svg)](https://promptql.hasura.io/)

[Sign Up](https://promptql.console.hasura.io/?pg=promptql_docs&plcmt=header&cta=sign-up)[Docs](https://promptql.hasura.io/docs)

[GitHub](https://github.com/hasura/graphql-engine)

*   [Overview](https://promptql.hasura.io/docs)
*   [Getting started](https://promptql.hasura.io/docs/getting-started)
*   [Deploy and share](https://promptql.hasura.io/docs/deploy-and-share)
*   Notes
    
    *   [100% Accuracy with RAG](https://promptql.hasura.io/docs/notes/rag-hundred-percent-accuracy)
    
*   Guides
    
    *   [Starting from scratch](https://promptql.hasura.io/docs/guides/start-scratch)
    *   [Connect Structured PostgreSQL](https://promptql.hasura.io/docs/guides/connecting-structured-data)
    *   [Connect Structured Snowlfake](https://promptql.hasura.io/docs/guides/connecting-structured-snowflake)
    *   [Connect APIs - Bulk data](https://promptql.hasura.io/docs/guides/connecting-apis-bulk-data)
    *   [Connect APIs directly](https://promptql.hasura.io/docs/guides/connecting-api-endpoints)
    *   [Connect Unstructured Data](https://promptql.hasura.io/docs/guides/connecting-unstructured-data)
    *   [Existing DDN project](https://promptql.hasura.io/docs/guides/existing-project)
    *   [PromptQL Guide](https://promptql.hasura.io/docs/guides/promptql-guide)
    *   [PromptQL Program API](https://promptql.hasura.io/docs/guides/program-api)
    
*   Tutorials
    
    *   [Apple Health Assistant](https://promptql.hasura.io/docs/tutorials/apple-health-assistant)
    *   [Huggingface Datasets](https://promptql.hasura.io/docs/tutorials/huggingface-csv-parquet-sqlite)
    *   [Kaggle Datasets](https://promptql.hasura.io/docs/tutorials/kaggle-csv-sqlite)
    *   [DuckDuckGo Web Search](https://promptql.hasura.io/docs/tutorials/duckduckgo-web-search)
    *   [Realtime Chat with BART API](https://promptql.hasura.io/docs/tutorials/bart-api)
    

On This Page

*   [Setup](https://promptql.hasura.io/docs/example-github#setup)
*   [Install the DDN CLI](https://promptql.hasura.io/docs/example-github#install-the-ddn-cli)
*   [Install Docker](https://promptql.hasura.io/docs/example-github#install-docker)
*   [Log in with the CLI](https://promptql.hasura.io/docs/example-github#log-in-with-the-cli)
*   [Validate the installation](https://promptql.hasura.io/docs/example-github#validate-the-installation)
*   [Build your PromptQL app](https://promptql.hasura.io/docs/example-github#build-your-promptql-app)
*   [Clone the example project](https://promptql.hasura.io/docs/example-github#clone-the-example-project)
*   [Set up your .env file](https://promptql.hasura.io/docs/example-github#set-up-your-env-file)
*   [Set up your GitHub repo](https://promptql.hasura.io/docs/example-github#set-up-your-github-repo)
*   [Setup your DDN project](https://promptql.hasura.io/docs/example-github#setup-your-ddn-project)
*   [Fire up your PromptQL project](https://promptql.hasura.io/docs/example-github#fire-up-your-promptql-project)
*   [Restarting the app](https://promptql.hasura.io/docs/example-github#restarting-the-app)
*   [Act on your data](https://promptql.hasura.io/docs/example-github#act-on-your-data)
*   [Open the PromptQL playground](https://promptql.hasura.io/docs/example-github#open-the-promptql-playground)
*   [Ask questions about your GitHub repo](https://promptql.hasura.io/docs/example-github#ask-questions-about-your-github-repo)

[Question? Give us feedback →](https://github.com/hasura/graphql-engine/issues/new?title=Feedback%20for%20%E2%80%9CGetting%20Started%E2%80%9D&labels=feedback)Scroll to top

[Docs](https://promptql.hasura.io/docs "Docs")Getting started

Getting started
===============

In this getting started guide, you’ll get hands on experience with PromptQL and the GitHub connector. We will be building a “Github Issues” assistant.

You will learn how to:

*   Set up PromptQL to work with a GitHub issues and pull requests.
    *   You will be able to do natural language query to triage feature requests, bugs and other issues with your connected Github repository.
*   Install all required prerequisites.
*   Create and configure the necessary API keys.
*   Run your PromptQL project in a local environment.
*   Ask your questions with PromptQL playground.

Setup[](https://promptql.hasura.io/docs/example-github#setup)
-------------------------------------------------------------

### Install the DDN CLI[](https://promptql.hasura.io/docs/example-github#install-the-ddn-cli)

MacOS or LinuxWindows

`bash copy curl -L https://graphql-engine-cdn.hasura.io/ddn/cli/v4/get.sh | bash `

*   Download the latest
    
    [DDN CLI installer for Windows.](https://graphql-engine-cdn.hasura.io/ddn/cli/v4/latest/DDN_CLI_Setup.exe)
  
*   Run the `DDN_CLI_Setup.exe` installer file and follow the instructions. This will only take a minute.
*   The DDN CLI is added to your `%PATH%` environment variable so that you can use the `ddn` command from your terminal.
    

### Install Docker[](https://promptql.hasura.io/docs/example-github#install-docker)

Follow the instructions on the [Docker website](https://docs.docker.com/engine/install/) to install Docker on your machine.

### Log in with the CLI[](https://promptql.hasura.io/docs/example-github#log-in-with-the-cli)

Logging in allows you to connect to the PromptQL runtime which is necessary for development. It also allows you to deploy your project to Hasura DDN.

```
ddn auth login
```

You will be redirected to DDN signup/login page.

### Validate the installation[](https://promptql.hasura.io/docs/example-github#validate-the-installation)

You can verify that the DDN CLI is installed correctly by running:

```
ddn doctor
```

Build your PromptQL app[](https://promptql.hasura.io/docs/example-github#build-your-promptql-app)
-------------------------------------------------------------------------------------------------

### Clone the example project[](https://promptql.hasura.io/docs/example-github#clone-the-example-project)

The [example project](https://github.com/hasura/example-promptql-github) is already set up to connect PromptQL to any GitHub repo.

```
git clone git@github.com:hasura/example-promptql-github.git
cd example-promptql-github
```

### Set up your .env file[](https://promptql.hasura.io/docs/example-github#set-up-your-env-file)

Set up your .env file with your GitHub API token.

```
cp .env.example .env
```

**Add GitHub API token to .env**

For the Github integration. Create an API token from [https://github.com/settings/tokens](https://github.com/settings/tokens)

```
# .env
 
...
GITHUB_API_TOKEN=<GITHUB_API_TOKEN>
```

This token only needs read access to the repo you are interested in.

![Image 4: Example: PromptQL on GitHub](https://promptql.hasura.io/_next/image?url=%2Fgithub-permissions-dark.png&w=2048&q=75)

### Set up your GitHub repo[](https://promptql.hasura.io/docs/example-github#set-up-your-github-repo)

Head to `app/connector/github/index.ts` and change the org name and the repo name to something you’d like:

```
// index.ts
 
...
  const manager = new GitHubIssueSyncManager('<org-name>', '<repo-name>');
  if (!process.env.GITHUB_API_TOKEN) {
...
```

### Setup your DDN project[](https://promptql.hasura.io/docs/example-github#setup-your-ddn-project)

This will create a Hasura DDN cloud project and set up PromptQL keys to connect to the PromptQL runtime.

```
ddn project init
```

### Fire up your PromptQL project[](https://promptql.hasura.io/docs/example-github#fire-up-your-promptql-project)

Build your supergraph.

```
ddn supergraph build local
```

Then bring up the PromptQL API server, the engine and the connector

```
ddn run docker-start
```

You’ll notice in amongst your Docker logs that your github synchronization has started.

Docker logs

\[2024-01-01 12:00:01\] Starting GitHub sync…  
\[2024-01-01 12:00:02\] Fetching repository metadata…

  
\[2024-01-01 12:00:03\] Syncing issues and pull requests…

  
\[2024-01-01 12:00:04\] Loading repository contents…

  
\[2024-01-01 12:00:05\] GitHub sync complete

If the specified repo has many issues or comments it may take some time to get them all and you may be rate limited. That’s ok, you can go ahead and try PromptQL without the process having fully finished yet.

If you notice some logs regarding GitHub permissions, check that your GitHub API token has the correct permissions for the repo you’re trying to access.

### Restarting the app[](https://promptql.hasura.io/docs/example-github#restarting-the-app)

If you made a mis-step or want to start from scratch, simply restarting the docker containers will reset all state including any loaded data.

```
ddn run docker-start
```

Act on your data[](https://promptql.hasura.io/docs/example-github#act-on-your-data)
-----------------------------------------------------------------------------------

### Open the PromptQL playground[](https://promptql.hasura.io/docs/example-github#open-the-promptql-playground)

In another terminal, run

```
ddn console --local
```

Browser support: PromptQL playground is supported on all browsers except Firefox and Safari. Support for these browsers should be available shortly.

### Ask questions about your GitHub repo[](https://promptql.hasura.io/docs/example-github#ask-questions-about-your-github-repo)

The console is a web app hosted at console.hasura.io that connects to your local PromptQL API and data sources. Your data is processed in the DDN PromptQL runtime but isn’t persisted externally.

Head over to the console and ask a few questions about your GitHub repo.

```
> What are the open pull requests?
> What kind of questions can I ask?
```

[Overview](https://promptql.hasura.io/docs "Overview")[Deploy and share](https://promptql.hasura.io/docs/deploy-and-share "Deploy and share")

## Metadata

```json
{
  "title": "Getting Started",
  "description": "",
  "url": "https://promptql.hasura.io/docs/example-github",
  "content": "Getting Started - Hasura PromptQL\n===============\n\n[![Image 3: QL Logo](https://promptql.hasura.io/ql-logo-dark.svg)](https://promptql.hasura.io/)\n\n[Sign Up](https://promptql.console.hasura.io/?pg=promptql_docs&plcmt=header&cta=sign-up)[Docs](https://promptql.hasura.io/docs)\n\n[GitHub](https://github.com/hasura/graphql-engine)\n\n*   [Overview](https://promptql.hasura.io/docs)\n*   [Getting started](https://promptql.hasura.io/docs/getting-started)\n*   [Deploy and share](https://promptql.hasura.io/docs/deploy-and-share)\n*   Notes\n    \n    *   [100% Accuracy with RAG](https://promptql.hasura.io/docs/notes/rag-hundred-percent-accuracy)\n    \n*   Guides\n    \n    *   [Starting from scratch](https://promptql.hasura.io/docs/guides/start-scratch)\n    *   [Connect Structured PostgreSQL](https://promptql.hasura.io/docs/guides/connecting-structured-data)\n    *   [Connect Structured Snowlfake](https://promptql.hasura.io/docs/guides/connecting-structured-snowflake)\n    *   [Connect APIs - Bulk data](https://promptql.hasura.io/docs/guides/connecting-apis-bulk-data)\n    *   [Connect APIs directly](https://promptql.hasura.io/docs/guides/connecting-api-endpoints)\n    *   [Connect Unstructured Data](https://promptql.hasura.io/docs/guides/connecting-unstructured-data)\n    *   [Existing DDN project](https://promptql.hasura.io/docs/guides/existing-project)\n    *   [PromptQL Guide](https://promptql.hasura.io/docs/guides/promptql-guide)\n    *   [PromptQL Program API](https://promptql.hasura.io/docs/guides/program-api)\n    \n*   Tutorials\n    \n    *   [Apple Health Assistant](https://promptql.hasura.io/docs/tutorials/apple-health-assistant)\n    *   [Huggingface Datasets](https://promptql.hasura.io/docs/tutorials/huggingface-csv-parquet-sqlite)\n    *   [Kaggle Datasets](https://promptql.hasura.io/docs/tutorials/kaggle-csv-sqlite)\n    *   [DuckDuckGo Web Search](https://promptql.hasura.io/docs/tutorials/duckduckgo-web-search)\n    *   [Realtime Chat with BART API](https://promptql.hasura.io/docs/tutorials/bart-api)\n    \n\nOn This Page\n\n*   [Setup](https://promptql.hasura.io/docs/example-github#setup)\n*   [Install the DDN CLI](https://promptql.hasura.io/docs/example-github#install-the-ddn-cli)\n*   [Install Docker](https://promptql.hasura.io/docs/example-github#install-docker)\n*   [Log in with the CLI](https://promptql.hasura.io/docs/example-github#log-in-with-the-cli)\n*   [Validate the installation](https://promptql.hasura.io/docs/example-github#validate-the-installation)\n*   [Build your PromptQL app](https://promptql.hasura.io/docs/example-github#build-your-promptql-app)\n*   [Clone the example project](https://promptql.hasura.io/docs/example-github#clone-the-example-project)\n*   [Set up your .env file](https://promptql.hasura.io/docs/example-github#set-up-your-env-file)\n*   [Set up your GitHub repo](https://promptql.hasura.io/docs/example-github#set-up-your-github-repo)\n*   [Setup your DDN project](https://promptql.hasura.io/docs/example-github#setup-your-ddn-project)\n*   [Fire up your PromptQL project](https://promptql.hasura.io/docs/example-github#fire-up-your-promptql-project)\n*   [Restarting the app](https://promptql.hasura.io/docs/example-github#restarting-the-app)\n*   [Act on your data](https://promptql.hasura.io/docs/example-github#act-on-your-data)\n*   [Open the PromptQL playground](https://promptql.hasura.io/docs/example-github#open-the-promptql-playground)\n*   [Ask questions about your GitHub repo](https://promptql.hasura.io/docs/example-github#ask-questions-about-your-github-repo)\n\n[Question? Give us feedback →](https://github.com/hasura/graphql-engine/issues/new?title=Feedback%20for%20%E2%80%9CGetting%20Started%E2%80%9D&labels=feedback)Scroll to top\n\n[Docs](https://promptql.hasura.io/docs \"Docs\")Getting started\n\nGetting started\n===============\n\nIn this getting started guide, you’ll get hands on experience with PromptQL and the GitHub connector. We will be building a “Github Issues” assistant.\n\nYou will learn how to:\n\n*   Set up PromptQL to work with a GitHub issues and pull requests.\n    *   You will be able to do natural language query to triage feature requests, bugs and other issues with your connected Github repository.\n*   Install all required prerequisites.\n*   Create and configure the necessary API keys.\n*   Run your PromptQL project in a local environment.\n*   Ask your questions with PromptQL playground.\n\nSetup[](https://promptql.hasura.io/docs/example-github#setup)\n-------------------------------------------------------------\n\n### Install the DDN CLI[](https://promptql.hasura.io/docs/example-github#install-the-ddn-cli)\n\nMacOS or LinuxWindows\n\n`bash copy curl -L https://graphql-engine-cdn.hasura.io/ddn/cli/v4/get.sh | bash `\n\n*   Download the latest\n    \n    [DDN CLI installer for Windows.](https://graphql-engine-cdn.hasura.io/ddn/cli/v4/latest/DDN_CLI_Setup.exe)\n  \n*   Run the `DDN_CLI_Setup.exe` installer file and follow the instructions. This will only take a minute.\n*   The DDN CLI is added to your `%PATH%` environment variable so that you can use the `ddn` command from your terminal.\n    \n\n### Install Docker[](https://promptql.hasura.io/docs/example-github#install-docker)\n\nFollow the instructions on the [Docker website](https://docs.docker.com/engine/install/) to install Docker on your machine.\n\n### Log in with the CLI[](https://promptql.hasura.io/docs/example-github#log-in-with-the-cli)\n\nLogging in allows you to connect to the PromptQL runtime which is necessary for development. It also allows you to deploy your project to Hasura DDN.\n\n```\nddn auth login\n```\n\nYou will be redirected to DDN signup/login page.\n\n### Validate the installation[](https://promptql.hasura.io/docs/example-github#validate-the-installation)\n\nYou can verify that the DDN CLI is installed correctly by running:\n\n```\nddn doctor\n```\n\nBuild your PromptQL app[](https://promptql.hasura.io/docs/example-github#build-your-promptql-app)\n-------------------------------------------------------------------------------------------------\n\n### Clone the example project[](https://promptql.hasura.io/docs/example-github#clone-the-example-project)\n\nThe [example project](https://github.com/hasura/example-promptql-github) is already set up to connect PromptQL to any GitHub repo.\n\n```\ngit clone git@github.com:hasura/example-promptql-github.git\ncd example-promptql-github\n```\n\n### Set up your .env file[](https://promptql.hasura.io/docs/example-github#set-up-your-env-file)\n\nSet up your .env file with your GitHub API token.\n\n```\ncp .env.example .env\n```\n\n**Add GitHub API token to .env**\n\nFor the Github integration. Create an API token from [https://github.com/settings/tokens](https://github.com/settings/tokens)\n\n```\n# .env\n \n...\nGITHUB_API_TOKEN=<GITHUB_API_TOKEN>\n```\n\nThis token only needs read access to the repo you are interested in.\n\n![Image 4: Example: PromptQL on GitHub](https://promptql.hasura.io/_next/image?url=%2Fgithub-permissions-dark.png&w=2048&q=75)\n\n### Set up your GitHub repo[](https://promptql.hasura.io/docs/example-github#set-up-your-github-repo)\n\nHead to `app/connector/github/index.ts` and change the org name and the repo name to something you’d like:\n\n```\n// index.ts\n \n...\n  const manager = new GitHubIssueSyncManager('<org-name>', '<repo-name>');\n  if (!process.env.GITHUB_API_TOKEN) {\n...\n```\n\n### Setup your DDN project[](https://promptql.hasura.io/docs/example-github#setup-your-ddn-project)\n\nThis will create a Hasura DDN cloud project and set up PromptQL keys to connect to the PromptQL runtime.\n\n```\nddn project init\n```\n\n### Fire up your PromptQL project[](https://promptql.hasura.io/docs/example-github#fire-up-your-promptql-project)\n\nBuild your supergraph.\n\n```\nddn supergraph build local\n```\n\nThen bring up the PromptQL API server, the engine and the connector\n\n```\nddn run docker-start\n```\n\nYou’ll notice in amongst your Docker logs that your github synchronization has started.\n\nDocker logs\n\n\\[2024-01-01 12:00:01\\] Starting GitHub sync…  \n\\[2024-01-01 12:00:02\\] Fetching repository metadata…\n\n  \n\\[2024-01-01 12:00:03\\] Syncing issues and pull requests…\n\n  \n\\[2024-01-01 12:00:04\\] Loading repository contents…\n\n  \n\\[2024-01-01 12:00:05\\] GitHub sync complete\n\nIf the specified repo has many issues or comments it may take some time to get them all and you may be rate limited. That’s ok, you can go ahead and try PromptQL without the process having fully finished yet.\n\nIf you notice some logs regarding GitHub permissions, check that your GitHub API token has the correct permissions for the repo you’re trying to access.\n\n### Restarting the app[](https://promptql.hasura.io/docs/example-github#restarting-the-app)\n\nIf you made a mis-step or want to start from scratch, simply restarting the docker containers will reset all state including any loaded data.\n\n```\nddn run docker-start\n```\n\nAct on your data[](https://promptql.hasura.io/docs/example-github#act-on-your-data)\n-----------------------------------------------------------------------------------\n\n### Open the PromptQL playground[](https://promptql.hasura.io/docs/example-github#open-the-promptql-playground)\n\nIn another terminal, run\n\n```\nddn console --local\n```\n\nBrowser support: PromptQL playground is supported on all browsers except Firefox and Safari. Support for these browsers should be available shortly.\n\n### Ask questions about your GitHub repo[](https://promptql.hasura.io/docs/example-github#ask-questions-about-your-github-repo)\n\nThe console is a web app hosted at console.hasura.io that connects to your local PromptQL API and data sources. Your data is processed in the DDN PromptQL runtime but isn’t persisted externally.\n\nHead over to the console and ask a few questions about your GitHub repo.\n\n```\n> What are the open pull requests?\n> What kind of questions can I ask?\n```\n\n[Overview](https://promptql.hasura.io/docs \"Overview\")[Deploy and share](https://promptql.hasura.io/docs/deploy-and-share \"Deploy and share\")",
  "usage": {
    "tokens": 2474
  }
}
```
