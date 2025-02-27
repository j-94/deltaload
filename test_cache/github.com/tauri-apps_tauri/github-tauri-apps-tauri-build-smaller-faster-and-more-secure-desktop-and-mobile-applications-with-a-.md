---
title: GitHub - tauri-apps/tauri: Build smaller, faster, and more secure desktop and mobile applications with a web frontend.
description: Build smaller, faster, and more secure desktop and mobile applications with a web frontend. - tauri-apps/tauri
url: https://github.com/tauri-apps/tauri
timestamp: 2025-01-20T15:31:15.675Z
domain: github.com
path: tauri-apps_tauri
---

# GitHub - tauri-apps/tauri: Build smaller, faster, and more secure desktop and mobile applications with a web frontend.


Build smaller, faster, and more secure desktop and mobile applications with a web frontend. - tauri-apps/tauri


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
tauri-apps
/
tauri
Public
 Sponsor
Notifications
Fork 2.7k
 Star 88.6k
Code
Issues
903
Pull requests
54
Discussions
Actions
Projects
1
Security
7
tauri-apps/tauri
 dev
Code
Folders and files
Name	Last commit message	Last commit date

Latest commit
tamadamas
chore: Rewrite simply "Localhost free term" in README.md within #10510 (
90c6546
 · 
History
5,272 Commits


.cargo
	
