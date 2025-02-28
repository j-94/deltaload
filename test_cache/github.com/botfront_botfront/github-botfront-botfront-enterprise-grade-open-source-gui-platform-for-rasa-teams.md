---
title: GitHub - botfront/botfront: Enterprise-grade open source GUI platform for Rasa teams
description: Enterprise-grade open source GUI platform for Rasa teams - botfront/botfront
url: https://github.com/botfront/botfront
timestamp: 2025-01-20T15:31:08.739Z
domain: github.com
path: botfront_botfront
---

# GitHub - botfront/botfront: Enterprise-grade open source GUI platform for Rasa teams


Enterprise-grade open source GUI platform for Rasa teams - botfront/botfront


## Content

Skip to content
Navigation Menu
Product
Solutions
Resources
Open Source
Enterprise
Pricing
Sign in
Sign up
This repository has been archived by the owner on May 5, 2021. It is now read-only.
botfront
/
botfront
Public archive
Notifications
Fork 325
 Star 804
Code
Issues
41
Pull requests
Discussions
Actions
Projects
Security
Insights
botfront/botfront
 master
Code
Folders and files
Name	Last commit message	Last commit date

Latest commit
Nathan Zylbersztejn
doc: not maintained anymore notice
88126fc
 · 
History
5,006 Commits


.github
	
Refactor: run tests and commit prior to deployment
	


.vscode
	
