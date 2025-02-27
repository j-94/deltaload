---
title: GitHub - MichaelDeBoey/gatsby-remark-embedder: Gatsby Remark plugin to embed well known services by their URL.
description: Gatsby Remark plugin to embed well known services by their URL. - MichaelDeBoey/gatsby-remark-embedder
url: https://github.com/MichaelDeBoey/gatsby-remark-embedder
timestamp: 2025-01-20T15:31:15.911Z
domain: github.com
path: MichaelDeBoey_gatsby-remark-embedder
---

# GitHub - MichaelDeBoey/gatsby-remark-embedder: Gatsby Remark plugin to embed well known services by their URL.


Gatsby Remark plugin to embed well known services by their URL. - MichaelDeBoey/gatsby-remark-embedder


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
MichaelDeBoey
/
gatsby-remark-embedder
Public
Notifications
Fork 59
 Star 298
Code
Issues
27
Pull requests
14
Actions
Security
Insights
MichaelDeBoey/gatsby-remark-embedder
 main
Code
Folders and files
Name	Last commit message	Last commit date

Latest commit
MichaelDeBoey
feat: support Gatsby 5.x (#245)
e80bce7
 · 
History
213 Commits


.github
	
feat: support Gatsby 5.x (#245)
	


art
	
chore: Optimize images (#35)
	


other
	
chore: rename master to main
	


src
	
chore: fix ESLint errors
	


.all-contributorsrc
	
docs: add jsjoeio as a contributor (#171)
	


.eslintignore
	
chore: Update dependencies
	


.eslintrc.js
	
chore: fix ESLint errors
	


.gitattributes
	
chore: Update dependencies
	


.gitignore
	
chore: Update dependencies
	


.huskyrc.js
	
chore: upgrade all tooling
	


.npmrc
	
chore: upgrade all tooling
	


.nvmrc
	
feat: support Gatsby 5.x (#245)
	


.prettierignore
	
chore: Extend kcd-scripts Prettier config instead of setting it manually
	


.prettierrc.js
	
chore: Update Prettier config
	


CHANGELOG.md
	
Initialize package
	


CODE_OF_CONDUCT.md
	
chore: Cleanup repo
	


CONTRIBUTING.md
	
chore: rename master to main
	


LICENSE
	
chore: upgrade all tooling
	


README.md
	
chore: rename master to main
	


package.json
	
feat: support Gatsby 5.x (#245)
	
Repository files navigation
README
Code of conduct
MIT license
gatsby-remark-embedder

Gatsby Remark plugin to embed well known services by their URL.

       

The problem

Trying to embed well known services (like CodePen, CodeSandbox, GIPHY, Instagram, Lichess, Pinterest, Slides, SoundCloud, Spotify, Streamable, Testing Playground, Twitch, Twitter or YouTube) into your Gatsby website can be hard, since you have to know how this needs to be done for all of these different services.

This solution

gatsby-remark-embedder tries to solve this problem for you by letting you just copy-paste the link to the gif/pen/pin/player/playground/post/sandbox/tweet/video you want to embed right from within your browser onto a separate line (surrounded by empty lines) and replace it with the proper embed-code.

Table of Contents
Installation
Usage
Supported services
CodePen
CodeSandbox
GIPHY
Instagram
Lichess
Pinterest
Slides
SoundCloud
Spotify
Streamable
Testing Playground
Twitch
Twitter
YouTube
Options
customTransformers
services
Inspiration
Issues
🐛 Bugs
💡 Feature Requests
Contributors ✨
LICENSE
Installation

This module is distributed via npm which is bundled with node and should be installed as one of your project's dependencies:

npm install gatsby-remark-embedder

or

yarn add gatsby-remark-embedder

This library has a required peerDependencies listing for gatsby and should be used as a plugin for gatsby-transformer-remark or gatsby-plugin-mdx.
Depending on the services you want to embed, you should also install gatsby-plugin-instagram-embed, gatsby-plugin-pinterest and/or gatsby-plugin-twitter.

Usage
// In your gatsby-config.js

module.exports = {
  // Find the 'plugins' array
  plugins: [
    {
      resolve: `gatsby-transformer-remark`,
      options: {
        plugins: [
          {
            resolve: `gatsby-remark-embedder`,
            options: {
              customTransformers: [
                // Your custom transformers
              ],
              services: {
                // The service-specific options by the name of the service
              },
            },
          },

          // Other plugins here...
        ],
      },
    },
  ],
};

or

// In your gatsby-config.js

module.exports = {
  // Find the 'plugins' array
  plugins: [
    {
      resolve: `gatsby-plugin-mdx`,
      options: {
        gatsbyRemarkPlugins: [
          {
            resolve: `gatsby-remark-embedder`,
            options: {
              customTransformers: [
                // Your custom transformers
              ],
              services: {
                // The service-specific options by the name of the service
              },
            },
          },

          // Other plugins here...
        ],
      },
    },
  ],
};
Supported services
CodePen
Usage
https://codepen.io/team/codepen/pen/PNaGbb
Result
CodeSandbox
Usage
https://codesandbox.io/s/ynn88nx9x?view=split
Result
GIPHY
Usage
https://giphy.com/gifs/howtogiphygifs-how-to-XatG8bioEwwVO
Result
Instagram

The returned HTML snippet from the Instagram transformer will only be automatically recognized as an embedded post when Instagram's embed JavaScript is included on the page.
Since the Instagram transformer doesn't include this JavaScript (because we don't want to include it multiple times on a page when having multiple embeds), you have to include it yourself. The recommended way of including it is by using gatsby-plugin-instagram-embed.

Usage
https://instagram.com/p/B60jPE6J8U-
Result
Options

All options should go under the Instagram namespace.

name	Type	Required	Default	Description
accessToken	string	✅		An App Access Token (recommended) or Client Access Token
accessToken

To get an App Access Token (recommended) or Client Access Token for the Instagram embed, check out the Instagram oEmbed access token docs and requirements.

The safest way to enter your accessToken is to set is as an environment variable.

Example
Lichess
Usage
https://lichess.org/MPJcy1JW
Result
Pinterest

The returned HTML snippet from the Pinterest transformer will only be automatically recognized as an embedded pin when Pinterest's embed JavaScript is included on the page.
Since the Pinterest transformer doesn't include this JavaScript (because we don't want to include it multiple times on a page when having multiple embeds), you have to include it yourself. The recommended way of including it is by using gatsby-plugin-pinterest.

Usage
https://pinterest.com/pin/99360735500167749
Result
Slides
Usage
https://slides.com/kentcdodds/oss-we-want
Result
SoundCloud
Usage
https://soundcloud.com/clemenswenners/africa
Result
Spotify
Usage
https://open.spotify.com/track/0It2bnTdLl2vyymzOkBI3L
Result
Streamable
Usage
https://streamable.com/moo
Result
Testing Playground
Usage
https://testing-playground.com/gist/fb336c386145b235372a0f57d5c58205/6d13e4ee508301c8b42f9d2cc8584e70bb05fb4a
Result
Twitch

Twitch embeds can only be embedded on HTTPS websites. Check out the Gatsby docs for setting this up when developing locally.

Usage
https://twitch.tv/videos/546761743
Result
Options

All options should go under the Twitch namespace.

name	Type	Required	Default	Description
parent	string / string[]	✅		Domain(s) that will be embedding Twitch. You must have one parent key for each domain your site uses.
parent

You could either put in (a) hardcoded value(s) or you could use environment variables that are available during the build process.

Netlify

Netlify has the URL, DEPLOY_URL and DEPLOY_PRIME_URL environment variables. Take a look at the Netlify docs for more info.

Example
Vercel

Vercel has the VERCEL_URL environment variable. Take a look at the Vercel docs for more info.

Example
Twitter

The returned HTML snippet from the Twitter transformer will only be automatically recognized as an Embedded Tweet when Twitter's widget JavaScript is included on the page.
Since the Twitter transformer doesn't include this JavaScript (because we don't want to include it multiple times on a page when having multiple embeds), you have to include it yourself. The recommended way of including it is by using gatsby-plugin-twitter.

Usage
https://twitter.com/MichaelDeBoey93/status/1152991421789548546

https://twitter.com/i/moments/994601867987619840

https://twitter.com/wesbos/timelines/1189618481672667136
Result
YouTube

The YouTube transformer (currently) only supports videos in the following formats:

Full url (https://youtube.com/watch?v=dQw4w9WgXcQ)
Short url (https://youtu.be/dQw4w9WgXcQ)
Usage
https://youtu.be/dQw4w9WgXcQ
Result
Options
customTransformers

The plugin allows you to pass an array of custom transformers that will be executed additionally to the default ones.

Properties

Each transformer should be an object which has the following properties:

getHTML(url, options)

The getHTML method is executed when the given URL has been matched to transform. It should return the transformed HTML.
This asynchronous function receives the URL to transform together with an options object to take into account when transforming.

name

The name is the value that needs to be used as a key in the services plugin option. The value for this key will be provided as the second argument to getHTML.

shouldTransform(url)

The shouldTransform method should check if the given URL matches the one intended to transform. It should return a boolean value.

Example transformer
// some-site-transformer.js
const getHTML = (url) => `<iframe src="${url}"></iframe>`;

const name = 'someSite';

const regex = /^https?:\/\/some-site\.com\//;
const shouldTransform = (url) => regex.test(url);

module.exports = { getHTML, name, shouldTransform };
services

The plugin also allows you to pass an object which keys that represent the name of the service to transform and the value that's an object with options for that specific service.

Inspiration

This whole plugin was extracted out of Kent C. Dodds' personal website.

The intention is to make this available to be used independently.

Issues

Looking to contribute? Look for the Good First Issue label.

🐛 Bugs

Please file an issue for bugs, missing documentation, or unexpected behavior.

See Bugs

💡 Feature Requests

Please file an issue to suggest new features. Vote on feature requests by adding a 👍. This helps maintainers prioritize what to work on.

See Feature Requests

Contributors ✨

Thanks goes to these people (emoji key):


Kent C. Dodds
💻 📖 🤔 🚇 ⚠️	
Michaël De Boey
🐛 💻 📖 ⚠️	
Kornel Dubieniecki
🐛	
Nick Nish
💻 ⚠️	
Caneco
🎨	
Anurag Hazra
🐛 💻 ⚠️ 📖	
Yash Joshi
💻 ⚠️

Christian C. Salvadó
💻 ⚠️	
James Simone
💻 ⚠️	
Agastya Chandrakant
💻 ⚠️	
Fábio Rosado
💻 ⚠️	
Arryangga Aliev Pratamaputra
🐛	
Eduardo Reveles
💻 ⚠️	
Michal Piechowiak
🐛 💻 ⚠️

Brad Garropy
🐛	
Ilya Lyamkin
💻	
Simon MacDonald
🐛 💻 ⚠️	
Nicky Meuleman
💻	
Ayush
💻	
TEEAARBEE
🐛	
Trevor Blades
📖

Titus
⚠️ 👀 💻	
Joe Previte
🐛

This project follows the all-contributors specification. Contributions of any kind welcome!

LICENSE

MIT

About

Gatsby Remark plugin to embed well known services by their URL.

Topics
markdown spotify instagram youtube twitch remark twitter giphy codepen soundcloud slides gatsby pinterest embed streamable codesandbox gatsby-plugin gatsby-remark testing-playground linchess
Resources
 Readme
License
 MIT license
Code of conduct
 Code of conduct
 Activity
Stars
 298 stars
Watchers
 10 watching
Forks
 59 forks
Report repository


Releases 44
v7.0.0
Latest
+ 43 releases


Packages
No packages published



Contributors
22
+ 8 contributors


Languages
JavaScript
100.0%
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
  "title": "GitHub - MichaelDeBoey/gatsby-remark-embedder: Gatsby Remark plugin to embed well known services by their URL.",
  "description": "Gatsby Remark plugin to embed well known services by their URL. - MichaelDeBoey/gatsby-remark-embedder",
  "url": "https://github.com/MichaelDeBoey/gatsby-remark-embedder?screenshot=true",
  "content": "Skip to content\nNavigation Menu\nProduct\nSolutions\nResources\nOpen Source\nEnterprise\nPricing\nSign in\nSign up\nMichaelDeBoey\n/\ngatsby-remark-embedder\nPublic\nNotifications\nFork 59\n Star 298\nCode\nIssues\n27\nPull requests\n14\nActions\nSecurity\nInsights\nMichaelDeBoey/gatsby-remark-embedder\n main\nCode\nFolders and files\nName\tLast commit message\tLast commit date\n\nLatest commit\nMichaelDeBoey\nfeat: support Gatsby 5.x (#245)\ne80bce7\n · \nHistory\n213 Commits\n\n\n.github\n\t\nfeat: support Gatsby 5.x (#245)\n\t\n\n\nart\n\t\nchore: Optimize images (#35)\n\t\n\n\nother\n\t\nchore: rename master to main\n\t\n\n\nsrc\n\t\nchore: fix ESLint errors\n\t\n\n\n.all-contributorsrc\n\t\ndocs: add jsjoeio as a contributor (#171)\n\t\n\n\n.eslintignore\n\t\nchore: Update dependencies\n\t\n\n\n.eslintrc.js\n\t\nchore: fix ESLint errors\n\t\n\n\n.gitattributes\n\t\nchore: Update dependencies\n\t\n\n\n.gitignore\n\t\nchore: Update dependencies\n\t\n\n\n.huskyrc.js\n\t\nchore: upgrade all tooling\n\t\n\n\n.npmrc\n\t\nchore: upgrade all tooling\n\t\n\n\n.nvmrc\n\t\nfeat: support Gatsby 5.x (#245)\n\t\n\n\n.prettierignore\n\t\nchore: Extend kcd-scripts Prettier config instead of setting it manually\n\t\n\n\n.prettierrc.js\n\t\nchore: Update Prettier config\n\t\n\n\nCHANGELOG.md\n\t\nInitialize package\n\t\n\n\nCODE_OF_CONDUCT.md\n\t\nchore: Cleanup repo\n\t\n\n\nCONTRIBUTING.md\n\t\nchore: rename master to main\n\t\n\n\nLICENSE\n\t\nchore: upgrade all tooling\n\t\n\n\nREADME.md\n\t\nchore: rename master to main\n\t\n\n\npackage.json\n\t\nfeat: support Gatsby 5.x (#245)\n\t\nRepository files navigation\nREADME\nCode of conduct\nMIT license\ngatsby-remark-embedder\n\nGatsby Remark plugin to embed well known services by their URL.\n\n       \n\nThe problem\n\nTrying to embed well known services (like CodePen, CodeSandbox, GIPHY, Instagram, Lichess, Pinterest, Slides, SoundCloud, Spotify, Streamable, Testing Playground, Twitch, Twitter or YouTube) into your Gatsby website can be hard, since you have to know how this needs to be done for all of these different services.\n\nThis solution\n\ngatsby-remark-embedder tries to solve this problem for you by letting you just copy-paste the link to the gif/pen/pin/player/playground/post/sandbox/tweet/video you want to embed right from within your browser onto a separate line (surrounded by empty lines) and replace it with the proper embed-code.\n\nTable of Contents\nInstallation\nUsage\nSupported services\nCodePen\nCodeSandbox\nGIPHY\nInstagram\nLichess\nPinterest\nSlides\nSoundCloud\nSpotify\nStreamable\nTesting Playground\nTwitch\nTwitter\nYouTube\nOptions\ncustomTransformers\nservices\nInspiration\nIssues\n🐛 Bugs\n💡 Feature Requests\nContributors ✨\nLICENSE\nInstallation\n\nThis module is distributed via npm which is bundled with node and should be installed as one of your project's dependencies:\n\nnpm install gatsby-remark-embedder\n\nor\n\nyarn add gatsby-remark-embedder\n\nThis library has a required peerDependencies listing for gatsby and should be used as a plugin for gatsby-transformer-remark or gatsby-plugin-mdx.\nDepending on the services you want to embed, you should also install gatsby-plugin-instagram-embed, gatsby-plugin-pinterest and/or gatsby-plugin-twitter.\n\nUsage\n// In your gatsby-config.js\n\nmodule.exports = {\n  // Find the 'plugins' array\n  plugins: [\n    {\n      resolve: `gatsby-transformer-remark`,\n      options: {\n        plugins: [\n          {\n            resolve: `gatsby-remark-embedder`,\n            options: {\n              customTransformers: [\n                // Your custom transformers\n              ],\n              services: {\n                // The service-specific options by the name of the service\n              },\n            },\n          },\n\n          // Other plugins here...\n        ],\n      },\n    },\n  ],\n};\n\nor\n\n// In your gatsby-config.js\n\nmodule.exports = {\n  // Find the 'plugins' array\n  plugins: [\n    {\n      resolve: `gatsby-plugin-mdx`,\n      options: {\n        gatsbyRemarkPlugins: [\n          {\n            resolve: `gatsby-remark-embedder`,\n            options: {\n              customTransformers: [\n                // Your custom transformers\n              ],\n              services: {\n                // The service-specific options by the name of the service\n              },\n            },\n          },\n\n          // Other plugins here...\n        ],\n      },\n    },\n  ],\n};\nSupported services\nCodePen\nUsage\nhttps://codepen.io/team/codepen/pen/PNaGbb\nResult\nCodeSandbox\nUsage\nhttps://codesandbox.io/s/ynn88nx9x?view=split\nResult\nGIPHY\nUsage\nhttps://giphy.com/gifs/howtogiphygifs-how-to-XatG8bioEwwVO\nResult\nInstagram\n\nThe returned HTML snippet from the Instagram transformer will only be automatically recognized as an embedded post when Instagram's embed JavaScript is included on the page.\nSince the Instagram transformer doesn't include this JavaScript (because we don't want to include it multiple times on a page when having multiple embeds), you have to include it yourself. The recommended way of including it is by using gatsby-plugin-instagram-embed.\n\nUsage\nhttps://instagram.com/p/B60jPE6J8U-\nResult\nOptions\n\nAll options should go under the Instagram namespace.\n\nname\tType\tRequired\tDefault\tDescription\naccessToken\tstring\t✅\t\tAn App Access Token (recommended) or Client Access Token\naccessToken\n\nTo get an App Access Token (recommended) or Client Access Token for the Instagram embed, check out the Instagram oEmbed access token docs and requirements.\n\nThe safest way to enter your accessToken is to set is as an environment variable.\n\nExample\nLichess\nUsage\nhttps://lichess.org/MPJcy1JW\nResult\nPinterest\n\nThe returned HTML snippet from the Pinterest transformer will only be automatically recognized as an embedded pin when Pinterest's embed JavaScript is included on the page.\nSince the Pinterest transformer doesn't include this JavaScript (because we don't want to include it multiple times on a page when having multiple embeds), you have to include it yourself. The recommended way of including it is by using gatsby-plugin-pinterest.\n\nUsage\nhttps://pinterest.com/pin/99360735500167749\nResult\nSlides\nUsage\nhttps://slides.com/kentcdodds/oss-we-want\nResult\nSoundCloud\nUsage\nhttps://soundcloud.com/clemenswenners/africa\nResult\nSpotify\nUsage\nhttps://open.spotify.com/track/0It2bnTdLl2vyymzOkBI3L\nResult\nStreamable\nUsage\nhttps://streamable.com/moo\nResult\nTesting Playground\nUsage\nhttps://testing-playground.com/gist/fb336c386145b235372a0f57d5c58205/6d13e4ee508301c8b42f9d2cc8584e70bb05fb4a\nResult\nTwitch\n\nTwitch embeds can only be embedded on HTTPS websites. Check out the Gatsby docs for setting this up when developing locally.\n\nUsage\nhttps://twitch.tv/videos/546761743\nResult\nOptions\n\nAll options should go under the Twitch namespace.\n\nname\tType\tRequired\tDefault\tDescription\nparent\tstring / string[]\t✅\t\tDomain(s) that will be embedding Twitch. You must have one parent key for each domain your site uses.\nparent\n\nYou could either put in (a) hardcoded value(s) or you could use environment variables that are available during the build process.\n\nNetlify\n\nNetlify has the URL, DEPLOY_URL and DEPLOY_PRIME_URL environment variables. Take a look at the Netlify docs for more info.\n\nExample\nVercel\n\nVercel has the VERCEL_URL environment variable. Take a look at the Vercel docs for more info.\n\nExample\nTwitter\n\nThe returned HTML snippet from the Twitter transformer will only be automatically recognized as an Embedded Tweet when Twitter's widget JavaScript is included on the page.\nSince the Twitter transformer doesn't include this JavaScript (because we don't want to include it multiple times on a page when having multiple embeds), you have to include it yourself. The recommended way of including it is by using gatsby-plugin-twitter.\n\nUsage\nhttps://twitter.com/MichaelDeBoey93/status/1152991421789548546\n\nhttps://twitter.com/i/moments/994601867987619840\n\nhttps://twitter.com/wesbos/timelines/1189618481672667136\nResult\nYouTube\n\nThe YouTube transformer (currently) only supports videos in the following formats:\n\nFull url (https://youtube.com/watch?v=dQw4w9WgXcQ)\nShort url (https://youtu.be/dQw4w9WgXcQ)\nUsage\nhttps://youtu.be/dQw4w9WgXcQ\nResult\nOptions\ncustomTransformers\n\nThe plugin allows you to pass an array of custom transformers that will be executed additionally to the default ones.\n\nProperties\n\nEach transformer should be an object which has the following properties:\n\ngetHTML(url, options)\n\nThe getHTML method is executed when the given URL has been matched to transform. It should return the transformed HTML.\nThis asynchronous function receives the URL to transform together with an options object to take into account when transforming.\n\nname\n\nThe name is the value that needs to be used as a key in the services plugin option. The value for this key will be provided as the second argument to getHTML.\n\nshouldTransform(url)\n\nThe shouldTransform method should check if the given URL matches the one intended to transform. It should return a boolean value.\n\nExample transformer\n// some-site-transformer.js\nconst getHTML = (url) => `<iframe src=\"${url}\"></iframe>`;\n\nconst name = 'someSite';\n\nconst regex = /^https?:\\/\\/some-site\\.com\\//;\nconst shouldTransform = (url) => regex.test(url);\n\nmodule.exports = { getHTML, name, shouldTransform };\nservices\n\nThe plugin also allows you to pass an object which keys that represent the name of the service to transform and the value that's an object with options for that specific service.\n\nInspiration\n\nThis whole plugin was extracted out of Kent C. Dodds' personal website.\n\nThe intention is to make this available to be used independently.\n\nIssues\n\nLooking to contribute? Look for the Good First Issue label.\n\n🐛 Bugs\n\nPlease file an issue for bugs, missing documentation, or unexpected behavior.\n\nSee Bugs\n\n💡 Feature Requests\n\nPlease file an issue to suggest new features. Vote on feature requests by adding a 👍. This helps maintainers prioritize what to work on.\n\nSee Feature Requests\n\nContributors ✨\n\nThanks goes to these people (emoji key):\n\n\nKent C. Dodds\n💻 📖 🤔 🚇 ⚠️\t\nMichaël De Boey\n🐛 💻 📖 ⚠️\t\nKornel Dubieniecki\n🐛\t\nNick Nish\n💻 ⚠️\t\nCaneco\n🎨\t\nAnurag Hazra\n🐛 💻 ⚠️ 📖\t\nYash Joshi\n💻 ⚠️\n\nChristian C. Salvadó\n💻 ⚠️\t\nJames Simone\n💻 ⚠️\t\nAgastya Chandrakant\n💻 ⚠️\t\nFábio Rosado\n💻 ⚠️\t\nArryangga Aliev Pratamaputra\n🐛\t\nEduardo Reveles\n💻 ⚠️\t\nMichal Piechowiak\n🐛 💻 ⚠️\n\nBrad Garropy\n🐛\t\nIlya Lyamkin\n💻\t\nSimon MacDonald\n🐛 💻 ⚠️\t\nNicky Meuleman\n💻\t\nAyush\n💻\t\nTEEAARBEE\n🐛\t\nTrevor Blades\n📖\n\nTitus\n⚠️ 👀 💻\t\nJoe Previte\n🐛\n\nThis project follows the all-contributors specification. Contributions of any kind welcome!\n\nLICENSE\n\nMIT\n\nAbout\n\nGatsby Remark plugin to embed well known services by their URL.\n\nTopics\nmarkdown spotify instagram youtube twitch remark twitter giphy codepen soundcloud slides gatsby pinterest embed streamable codesandbox gatsby-plugin gatsby-remark testing-playground linchess\nResources\n Readme\nLicense\n MIT license\nCode of conduct\n Code of conduct\n Activity\nStars\n 298 stars\nWatchers\n 10 watching\nForks\n 59 forks\nReport repository\n\n\nReleases 44\nv7.0.0\nLatest\n+ 43 releases\n\n\nPackages\nNo packages published\n\n\n\nContributors\n22\n+ 8 contributors\n\n\nLanguages\nJavaScript\n100.0%\nFooter\n© 2025 GitHub, Inc.\nFooter navigation\nTerms\nPrivacy\nSecurity\nStatus\nDocs\nContact\nManage cookies\nDo not share my personal information",
  "usage": {
    "tokens": 2815
  }
}
```