chore: promote to v2 stable (#11198)
	


.changes
	
fix(cli): Add clipboard-manager to known plugins (#12442)
	


.devcontainer
	
Change V1 links to V2 site (#11111)
	


.docker/cross
	
fix(cross): Fix docker image and cross setup (#8094)
	


.github
	
ci(deps): Update repository-dispatch to v3 (#12169)
	


.scripts/ci
	
ci: fix a few relative paths (#10813)
	


.vscode
	
ci: check toml formatting with taplo-cli (#10787)
	


audits
	
add v2 report (#10554)
	


bench
	
fix(cli): Ignore file access events (#12164)
	


crates
	
fix(cli): Add clipboard-manager to known plugins (#12442)
	


examples
	
chore: Fix clippy 1.84 warnings (#12328)
	


packages
	
chore(deps): update dependency rollup to v4.31.0 (dev) (#12446)
	


supply-chain
	
ci: check toml formatting with taplo-cli (#10787)
	


.editorconfig
	
feat(icons): add and test icon generation for tauri (#55)
	


.gitignore
	
Restructure the repository (#10796)
	


.prettierignore
	
feat: add tauri-schema-worker (#10871)
	


.prettierrc
	
chore: remove unneeded prettier config (#10885)
	


.taurignore
	
chore: add root taurignore (#10805)
	


ARCHITECTURE.md
	
Change V1 links to V2 site (#11111)
	


Cargo.lock
	
apply version updates (#12425)
	


Cargo.toml
	
fix: downgrade MSRV to 1.77.2 to support Windows 7 (#11205)
	


LICENSE.spdx
	
chore: update copyright year (#12170)
	


LICENSE_APACHE-2.0
	
feat(license): SPDX Headers (#1449)
	


LICENSE_MIT
	
feat(license): SPDX Headers (#1449)
	


README.md
	
chore: Rewrite simply "Localhost free term" in README.md within #10510 (
	


SECURITY.md
	
’ -> ' (#9686)
	


dependabot.yml
	
Restructure the repository (#10796)
	


package.json
	
chore(deps): update all js dev dependencies (#11941)
	


pnpm-lock.yaml
	
chore(deps): update dependency rollup to v4.31.0 (dev) (#12446)
	


pnpm-workspace.yaml
	
feat: add tauri-schema-worker (#10871)
	


renovate.json
	
chore(config): migrate renovate config (#12099)
	


rustfmt.toml
	
feat(cli): generate signature for updater-enabled bundles (#9446)
	
Repository files navigation
README
Code of conduct
Apache-2.0 license
MIT license
Security

       

Introduction

Tauri is a framework for building tiny, blazingly fast binaries for all major desktop platforms. Developers can integrate any front-end framework that compiles to HTML, JS and CSS for building their user interface. The backend of the application is a rust-sourced binary with an API that the front-end can interact with.

The user interface in Tauri apps currently leverages tao as a window handling library on macOS, Windows, Linux, Android and iOS. To render your application, Tauri uses WRY, a library which provides a unified interface to the system webview, leveraging WKWebView on macOS & iOS, WebView2 on Windows, WebKitGTK on Linux and Android System WebView on Android.

To learn more about the details of how all of these pieces fit together, please consult this ARCHITECTURE.md document.

Getting Started

If you are interested in making a tauri app, please visit the documentation website.

The quickest way to get started is to install the prerequisites for your system and create a new project with create-tauri-app. For example with npm:

npm create tauri-app@latest
Features

The list of Tauri's features includes, but is not limited to:

Built-in app bundler to create app bundles in formats like .app, .dmg, .deb, .rpm, .AppImage and Windows installers like .exe (via NSIS) and .msi (via WiX).
Built-in self updater (desktop only)
System tray icons
Native notifications
Native WebView Protocol (tauri doesn't create a localhost http(s) server to serve the WebView contents)
GitHub action for streamlined CI
VS Code extension
Platforms

Tauri currently supports development and distribution on the following platforms:

Platform	Versions
Windows	7 and above
macOS	10.15 and above
Linux	webkit2gtk 4.0 for Tauri v1 (for example Ubuntu 18.04). webkit2gtk 4.1 for Tauri v2 (for example Ubuntu 22.04).
iOS/iPadOS (beta)	9 and above
Android (beta)	7 and above
Contributing

Before you start working on something, it's best to check if there is an existing issue first. It's also a good idea to stop by the Discord server and confirm with the team if it makes sense or if someone else is already working on it.

Please make sure to read the Contributing Guide before making a pull request.

Thank you to everyone contributing to Tauri!

Documentation

Documentation in a polyglot system is a tricky proposition. To this end, we prefer to use inline documentation in the Rust & JS source code as much as possible. Check out the hosting repository for the documentation site for further information: https://github.com/tauri-apps/tauri-docs

Partners

For the complete list of sponsors please visit our website and Open Collective.

Organization

Tauri aims to be a sustainable collective based on principles that guide sustainable free and open software communities. To this end it has become a Programme within the Commons Conservancy, and you can contribute financially via Open Collective.

Licenses

Code: (c) 2015 - Present - The Tauri Programme within The Commons Conservancy.

MIT or MIT/Apache 2.0 where applicable.

Logo: CC-BY-NC-ND

Original Tauri Logo Designs by Alve Larsson, Daniel Thompson-Yvetot and Guillaume Chau

About

Build smaller, faster, and more secure desktop and mobile applications with a web frontend.

tauri.app
Topics
desktop-app rust webview high-performance mobile-app web-frontend native-app
Resources
 Readme
License
 Apache-2.0, MIT licenses found
Code of conduct
 Code of conduct
Security policy
 Security policy
 Activity
 Custom properties
Stars
 88.6k stars
Watchers
 516 watching
Forks
 2.7k forks
Report repository


Releases 1,364
tauri-cli v2.2.5
Latest
+ 1,363 releases


Sponsor this project
tauri-apps Tauri
opencollective.com/tauri
Learn more about GitHub Sponsors


Packages
1
tauri/aarch64-unknown-linux-gnu


Contributors
429
+ 415 contributors


Languages
Rust
82.7%
 
TypeScript
7.1%
 
NSIS
3.6%
 
Kotlin
2.1%
 
JavaScript
1.7%
 
Shell
1.5%
 
Other
1.3%
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
  "title": "GitHub - tauri-apps/tauri: Build smaller, faster, and more secure desktop and mobile applications with a web frontend.",
  "description": "Build smaller, faster, and more secure desktop and mobile applications with a web frontend. - tauri-apps/tauri",
  "url": "https://github.com/tauri-apps/tauri?screenshot=true",
  "content": "Skip to content\nNavigation Menu\nProduct\nSolutions\nResources\nOpen Source\nEnterprise\nPricing\nSign in\nSign up\ntauri-apps\n/\ntauri\nPublic\n Sponsor\nNotifications\nFork 2.7k\n Star 88.6k\nCode\nIssues\n903\nPull requests\n54\nDiscussions\nActions\nProjects\n1\nSecurity\n7\ntauri-apps/tauri\n dev\nCode\nFolders and files\nName\tLast commit message\tLast commit date\n\nLatest commit\ntamadamas\nchore: Rewrite simply \"Localhost free term\" in README.md within #10510 (\n90c6546\n · \nHistory\n5,272 Commits\n\n\n.cargo\n\t\nchore: promote to v2 stable (#11198)\n\t\n\n\n.changes\n\t\nfix(cli): Add clipboard-manager to known plugins (#12442)\n\t\n\n\n.devcontainer\n\t\nChange V1 links to V2 site (#11111)\n\t\n\n\n.docker/cross\n\t\nfix(cross): Fix docker image and cross setup (#8094)\n\t\n\n\n.github\n\t\nci(deps): Update repository-dispatch to v3 (#12169)\n\t\n\n\n.scripts/ci\n\t\nci: fix a few relative paths (#10813)\n\t\n\n\n.vscode\n\t\nci: check toml formatting with taplo-cli (#10787)\n\t\n\n\naudits\n\t\nadd v2 report (#10554)\n\t\n\n\nbench\n\t\nfix(cli): Ignore file access events (#12164)\n\t\n\n\ncrates\n\t\nfix(cli): Add clipboard-manager to known plugins (#12442)\n\t\n\n\nexamples\n\t\nchore: Fix clippy 1.84 warnings (#12328)\n\t\n\n\npackages\n\t\nchore(deps): update dependency rollup to v4.31.0 (dev) (#12446)\n\t\n\n\nsupply-chain\n\t\nci: check toml formatting with taplo-cli (#10787)\n\t\n\n\n.editorconfig\n\t\nfeat(icons): add and test icon generation for tauri (#55)\n\t\n\n\n.gitignore\n\t\nRestructure the repository (#10796)\n\t\n\n\n.prettierignore\n\t\nfeat: add tauri-schema-worker (#10871)\n\t\n\n\n.prettierrc\n\t\nchore: remove unneeded prettier config (#10885)\n\t\n\n\n.taurignore\n\t\nchore: add root taurignore (#10805)\n\t\n\n\nARCHITECTURE.md\n\t\nChange V1 links to V2 site (#11111)\n\t\n\n\nCargo.lock\n\t\napply version updates (#12425)\n\t\n\n\nCargo.toml\n\t\nfix: downgrade MSRV to 1.77.2 to support Windows 7 (#11205)\n\t\n\n\nLICENSE.spdx\n\t\nchore: update copyright year (#12170)\n\t\n\n\nLICENSE_APACHE-2.0\n\t\nfeat(license): SPDX Headers (#1449)\n\t\n\n\nLICENSE_MIT\n\t\nfeat(license): SPDX Headers (#1449)\n\t\n\n\nREADME.md\n\t\nchore: Rewrite simply \"Localhost free term\" in README.md within #10510 (\n\t\n\n\nSECURITY.md\n\t\n’ -> ' (#9686)\n\t\n\n\ndependabot.yml\n\t\nRestructure the repository (#10796)\n\t\n\n\npackage.json\n\t\nchore(deps): update all js dev dependencies (#11941)\n\t\n\n\npnpm-lock.yaml\n\t\nchore(deps): update dependency rollup to v4.31.0 (dev) (#12446)\n\t\n\n\npnpm-workspace.yaml\n\t\nfeat: add tauri-schema-worker (#10871)\n\t\n\n\nrenovate.json\n\t\nchore(config): migrate renovate config (#12099)\n\t\n\n\nrustfmt.toml\n\t\nfeat(cli): generate signature for updater-enabled bundles (#9446)\n\t\nRepository files navigation\nREADME\nCode of conduct\nApache-2.0 license\nMIT license\nSecurity\n\n       \n\nIntroduction\n\nTauri is a framework for building tiny, blazingly fast binaries for all major desktop platforms. Developers can integrate any front-end framework that compiles to HTML, JS and CSS for building their user interface. The backend of the application is a rust-sourced binary with an API that the front-end can interact with.\n\nThe user interface in Tauri apps currently leverages tao as a window handling library on macOS, Windows, Linux, Android and iOS. To render your application, Tauri uses WRY, a library which provides a unified interface to the system webview, leveraging WKWebView on macOS & iOS, WebView2 on Windows, WebKitGTK on Linux and Android System WebView on Android.\n\nTo learn more about the details of how all of these pieces fit together, please consult this ARCHITECTURE.md document.\n\nGetting Started\n\nIf you are interested in making a tauri app, please visit the documentation website.\n\nThe quickest way to get started is to install the prerequisites for your system and create a new project with create-tauri-app. For example with npm:\n\nnpm create tauri-app@latest\nFeatures\n\nThe list of Tauri's features includes, but is not limited to:\n\nBuilt-in app bundler to create app bundles in formats like .app, .dmg, .deb, .rpm, .AppImage and Windows installers like .exe (via NSIS) and .msi (via WiX).\nBuilt-in self updater (desktop only)\nSystem tray icons\nNative notifications\nNative WebView Protocol (tauri doesn't create a localhost http(s) server to serve the WebView contents)\nGitHub action for streamlined CI\nVS Code extension\nPlatforms\n\nTauri currently supports development and distribution on the following platforms:\n\nPlatform\tVersions\nWindows\t7 and above\nmacOS\t10.15 and above\nLinux\twebkit2gtk 4.0 for Tauri v1 (for example Ubuntu 18.04). webkit2gtk 4.1 for Tauri v2 (for example Ubuntu 22.04).\niOS/iPadOS (beta)\t9 and above\nAndroid (beta)\t7 and above\nContributing\n\nBefore you start working on something, it's best to check if there is an existing issue first. It's also a good idea to stop by the Discord server and confirm with the team if it makes sense or if someone else is already working on it.\n\nPlease make sure to read the Contributing Guide before making a pull request.\n\nThank you to everyone contributing to Tauri!\n\nDocumentation\n\nDocumentation in a polyglot system is a tricky proposition. To this end, we prefer to use inline documentation in the Rust & JS source code as much as possible. Check out the hosting repository for the documentation site for further information: https://github.com/tauri-apps/tauri-docs\n\nPartners\n\nFor the complete list of sponsors please visit our website and Open Collective.\n\nOrganization\n\nTauri aims to be a sustainable collective based on principles that guide sustainable free and open software communities. To this end it has become a Programme within the Commons Conservancy, and you can contribute financially via Open Collective.\n\nLicenses\n\nCode: (c) 2015 - Present - The Tauri Programme within The Commons Conservancy.\n\nMIT or MIT/Apache 2.0 where applicable.\n\nLogo: CC-BY-NC-ND\n\nOriginal Tauri Logo Designs by Alve Larsson, Daniel Thompson-Yvetot and Guillaume Chau\n\nAbout\n\nBuild smaller, faster, and more secure desktop and mobile applications with a web frontend.\n\ntauri.app\nTopics\ndesktop-app rust webview high-performance mobile-app web-frontend native-app\nResources\n Readme\nLicense\n Apache-2.0, MIT licenses found\nCode of conduct\n Code of conduct\nSecurity policy\n Security policy\n Activity\n Custom properties\nStars\n 88.6k stars\nWatchers\n 516 watching\nForks\n 2.7k forks\nReport repository\n\n\nReleases 1,364\ntauri-cli v2.2.5\nLatest\n+ 1,363 releases\n\n\nSponsor this project\ntauri-apps Tauri\nopencollective.com/tauri\nLearn more about GitHub Sponsors\n\n\nPackages\n1\ntauri/aarch64-unknown-linux-gnu\n\n\nContributors\n429\n+ 415 contributors\n\n\nLanguages\nRust\n82.7%\n \nTypeScript\n7.1%\n \nNSIS\n3.6%\n \nKotlin\n2.1%\n \nJavaScript\n1.7%\n \nShell\n1.5%\n \nOther\n1.3%\nFooter\n© 2025 GitHub, Inc.\nFooter navigation\nTerms\nPrivacy\nSecurity\nStatus\nDocs\nContact\nManage cookies\nDo not share my personal information",
  "usage": {
    "tokens": 1742
  }
}
```
