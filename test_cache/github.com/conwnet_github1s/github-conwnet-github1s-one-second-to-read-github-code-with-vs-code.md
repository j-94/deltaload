---
title: GitHub - conwnet/github1s: One second to read GitHub code with VS Code.
description: One second to read GitHub code with VS Code. Contribute to conwnet/github1s development by creating an account on GitHub.
url: https://github.com/conwnet/github1s
timestamp: 2025-01-20T15:31:13.303Z
domain: github.com
path: conwnet_github1s
---

# GitHub - conwnet/github1s: One second to read GitHub code with VS Code.


One second to read GitHub code with VS Code. Contribute to conwnet/github1s development by creating an account on GitHub.


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
conwnet
/
github1s
Public
Notifications
Fork 877
 Star 23k
Code
Issues
54
Pull requests
2
Discussions
Actions
Projects
Wiki
Security
conwnet/github1s
 master
Code
Folders and files
Name	Last commit message	Last commit date

Latest commit
conwnet
feat: support multiple languages (#616)
6b2463f
 · 
History
422 Commits


.devcontainer
	
chore: bump vscode to 1.96.2 (#614)
	


.github
	
feat: support multiple languages (#616)
	


.husky
	
chore: bump vscode to 1.96.2 (#614)
	


docs
	
chore: bump vscode to 1.96.2 (#614)
	


extensions
	
chore(deps-dev): bump webpack in /extensions/github1s (#615)
	


functions
	
fix: github/gitlab auth callback (#607)
	


public
	
chore: bump vscode to 1.96.2 (#614)
	


resources/images
	
chore: update webpack config (#489)
	


scripts
	
feat: support multiple languages (#616)
	


src
	
feat: support multiple languages (#616)
	


tests
	
chore: bump vscode to 1.96.2 (#614)
	


vscode-web
	
feat: support multiple languages (#616)
	


.editorconfig
	
feat: add eslint add fix indent
	


.gitignore
	
chore: bump vscode to 1.96.2 (#614)
	


.gitpod.Dockerfile
	
Configure Gitpod.
	


.gitpod.yml
	
chore: bump vscode to 1.96.2 (#614)
	


.prettierignore
	
chore: bump vscode to 1.96.2 (#614)
	


.prettierrc.js
	
chore: bump vscode to 1.96.2 (#614)
	


LICENSE
	
chore: license
	


README.md
	
chore: bump vscode to 1.96.2 (#614)
	


eslint.config.js
	
chore: bump vscode to 1.96.2 (#614)
	


package-lock.json
	
feat: support multiple languages (#616)
	


package.json
	
feat: support multiple languages (#616)
	


tsconfig.json
	
chore: bump vscode to 1.96.2 (#614)
	


webpack.config.js
	
feat: support multiple languages (#616)
	
Repository files navigation
README
MIT license

github1s

One second to read GitHub code with VS Code.

Usage

Just add 1s after github and press Enter in the browser address bar for any repository you want to read.

For example, try it on the VS Code repo:

https://github1s.com/microsoft/vscode

You can also use https://gitlab1s.com or https://npmjs1s.com in the same way.

For browser extensions, see Third-party Related Projects.

Or save the following code snippet as a bookmarklet, you can use it to quickly switch between github.com and github1s.com (GitHub markdown doesn't allow js links, so just copy it into a bookmark).

javascript: window.location.href = window.location.href.replace(/github(1s)?.com/, function(match, p1) { return p1 ? 'github.com' : 'github1s.com' })

Develop in the cloud

To edit files, run Docker containers, create pull requests and more, click the "Develop your project on Gitpod" button in the status bar. You can also open the Command Palette (default shortcut Ctrl+Shift+P) and choose GitHub1s: Edit files in Gitpod.

Documentation
How it works
Roadmap
Enabling Private Repositories

If you want to view non-public repositories, you need to add an OAuth token. The token is stored only in your browser, and only send to GitHub when fetching your repository's files. Click on the icon near the bottom of the left-hand row of icons, and the dialog box will prompt you for it, and even take you to your GitHub settings page to generate one, if needed.

Screenshots

Development
Cloud-based development

You can start an online development environment with Gitpod by clicking the following button:

Local development
git clone git@github.com:conwnet/github1s.git
cd github1s
npm install
npm run watch
# The cli will automatically open http://localhost:8080 once the build is completed.
# You can visit http://localhost:8080/conwnet/github1s if it doesn't.
Local development with full VS Code build

You need these prerequisites (the same ones as for VS Code) for development with full VS Code build. Please make sure you could build VS Code locally before the watch mode.

To verify the build:

cd github1s
npm run build:vscode

After the initial successful build, you could use the watch mode:

cd github1s
npm install
npm run watch-with-vscode
# The cli will automatically open http://localhost:8080 once the build is completed.
# You can visit http://localhost:8080/conwnet/github1s if it doesn't.
... or ... VS Code + Docker Development

You can use the VS Code plugin Remote-Containers Dev Container to use a Docker container as a development environment.

Install the Remote-Containers plugin in VS Code & Docker

Open the Command Palette (default shortcut Ctrl+Shift+P) and choose Remote-Containers: Clone Repository in Container Volume...

Enter the repo, in this case https://github.com/conwnet/github1s.git or your forked repo

Pick either, Create a unique volume or Create a new volume

Now VS Code will create the docker container and connect to the new container so you can use this as a fully setup environment!

Open a new VS Code Terminal, then you can run the npm install commands listed above.

npm install
npm run watch
# The cli will automatically open http://localhost:8080 once the build is completed.
# You can visit http://localhost:8080/conwnet/github1s if it doesn't.
Format all codes
npm run format

It uses prettier to format all possible codes.

Build
npm install
npm run build
Feedback
If something is not working, create an issue
Sponsors

The continued development and maintenance of GitHub1s is made possible by these generous sponsors:

Partners

We are partnered with OSS Insight to get the Trending Repositories & some more Interesting Analytics. OSS Insight provides deep insights into GitHub repos, developers, and curated repo lists from billions of GitHub events. It’s built with TiDB Cloud.

Maintainers! 😊

netcon
💻 🖋	
xcv58
💻 🖋	
Siddhant Khare
💻 🖋
Stargazers over time

Third-party Related Projects
About

One second to read GitHub code with VS Code.

github1s.com
Topics
vscode hacktoberfest
Resources
 Readme
License
 MIT license
 Activity
Stars
 23k stars
Watchers
 109 watching
Forks
 877 forks
Report repository


Releases 52
0.27.5 (Jan 13, 2025)
Latest
+ 51 releases


Packages
No packages published



Contributors
45
+ 31 contributors


Languages
TypeScript
81.7%
 
HTML
6.8%
 
JavaScript
6.6%
 
CSS
4.8%
 
Other
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
  "title": "GitHub - conwnet/github1s: One second to read GitHub code with VS Code.",
  "description": "One second to read GitHub code with VS Code. Contribute to conwnet/github1s development by creating an account on GitHub.",
  "url": "https://github.com/conwnet/github1s?screenshot=true",
  "content": "Skip to content\nNavigation Menu\nProduct\nSolutions\nResources\nOpen Source\nEnterprise\nPricing\nSign in\nSign up\nconwnet\n/\ngithub1s\nPublic\nNotifications\nFork 877\n Star 23k\nCode\nIssues\n54\nPull requests\n2\nDiscussions\nActions\nProjects\nWiki\nSecurity\nconwnet/github1s\n master\nCode\nFolders and files\nName\tLast commit message\tLast commit date\n\nLatest commit\nconwnet\nfeat: support multiple languages (#616)\n6b2463f\n · \nHistory\n422 Commits\n\n\n.devcontainer\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\n.github\n\t\nfeat: support multiple languages (#616)\n\t\n\n\n.husky\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\ndocs\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\nextensions\n\t\nchore(deps-dev): bump webpack in /extensions/github1s (#615)\n\t\n\n\nfunctions\n\t\nfix: github/gitlab auth callback (#607)\n\t\n\n\npublic\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\nresources/images\n\t\nchore: update webpack config (#489)\n\t\n\n\nscripts\n\t\nfeat: support multiple languages (#616)\n\t\n\n\nsrc\n\t\nfeat: support multiple languages (#616)\n\t\n\n\ntests\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\nvscode-web\n\t\nfeat: support multiple languages (#616)\n\t\n\n\n.editorconfig\n\t\nfeat: add eslint add fix indent\n\t\n\n\n.gitignore\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\n.gitpod.Dockerfile\n\t\nConfigure Gitpod.\n\t\n\n\n.gitpod.yml\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\n.prettierignore\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\n.prettierrc.js\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\nLICENSE\n\t\nchore: license\n\t\n\n\nREADME.md\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\neslint.config.js\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\npackage-lock.json\n\t\nfeat: support multiple languages (#616)\n\t\n\n\npackage.json\n\t\nfeat: support multiple languages (#616)\n\t\n\n\ntsconfig.json\n\t\nchore: bump vscode to 1.96.2 (#614)\n\t\n\n\nwebpack.config.js\n\t\nfeat: support multiple languages (#616)\n\t\nRepository files navigation\nREADME\nMIT license\n\ngithub1s\n\nOne second to read GitHub code with VS Code.\n\nUsage\n\nJust add 1s after github and press Enter in the browser address bar for any repository you want to read.\n\nFor example, try it on the VS Code repo:\n\nhttps://github1s.com/microsoft/vscode\n\nYou can also use https://gitlab1s.com or https://npmjs1s.com in the same way.\n\nFor browser extensions, see Third-party Related Projects.\n\nOr save the following code snippet as a bookmarklet, you can use it to quickly switch between github.com and github1s.com (GitHub markdown doesn't allow js links, so just copy it into a bookmark).\n\njavascript: window.location.href = window.location.href.replace(/github(1s)?.com/, function(match, p1) { return p1 ? 'github.com' : 'github1s.com' })\n\nDevelop in the cloud\n\nTo edit files, run Docker containers, create pull requests and more, click the \"Develop your project on Gitpod\" button in the status bar. You can also open the Command Palette (default shortcut Ctrl+Shift+P) and choose GitHub1s: Edit files in Gitpod.\n\nDocumentation\nHow it works\nRoadmap\nEnabling Private Repositories\n\nIf you want to view non-public repositories, you need to add an OAuth token. The token is stored only in your browser, and only send to GitHub when fetching your repository's files. Click on the icon near the bottom of the left-hand row of icons, and the dialog box will prompt you for it, and even take you to your GitHub settings page to generate one, if needed.\n\nScreenshots\n\nDevelopment\nCloud-based development\n\nYou can start an online development environment with Gitpod by clicking the following button:\n\nLocal development\ngit clone git@github.com:conwnet/github1s.git\ncd github1s\nnpm install\nnpm run watch\n# The cli will automatically open http://localhost:8080 once the build is completed.\n# You can visit http://localhost:8080/conwnet/github1s if it doesn't.\nLocal development with full VS Code build\n\nYou need these prerequisites (the same ones as for VS Code) for development with full VS Code build. Please make sure you could build VS Code locally before the watch mode.\n\nTo verify the build:\n\ncd github1s\nnpm run build:vscode\n\nAfter the initial successful build, you could use the watch mode:\n\ncd github1s\nnpm install\nnpm run watch-with-vscode\n# The cli will automatically open http://localhost:8080 once the build is completed.\n# You can visit http://localhost:8080/conwnet/github1s if it doesn't.\n... or ... VS Code + Docker Development\n\nYou can use the VS Code plugin Remote-Containers Dev Container to use a Docker container as a development environment.\n\nInstall the Remote-Containers plugin in VS Code & Docker\n\nOpen the Command Palette (default shortcut Ctrl+Shift+P) and choose Remote-Containers: Clone Repository in Container Volume...\n\nEnter the repo, in this case https://github.com/conwnet/github1s.git or your forked repo\n\nPick either, Create a unique volume or Create a new volume\n\nNow VS Code will create the docker container and connect to the new container so you can use this as a fully setup environment!\n\nOpen a new VS Code Terminal, then you can run the npm install commands listed above.\n\nnpm install\nnpm run watch\n# The cli will automatically open http://localhost:8080 once the build is completed.\n# You can visit http://localhost:8080/conwnet/github1s if it doesn't.\nFormat all codes\nnpm run format\n\nIt uses prettier to format all possible codes.\n\nBuild\nnpm install\nnpm run build\nFeedback\nIf something is not working, create an issue\nSponsors\n\nThe continued development and maintenance of GitHub1s is made possible by these generous sponsors:\n\nPartners\n\nWe are partnered with OSS Insight to get the Trending Repositories & some more Interesting Analytics. OSS Insight provides deep insights into GitHub repos, developers, and curated repo lists from billions of GitHub events. It’s built with TiDB Cloud.\n\nMaintainers! 😊\n\nnetcon\n💻 🖋\t\nxcv58\n💻 🖋\t\nSiddhant Khare\n💻 🖋\nStargazers over time\n\nThird-party Related Projects\nAbout\n\nOne second to read GitHub code with VS Code.\n\ngithub1s.com\nTopics\nvscode hacktoberfest\nResources\n Readme\nLicense\n MIT license\n Activity\nStars\n 23k stars\nWatchers\n 109 watching\nForks\n 877 forks\nReport repository\n\n\nReleases 52\n0.27.5 (Jan 13, 2025)\nLatest\n+ 51 releases\n\n\nPackages\nNo packages published\n\n\n\nContributors\n45\n+ 31 contributors\n\n\nLanguages\nTypeScript\n81.7%\n \nHTML\n6.8%\n \nJavaScript\n6.6%\n \nCSS\n4.8%\n \nOther\n0.1%\nFooter\n© 2025 GitHub, Inc.\nFooter navigation\nTerms\nPrivacy\nSecurity\nStatus\nDocs\nContact\nManage cookies\nDo not share my personal information",
  "usage": {
    "tokens": 1620
  }
}
```
