---
title: GitHub - system-ui/theme-ui: Build consistent, themeable React apps based on constraint-based design principles
description: Build consistent, themeable React apps based on constraint-based design principles - system-ui/theme-ui
url: https://github.com/system-ui/theme-ui
timestamp: 2025-01-20T15:31:07.597Z
domain: github.com
path: system-ui_theme-ui
---

# GitHub - system-ui/theme-ui: Build consistent, themeable React apps based on constraint-based design principles


Build consistent, themeable React apps based on constraint-based design principles - system-ui/theme-ui


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
system-ui
/
theme-ui
Public
Notifications
Fork 673
 Star 5.3k
Code
Issues
49
Pull requests
18
Discussions
Actions
Security
Insights
system-ui/theme-ui
 develop
Code
Folders and files
Name	Last commit message	Last commit date

Latest commit
hasparus
Bump versions to: 0.17.2-develop.0 [skip ci]
e6cf9b6
 · 
History
4,714 Commits


.codesandbox
	
Update docs dependencies
	


.github
	
ci: fetch before release
	


.husky/_
	
chore: install auto
	


examples
	
chore(deps): bump next from 14.2.15 to 15.0.3
	


packages
	
Bump versions to: 0.17.2-develop.0 [skip ci]
	


scripts
	
feat: bump deps, including Emotion
	


.all-contributorsrc
	
Update contributors [skip ci]
	


.eslintignore
	
Add .md to .eslintignore
	


.eslintrc.js
	
chore(eslint): disable jsx-pascal-case rule for now
	


.gitignore
	
chore: add .env to .gitignore
	


.npmrc
	
chore(test): make tests work after adopting pnpm
	


.nvmrc
	
wip(mdx): make mdx test run in mjs
	


.pnpmfile.cjs
	
Update lockfile
	


.prettierignore
	
Fix code block syntax colors broken by MDX 2 bump
	


CHANGELOG.md
	
Update CHANGELOG.md [skip ci]
	


CODE_OF_CONDUCT.md
	
Format
	


CONTRIBUTING.md
	
chore: Update Contributing doc with pnpm info
	


LICENSE.md
	
Ran yarn format
	


MIGRATING.md
	
Add missing migration notes on 0.16 to docs
	


README.md
	
Update workspaces setup
	


auto.config.ts
	
chore: disable all-contributors auto plugin
	


babel.config.js
	
Add importSource to babel.config.js
	


codechecks.yml
	
ci(codechecks): use yml
	


jest-preprocess.js
	
chore(gatsby-plugin-theme-ui): make tests work
	


jest.config.ts
	
Update docs dependencies
	


lint-staged.config.js
	
Edit lint-staged config
	


package.json
	
chore: bump Auto
	


pnpm-lock.yaml
	
chore(deps): bump next from 14.2.15 to 15.0.3
	


pnpm-workspace.yaml
	
wip: use PNPM because we need workspace: protocol for tests
	


prettier.config.js
	
docs(examples/next): use TS, variants and improve contrast
	


tsconfig.json
	
Remove occurences of /** @jsx jsx */
	


tsconfig.options.json
	
Remove occurences of /** @jsx jsx */
	


tsconfig.test.json
	
Remove occurences of /** @jsx jsx */
	


vercel.json
	
Group & update all MDX-related docs
	
Repository files navigation
README
Code of conduct
MIT license

Theme UI

The Design Graph Framework

 

   

   
 


Theme UI is a library for creating themeable user interfaces based on constraint-based design principles. Build custom component libraries, design systems, web applications, Gatsby themes, and more with a flexible API for best-in-class developer ergonomics.

stable docs: https://theme-ui.com
develop (prerelease) docs: https://dev.theme-ui.com

Built for design systems, white-labels, themes, and other applications where customizing colors, typography, and layout are treated as first-class citizens and based on a standard Theme Specification, Theme UI is intended to work in a variety of applications, libraries, and other UI components. Colors, typography, and layout styles derived from customizable theme-based design scales help you build UI rooted in constraint-based design principles.