feat(cli): improvements in version management and file generation (#396)
	


botfront
	
refactor: improve training webhook error messages (#985)
	


cli
	
chore(release): 1.0.5
	


docs
	
docs: update deployment webhook documentation
	


scripts
	
refactor: migration to Rasa 2.0
	


.codeclimate.yml
	
chore: remove dead code (#433)
	


.dockerignore
	
chore: first commit
	


.gitignore
	
docs: bring back docs (#880)
	


.prettierrc
	
fix: display update warnings for bot sequences
	


CHANGELOG.md
	
chore(release): 1.0.5
	


CODE_OF_CONDUCT.md
	
Create CODE_OF_CONDUCT.md
	


Dockerfile
	
chore: update to Meteor 2 (#902)
	


LICENSE
	
refactor: license
	


README.md
	
doc: not maintained anymore notice
	


botfront_animation.gif
	
docs: fix animation in readme
	


commitlint.config.js
	
chore: commit lint config
	


entrypoint.sh
	
chore: fixed paths in docker entrypoint
	


netlify.toml
	
docs: change docs urls and implement redirects (#329)
	


npmrc.enc
	
ci: npm package published on succesful tag build
	
Repository files navigation
README
Code of conduct
Apache-2.0 license

   



This project is not maintained anymore and will not receive further updates.

Highlights • Features • Quick start • Development

Release Notes •



What is it

Botfront is an open-source enterprise-grade conversational platform built with Rasa. It provides super intuitive interfaces and collaborative features to domain experts, conversational designers and engineers.



Highlights
😎
Easy to use
	
🎓
Powerful
	
💻️
Developer friendly

Our main goal is to lower the technical barrier to entry in conversational AI. Implementing context-aware conversations should be as easy as chatting.	Botfront uses Rasa, a powerful and production ready conversational AI library. Botfront exposes all Rasa functionalities and abstracts its complexity.	Botfront's intuitive CLI orchestrates all Botfront's services on your development machine.
Authoring, training, auto reloading actions code, it just works!


Features
An intuitive interface for stories and rules
	Botfront provides a unique and natural conversation authoring experience. You can create complex dialog flows in minutes

A flow chart editor for forms
	A super intuitive flow chart editor for conversations that do not require machine learning

Automated tests
	Create automated tests in one click from conversations, get detailed reports and deploy in confidence.

Git integration
	Version your work on a repository with the new Git integration.

Train & evaluate NLU models
	Botfront comes with a complete NLU toolbox. You can tag vast amounts of data efficiently, train and evaluate models. Several evaluation methods are available depending on the development stage of your model, and you can annotate incoming NLU data

Rasa integration
	Botfront exposes all Rasa features and concepts and and makes them accessible at a higher level for faster development. You can export a Botfront project and use it with Rasa at any time.

Enterprise ready
	Scale your conversational AI practice with enterprise grade projects and user management, RBAC and flexible deployment options.


Quick Start

Botfront only requires a recent version of Docker. You can install the CLI with the following:

npm install -g botfront

Then just run botfrontto get started.



Documentation

The official documentation of Botfront is hosted on botfront.io. It is automatically built and updated on every new release. Once you've installed the cli you can also use botfront docs to open it.

We welcome contributions! It can be as easy as clicking on the "Edit page on Github" link at the bottom of every documentation pages.

Development
Installation
Botfront is a Meteor app, so the first step is to install Meteor
Then clone this repo and install the dependencies:
git clone https://github.com/botfront/botfront
cd botfront/botfront
meteor npm install
Install the CLI from the source code:
# if you installed Botfront from npm uninstall it.
npm uninstall -g botfront
# Install the cli from the source code
cd cli && npm link

Botfront needs to be connected to other services, especially Rasa. To do this, you need to create a regular project, and start Botfront with a dedicated configuration:

Create a Botfront project with botfront init (somewhere else, not in the repo)
Start your project with botfront up -e botfront. This will run all services except the Botfront app, since you are going to run it with Meteor locally
Go back to the botfront checkout cd botfront/botfront and run Botfront with meteor npm run start:docker-compose.dev. Botfront will be available at http://localhost:3000 so open your browser and happy editing 😸
TroubleShooting

Some botfront cli commands that may help if you run into problems:

botfront init     # create a new botfront project
botfront logs     # show the logs!
botfront killall  # stop all docker services
botfront down     # stop all botfront services
botfront up       # restart botfront
botfront docs     # open the docs in your browser

Note that these should be run from the same directory as your botfront project

Contribute

We ❤️ contributions of all size and sorts. If you find a typo, if you want to improve a section of the documentation or if you want to help with a bug or a feature, here are the steps:

Fork the repo and create a new branch, say fix-botfront-typo-1
Fix/improve the codebase
Commit the changes. Commit message must follow the naming convention, say fix(conversation builder): display story groups in alphabetical order
Make a pull request. Pull request name must follow the naming convention. It can simply be one of your commit messages, just copy paste it, e.g. fix(readme): improve the readability and move sections
Submit your pull request and wait for all checks passed (up to an hour)
Request reviews from one of the developers from our core team.
Get a 👍 and PR gets merged.

Well done! Once a PR gets merged, here are the things happened next:

all Docker images tagged with branch-master will be automatically updated in an hour. You may check the status on the Actions tab.
your contribution and commits will be included in our release note.
Testing

End to end tests are using the Cypress testing framework.

To manually run the Cypress tests, you need to have Botfront running in development mode. Some tests also require Rasa to be available.

Once you are at the root of the repo, you can enter the following.

cd botfront
# if you want to open Cypress' graphical interface
npx cypress open
# If you want to run the whole suite in headless mode
# This could take up to an hour depending on your computer
npx cypress run
# If you want to run a specific test
npx cypress run --spec "cypress/integration/02_training/training.spec.js"
Commit messages naming convention

To help everyone with understanding the commit history of Botfront, we employ commitlint to enforce the commit styles:

type(scope?): subject


where type is one of the following:

build
ci
chore
docs
feat
fix
perf
refactor
revert
style
test

scope is optional, represents the module your commit working on.

subject explains the commit.

As an example, a commit that improved the documentation:

docs(conversation builder): update slots manager screenshot.



License

Copyright (C) 2021 Dialogue Technologies Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0


Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.(C) 2021 Dialogue Technologies Inc. All rights reserved.

About

Enterprise-grade open source GUI platform for Rasa teams

botfront.io
Topics
conversational-ui chatbots chat-bot rasa chatbot-framework conversational-agents conversational-interface conversational-bots conversational-ai rasa-core rasa-ui dialogflow rasa-x botfront
Resources
 Readme
License
 Apache-2.0 license
Code of conduct
 Code of conduct
 Activity
 Custom properties
Stars
 804 stars
Watchers
 35 watching
Forks
 325 forks
Report repository


Releases 81
v1.0.5
Latest
+ 80 releases


Packages
No packages published



Contributors
14


Languages
JavaScript
99.3%
 
Less
0.3%
 
Shell
0.1%
 
Dockerfile
0.1%
 
Python
0.1%
 
CSS
0.1%
Footer
© 2025 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information

## Metadata

```json
{
  "title": "GitHub - botfront/botfront: Enterprise-grade open source GUI platform for Rasa teams",
  "description": "Enterprise-grade open source GUI platform for Rasa teams - botfront/botfront",
  "url": "https://github.com/botfront/botfront?screenshot=true",
  "content": "Skip to content\nNavigation Menu\nProduct\nSolutions\nResources\nOpen Source\nEnterprise\nPricing\nSign in\nSign up\nThis repository has been archived by the owner on May 5, 2021. It is now read-only.\nbotfront\n/\nbotfront\nPublic archive\nNotifications\nFork 325\n Star 804\nCode\nIssues\n41\nPull requests\nDiscussions\nActions\nProjects\nSecurity\nInsights\nbotfront/botfront\n master\nCode\nFolders and files\nName\tLast commit message\tLast commit date\n\nLatest commit\nNathan Zylbersztejn\ndoc: not maintained anymore notice\n88126fc\n · \nHistory\n5,006 Commits\n\n\n.github\n\t\nRefactor: run tests and commit prior to deployment\n\t\n\n\n.vscode\n\t\nfeat(cli): improvements in version management and file generation (#396)\n\t\n\n\nbotfront\n\t\nrefactor: improve training webhook error messages (#985)\n\t\n\n\ncli\n\t\nchore(release): 1.0.5\n\t\n\n\ndocs\n\t\ndocs: update deployment webhook documentation\n\t\n\n\nscripts\n\t\nrefactor: migration to Rasa 2.0\n\t\n\n\n.codeclimate.yml\n\t\nchore: remove dead code (#433)\n\t\n\n\n.dockerignore\n\t\nchore: first commit\n\t\n\n\n.gitignore\n\t\ndocs: bring back docs (#880)\n\t\n\n\n.prettierrc\n\t\nfix: display update warnings for bot sequences\n\t\n\n\nCHANGELOG.md\n\t\nchore(release): 1.0.5\n\t\n\n\nCODE_OF_CONDUCT.md\n\t\nCreate CODE_OF_CONDUCT.md\n\t\n\n\nDockerfile\n\t\nchore: update to Meteor 2 (#902)\n\t\n\n\nLICENSE\n\t\nrefactor: license\n\t\n\n\nREADME.md\n\t\ndoc: not maintained anymore notice\n\t\n\n\nbotfront_animation.gif\n\t\ndocs: fix animation in readme\n\t\n\n\ncommitlint.config.js\n\t\nchore: commit lint config\n\t\n\n\nentrypoint.sh\n\t\nchore: fixed paths in docker entrypoint\n\t\n\n\nnetlify.toml\n\t\ndocs: change docs urls and implement redirects (#329)\n\t\n\n\nnpmrc.enc\n\t\nci: npm package published on succesful tag build\n\t\nRepository files navigation\nREADME\nCode of conduct\nApache-2.0 license\n\n   \n\n\n\nThis project is not maintained anymore and will not receive further updates.\n\nHighlights • Features • Quick start • Development\n\nRelease Notes •\n\n\n\nWhat is it\n\nBotfront is an open-source enterprise-grade conversational platform built with Rasa. It provides super intuitive interfaces and collaborative features to domain experts, conversational designers and engineers.\n\n\n\nHighlights\n😎\nEasy to use\n\t\n🎓\nPowerful\n\t\n💻️\nDeveloper friendly\n\nOur main goal is to lower the technical barrier to entry in conversational AI. Implementing context-aware conversations should be as easy as chatting.\tBotfront uses Rasa, a powerful and production ready conversational AI library. Botfront exposes all Rasa functionalities and abstracts its complexity.\tBotfront's intuitive CLI orchestrates all Botfront's services on your development machine.\nAuthoring, training, auto reloading actions code, it just works!\n\n\nFeatures\nAn intuitive interface for stories and rules\n\tBotfront provides a unique and natural conversation authoring experience. You can create complex dialog flows in minutes\n\nA flow chart editor for forms\n\tA super intuitive flow chart editor for conversations that do not require machine learning\n\nAutomated tests\n\tCreate automated tests in one click from conversations, get detailed reports and deploy in confidence.\n\nGit integration\n\tVersion your work on a repository with the new Git integration.\n\nTrain & evaluate NLU models\n\tBotfront comes with a complete NLU toolbox. You can tag vast amounts of data efficiently, train and evaluate models. Several evaluation methods are available depending on the development stage of your model, and you can annotate incoming NLU data\n\nRasa integration\n\tBotfront exposes all Rasa features and concepts and and makes them accessible at a higher level for faster development. You can export a Botfront project and use it with Rasa at any time.\n\nEnterprise ready\n\tScale your conversational AI practice with enterprise grade projects and user management, RBAC and flexible deployment options.\n\n\nQuick Start\n\nBotfront only requires a recent version of Docker. You can install the CLI with the following:\n\nnpm install -g botfront\n\nThen just run botfrontto get started.\n\n\n\nDocumentation\n\nThe official documentation of Botfront is hosted on botfront.io. It is automatically built and updated on every new release. Once you've installed the cli you can also use botfront docs to open it.\n\nWe welcome contributions! It can be as easy as clicking on the \"Edit page on Github\" link at the bottom of every documentation pages.\n\nDevelopment\nInstallation\nBotfront is a Meteor app, so the first step is to install Meteor\nThen clone this repo and install the dependencies:\ngit clone https://github.com/botfront/botfront\ncd botfront/botfront\nmeteor npm install\nInstall the CLI from the source code:\n# if you installed Botfront from npm uninstall it.\nnpm uninstall -g botfront\n# Install the cli from the source code\ncd cli && npm link\n\nBotfront needs to be connected to other services, especially Rasa. To do this, you need to create a regular project, and start Botfront with a dedicated configuration:\n\nCreate a Botfront project with botfront init (somewhere else, not in the repo)\nStart your project with botfront up -e botfront. This will run all services except the Botfront app, since you are going to run it with Meteor locally\nGo back to the botfront checkout cd botfront/botfront and run Botfront with meteor npm run start:docker-compose.dev. Botfront will be available at http://localhost:3000 so open your browser and happy editing 😸\nTroubleShooting\n\nSome botfront cli commands that may help if you run into problems:\n\nbotfront init     # create a new botfront project\nbotfront logs     # show the logs!\nbotfront killall  # stop all docker services\nbotfront down     # stop all botfront services\nbotfront up       # restart botfront\nbotfront docs     # open the docs in your browser\n\nNote that these should be run from the same directory as your botfront project\n\nContribute\n\nWe ❤️ contributions of all size and sorts. If you find a typo, if you want to improve a section of the documentation or if you want to help with a bug or a feature, here are the steps:\n\nFork the repo and create a new branch, say fix-botfront-typo-1\nFix/improve the codebase\nCommit the changes. Commit message must follow the naming convention, say fix(conversation builder): display story groups in alphabetical order\nMake a pull request. Pull request name must follow the naming convention. It can simply be one of your commit messages, just copy paste it, e.g. fix(readme): improve the readability and move sections\nSubmit your pull request and wait for all checks passed (up to an hour)\nRequest reviews from one of the developers from our core team.\nGet a 👍 and PR gets merged.\n\nWell done! Once a PR gets merged, here are the things happened next:\n\nall Docker images tagged with branch-master will be automatically updated in an hour. You may check the status on the Actions tab.\nyour contribution and commits will be included in our release note.\nTesting\n\nEnd to end tests are using the Cypress testing framework.\n\nTo manually run the Cypress tests, you need to have Botfront running in development mode. Some tests also require Rasa to be available.\n\nOnce you are at the root of the repo, you can enter the following.\n\ncd botfront\n# if you want to open Cypress' graphical interface\nnpx cypress open\n# If you want to run the whole suite in headless mode\n# This could take up to an hour depending on your computer\nnpx cypress run\n# If you want to run a specific test\nnpx cypress run --spec \"cypress/integration/02_training/training.spec.js\"\nCommit messages naming convention\n\nTo help everyone with understanding the commit history of Botfront, we employ commitlint to enforce the commit styles:\n\ntype(scope?): subject\n\n\nwhere type is one of the following:\n\nbuild\nci\nchore\ndocs\nfeat\nfix\nperf\nrefactor\nrevert\nstyle\ntest\n\nscope is optional, represents the module your commit working on.\n\nsubject explains the commit.\n\nAs an example, a commit that improved the documentation:\n\ndocs(conversation builder): update slots manager screenshot.\n\n\n\nLicense\n\nCopyright (C) 2021 Dialogue Technologies Inc.\n\nLicensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at\n\nhttp://www.apache.org/licenses/LICENSE-2.0\n\n\nUnless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.(C) 2021 Dialogue Technologies Inc. All rights reserved.\n\nAbout\n\nEnterprise-grade open source GUI platform for Rasa teams\n\nbotfront.io\nTopics\nconversational-ui chatbots chat-bot rasa chatbot-framework conversational-agents conversational-interface conversational-bots conversational-ai rasa-core rasa-ui dialogflow rasa-x botfront\nResources\n Readme\nLicense\n Apache-2.0 license\nCode of conduct\n Code of conduct\n Activity\n Custom properties\nStars\n 804 stars\nWatchers\n 35 watching\nForks\n 325 forks\nReport repository\n\n\nReleases 81\nv1.0.5\nLatest\n+ 80 releases\n\n\nPackages\nNo packages published\n\n\n\nContributors\n14\n\n\nLanguages\nJavaScript\n99.3%\n \nLess\n0.3%\n \nShell\n0.1%\n \nDockerfile\n0.1%\n \nPython\n0.1%\n \nCSS\n0.1%\nFooter\n© 2025 GitHub, Inc.\nFooter navigation\nTerms\nPrivacy\nSecurity\nStatus\nDocs\nContact\nManage cookies\nDo not share my personal information",
  "usage": {
    "tokens": 2104
  }
}
```
