---
title: GitHub - redwoodjs/redwood: The App Framework for Startups
description: The App Framework for Startups. Contribute to redwoodjs/redwood development by creating an account on GitHub.
url: https://github.com/redwoodjs/redwood
timestamp: 2025-01-20T15:31:12.653Z
domain: github.com
path: redwoodjs_redwood
---

# GitHub - redwoodjs/redwood: The App Framework for Startups


The App Framework for Startups. Contribute to redwoodjs/redwood development by creating an account on GitHub.


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
redwoodjs
/
redwood
Public
Notifications
Fork 1k
 Star 17.5k
Code
Issues
430
Pull requests
38
Actions
Projects
3
Security
1
Insights
redwoodjs/redwood
 main
Code
Folders and files
Name	Last commit message	Last commit date

Latest commit
renovate[bot]
fix(deps): update dependency isbot to v5.1.21 (#11912)
37916c9
 · 
History
12,004 Commits


.changesets
	
Revert "[Router][TS] Auto-complete route names for unauthenticated pr…
	


.github
	
chore(deps) re-upgrade to yarn 4.6.0 (#11911)
	


.vscode
	
Adds background job scheduling and execution (#11238)
	


__fixtures__
	
chore(deps) re-upgrade to yarn 4.6.0 (#11911)
	


docs
	
chore(deps) re-upgrade to yarn 4.6.0 (#11911)
	


packages
	
fix(deps): update dependency isbot to v5.1.21 (#11912)
	


tasks
	
feat(dbAuth): Lax SameSite cookie policy (#11889)
	


.dependency-cruiser.mjs
	
chore(formatting): Formatting 1 of n (#11251)
	


.editorconfig
	
chore(formatting): Remove 'insert_final_newline' from editor config (#…
	


.eslintrc.js
	
chore(uploads): Reorganise, change uploads package to storage (#11411)
	


.gitattributes
	
chore(formatting): Formatting 1 of n (#11251)
	


.gitignore
	
chore(deps): update chore (#11042)
	


.gitpod.yml
	
chore(formatting): Formatting 1 of n (#11251)
	


.prettierignore
	
chore(prettier): Ignore a few docs pages because of prettier issue (#…
	


.yarnrc.yml
	
chore(deps): update yarn to v4 (#9343)
	


CHANGELOG.md
	
fix(esm): use CJS wrapper for ESM default interop (#10119)
	


CODE_OF_CONDUCT.md
	
Add David Price to enforcement section.
	


CONTRIBUTING.md
	
chore(formatting): Format readme files (#11248)
	


CONTRIBUTORS.md
	
chore(formatting): Format readme files (#11248)
	


LICENSE
	
Update year in LICENSE (#2135)
	


README.md
	
chore(readme): Add my middle initials (#11310)
	


SECURITY.md
	
chore(formatting): Format readme files (#11248)
	


babel.config.js
	
Use TS 5.3 import attributes (#9591)
	


lerna.json
	
restore workspace:* in package.json files
	


nx.json
	
chore(formatting): Formatting 1 of n (#11251)
	


package.json
	
chore(deps) re-upgrade to yarn 4.6.0 (#11911)
	


prettier.config.js
	
chore(lint): fix prettier configs and ignores (#11295)
	


tsconfig.compilerOption.json
	
Disable unused imports/ vars/ params in TypeScript compiler, opt for …
	


tsconfig.eslint.json
	
chore(lint): enable '@typescript-eslint/only-throw-error' (#11260)
	


tsconfig.json
	
chore: update lerna to 5.1 and enable nx (#5759)
	


yarn.config.cjs
	
chore(yarn): update to use js config for constraints (#11290)
	


yarn.lock
	
fix(deps): update dependency isbot to v5.1.21 (#11912)
	
Repository files navigation
README
Code of conduct
MIT license
Security

Redwood

by Tom Preston-Werner, Peter Pistorius, Rob Cameron, David Price, and more than 250 amazing contributors (see end of file for a full list).

Bighorn Epoch (current development epoch)

NOTE: This section of the Readme is aspirational for the current development epoch we call Bighorn. Bighorn has not yet been released, but when it is, it will fulfill the promises of what you read below. If you’d like to help us on this journey, please say hi in the Community Forums!

Redwood is a framework for quickly creating React-based web applications that provide an amazing end user experience. Our goal is to be simple and approachable enough for use in prototypes and hackathons, but performant and comprehensive enough to evolve into your next startup.

We accomplish this in two primary ways:

Redwood is opinionated and full-stack. We’ve chosen the best technologies in the JS/TS ecosystem and beautifully integrated them into a cohesive framework that lets you get things done instead of endlessly evaluating technology options. You can get started using Redwood without a backend, but the framework really shines when you’re building a data driven application. Our transparent data fetching and optional GraphQL API make building and growing your application easier than you expect!

Redwood’s declarative data fetching and simple form submission features are built on top of RSC + Server Actions and simplify common use cases so you can focus on your users’ experience. Creating the best, most responsive user interfaces requires reasoning about whether code should execute on the server or the client. Redwood makes it easy to choose the best execution context for your code by leveraging the power of React Server Components.

The entire framework is built with TypeScript, so you get type safety from the router to the database and everywhere in-between. If you’d rather build your app with JavaScript, you can do that too, and still enjoy great code completion features in your favorite editor.

TRY BIGHORN: While Bighorn does not yet have a production release, we do publish the latest code as canaries, and we welcome you to experiment with them! The best way to get familiar with these canaries is to keep an eye on the Redwood Blog.

Arapahoe Epoch (current stable release)

Redwood is an opinionated, full-stack, JavaScript/TypeScript web application framework designed to keep you moving fast as your app grows from side project to startup.

At the highest level, a Redwood app is a React frontend that talks to a custom GraphQL API. The API uses Prisma to operate on a database. Out of the box you get tightly integrated testing with Jest, logging with Pino, and a UI component catalog with Storybook. Setting up authentication (like Auth0) or CSS frameworks (like Tailwind CSS) are a single command line invocation away. And to top it off, Redwood's architecture allows you to deploy to either serverless providers (e.g. Netlify, Vercel) or traditional server and container providers (e.g. AWS, Render) with nearly no code changes between the two!

By making a lot of decisions for you, Redwood lets you get to work on what makes your application special, instead of wasting cycles choosing and re-choosing various technologies and configurations. Plus, because Redwood is a proper framework, you benefit from continued performance and feature upgrades over time and with minimum effort.

TUTORIAL: The best way to get to know Redwood is by going through the extensive Redwood Tutorial. Have fun!

QUICK START: You can install and run a full-stack Redwood application on your machine with only a couple commands. Check out the Quick Start guide to get started.

DOCS: Visit the full RedwoodJS Documentation for extensive reference docs and guides.

About

Redwood is the latest open source project initiated by Tom Preston-Werner, cofounder of GitHub (most popular code host on the planet), creator of Jekyll (one of the first and most popular static site generators), creator of Gravatar (the most popular avatar service on the planet), author of the Semantic Versioning specification (powers the Node packaging ecosystem), and inventor of TOML (an obvious, minimal configuration language used by many projects).

Technologies

We are obsessed with developer experience and eliminating as much boilerplate as possible. Where existing libraries elegantly solve our problems, we use them; where they don't, we write our own solutions. The end result is a JavaScript development experience you can fall in love with!

Here's a quick taste of the technologies a standard Redwood application will use:

React
Vite
Prisma
Jest
Storybook
Pino

If you'd like to use our optional built-in GraphQL API support, here's our stack:

GraphQL
GraphQL Yoga
Envelop
Apollo Client
Roadmap

A framework like Redwood has a lot of moving parts; the Roadmap is a great way to get a high-level overview of where the framework is relative to where we want it to be. And since we link to all of our GitHub project boards, it's also a great way to get involved! Roadmap

Why is it called Redwood?

(A history, by Tom Preston-Werner)

Where I live in Northern California there is a type of tree called a redwood. Redwoods are HUGE, the tallest in the world, some topping out at 115 meters (380 feet) in height. The eldest of the still-living redwoods sprouted from the ground an astonishing 3,200 years ago. To stand among them is transcendent. Sometimes, when I need to think or be creative, I will journey to my favorite grove of redwoods and walk among these giants, soaking myself in their silent grandeur.

In addition, Redwoods have a few properties that I thought would be aspirational for my nascent web app framework. Namely:

Redwoods are beautiful as saplings, and grow to be majestic. What if you could feel that way about your web app?

Redwood pinecones are dense and surprisingly small. Can we allow you to get more done with less code?

Redwood trees are resistant to fire. Surprisingly robust to disaster scenarios, just like a great web framework should be!

Redwoods appear complex from afar, but simple up close. Their branching structure provides order and allows for emergent complexity within a simple framework. Can a web framework do the same?

And there you have it.

Contributors

A gigantic "Thank YOU!" to everyone below who has contributed to one or more Redwood projects: Framework, Website, Docs, and Create-Redwood Template. 🚀

Core Team: Leadership

Amy Haywood Dutton	
David Price	
Tobbe Lundberg	
Tom Preston-Werner
Core Team: Maintainer and Community Leads

David Thyresson
maintainer	
Daniel Choudhury
maintainer	
Keith T Elliot
community	
Barrett Burnworth
community	
Josh GM Walker
maintainer
Founders

Tom Preston-Werner	
Peter Pistorius	
Rob Cameron	
David Price
Core Team: Alumni

Aldo Bucchi
	
Aditya Pandey
	
Amanda Giannelli
	
Alice Zhao
	
Simon Gagnon


Chris van der Merwe
	
Ryan Lockard
	
Peter Colapietro
	
noire.munich	
Forrest Hayes


Robert
	
Anthony Campolo
	
Claire Froelich
	
Kim-Adeline Miguel
	
Dominic Saadi


Kris Coulson

All Contributors

Anton Moiseev	
Mohsen Azimi	
Christopher Burns	
Terris Kremer	
James George

Brett Jackson	
Guilherme Pacheco	
Kasper Mikiewicz	
chris-hailstorm	
Jai

Lachlan Campbell	
Satya Rohith	
Steven Normore	
Mads Rosenberg	
Ted Stoychev

eurobob	
Vikash	
Adrian Mato	
Anirudh Nimmagadda	
Ben McCann

Chris Ball	
Suvash Thapaliya	
Thieffen Delabaere	
swyx	
Max Leon

Maxim Geerinck	
Niket Patel	
0xflotus	
Anthony Powell	
Aryan J

Brian Ketelsen	
Dominic Chapman	
Evan Moncuso	
Georgy Petukhov	
Gianni Moschini

Giel	
Jani Monoses	
Johan Eliasson	
Leonardo Elias	
Logan Houp

Loren ☺️	
Mark Pollmann	
Matthew Leffler	
Michele Gerarduzzi	
Nick Gill

Nicholas Joy Christ	
Olivier Lance	
Phuoc Do	
Rocky Meza	
Sharan Kumar S

Simeon Griggs	
Taylor Milliman	
Zach Hammer	
Przemyslaw T	
Hemil Desai

Alessio Montel	
Anthony Morris	
Beto	
Turadg Aleahmad	
Paul Karayan

Nikolas	
guledali	
Yong Joseph Bakos	
Gerd Jungbluth	
James Highsmith

Troy Rosenberg	
Amr Fahim	
dfundingsland	
Eduardo Reveles	
Jeffrey Horn

matthewhembree	
Robert Bolender	
Shivam Chahar	
Aaron Sumner	
Alvin Crespo

Chris Ellis	
Colin Ross	
Dennis Dang	
Derrick Pelletier	
Jeroen van Baarsen

Matan Kushner	
Matthew Rathbone	
Michal Weisman	
Miguel Oller	
Mudassar Ali

Nate Finch	
Paweł Kowalski	
Punit Makwana	
Scott Chacon	
scott

Scott Walkinshaw	
Stephan van Diepen	
bpenno	
Tim Trautman	
Zachary McKenna

Ryan Hayes	
Evan Weaver	
cr1at0rs	
qooqu	
Android Dev Notes

Jeremy Kratz	
Monica Powell	
Ganesh Rane	
Ryan Doyle	
Matt Reetz

Punit Makwana	
shzmr	
esteban-url	
Kurt Hutten	
António Meireles

Brent Guffens	
Santhosh Laguduwa	
Marco Bucchi	
Johnny Choudhury-Lucas	
Steven Almeroth

lumenCodes	
_robobunny	
Kevin Poston	
Davy Hausser	
Mohinder Saluja

Lamanda	
ryancwalsh	
Nick Geerts	
miku86	
Krisztiaan

Jonathan Derrough	
Asdethprime	
Brian Solon	
Chris Chapman	
Joël Galeran

Mariah	
Tyler Scott Williams	
Vania Kucher	
Viren Bhagat	
William

dcgoodwin2112	
Bennett Rogers	
Daniel O'Neill	
David Yu	
Adithya Sunil

Edward Jiang	
Manuel Kallenbach	
Nick Schmitt	
Jon Meyers	
Matthew Bush

Patrick Gallagher	
Himank Pathak	
Morgan Spencer	
Pedro Piñera Buendía	
Matt Sutkowski

Justin Etheredge	
Zain Fathoni	
Shrill Shrestha	
Brent Anderson	
Vinaya Sathyanarayana

Will Minshew	
Tawfik Yasser	
Sébastien Lorber	
Charlie Ray	
Kim, Jang-hwan

TagawaHirotaka	
Andrew Lam	
Brandon DuRette	
Curtis Reimer	
Kevin Brown

Nikolaj Ivancic	
Nuno Pato	
Renan Andrade	
Sai Deepesh	
bl-ue

Sven Hanssen	
Mudassar Ali	
SangHee Kim	
Subhash Chandra	
KimSeonghyeon

Zhihao Cui	
Kyle Corbitt	
Sean Doughty	
Zak Mandhro	
bozdoz

Isaac Tait	
Jace	
Noah Bernsohn	
rene-demonsters	
Sergey Sharov

Tim Pap	
in-in	
mlabate	
Pablo Dejuan	
bugsfunny

Luís Pinto	
Leigh Halliday	
BlackHawkSigma	
Devin MacGillivray	
Francisco Jaramillo

Orta Therox	
Tharshan Muthulingam	
Brian Liu	
allen joslin	
Ryan Wang

Vashiru	
Ron Dyar	
Todd Pressley	
Zack Sheppard	
AlbertGao

vchoy	
Daniel Macovei	
Peter Perlepes	
Benedict Adams	
Hampus Kraft

Harun Kilic	
Mike Nikles	
Mohammad Shahbaz Alam	
Moulik Aggarwal	
Omar El-Domeiri

Paul McKellar	
Sarthak Mohanty	
Justin Jurenka	
Jens Lindström	
Hampus Kraft

Ryan Chenkie	
George Cameron	
John	
Shannon Smith	
Bob

facinick	
Teodoro Villaneuva	
Sarvesh Limaye	
Shantanu Zadbuke	
Duke Manh

Michael Marino	
Igor Savin	
Jacob Arriola	
Jingying Gu	
Tim Kolberger

nzdjb	
Hannah Vivian Shaw	
usman kareemee	
watway	
Edward Mason

Mateo Carriquí	
kataqatsi	
Jeff Schroeder	
mnm	
BBurnworth

Jonathan	
Rishabh Poddar	
Vitalii Melnychuk	
Buck DeFore	
Kamarel Malanda

Manuel Vila	
Arda TANRIKULU	
Tristan Lee	
Agustina Chaer	
Charles Tison

Josema Sar	
Ken Greeff	
Wiktor Sienkiewicz	
Alejandro Frias	
Aleksandra

Ian McPhail	
Kyle Stewart	
Laurin Quast	
Martin Juhasz	
Odee

Stephen Handley	
Syeda Zainab	
joriswill	
szainab	
twodotsmax

Michael Shilman	
nickpdemarco	
davidlcorbitt	
ROZBEH	
Anh Le (Andy)

IsaacHook	
Matt Sears	
MthBarber	
Safi Nettah	
dietler

Guedis	
rkmitra1	
m3t	
Brandon Bayer	
Matt Murphy

jessicard	
Pete McCarthy	
Philzen	
Vik	
Carl Hallén Jansson

Chen Liu	
Manish	
Zach Peters	
Benas Mandravickas	
COCL2022

Ella	
Eric Kitaif	
Giuseppe Caruso	
Ian Walter	
Jedde Bowman

Johan Eliasson	
Lee Staples	
Leo Thorp	
Matthieu Napoli	
Nik F P

Olyno	
Robert Tirta	
The Ape Collector	
ccnklc	
cremno

dkmooers	
hbellahc	
hello there	
llmaboi	
Changsoon Bok

Kristoffer K.	
Justin Kuntz	
Paine Leffler	
Paul Venable	
Peter Chen

Yann	
Andre Wruszczak	
Anton Mihaylov	
Miguel Parramón	
Fabio Lazzaroni

Rushabh Javeri	
Anders Søgaard	
kunalarya	
Aleph Retamal	
Alon

Bouzid Badreddine	
Charly POLY	
Guillaume Mantopoulos	
Jan Henning	
Jonas Oberschweiber

Jordan Rolph	
Jorge Venegas	
Kolja Lampe	
Leon	
Masvoras

Min ho Kim	
Pin Sern	
RUI OKAZAKI	
Syahrizal Ardana	
craineum

hello there	
Matt Driscoll	
paikwiki	
Mark Wiemer	
Alex Hughes

Erica Pisani	
Fatih Altinok	
Kris	
Krupali Makadiya	
Malted

Michelle Greer	
Nikola Hristov	
Swarit Choudhari	
Lina	
pwellner

Jay O'Conor	
Stan Duprey	
Victor Savkin	
Łukasz Sowa	
Andrew Lam

Daniel Jalkut	
Eli	
NoahC5	
Tommy Marshall	
Zachary Vander Velden

pantheredeye	
Kirby Douglas Ellingson	
Sergio Guzman	
Eric Howey	
Erik Guzman

IRSHAD WANI	
Niall	
Nikola Hristov	
Rui Okazaki	
Sunjay Armstead

Justin	
kam c.	
makdeb	
payapula	
willks

Josh GM Walker	
Ari Mendelow	
Jake Zhao	
psirus0588	
Eric Rabinowitz

Maximilian Raschle	
nikolaxhristov	
Alon Bukai	
Han Ke	
Matt Chapman

Rowin Mol	
Christopher Burns	
Alex Lilly	
dphuang2	
Daniel Escoto

James Hester	
Guillaume Mantopoulos	
Linus Timm	
Mina Abadir	
Tom Dickson

Tyler	
Christian Bergschneider	
Emre Erdoğan	
Toshinori Tsugita	
Ajit Kumar Goel

Tai Vo	
Sam Huang	
Stefanos Anagnostou	
dennemark	
Aaron Rackley (EverydayTinkerer)

Brent Scheibelhut	
Cal Courtney	
Jai Srivastav	
Tilmann	
cheddar

Bryan Clark	
Carl Lange	
Chris Davis	
David Kus	
Flouse

Hannes Tiede	
Lucas-Bide	
Martin Váňa	
Chris Rogers	
Samanvay Karambhe

alireza rais sattari	
aslaker	
zach-withcoherence	
tuxcommunity	
Ted

Dalton Craven	
Drikus Roor	
Eka	
ModupeD	
Nemi Shah

Rodrigo Medina	
Russell Anthony	
Jason Daniel	
ray hatfield	
swyx.io

BWizard06	
Bigood	
Cristi Ciobanu	
Gilliard Macedo	
Lee Ravenberg

Matthew Phillips	
Rui Lima	
Sheng Chou	
yahhuh

Redwood projects (mostly) follow the all-contributions specification. Contributions of any kind are welcome.

About

The App Framework for Startups

redwoodjs.com
Topics
react graphql apollo jamstack hacktoberfest prisma
Resources
 Readme
License
 MIT license
Code of conduct
 Code of conduct
Security policy
 Security policy
 Activity
 Custom properties
Stars
 17.5k stars
Watchers
 100 watching
Forks
 1k forks
Report repository


Releases 299
v8.4.2
Latest
+ 298 releases


Packages
No packages published



Used by 5.4k
+ 5,431


Contributors
447
+ 433 contributors


Languages
TypeScript
62.9%
 
JavaScript
36.4%
 
CSS
0.4%
 
HTML
0.1%
 
Shell
0.1%
 
Dockerfile
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
  "title": "GitHub - redwoodjs/redwood: The App Framework for Startups",
  "description": "The App Framework for Startups. Contribute to redwoodjs/redwood development by creating an account on GitHub.",
  "url": "https://github.com/redwoodjs/redwood?screenshot=true",
  "content": "Skip to content\nNavigation Menu\nProduct\nSolutions\nResources\nOpen Source\nEnterprise\nPricing\nSign in\nSign up\nredwoodjs\n/\nredwood\nPublic\nNotifications\nFork 1k\n Star 17.5k\nCode\nIssues\n430\nPull requests\n38\nActions\nProjects\n3\nSecurity\n1\nInsights\nredwoodjs/redwood\n main\nCode\nFolders and files\nName\tLast commit message\tLast commit date\n\nLatest commit\nrenovate[bot]\nfix(deps): update dependency isbot to v5.1.21 (#11912)\n37916c9\n · \nHistory\n12,004 Commits\n\n\n.changesets\n\t\nRevert \"[Router][TS] Auto-complete route names for unauthenticated pr…\n\t\n\n\n.github\n\t\nchore(deps) re-upgrade to yarn 4.6.0 (#11911)\n\t\n\n\n.vscode\n\t\nAdds background job scheduling and execution (#11238)\n\t\n\n\n__fixtures__\n\t\nchore(deps) re-upgrade to yarn 4.6.0 (#11911)\n\t\n\n\ndocs\n\t\nchore(deps) re-upgrade to yarn 4.6.0 (#11911)\n\t\n\n\npackages\n\t\nfix(deps): update dependency isbot to v5.1.21 (#11912)\n\t\n\n\ntasks\n\t\nfeat(dbAuth): Lax SameSite cookie policy (#11889)\n\t\n\n\n.dependency-cruiser.mjs\n\t\nchore(formatting): Formatting 1 of n (#11251)\n\t\n\n\n.editorconfig\n\t\nchore(formatting): Remove 'insert_final_newline' from editor config (#…\n\t\n\n\n.eslintrc.js\n\t\nchore(uploads): Reorganise, change uploads package to storage (#11411)\n\t\n\n\n.gitattributes\n\t\nchore(formatting): Formatting 1 of n (#11251)\n\t\n\n\n.gitignore\n\t\nchore(deps): update chore (#11042)\n\t\n\n\n.gitpod.yml\n\t\nchore(formatting): Formatting 1 of n (#11251)\n\t\n\n\n.prettierignore\n\t\nchore(prettier): Ignore a few docs pages because of prettier issue (#…\n\t\n\n\n.yarnrc.yml\n\t\nchore(deps): update yarn to v4 (#9343)\n\t\n\n\nCHANGELOG.md\n\t\nfix(esm): use CJS wrapper for ESM default interop (#10119)\n\t\n\n\nCODE_OF_CONDUCT.md\n\t\nAdd David Price to enforcement section.\n\t\n\n\nCONTRIBUTING.md\n\t\nchore(formatting): Format readme files (#11248)\n\t\n\n\nCONTRIBUTORS.md\n\t\nchore(formatting): Format readme files (#11248)\n\t\n\n\nLICENSE\n\t\nUpdate year in LICENSE (#2135)\n\t\n\n\nREADME.md\n\t\nchore(readme): Add my middle initials (#11310)\n\t\n\n\nSECURITY.md\n\t\nchore(formatting): Format readme files (#11248)\n\t\n\n\nbabel.config.js\n\t\nUse TS 5.3 import attributes (#9591)\n\t\n\n\nlerna.json\n\t\nrestore workspace:* in package.json files\n\t\n\n\nnx.json\n\t\nchore(formatting): Formatting 1 of n (#11251)\n\t\n\n\npackage.json\n\t\nchore(deps) re-upgrade to yarn 4.6.0 (#11911)\n\t\n\n\nprettier.config.js\n\t\nchore(lint): fix prettier configs and ignores (#11295)\n\t\n\n\ntsconfig.compilerOption.json\n\t\nDisable unused imports/ vars/ params in TypeScript compiler, opt for …\n\t\n\n\ntsconfig.eslint.json\n\t\nchore(lint): enable '@typescript-eslint/only-throw-error' (#11260)\n\t\n\n\ntsconfig.json\n\t\nchore: update lerna to 5.1 and enable nx (#5759)\n\t\n\n\nyarn.config.cjs\n\t\nchore(yarn): update to use js config for constraints (#11290)\n\t\n\n\nyarn.lock\n\t\nfix(deps): update dependency isbot to v5.1.21 (#11912)\n\t\nRepository files navigation\nREADME\nCode of conduct\nMIT license\nSecurity\n\nRedwood\n\nby Tom Preston-Werner, Peter Pistorius, Rob Cameron, David Price, and more than 250 amazing contributors (see end of file for a full list).\n\nBighorn Epoch (current development epoch)\n\nNOTE: This section of the Readme is aspirational for the current development epoch we call Bighorn. Bighorn has not yet been released, but when it is, it will fulfill the promises of what you read below. If you’d like to help us on this journey, please say hi in the Community Forums!\n\nRedwood is a framework for quickly creating React-based web applications that provide an amazing end user experience. Our goal is to be simple and approachable enough for use in prototypes and hackathons, but performant and comprehensive enough to evolve into your next startup.\n\nWe accomplish this in two primary ways:\n\nRedwood is opinionated and full-stack. We’ve chosen the best technologies in the JS/TS ecosystem and beautifully integrated them into a cohesive framework that lets you get things done instead of endlessly evaluating technology options. You can get started using Redwood without a backend, but the framework really shines when you’re building a data driven application. Our transparent data fetching and optional GraphQL API make building and growing your application easier than you expect!\n\nRedwood’s declarative data fetching and simple form submission features are built on top of RSC + Server Actions and simplify common use cases so you can focus on your users’ experience. Creating the best, most responsive user interfaces requires reasoning about whether code should execute on the server or the client. Redwood makes it easy to choose the best execution context for your code by leveraging the power of React Server Components.\n\nThe entire framework is built with TypeScript, so you get type safety from the router to the database and everywhere in-between. If you’d rather build your app with JavaScript, you can do that too, and still enjoy great code completion features in your favorite editor.\n\nTRY BIGHORN: While Bighorn does not yet have a production release, we do publish the latest code as canaries, and we welcome you to experiment with them! The best way to get familiar with these canaries is to keep an eye on the Redwood Blog.\n\nArapahoe Epoch (current stable release)\n\nRedwood is an opinionated, full-stack, JavaScript/TypeScript web application framework designed to keep you moving fast as your app grows from side project to startup.\n\nAt the highest level, a Redwood app is a React frontend that talks to a custom GraphQL API. The API uses Prisma to operate on a database. Out of the box you get tightly integrated testing with Jest, logging with Pino, and a UI component catalog with Storybook. Setting up authentication (like Auth0) or CSS frameworks (like Tailwind CSS) are a single command line invocation away. And to top it off, Redwood's architecture allows you to deploy to either serverless providers (e.g. Netlify, Vercel) or traditional server and container providers (e.g. AWS, Render) with nearly no code changes between the two!\n\nBy making a lot of decisions for you, Redwood lets you get to work on what makes your application special, instead of wasting cycles choosing and re-choosing various technologies and configurations. Plus, because Redwood is a proper framework, you benefit from continued performance and feature upgrades over time and with minimum effort.\n\nTUTORIAL: The best way to get to know Redwood is by going through the extensive Redwood Tutorial. Have fun!\n\nQUICK START: You can install and run a full-stack Redwood application on your machine with only a couple commands. Check out the Quick Start guide to get started.\n\nDOCS: Visit the full RedwoodJS Documentation for extensive reference docs and guides.\n\nAbout\n\nRedwood is the latest open source project initiated by Tom Preston-Werner, cofounder of GitHub (most popular code host on the planet), creator of Jekyll (one of the first and most popular static site generators), creator of Gravatar (the most popular avatar service on the planet), author of the Semantic Versioning specification (powers the Node packaging ecosystem), and inventor of TOML (an obvious, minimal configuration language used by many projects).\n\nTechnologies\n\nWe are obsessed with developer experience and eliminating as much boilerplate as possible. Where existing libraries elegantly solve our problems, we use them; where they don't, we write our own solutions. The end result is a JavaScript development experience you can fall in love with!\n\nHere's a quick taste of the technologies a standard Redwood application will use:\n\nReact\nVite\nPrisma\nJest\nStorybook\nPino\n\nIf you'd like to use our optional built-in GraphQL API support, here's our stack:\n\nGraphQL\nGraphQL Yoga\nEnvelop\nApollo Client\nRoadmap\n\nA framework like Redwood has a lot of moving parts; the Roadmap is a great way to get a high-level overview of where the framework is relative to where we want it to be. And since we link to all of our GitHub project boards, it's also a great way to get involved! Roadmap\n\nWhy is it called Redwood?\n\n(A history, by Tom Preston-Werner)\n\nWhere I live in Northern California there is a type of tree called a redwood. Redwoods are HUGE, the tallest in the world, some topping out at 115 meters (380 feet) in height. The eldest of the still-living redwoods sprouted from the ground an astonishing 3,200 years ago. To stand among them is transcendent. Sometimes, when I need to think or be creative, I will journey to my favorite grove of redwoods and walk among these giants, soaking myself in their silent grandeur.\n\nIn addition, Redwoods have a few properties that I thought would be aspirational for my nascent web app framework. Namely:\n\nRedwoods are beautiful as saplings, and grow to be majestic. What if you could feel that way about your web app?\n\nRedwood pinecones are dense and surprisingly small. Can we allow you to get more done with less code?\n\nRedwood trees are resistant to fire. Surprisingly robust to disaster scenarios, just like a great web framework should be!\n\nRedwoods appear complex from afar, but simple up close. Their branching structure provides order and allows for emergent complexity within a simple framework. Can a web framework do the same?\n\nAnd there you have it.\n\nContributors\n\nA gigantic \"Thank YOU!\" to everyone below who has contributed to one or more Redwood projects: Framework, Website, Docs, and Create-Redwood Template. 🚀\n\nCore Team: Leadership\n\nAmy Haywood Dutton\t\nDavid Price\t\nTobbe Lundberg\t\nTom Preston-Werner\nCore Team: Maintainer and Community Leads\n\nDavid Thyresson\nmaintainer\t\nDaniel Choudhury\nmaintainer\t\nKeith T Elliot\ncommunity\t\nBarrett Burnworth\ncommunity\t\nJosh GM Walker\nmaintainer\nFounders\n\nTom Preston-Werner\t\nPeter Pistorius\t\nRob Cameron\t\nDavid Price\nCore Team: Alumni\n\nAldo Bucchi\n\t\nAditya Pandey\n\t\nAmanda Giannelli\n\t\nAlice Zhao\n\t\nSimon Gagnon\n\n\nChris van der Merwe\n\t\nRyan Lockard\n\t\nPeter Colapietro\n\t\nnoire.munich\t\nForrest Hayes\n\n\nRobert\n\t\nAnthony Campolo\n\t\nClaire Froelich\n\t\nKim-Adeline Miguel\n\t\nDominic Saadi\n\n\nKris Coulson\n\nAll Contributors\n\nAnton Moiseev\t\nMohsen Azimi\t\nChristopher Burns\t\nTerris Kremer\t\nJames George\n\nBrett Jackson\t\nGuilherme Pacheco\t\nKasper Mikiewicz\t\nchris-hailstorm\t\nJai\n\nLachlan Campbell\t\nSatya Rohith\t\nSteven Normore\t\nMads Rosenberg\t\nTed Stoychev\n\neurobob\t\nVikash\t\nAdrian Mato\t\nAnirudh Nimmagadda\t\nBen McCann\n\nChris Ball\t\nSuvash Thapaliya\t\nThieffen Delabaere\t\nswyx\t\nMax Leon\n\nMaxim Geerinck\t\nNiket Patel\t\n0xflotus\t\nAnthony Powell\t\nAryan J\n\nBrian Ketelsen\t\nDominic Chapman\t\nEvan Moncuso\t\nGeorgy Petukhov\t\nGianni Moschini\n\nGiel\t\nJani Monoses\t\nJohan Eliasson\t\nLeonardo Elias\t\nLogan Houp\n\nLoren ☺️\t\nMark Pollmann\t\nMatthew Leffler\t\nMichele Gerarduzzi\t\nNick Gill\n\nNicholas Joy Christ\t\nOlivier Lance\t\nPhuoc Do\t\nRocky Meza\t\nSharan Kumar S\n\nSimeon Griggs\t\nTaylor Milliman\t\nZach Hammer\t\nPrzemyslaw T\t\nHemil Desai\n\nAlessio Montel\t\nAnthony Morris\t\nBeto\t\nTuradg Aleahmad\t\nPaul Karayan\n\nNikolas\t\nguledali\t\nYong Joseph Bakos\t\nGerd Jungbluth\t\nJames Highsmith\n\nTroy Rosenberg\t\nAmr Fahim\t\ndfundingsland\t\nEduardo Reveles\t\nJeffrey Horn\n\nmatthewhembree\t\nRobert Bolender\t\nShivam Chahar\t\nAaron Sumner\t\nAlvin Crespo\n\nChris Ellis\t\nColin Ross\t\nDennis Dang\t\nDerrick Pelletier\t\nJeroen van Baarsen\n\nMatan Kushner\t\nMatthew Rathbone\t\nMichal Weisman\t\nMiguel Oller\t\nMudassar Ali\n\nNate Finch\t\nPaweł Kowalski\t\nPunit Makwana\t\nScott Chacon\t\nscott\n\nScott Walkinshaw\t\nStephan van Diepen\t\nbpenno\t\nTim Trautman\t\nZachary McKenna\n\nRyan Hayes\t\nEvan Weaver\t\ncr1at0rs\t\nqooqu\t\nAndroid Dev Notes\n\nJeremy Kratz\t\nMonica Powell\t\nGanesh Rane\t\nRyan Doyle\t\nMatt Reetz\n\nPunit Makwana\t\nshzmr\t\nesteban-url\t\nKurt Hutten\t\nAntónio Meireles\n\nBrent Guffens\t\nSanthosh Laguduwa\t\nMarco Bucchi\t\nJohnny Choudhury-Lucas\t\nSteven Almeroth\n\nlumenCodes\t\n_robobunny\t\nKevin Poston\t\nDavy Hausser\t\nMohinder Saluja\n\nLamanda\t\nryancwalsh\t\nNick Geerts\t\nmiku86\t\nKrisztiaan\n\nJonathan Derrough\t\nAsdethprime\t\nBrian Solon\t\nChris Chapman\t\nJoël Galeran\n\nMariah\t\nTyler Scott Williams\t\nVania Kucher\t\nViren Bhagat\t\nWilliam\n\ndcgoodwin2112\t\nBennett Rogers\t\nDaniel O'Neill\t\nDavid Yu\t\nAdithya Sunil\n\nEdward Jiang\t\nManuel Kallenbach\t\nNick Schmitt\t\nJon Meyers\t\nMatthew Bush\n\nPatrick Gallagher\t\nHimank Pathak\t\nMorgan Spencer\t\nPedro Piñera Buendía\t\nMatt Sutkowski\n\nJustin Etheredge\t\nZain Fathoni\t\nShrill Shrestha\t\nBrent Anderson\t\nVinaya Sathyanarayana\n\nWill Minshew\t\nTawfik Yasser\t\nSébastien Lorber\t\nCharlie Ray\t\nKim, Jang-hwan\n\nTagawaHirotaka\t\nAndrew Lam\t\nBrandon DuRette\t\nCurtis Reimer\t\nKevin Brown\n\nNikolaj Ivancic\t\nNuno Pato\t\nRenan Andrade\t\nSai Deepesh\t\nbl-ue\n\nSven Hanssen\t\nMudassar Ali\t\nSangHee Kim\t\nSubhash Chandra\t\nKimSeonghyeon\n\nZhihao Cui\t\nKyle Corbitt\t\nSean Doughty\t\nZak Mandhro\t\nbozdoz\n\nIsaac Tait\t\nJace\t\nNoah Bernsohn\t\nrene-demonsters\t\nSergey Sharov\n\nTim Pap\t\nin-in\t\nmlabate\t\nPablo Dejuan\t\nbugsfunny\n\nLuís Pinto\t\nLeigh Halliday\t\nBlackHawkSigma\t\nDevin MacGillivray\t\nFrancisco Jaramillo\n\nOrta Therox\t\nTharshan Muthulingam\t\nBrian Liu\t\nallen joslin\t\nRyan Wang\n\nVashiru\t\nRon Dyar\t\nTodd Pressley\t\nZack Sheppard\t\nAlbertGao\n\nvchoy\t\nDaniel Macovei\t\nPeter Perlepes\t\nBenedict Adams\t\nHampus Kraft\n\nHarun Kilic\t\nMike Nikles\t\nMohammad Shahbaz Alam\t\nMoulik Aggarwal\t\nOmar El-Domeiri\n\nPaul McKellar\t\nSarthak Mohanty\t\nJustin Jurenka\t\nJens Lindström\t\nHampus Kraft\n\nRyan Chenkie\t\nGeorge Cameron\t\nJohn\t\nShannon Smith\t\nBob\n\nfacinick\t\nTeodoro Villaneuva\t\nSarvesh Limaye\t\nShantanu Zadbuke\t\nDuke Manh\n\nMichael Marino\t\nIgor Savin\t\nJacob Arriola\t\nJingying Gu\t\nTim Kolberger\n\nnzdjb\t\nHannah Vivian Shaw\t\nusman kareemee\t\nwatway\t\nEdward Mason\n\nMateo Carriquí\t\nkataqatsi\t\nJeff Schroeder\t\nmnm\t\nBBurnworth\n\nJonathan\t\nRishabh Poddar\t\nVitalii Melnychuk\t\nBuck DeFore\t\nKamarel Malanda\n\nManuel Vila\t\nArda TANRIKULU\t\nTristan Lee\t\nAgustina Chaer\t\nCharles Tison\n\nJosema Sar\t\nKen Greeff\t\nWiktor Sienkiewicz\t\nAlejandro Frias\t\nAleksandra\n\nIan McPhail\t\nKyle Stewart\t\nLaurin Quast\t\nMartin Juhasz\t\nOdee\n\nStephen Handley\t\nSyeda Zainab\t\njoriswill\t\nszainab\t\ntwodotsmax\n\nMichael Shilman\t\nnickpdemarco\t\ndavidlcorbitt\t\nROZBEH\t\nAnh Le (Andy)\n\nIsaacHook\t\nMatt Sears\t\nMthBarber\t\nSafi Nettah\t\ndietler\n\nGuedis\t\nrkmitra1\t\nm3t\t\nBrandon Bayer\t\nMatt Murphy\n\njessicard\t\nPete McCarthy\t\nPhilzen\t\nVik\t\nCarl Hallén Jansson\n\nChen Liu\t\nManish\t\nZach Peters\t\nBenas Mandravickas\t\nCOCL2022\n\nElla\t\nEric Kitaif\t\nGiuseppe Caruso\t\nIan Walter\t\nJedde Bowman\n\nJohan Eliasson\t\nLee Staples\t\nLeo Thorp\t\nMatthieu Napoli\t\nNik F P\n\nOlyno\t\nRobert Tirta\t\nThe Ape Collector\t\nccnklc\t\ncremno\n\ndkmooers\t\nhbellahc\t\nhello there\t\nllmaboi\t\nChangsoon Bok\n\nKristoffer K.\t\nJustin Kuntz\t\nPaine Leffler\t\nPaul Venable\t\nPeter Chen\n\nYann\t\nAndre Wruszczak\t\nAnton Mihaylov\t\nMiguel Parramón\t\nFabio Lazzaroni\n\nRushabh Javeri\t\nAnders Søgaard\t\nkunalarya\t\nAleph Retamal\t\nAlon\n\nBouzid Badreddine\t\nCharly POLY\t\nGuillaume Mantopoulos\t\nJan Henning\t\nJonas Oberschweiber\n\nJordan Rolph\t\nJorge Venegas\t\nKolja Lampe\t\nLeon\t\nMasvoras\n\nMin ho Kim\t\nPin Sern\t\nRUI OKAZAKI\t\nSyahrizal Ardana\t\ncraineum\n\nhello there\t\nMatt Driscoll\t\npaikwiki\t\nMark Wiemer\t\nAlex Hughes\n\nErica Pisani\t\nFatih Altinok\t\nKris\t\nKrupali Makadiya\t\nMalted\n\nMichelle Greer\t\nNikola Hristov\t\nSwarit Choudhari\t\nLina\t\npwellner\n\nJay O'Conor\t\nStan Duprey\t\nVictor Savkin\t\nŁukasz Sowa\t\nAndrew Lam\n\nDaniel Jalkut\t\nEli\t\nNoahC5\t\nTommy Marshall\t\nZachary Vander Velden\n\npantheredeye\t\nKirby Douglas Ellingson\t\nSergio Guzman\t\nEric Howey\t\nErik Guzman\n\nIRSHAD WANI\t\nNiall\t\nNikola Hristov\t\nRui Okazaki\t\nSunjay Armstead\n\nJustin\t\nkam c.\t\nmakdeb\t\npayapula\t\nwillks\n\nJosh GM Walker\t\nAri Mendelow\t\nJake Zhao\t\npsirus0588\t\nEric Rabinowitz\n\nMaximilian Raschle\t\nnikolaxhristov\t\nAlon Bukai\t\nHan Ke\t\nMatt Chapman\n\nRowin Mol\t\nChristopher Burns\t\nAlex Lilly\t\ndphuang2\t\nDaniel Escoto\n\nJames Hester\t\nGuillaume Mantopoulos\t\nLinus Timm\t\nMina Abadir\t\nTom Dickson\n\nTyler\t\nChristian Bergschneider\t\nEmre Erdoğan\t\nToshinori Tsugita\t\nAjit Kumar Goel\n\nTai Vo\t\nSam Huang\t\nStefanos Anagnostou\t\ndennemark\t\nAaron Rackley (EverydayTinkerer)\n\nBrent Scheibelhut\t\nCal Courtney\t\nJai Srivastav\t\nTilmann\t\ncheddar\n\nBryan Clark\t\nCarl Lange\t\nChris Davis\t\nDavid Kus\t\nFlouse\n\nHannes Tiede\t\nLucas-Bide\t\nMartin Váňa\t\nChris Rogers\t\nSamanvay Karambhe\n\nalireza rais sattari\t\naslaker\t\nzach-withcoherence\t\ntuxcommunity\t\nTed\n\nDalton Craven\t\nDrikus Roor\t\nEka\t\nModupeD\t\nNemi Shah\n\nRodrigo Medina\t\nRussell Anthony\t\nJason Daniel\t\nray hatfield\t\nswyx.io\n\nBWizard06\t\nBigood\t\nCristi Ciobanu\t\nGilliard Macedo\t\nLee Ravenberg\n\nMatthew Phillips\t\nRui Lima\t\nSheng Chou\t\nyahhuh\n\nRedwood projects (mostly) follow the all-contributions specification. Contributions of any kind are welcome.\n\nAbout\n\nThe App Framework for Startups\n\nredwoodjs.com\nTopics\nreact graphql apollo jamstack hacktoberfest prisma\nResources\n Readme\nLicense\n MIT license\nCode of conduct\n Code of conduct\nSecurity policy\n Security policy\n Activity\n Custom properties\nStars\n 17.5k stars\nWatchers\n 100 watching\nForks\n 1k forks\nReport repository\n\n\nReleases 299\nv8.4.2\nLatest\n+ 298 releases\n\n\nPackages\nNo packages published\n\n\n\nUsed by 5.4k\n+ 5,431\n\n\nContributors\n447\n+ 433 contributors\n\n\nLanguages\nTypeScript\n62.9%\n \nJavaScript\n36.4%\n \nCSS\n0.4%\n \nHTML\n0.1%\n \nShell\n0.1%\n \nDockerfile\n0.1%\nFooter\n© 2025 GitHub, Inc.\nFooter navigation\nTerms\nPrivacy\nSecurity\nStatus\nDocs\nContact\nManage cookies\nDo not share my personal information",
  "usage": {
    "tokens": 4773
  }
}
```