The next evolution of Styled System
From the creators of utility-based, atomic CSS methodologies
Theme-based styling with the sx prop
Compatible with virtually any UI component library
Works with existing Styled System components
Quick mobile-first responsive styles
Built-in support for dark modes
Primitive page layout components
Completely customizable with robust theming
Built with a standard Theme Specification for interoperability
Built with Emotion for scoped styles
Plugin for use in Gatsby sites and themes
Style MDX content with a simple, expressive API
Works with Typography.js themes
Getting Started
npm install theme-ui @emotion/react

If you don't need color modes or components you can install @theme-ui/core.

Any styles in your app can reference values from the global theme object. To provide the theme in context, wrap your application with the ThemeUIProvider component and pass in a custom theme object.

// basic usage
import { ThemeUIProvider } from 'theme-ui'
import theme from './theme'

export default (props) => (
  <ThemeUIProvider theme={theme}>{props.children}</ThemeUIProvider>
)

The theme object follows the System UI Theme Specification, which lets you define custom color palettes, typographic scales, fonts, and more. Read more about theming.

// example theme.js
export default {
  fonts: {
    body: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif',
    heading: '"Avenir Next", sans-serif',
    monospace: 'Menlo, monospace',
  },
  colors: {
    text: '#000',
    background: '#fff',
    primary: '#33e',
  },
}
sx prop

The sx prop works similarly to Emotion's css prop, accepting style objects to add CSS directly to an element in JSX, but includes extra theme-aware functionality. Using the sx prop for styles means that certain properties can reference values defined in your theme object. This is intended to make keeping styles consistent throughout your app the easy thing to do.

The sx prop only works in modules that have defined a custom pragma at the top of the file, which replaces the default React JSX functions. This means you can control which modules in your application opt into this feature without the need for a Babel plugin or additional configuration.

/** @jsxImportSource theme-ui */

export default (props) => (
  <div
    sx={{
      fontWeight: 'bold',
      fontSize: 4, // picks up value from `theme.fontSizes[4]`
      color: 'primary', // picks up value from `theme.colors.primary`
    }}
  >
    Hello
  </div>
)

Read more about how the custom pragma works.

Responsive styles

The sx prop also supports using arrays as values to change properties responsively with a mobile-first approach. This API originated in Styled System and is intended as a terser syntax for applying responsive styles across a singular dimension.

/** @jsxImportSource theme-ui */

export default (props) => (
  <div
    sx={{
      // applies width 100% to all viewport widths,
      // width 50% above the first breakpoint,
      // and 25% above the next breakpoint
      width: ['100%', '50%', '25%'],
    }}
  />
)
Documentation
Theming
The sx Prop
Layout
Color Modes
Theme Spec
Themed
MDX Components
Gatsby Plugin
API

MIT License

Contributors ✨

Thanks goes to these wonderful people (emoji key):


Brent Jackson
🤔 💻 🎨 📖 💡 ⚠️ 👀	
Piotr Monwid-Olechnowicz
💻 📖 ⚠️ 👀 💡	
Dany Castillo
💻 📖 💡 ⚠️	
Jordan Overbye
💻 💡 ⚠️	
Lachlan Campbell
💻 💡 ⚠️ 👀 📖 💬	
John Otander
💻 👀 📖 ⚠️ 🤔	
David Burles
💻 👀 ⚠️ 📖	
Max Stoiber
💻 👀 ⚠️ 💡

Atanas Stoyanov
💻 💬 ⚠️ 🐛 📖	
Lennart
💻 🐛 📖 💡	
Aleksandra Sikora
💻	
LB
💻 ⚠️	
Francis Champagne
💻 🐛 ⚠️ 📖	
Alex Page
💻 📖	
Adam Schay
💻	
Alex
💻 📖

