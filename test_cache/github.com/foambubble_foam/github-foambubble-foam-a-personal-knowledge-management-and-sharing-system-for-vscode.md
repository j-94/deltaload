---
title: GitHub - foambubble/foam: A personal knowledge management and sharing system for VSCode
description: A personal knowledge management and sharing system for VSCode - foambubble/foam
url: https://github.com/foambubble/foam
timestamp: 2025-01-20T15:31:55.544Z
domain: github.com
path: foambubble_foam
---

# GitHub - foambubble/foam: A personal knowledge management and sharing system for VSCode


A personal knowledge management and sharing system for VSCode - foambubble/foam


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
foambubble
/
foam
Public
Notifications
Fork 672
 Star 15.6k
Code
Issues
111
Pull requests
6
Discussions
Actions
Projects
Security
Insights
foambubble/foam
 master
Code
Folders and files
Name	Last commit message	Last commit date

Latest commit
allcontributors[bot]
add markschaver as a contributor for doc (#1416)
6be4f00
 · 
History
1,149 Commits


.github
	
Readding markdown-all-in-one in extension list and fixing script
	


.vscode
	
Setting prettier as default formatter for typescript
	


assets/screenshots
	
Feature: sync links on file rename (#969)
	


docs
	
add markschaver as a contributor for doc (#1416)
	


packages/foam-vscode
	
Edited command menu titles to make case consistent (#1415)
	


.all-contributorsrc
	
add markschaver as a contributor for doc (#1416)
	


.editorconfig
	
consolidated prettier configuration in root package.json file (#429)
	


.eslintrc.json
	
Updated a bunch of dependencies (#1160)
	


.gitattributes
	
.gitattributes: create
	


.gitignore
	
Foam as Web Extension (#1395)
	


.yarnrc
	
Improve testing experience (#881)
	


LICENSE
	
Refactored URI for Foam API v1 (#537)
	


lerna.json
	
v0.26.4
	


package-lock.json
	
Improve performance via Triemap in workspace (#1406)
	


package.json
	
Update Jest to v29 (#1271)
	


readme.md
	
add markschaver as a contributor for doc (#1416)
	


tsconfig.base.json
	
Extracted foam-cli to https://github.com/foambubble/foam-cli (#535)
	


typos.toml
	
Add GH Action workflow to check spell (#1221)
	


yarn.lock
	
Improve performance via Triemap in workspace (#1406)
	
Repository files navigation
README
License

Foam

👀This is an early stage project under rapid development. For updates join the Foam community Discord! 💬

 

Foam is a personal knowledge management and sharing system inspired by Roam Research, built on Visual Studio Code and GitHub.

You can use Foam for organising your research, keeping re-discoverable notes, writing long-form content and, optionally, publishing it to the web.

Foam is free, open source, and extremely extensible to suit your personal workflow. You own the information you create with Foam, and you're free to share it, and collaborate on it with anyone you want.

Features
Graph Visualization

See how your notes are connected via a graph with the Foam: Show Graph command.

Link Autocompletion

Foam helps you create the connections between your notes, and your placeholders as well.

Sync links on file rename

Foam updates the links to renamed files, so your notes stay consistent.

Unique identifiers across directories

Foam supports files with the same name in multiple directories. It will use the minimum identifier required, and even report and help you fix existing ambiguous wikilinks.

Link Preview and Navigation

Go to definition, Peek References

See where a note is being referenced in your knowledge base.

Navigation in Preview

Navigate your rendered notes in the VS Code preview panel.

Note embed

Embed the content from other notes.

Support for sections

Foam supports autocompletion, navigation, embedding and diagnostics for note sections. Just use the standard wiki syntax of [[resource#Section Title]].

Link Alias

Foam supports link aliasing, so you can have a [[wikilink]], or a [[wikilink|alias]].

Templates

Use custom templates to have avoid repetitve work on your notes.

Backlinks Panel

Quickly check which notes are referencing the currently active note. See for each occurrence the context in which it lives, as well as a preview of the note.

Tag Explorer Panel

Tag your notes and navigate them with the Tag Explorer. Foam also supports hierarchical tags.

Orphans and Placeholder Panels

Orphans are notes that have no inbound nor outbound links. Placeholders are dangling links, or notes without content. Keep them under control, and your knowledge base in a better state, by using this panel.

Syntax highlight

Foam highlights wikilinks and placeholder differently, to help you visualize your knowledge base.

Daily note

Create a journal with daily notes.

Generate references for your wikilinks

Create markdown references for [[wikilinks]], to use your notes in a non-Foam workspace. With references you can also make your notes navigable both in GitHub UI as well as GitHub Pages.

Commands
Explore your knowledge base with the Foam: Open Random Note command
Access your daily note with the Foam: Open Daily Note command
Create a new note with the Foam: Create New Note command
This becomes very powerful when combined with note templates and the Foam: Create New Note from Template command
See your workspace as a connected graph with the Foam: Show Graph command
Recipes

People use Foam in different ways for different use cases, check out the recipes page for inspiration!

Getting started

Whether you want to build a Second Brain or a Zettelkasten, write a book, or just get better at long-term learning, Foam can help you organise your thoughts if you follow these simple rules:

Create a single Foam workspace for all your knowledge and research following the [[Getting started]] guide.
Write your thoughts in markdown documents (I like to call them Bubbles, but that might be more than a little twee). These documents should be atomic: Put things that belong together into a single document, and limit its content to that single topic. (source)
Use Foam's shortcuts and autocompletions to link your thoughts together with [[wikilinks]], and navigate between them to explore your knowledge graph.
Get an overview of your Foam workspace using the [[Graph Visualisation]], and discover relationships between your thoughts with the use of [Backlinking].

You can also use our Foam template:

Log in on your GitHub account.
Create a GitHub repository from foam-template. If you want to keep your thoughts to yourself, remember to set the repository private.
Clone the repository and open it in VS Code.
When prompted to install recommended extensions, click Install all (or Show Recommendations if you want to review and install them one by one).

This will also install Foam, but if you already have it installed, that's ok, just make sure you're up to date on the latest version.

Requirements

High tolerance for alpha-grade software. Foam is still a Work in Progress. Rest assured it will never lock you in, nor compromise your files, but sometimes some features might break ;)

Known Issues

See the issues on our GitHub repo ;)

Release Notes

See the CHANGELOG.

Learn more

Head over to the 👉Published version of this Foam workspace to see Foam in action and read the rest of the documentation!

Quick links to next documentation sections

What's in a Foam?
Getting started
Features
Call To Adventure
Thanks and attribution

You can also browse the docs folder.

License

Foam is licensed under the MIT license.

Contribution Guide

See the Contribution Guide

Code of conduct

See the Code of Conduct

Contributors ✨

Thanks goes to these wonderful people (emoji key):


Jani Eväkallio
💻 📖	
Joe Previte
💻 📖	
Riccardo
💻 📖	
Janne Ojanaho
💻 📖	
Paul Shen
📖	
coffenbacher
📖	
Mathieu Dutour
📖

Michael Hansen
📖	
David Nadlinger
📖	
Fernando
📖	
Juan Gonzalez
📖	
Louie Christie
📖	
Sandro
📖	
Simon Knott
📖

Steven
📖	
Tim
📖	
Saurav Khdoolia
📖	
Ankit Tiwari
📖 ⚠️ 💻	
Ayush Baweja
📖	
TaiChi-IO
📖	
Juan F Gonzalez
📖

Sanket Dasgupta
📖 💻	
Nicholas Stafie
📖	
Francis Hamel
💻	
digiguru
💻 📖	
CHIRAG SINGHAL
💻	
Jonathan Carter
📖	
Julian Elve
📖

Thomas Koppelaar
💬 💻 📓	
Akshay
💻	
John Lindquist
📖	
Ashwin Ramaswami
📖	
Claudio Canales
📖	
vitaly-pevgonen
📖	
Dmitry Shemetov
📖

hooncp
📖	
Martin Laws
📖	
Sean K Smith
💻	
Kevin Neely
📖	
Arief Rahmansyah
📖	
Vishesh Handa
📖	
Hitesh Kumar
📖

Spencer Woo
📖	
ingalless
💻 📖	
José Duarte
💻 📖	
Yenly
📖	
hikerpig
💻	
Sigfried Gold
📖	
Tristan Sokol
💻

Danil Rodin
📖	
Scott Williams
📖	
jackiexiao
📖	
John B Nelson
📖	
Asif Mehedi
📖	
Tan Li
💻	
Shauna Gordon
📖

Mike Cluck
💻	
Brandon Pugh
💻	
Max Davitt
📖	
Brian Anglin
📖	
elswork
📖	
léon h
💻	
Nikhil Nygaard
📖

Mark Dixon
💻	
Joel James
💻	
Hashiguchi Ryo
📖	
Michael Overmeyer
💻	
Derrick Qin
📖	
Omar López
📖	
Robin King
💻

Dheepak
📖	
Daniel VG
📖	
Barabas
💻	
Engincan VESKE
📖	
Paul de Raaij
💻	
Scott Bronson
📖	
Rafael Riedel
📖

Pearcekieser
📖	
Owen Young
📖 🖋	
Prashanth Subrahmanyam
📖	
Jonas SPRENGER
💻	
Paul
📖	
Ikko Ashimine
📖	
memeplex
💻

AndreiD049
💻	
Yan
📖	
Jim Tittsler
📖	
Malcolm Mielle
📖	
Veesar
📖	
bentongxyz
💻	
Brian DeVries
💻

Clifford Fajardo
🔧	
Chris Usick
💻	
Joe DeCock
💻	
Drew Tyler
📖	
Lauviah0622
💻	
Josh Dover
💻	
Phil Helm
📖

Larry Li
💻	
Joe Taber
📖	
Woosuk Park
📖	
Daniel Murphy
💻	
Dominic D
💻	
luca
📖	
Lloyd Jackman
📖

sn3akiwhizper
📖	
jonathan berger
📖	
Daniel Wang
💻	
Liu YongLiang
📖	
Scott Akerman
💻	
Jim Graham
💻	
Zhizhen He
🔧

Tony Cheneau
📖	
Nicholas Latham
💻	
Tomochika Hara
📖	
Daniel Carosone
📖	
Miguel Angel Bruni Montero
💻	
Kevin Walsh
📖	
Xinglan Liu
💻

Thomas Hegghammer
📖	
Piotr Mrzygłosz
📖	
Mark Schaver
📖

This project follows the all-contributors specification. Contributions of any kind welcome!

About

A personal knowledge management and sharing system for VSCode

foambubble.github.io/
Topics
markdown markdown-editor vscode note-taking graph-visualisation pkm personal-knowledge-base notes-app zettelkasten
Resources
 Readme
License
 View license
 Activity
 Custom properties
Stars
 15.6k stars
Watchers
 123 watching
Forks
 672 forks
Report repository


Releases 97
v0.26.4
Latest
+ 96 releases


Packages
No packages published



Contributors
139
+ 125 contributors


Languages
TypeScript
96.0%
 
JavaScript
3.6%
 
Other
0.4%
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
  "title": "GitHub - foambubble/foam: A personal knowledge management and sharing system for VSCode",
  "description": "A personal knowledge management and sharing system for VSCode - foambubble/foam",
  "url": "https://github.com/foambubble/foam?screenshot=true",
  "content": "Skip to content\nNavigation Menu\nProduct\nSolutions\nResources\nOpen Source\nEnterprise\nPricing\nSign in\nSign up\nfoambubble\n/\nfoam\nPublic\nNotifications\nFork 672\n Star 15.6k\nCode\nIssues\n111\nPull requests\n6\nDiscussions\nActions\nProjects\nSecurity\nInsights\nfoambubble/foam\n master\nCode\nFolders and files\nName\tLast commit message\tLast commit date\n\nLatest commit\nallcontributors[bot]\nadd markschaver as a contributor for doc (#1416)\n6be4f00\n · \nHistory\n1,149 Commits\n\n\n.github\n\t\nReadding markdown-all-in-one in extension list and fixing script\n\t\n\n\n.vscode\n\t\nSetting prettier as default formatter for typescript\n\t\n\n\nassets/screenshots\n\t\nFeature: sync links on file rename (#969)\n\t\n\n\ndocs\n\t\nadd markschaver as a contributor for doc (#1416)\n\t\n\n\npackages/foam-vscode\n\t\nEdited command menu titles to make case consistent (#1415)\n\t\n\n\n.all-contributorsrc\n\t\nadd markschaver as a contributor for doc (#1416)\n\t\n\n\n.editorconfig\n\t\nconsolidated prettier configuration in root package.json file (#429)\n\t\n\n\n.eslintrc.json\n\t\nUpdated a bunch of dependencies (#1160)\n\t\n\n\n.gitattributes\n\t\n.gitattributes: create\n\t\n\n\n.gitignore\n\t\nFoam as Web Extension (#1395)\n\t\n\n\n.yarnrc\n\t\nImprove testing experience (#881)\n\t\n\n\nLICENSE\n\t\nRefactored URI for Foam API v1 (#537)\n\t\n\n\nlerna.json\n\t\nv0.26.4\n\t\n\n\npackage-lock.json\n\t\nImprove performance via Triemap in workspace (#1406)\n\t\n\n\npackage.json\n\t\nUpdate Jest to v29 (#1271)\n\t\n\n\nreadme.md\n\t\nadd markschaver as a contributor for doc (#1416)\n\t\n\n\ntsconfig.base.json\n\t\nExtracted foam-cli to https://github.com/foambubble/foam-cli (#535)\n\t\n\n\ntypos.toml\n\t\nAdd GH Action workflow to check spell (#1221)\n\t\n\n\nyarn.lock\n\t\nImprove performance via Triemap in workspace (#1406)\n\t\nRepository files navigation\nREADME\nLicense\n\nFoam\n\n👀This is an early stage project under rapid development. For updates join the Foam community Discord! 💬\n\n \n\nFoam is a personal knowledge management and sharing system inspired by Roam Research, built on Visual Studio Code and GitHub.\n\nYou can use Foam for organising your research, keeping re-discoverable notes, writing long-form content and, optionally, publishing it to the web.\n\nFoam is free, open source, and extremely extensible to suit your personal workflow. You own the information you create with Foam, and you're free to share it, and collaborate on it with anyone you want.\n\nFeatures\nGraph Visualization\n\nSee how your notes are connected via a graph with the Foam: Show Graph command.\n\nLink Autocompletion\n\nFoam helps you create the connections between your notes, and your placeholders as well.\n\nSync links on file rename\n\nFoam updates the links to renamed files, so your notes stay consistent.\n\nUnique identifiers across directories\n\nFoam supports files with the same name in multiple directories. It will use the minimum identifier required, and even report and help you fix existing ambiguous wikilinks.\n\nLink Preview and Navigation\n\nGo to definition, Peek References\n\nSee where a note is being referenced in your knowledge base.\n\nNavigation in Preview\n\nNavigate your rendered notes in the VS Code preview panel.\n\nNote embed\n\nEmbed the content from other notes.\n\nSupport for sections\n\nFoam supports autocompletion, navigation, embedding and diagnostics for note sections. Just use the standard wiki syntax of [[resource#Section Title]].\n\nLink Alias\n\nFoam supports link aliasing, so you can have a [[wikilink]], or a [[wikilink|alias]].\n\nTemplates\n\nUse custom templates to have avoid repetitve work on your notes.\n\nBacklinks Panel\n\nQuickly check which notes are referencing the currently active note. See for each occurrence the context in which it lives, as well as a preview of the note.\n\nTag Explorer Panel\n\nTag your notes and navigate them with the Tag Explorer. Foam also supports hierarchical tags.\n\nOrphans and Placeholder Panels\n\nOrphans are notes that have no inbound nor outbound links. Placeholders are dangling links, or notes without content. Keep them under control, and your knowledge base in a better state, by using this panel.\n\nSyntax highlight\n\nFoam highlights wikilinks and placeholder differently, to help you visualize your knowledge base.\n\nDaily note\n\nCreate a journal with daily notes.\n\nGenerate references for your wikilinks\n\nCreate markdown references for [[wikilinks]], to use your notes in a non-Foam workspace. With references you can also make your notes navigable both in GitHub UI as well as GitHub Pages.\n\nCommands\nExplore your knowledge base with the Foam: Open Random Note command\nAccess your daily note with the Foam: Open Daily Note command\nCreate a new note with the Foam: Create New Note command\nThis becomes very powerful when combined with note templates and the Foam: Create New Note from Template command\nSee your workspace as a connected graph with the Foam: Show Graph command\nRecipes\n\nPeople use Foam in different ways for different use cases, check out the recipes page for inspiration!\n\nGetting started\n\nWhether you want to build a Second Brain or a Zettelkasten, write a book, or just get better at long-term learning, Foam can help you organise your thoughts if you follow these simple rules:\n\nCreate a single Foam workspace for all your knowledge and research following the [[Getting started]] guide.\nWrite your thoughts in markdown documents (I like to call them Bubbles, but that might be more than a little twee). These documents should be atomic: Put things that belong together into a single document, and limit its content to that single topic. (source)\nUse Foam's shortcuts and autocompletions to link your thoughts together with [[wikilinks]], and navigate between them to explore your knowledge graph.\nGet an overview of your Foam workspace using the [[Graph Visualisation]], and discover relationships between your thoughts with the use of [Backlinking].\n\nYou can also use our Foam template:\n\nLog in on your GitHub account.\nCreate a GitHub repository from foam-template. If you want to keep your thoughts to yourself, remember to set the repository private.\nClone the repository and open it in VS Code.\nWhen prompted to install recommended extensions, click Install all (or Show Recommendations if you want to review and install them one by one).\n\nThis will also install Foam, but if you already have it installed, that's ok, just make sure you're up to date on the latest version.\n\nRequirements\n\nHigh tolerance for alpha-grade software. Foam is still a Work in Progress. Rest assured it will never lock you in, nor compromise your files, but sometimes some features might break ;)\n\nKnown Issues\n\nSee the issues on our GitHub repo ;)\n\nRelease Notes\n\nSee the CHANGELOG.\n\nLearn more\n\nHead over to the 👉Published version of this Foam workspace to see Foam in action and read the rest of the documentation!\n\nQuick links to next documentation sections\n\nWhat's in a Foam?\nGetting started\nFeatures\nCall To Adventure\nThanks and attribution\n\nYou can also browse the docs folder.\n\nLicense\n\nFoam is licensed under the MIT license.\n\nContribution Guide\n\nSee the Contribution Guide\n\nCode of conduct\n\nSee the Code of Conduct\n\nContributors ✨\n\nThanks goes to these wonderful people (emoji key):\n\n\nJani Eväkallio\n💻 📖\t\nJoe Previte\n💻 📖\t\nRiccardo\n💻 📖\t\nJanne Ojanaho\n💻 📖\t\nPaul Shen\n📖\t\ncoffenbacher\n📖\t\nMathieu Dutour\n📖\n\nMichael Hansen\n📖\t\nDavid Nadlinger\n📖\t\nFernando\n📖\t\nJuan Gonzalez\n📖\t\nLouie Christie\n📖\t\nSandro\n📖\t\nSimon Knott\n📖\n\nSteven\n📖\t\nTim\n📖\t\nSaurav Khdoolia\n📖\t\nAnkit Tiwari\n📖 ⚠️ 💻\t\nAyush Baweja\n📖\t\nTaiChi-IO\n📖\t\nJuan F Gonzalez\n📖\n\nSanket Dasgupta\n📖 💻\t\nNicholas Stafie\n📖\t\nFrancis Hamel\n💻\t\ndigiguru\n💻 📖\t\nCHIRAG SINGHAL\n💻\t\nJonathan Carter\n📖\t\nJulian Elve\n📖\n\nThomas Koppelaar\n💬 💻 📓\t\nAkshay\n💻\t\nJohn Lindquist\n📖\t\nAshwin Ramaswami\n📖\t\nClaudio Canales\n📖\t\nvitaly-pevgonen\n📖\t\nDmitry Shemetov\n📖\n\nhooncp\n📖\t\nMartin Laws\n📖\t\nSean K Smith\n💻\t\nKevin Neely\n📖\t\nArief Rahmansyah\n📖\t\nVishesh Handa\n📖\t\nHitesh Kumar\n📖\n\nSpencer Woo\n📖\t\ningalless\n💻 📖\t\nJosé Duarte\n💻 📖\t\nYenly\n📖\t\nhikerpig\n💻\t\nSigfried Gold\n📖\t\nTristan Sokol\n💻\n\nDanil Rodin\n📖\t\nScott Williams\n📖\t\njackiexiao\n📖\t\nJohn B Nelson\n📖\t\nAsif Mehedi\n📖\t\nTan Li\n💻\t\nShauna Gordon\n📖\n\nMike Cluck\n💻\t\nBrandon Pugh\n💻\t\nMax Davitt\n📖\t\nBrian Anglin\n📖\t\nelswork\n📖\t\nléon h\n💻\t\nNikhil Nygaard\n📖\n\nMark Dixon\n💻\t\nJoel James\n💻\t\nHashiguchi Ryo\n📖\t\nMichael Overmeyer\n💻\t\nDerrick Qin\n📖\t\nOmar López\n📖\t\nRobin King\n💻\n\nDheepak\n📖\t\nDaniel VG\n📖\t\nBarabas\n💻\t\nEngincan VESKE\n📖\t\nPaul de Raaij\n💻\t\nScott Bronson\n📖\t\nRafael Riedel\n📖\n\nPearcekieser\n📖\t\nOwen Young\n📖 🖋\t\nPrashanth Subrahmanyam\n📖\t\nJonas SPRENGER\n💻\t\nPaul\n📖\t\nIkko Ashimine\n📖\t\nmemeplex\n💻\n\nAndreiD049\n💻\t\nYan\n📖\t\nJim Tittsler\n📖\t\nMalcolm Mielle\n📖\t\nVeesar\n📖\t\nbentongxyz\n💻\t\nBrian DeVries\n💻\n\nClifford Fajardo\n🔧\t\nChris Usick\n💻\t\nJoe DeCock\n💻\t\nDrew Tyler\n📖\t\nLauviah0622\n💻\t\nJosh Dover\n💻\t\nPhil Helm\n📖\n\nLarry Li\n💻\t\nJoe Taber\n📖\t\nWoosuk Park\n📖\t\nDaniel Murphy\n💻\t\nDominic D\n💻\t\nluca\n📖\t\nLloyd Jackman\n📖\n\nsn3akiwhizper\n📖\t\njonathan berger\n📖\t\nDaniel Wang\n💻\t\nLiu YongLiang\n📖\t\nScott Akerman\n💻\t\nJim Graham\n💻\t\nZhizhen He\n🔧\n\nTony Cheneau\n📖\t\nNicholas Latham\n💻\t\nTomochika Hara\n📖\t\nDaniel Carosone\n📖\t\nMiguel Angel Bruni Montero\n💻\t\nKevin Walsh\n📖\t\nXinglan Liu\n💻\n\nThomas Hegghammer\n📖\t\nPiotr Mrzygłosz\n📖\t\nMark Schaver\n📖\n\nThis project follows the all-contributors specification. Contributions of any kind welcome!\n\nAbout\n\nA personal knowledge management and sharing system for VSCode\n\nfoambubble.github.io/\nTopics\nmarkdown markdown-editor vscode note-taking graph-visualisation pkm personal-knowledge-base notes-app zettelkasten\nResources\n Readme\nLicense\n View license\n Activity\n Custom properties\nStars\n 15.6k stars\nWatchers\n 123 watching\nForks\n 672 forks\nReport repository\n\n\nReleases 97\nv0.26.4\nLatest\n+ 96 releases\n\n\nPackages\nNo packages published\n\n\n\nContributors\n139\n+ 125 contributors\n\n\nLanguages\nTypeScript\n96.0%\n \nJavaScript\n3.6%\n \nOther\n0.4%\nFooter\n© 2025 GitHub, Inc.\nFooter navigation\nTerms\nPrivacy\nSecurity\nStatus\nDocs\nContact\nManage cookies\nDo not share my personal information",
  "usage": {
    "tokens": 2792
  }
}
```