James Edmonds
💻 📖	
Florent SCHILDKNECHT
💻 📖	
Cole Bemis
💻 ⚠️ 📖	
John Letey
📖	
Yuraima Estevez
💻	
Allan Pope
💻 📖	
Emmanuel Pilande
💻	
Justin Hall
💻

Marek
💻 🐛	
Björn Clees
📖 💻	
Iurii Kucherov
📖	
Joe Strouth
💻 🐛	
Stewart Everett
💻	
Travis Arnold
💻 📖	
Ivo Reis
💻	
Benedikt Rötsch
🐛 📖

Jacob Cofman
📖	
John Letey
📖	
Lawrence Gosset
📖	
Markos Konstantopoulos
📖	
Robin Millette
💻	
Rodney Folz
💻	
Rodrigo Pombo
💻 ⚠️ 📖	
Scott Silvi
📖

Shawn Allen
📖	
Tomas Carnecky
💻 🐛	
John Polacek
💻 🐛	
mackie
💻	
Aaron Adams
💻 🐛 📖	
Amberley
💻	
Andreea Năstase
📖	
Anson Low Z.F
🐛 📖

Bernhard Gschwantner
💻	
Bhanu Prakash Korthiwada
📖	
Bruno Lemos
📖	
Bryce Fischer
💻	
Dan Wood
📖	
Debs
📖	
Edward O'Reilly
💻 🐛	
Eric Schaefer
💻

Felix Green
📖	
Gerhard Bliedung
💻 🐛	
Guayo Mena
💡	
Guilherme Lima
📖	
Herb Caudill
📖	
Jacob Bolda
💻 🐛	
Jason Lengstorf
🐛 📖	
Jason Rundell (he/him)
💡

Joe Race
📖	
Kanstantsin Klimashevich
📖	
Eka
📖 🐛	
Keir Williams
📖	
Kristóf Poduszló
💻 🐛 🤔	
Kyle Gill
📖	
Kyle Holmberg
📖	
Jay Laiche
💻

Marc Wiest
💻	
Matheus Teixeira
💻	
matt-cratebind
📖	
Matt Zabriskie
💻	
Maxime Khoy
💻	
Michael Friedman
📖	
Michael Zetterberg fd. Lopez
💻	
Nathan Knowler
💻

Neeraj Lagwankar
📖	
Owen Young
💻	
Patrick Arminio
💻 🐛	
Pedro Duarte
💻	
Ray Clanan
💻	
Rich Werden
📖	
Rob Phoenix
📖 🐛	
Robert Moggach
💻 🐛

Anand Narayan
💻 🐛	
Sam Poder
📖	
Sam Rose
📖	
Sohrab
💻	
Spencer Rinehart
💻	
Steve
📖	
Steve Barton
📖	
Tim Reynolds
💻 🐛

Vinícius Lemes
📖	
Yihwan Kim
💻 🐛	
Yuriy Burychka
📖	
Zolwiastyl
💻	
Amrish Kushwaha
💻	
Joe Bell
💻 🐛	
kenny-loveholidays
💻	
⦇⦀∙ˇ∎ˇ∙⦀⦈
💻 🐛

navsgh
📖	
Shane O'Neill
📖	
汪磊
💻 🐛	
Carolin Maisenbacher
💻 📖 ⚠️	
Alex Chan
📖 💡 ⚠️ 💻	
Kenny
💻	
Jordie Bodlay
📖	
Matt Gleich
📖

William Pei
📖 💡 💻 ⚠️	
Greg Poole
📖	
Akash
📖 💻	
Cannon Lock
📖	
kamatte
📖 💻	
Simen A. W. Olsen
📖 💡 ⚠️ 💻	
Wahid Rahim
📖 💡 💻	
Justin Cooper
📖

CJ
📖 💻

This project follows the all-contributors specification. Contributions of any kind welcome!

About

Build consistent, themeable React apps based on constraint-based design principles

theme-ui.com
Topics
react theme color design ui layout typography style emotion design-tokens mdx design-system
Resources
 Readme
License
 MIT license
Code of conduct
 Code of conduct
 Activity
 Custom properties
Stars
 5.3k stars
Watchers
 42 watching
Forks
 673 forks
Report repository


Releases 174
v0.17.1
Latest
+ 173 releases


Used by 36.5k
+ 36,538


Contributors
138
+ 124 contributors


Languages
TypeScript
59.6%
 
MDX
28.1%
 
JavaScript
11.1%
 
HTML
1.1%
 
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
  "title": "GitHub - system-ui/theme-ui: Build consistent, themeable React apps based on constraint-based design principles",
  "description": "Build consistent, themeable React apps based on constraint-based design principles - system-ui/theme-ui",
  "url": "https://github.com/system-ui/theme-ui?screenshot=true",
  "content": "Skip to content\nNavigation Menu\nProduct\nSolutions\nResources\nOpen Source\nEnterprise\nPricing\nSign in\nSign up\nsystem-ui\n/\ntheme-ui\nPublic\nNotifications\nFork 673\n Star 5.3k\nCode\nIssues\n49\nPull requests\n18\nDiscussions\nActions\nSecurity\nInsights\nsystem-ui/theme-ui\n develop\nCode\nFolders and files\nName\tLast commit message\tLast commit date\n\nLatest commit\nhasparus\nBump versions to: 0.17.2-develop.0 [skip ci]\ne6cf9b6\n · \nHistory\n4,714 Commits\n\n\n.codesandbox\n\t\nUpdate docs dependencies\n\t\n\n\n.github\n\t\nci: fetch before release\n\t\n\n\n.husky/_\n\t\nchore: install auto\n\t\n\n\nexamples\n\t\nchore(deps): bump next from 14.2.15 to 15.0.3\n\t\n\n\npackages\n\t\nBump versions to: 0.17.2-develop.0 [skip ci]\n\t\n\n\nscripts\n\t\nfeat: bump deps, including Emotion\n\t\n\n\n.all-contributorsrc\n\t\nUpdate contributors [skip ci]\n\t\n\n\n.eslintignore\n\t\nAdd .md to .eslintignore\n\t\n\n\n.eslintrc.js\n\t\nchore(eslint): disable jsx-pascal-case rule for now\n\t\n\n\n.gitignore\n\t\nchore: add .env to .gitignore\n\t\n\n\n.npmrc\n\t\nchore(test): make tests work after adopting pnpm\n\t\n\n\n.nvmrc\n\t\nwip(mdx): make mdx test run in mjs\n\t\n\n\n.pnpmfile.cjs\n\t\nUpdate lockfile\n\t\n\n\n.prettierignore\n\t\nFix code block syntax colors broken by MDX 2 bump\n\t\n\n\nCHANGELOG.md\n\t\nUpdate CHANGELOG.md [skip ci]\n\t\n\n\nCODE_OF_CONDUCT.md\n\t\nFormat\n\t\n\n\nCONTRIBUTING.md\n\t\nchore: Update Contributing doc with pnpm info\n\t\n\n\nLICENSE.md\n\t\nRan yarn format\n\t\n\n\nMIGRATING.md\n\t\nAdd missing migration notes on 0.16 to docs\n\t\n\n\nREADME.md\n\t\nUpdate workspaces setup\n\t\n\n\nauto.config.ts\n\t\nchore: disable all-contributors auto plugin\n\t\n\n\nbabel.config.js\n\t\nAdd importSource to babel.config.js\n\t\n\n\ncodechecks.yml\n\t\nci(codechecks): use yml\n\t\n\n\njest-preprocess.js\n\t\nchore(gatsby-plugin-theme-ui): make tests work\n\t\n\n\njest.config.ts\n\t\nUpdate docs dependencies\n\t\n\n\nlint-staged.config.js\n\t\nEdit lint-staged config\n\t\n\n\npackage.json\n\t\nchore: bump Auto\n\t\n\n\npnpm-lock.yaml\n\t\nchore(deps): bump next from 14.2.15 to 15.0.3\n\t\n\n\npnpm-workspace.yaml\n\t\nwip: use PNPM because we need workspace: protocol for tests\n\t\n\n\nprettier.config.js\n\t\ndocs(examples/next): use TS, variants and improve contrast\n\t\n\n\ntsconfig.json\n\t\nRemove occurences of /** @jsx jsx */\n\t\n\n\ntsconfig.options.json\n\t\nRemove occurences of /** @jsx jsx */\n\t\n\n\ntsconfig.test.json\n\t\nRemove occurences of /** @jsx jsx */\n\t\n\n\nvercel.json\n\t\nGroup & update all MDX-related docs\n\t\nRepository files navigation\nREADME\nCode of conduct\nMIT license\n\nTheme UI\n\nThe Design Graph Framework\n\n \n\n   \n\n   \n \n\n\nTheme UI is a library for creating themeable user interfaces based on constraint-based design principles. Build custom component libraries, design systems, web applications, Gatsby themes, and more with a flexible API for best-in-class developer ergonomics.\n\nstable docs: https://theme-ui.com\ndevelop (prerelease) docs: https://dev.theme-ui.com\n\nBuilt for design systems, white-labels, themes, and other applications where customizing colors, typography, and layout are treated as first-class citizens and based on a standard Theme Specification, Theme UI is intended to work in a variety of applications, libraries, and other UI components. Colors, typography, and layout styles derived from customizable theme-based design scales help you build UI rooted in constraint-based design principles.\n\nThe next evolution of Styled System\nFrom the creators of utility-based, atomic CSS methodologies\nTheme-based styling with the sx prop\nCompatible with virtually any UI component library\nWorks with existing Styled System components\nQuick mobile-first responsive styles\nBuilt-in support for dark modes\nPrimitive page layout components\nCompletely customizable with robust theming\nBuilt with a standard Theme Specification for interoperability\nBuilt with Emotion for scoped styles\nPlugin for use in Gatsby sites and themes\nStyle MDX content with a simple, expressive API\nWorks with Typography.js themes\nGetting Started\nnpm install theme-ui @emotion/react\n\nIf you don't need color modes or components you can install @theme-ui/core.\n\nAny styles in your app can reference values from the global theme object. To provide the theme in context, wrap your application with the ThemeUIProvider component and pass in a custom theme object.\n\n// basic usage\nimport { ThemeUIProvider } from 'theme-ui'\nimport theme from './theme'\n\nexport default (props) => (\n  <ThemeUIProvider theme={theme}>{props.children}</ThemeUIProvider>\n)\n\nThe theme object follows the System UI Theme Specification, which lets you define custom color palettes, typographic scales, fonts, and more. Read more about theming.\n\n// example theme.js\nexport default {\n  fonts: {\n    body: 'system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, \"Helvetica Neue\", sans-serif',\n    heading: '\"Avenir Next\", sans-serif',\n    monospace: 'Menlo, monospace',\n  },\n  colors: {\n    text: '#000',\n    background: '#fff',\n    primary: '#33e',\n  },\n}\nsx prop\n\nThe sx prop works similarly to Emotion's css prop, accepting style objects to add CSS directly to an element in JSX, but includes extra theme-aware functionality. Using the sx prop for styles means that certain properties can reference values defined in your theme object. This is intended to make keeping styles consistent throughout your app the easy thing to do.\n\nThe sx prop only works in modules that have defined a custom pragma at the top of the file, which replaces the default React JSX functions. This means you can control which modules in your application opt into this feature without the need for a Babel plugin or additional configuration.\n\n/** @jsxImportSource theme-ui */\n\nexport default (props) => (\n  <div\n    sx={{\n      fontWeight: 'bold',\n      fontSize: 4, // picks up value from `theme.fontSizes[4]`\n      color: 'primary', // picks up value from `theme.colors.primary`\n    }}\n  >\n    Hello\n  </div>\n)\n\nRead more about how the custom pragma works.\n\nResponsive styles\n\nThe sx prop also supports using arrays as values to change properties responsively with a mobile-first approach. This API originated in Styled System and is intended as a terser syntax for applying responsive styles across a singular dimension.\n\n/** @jsxImportSource theme-ui */\n\nexport default (props) => (\n  <div\n    sx={{\n      // applies width 100% to all viewport widths,\n      // width 50% above the first breakpoint,\n      // and 25% above the next breakpoint\n      width: ['100%', '50%', '25%'],\n    }}\n  />\n)\nDocumentation\nTheming\nThe sx Prop\nLayout\nColor Modes\nTheme Spec\nThemed\nMDX Components\nGatsby Plugin\nAPI\n\nMIT License\n\nContributors ✨\n\nThanks goes to these wonderful people (emoji key):\n\n\nBrent Jackson\n🤔 💻 🎨 📖 💡 ⚠️ 👀\t\nPiotr Monwid-Olechnowicz\n💻 📖 ⚠️ 👀 💡\t\nDany Castillo\n💻 📖 💡 ⚠️\t\nJordan Overbye\n💻 💡 ⚠️\t\nLachlan Campbell\n💻 💡 ⚠️ 👀 📖 💬\t\nJohn Otander\n💻 👀 📖 ⚠️ 🤔\t\nDavid Burles\n💻 👀 ⚠️ 📖\t\nMax Stoiber\n💻 👀 ⚠️ 💡\n\nAtanas Stoyanov\n💻 💬 ⚠️ 🐛 📖\t\nLennart\n💻 🐛 📖 💡\t\nAleksandra Sikora\n💻\t\nLB\n💻 ⚠️\t\nFrancis Champagne\n💻 🐛 ⚠️ 📖\t\nAlex Page\n💻 📖\t\nAdam Schay\n💻\t\nAlex\n💻 📖\n\nJames Edmonds\n💻 📖\t\nFlorent SCHILDKNECHT\n💻 📖\t\nCole Bemis\n💻 ⚠️ 📖\t\nJohn Letey\n📖\t\nYuraima Estevez\n💻\t\nAllan Pope\n💻 📖\t\nEmmanuel Pilande\n💻\t\nJustin Hall\n💻\n\nMarek\n💻 🐛\t\nBjörn Clees\n📖 💻\t\nIurii Kucherov\n📖\t\nJoe Strouth\n💻 🐛\t\nStewart Everett\n💻\t\nTravis Arnold\n💻 📖\t\nIvo Reis\n💻\t\nBenedikt Rötsch\n🐛 📖\n\nJacob Cofman\n📖\t\nJohn Letey\n📖\t\nLawrence Gosset\n📖\t\nMarkos Konstantopoulos\n📖\t\nRobin Millette\n💻\t\nRodney Folz\n💻\t\nRodrigo Pombo\n💻 ⚠️ 📖\t\nScott Silvi\n📖\n\nShawn Allen\n📖\t\nTomas Carnecky\n💻 🐛\t\nJohn Polacek\n💻 🐛\t\nmackie\n💻\t\nAaron Adams\n💻 🐛 📖\t\nAmberley\n💻\t\nAndreea Năstase\n📖\t\nAnson Low Z.F\n🐛 📖\n\nBernhard Gschwantner\n💻\t\nBhanu Prakash Korthiwada\n📖\t\nBruno Lemos\n📖\t\nBryce Fischer\n💻\t\nDan Wood\n📖\t\nDebs\n📖\t\nEdward O'Reilly\n💻 🐛\t\nEric Schaefer\n💻\n\nFelix Green\n📖\t\nGerhard Bliedung\n💻 🐛\t\nGuayo Mena\n💡\t\nGuilherme Lima\n📖\t\nHerb Caudill\n📖\t\nJacob Bolda\n💻 🐛\t\nJason Lengstorf\n🐛 📖\t\nJason Rundell (he/him)\n💡\n\nJoe Race\n📖\t\nKanstantsin Klimashevich\n📖\t\nEka\n📖 🐛\t\nKeir Williams\n📖\t\nKristóf Poduszló\n💻 🐛 🤔\t\nKyle Gill\n📖\t\nKyle Holmberg\n📖\t\nJay Laiche\n💻\n\nMarc Wiest\n💻\t\nMatheus Teixeira\n💻\t\nmatt-cratebind\n📖\t\nMatt Zabriskie\n💻\t\nMaxime Khoy\n💻\t\nMichael Friedman\n📖\t\nMichael Zetterberg fd. Lopez\n💻\t\nNathan Knowler\n💻\n\nNeeraj Lagwankar\n📖\t\nOwen Young\n💻\t\nPatrick Arminio\n💻 🐛\t\nPedro Duarte\n💻\t\nRay Clanan\n💻\t\nRich Werden\n📖\t\nRob Phoenix\n📖 🐛\t\nRobert Moggach\n💻 🐛\n\nAnand Narayan\n💻 🐛\t\nSam Poder\n📖\t\nSam Rose\n📖\t\nSohrab\n💻\t\nSpencer Rinehart\n💻\t\nSteve\n📖\t\nSteve Barton\n📖\t\nTim Reynolds\n💻 🐛\n\nVinícius Lemes\n📖\t\nYihwan Kim\n💻 🐛\t\nYuriy Burychka\n📖\t\nZolwiastyl\n💻\t\nAmrish Kushwaha\n💻\t\nJoe Bell\n💻 🐛\t\nkenny-loveholidays\n💻\t\n⦇⦀∙ˇ∎ˇ∙⦀⦈\n💻 🐛\n\nnavsgh\n📖\t\nShane O'Neill\n📖\t\n汪磊\n💻 🐛\t\nCarolin Maisenbacher\n💻 📖 ⚠️\t\nAlex Chan\n📖 💡 ⚠️ 💻\t\nKenny\n💻\t\nJordie Bodlay\n📖\t\nMatt Gleich\n📖\n\nWilliam Pei\n📖 💡 💻 ⚠️\t\nGreg Poole\n📖\t\nAkash\n📖 💻\t\nCannon Lock\n📖\t\nkamatte\n📖 💻\t\nSimen A. W. Olsen\n📖 💡 ⚠️ 💻\t\nWahid Rahim\n📖 💡 💻\t\nJustin Cooper\n📖\n\nCJ\n📖 💻\n\nThis project follows the all-contributors specification. Contributions of any kind welcome!\n\nAbout\n\nBuild consistent, themeable React apps based on constraint-based design principles\n\ntheme-ui.com\nTopics\nreact theme color design ui layout typography style emotion design-tokens mdx design-system\nResources\n Readme\nLicense\n MIT license\nCode of conduct\n Code of conduct\n Activity\n Custom properties\nStars\n 5.3k stars\nWatchers\n 42 watching\nForks\n 673 forks\nReport repository\n\n\nReleases 174\nv0.17.1\nLatest\n+ 173 releases\n\n\nUsed by 36.5k\n+ 36,538\n\n\nContributors\n138\n+ 124 contributors\n\n\nLanguages\nTypeScript\n59.6%\n \nMDX\n28.1%\n \nJavaScript\n11.1%\n \nHTML\n1.1%\n \nOther\n0.1%\nFooter\n© 2025 GitHub, Inc.\nFooter navigation\nTerms\nPrivacy\nSecurity\nStatus\nDocs\nContact\nManage cookies\nDo not share my personal information",
  "usage": {
    "tokens": 3077
  }
}
```
