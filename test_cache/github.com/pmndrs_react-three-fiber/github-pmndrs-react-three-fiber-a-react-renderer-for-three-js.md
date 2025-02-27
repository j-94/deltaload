---
title: GitHub - pmndrs/react-three-fiber: 🇨🇭 A React renderer for Three.js
description: 🇨🇭 A React renderer for Three.js. Contribute to pmndrs/react-three-fiber development by creating an account on GitHub.
url: https://github.com/pmndrs/react-three-fiber
timestamp: 2025-01-20T15:31:04.558Z
domain: github.com
path: pmndrs_react-three-fiber
---

# GitHub - pmndrs/react-three-fiber: 🇨🇭 A React renderer for Three.js


🇨🇭 A React renderer for Three.js. Contribute to pmndrs/react-three-fiber development by creating an account on GitHub.


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
pmndrs
/
react-three-fiber
Public
 Sponsor
Notifications
Fork 1.6k
 Star 28k
Code
Issues
69
Pull requests
16
Discussions
Actions
Projects
Security
Insights
pmndrs/react-three-fiber
 master
Code
Folders and files
Name	Last commit message	Last commit date

Latest commit
CodyJasonBennett
RELEASING: Releasing 2 package(s)
ec4f00b
 · 
History
2,691 Commits


.changeset
	
RELEASING: Releasing 2 package(s)
	


.codesandbox
	
csb: node 18 (#3157)
	


.github
	
chore: docs gh + dd links
	


.husky
	
um, npx?
	


docs
	
Merge pull request #3413 from tbtiberiu/fix/docs-sandpack-error
	


example
	
fix(native): drop use-measure for react-dom peerdep (#3323)
	


packages
	
RELEASING: Releasing 2 package(s)
	


.eslintignore
	
chore(internals): [v6] use preconstruct
	


.eslintrc.json
	
chore: disable mixed imports rule
	


.gitignore
	
V8, react 18 beta (#1630)
	


.prettierignore
	
chore: Prettier CI/CD, remove deprecated options (#3260)
	


.prettierrc
	
chore: Prettier CI/CD, remove deprecated options (#3260)
	


CONTRIBUTING.md
	
clarify that yarn 1 is required, not just yarn (#2896)
	


LICENSE
	
Update LICENSE
	


babel.config.js
	
Use new JSX runtime (#3256)
	


jest.config.js
	
feat: add ESLint package @react-three/eslint-plugin (#2698)
	


package.json
	
chore: update docs for React 19 info
	


readme.md
	
chore: move warnings to top of readme
	


tsconfig.json
	
Use new JSX runtime (#3256)
	


yarn.lock
	
fix(native): drop use-measure for react-dom peerdep (#3323)
	
Repository files navigation
README
MIT license

Warning

R3F v8 is not compatible with React 19 or Next 15, which uses React 19. Use the R3F v9 RC instead which can be installed with @react-three/fiber@rc.

Note

While we work on R3F v9 you can track compatibility of different libraries and common workarounds here.

@react-three/fiber

      

react-three-fiber is a React renderer for threejs.

Build your scene declaratively with re-usable, self-contained components that react to state, are readily interactive and can participate in React's ecosystem.

npm install three @types/three @react-three/fiber
Does it have limitations?

None. Everything that works in Threejs will work here without exception.

Is it slower than plain Threejs?

No. There is no overhead. Components render outside of React. It outperforms Threejs in scale due to React's scheduling abilities.

Can it keep up with frequent feature updates to Threejs?

Yes. It merely expresses Threejs in JSX, <mesh /> dynamically turns into new THREE.Mesh(). If a new Threejs version adds, removes or changes features, it will be available to you instantly without depending on updates to this library.

What does it look like?
Let's make a re-usable component that has its own state, reacts to user-input and participates in the render-loop. (live demo).	
import { createRoot } from 'react-dom/client'
import React, { useRef, useState } from 'react'
import { Canvas, useFrame } from '@react-three/fiber'

function Box(props) {
  // This reference gives us direct access to the THREE.Mesh object
  const ref = useRef()
  // Hold state for hovered and clicked events
  const [hovered, hover] = useState(false)
  const [clicked, click] = useState(false)
  // Subscribe this component to the render-loop, rotate the mesh every frame
  useFrame((state, delta) => (ref.current.rotation.x += delta))
  // Return the view, these are regular Threejs elements expressed in JSX
  return (
    <mesh
      {...props}
      ref={ref}
      scale={clicked ? 1.5 : 1}
      onClick={(event) => click(!clicked)}
      onPointerOver={(event) => hover(true)}
      onPointerOut={(event) => hover(false)}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color={hovered ? 'hotpink' : 'orange'} />
    </mesh>
  )
}

createRoot(document.getElementById('root')).render(
  <Canvas>
    <ambientLight intensity={Math.PI / 2} />
    <spotLight position={[10, 10, 10]} angle={0.15} penumbra={1} decay={0} intensity={Math.PI} />
    <pointLight position={[-10, -10, -10]} decay={0} intensity={Math.PI} />
    <Box position={[-1.2, 0, 0]} />
    <Box position={[1.2, 0, 0]} />
  </Canvas>,
)
Show TypeScript example
Show React Native example
Documentation, tutorials, examples

Visit docs.pmnd.rs

First steps

You need to be versed in both React and Threejs before rushing into this. If you are unsure about React consult the official React docs, especially the section about hooks. As for Threejs, make sure you at least glance over the following links:

Make sure you have a basic grasp of Threejs. Keep that site open.
When you know what a scene is, a camera, mesh, geometry, material, fork the demo above.
Look up the JSX elements that you see (mesh, ambientLight, etc), all threejs exports are native to three-fiber.
Try changing some values, scroll through our API to see what the various settings and hooks do.

Some helpful material:

Threejs-docs and examples
Discover Threejs, especially the Tips and Tricks chapter for best practices
Bruno Simons Threejs Jouney, arguably the best learning resource, now includes a full R3F chapter

Ecosystem

There is a vibrant and extensive eco system around three-fiber, full of libraries, helpers and abstractions.

@react-three/drei – useful helpers, this is an eco system in itself
@react-three/gltfjsx – turns GLTFs into JSX components
@react-three/postprocessing – post-processing effects
@react-three/uikit – WebGL rendered UI components for three-fiber
@react-three/test-renderer – for unit tests in node
@react-three/offscreen – offscreen/worker canvas for react-three-fiber
@react-three/flex – flexbox for react-three-fiber
@react-three/xr – VR/AR controllers and events
@react-three/csg – constructive solid geometry
@react-three/rapier – 3D physics using Rapier
@react-three/cannon – 3D physics using Cannon
@react-three/p2 – 2D physics using P2
@react-three/a11y – real a11y for your scene
@react-three/gpu-pathtracer – realistic path tracing
create-r3f-app next – nextjs starter
lamina – layer based shader materials
zustand – flux based state management
jotai – atoms based state management
valtio – proxy based state management
react-spring – a spring-physics-based animation library
framer-motion-3d – framer motion, a popular animation library
use-gesture – mouse/touch gestures
leva – create GUI controls in seconds
maath – a kitchen sink for math helpers
miniplex – ECS (entity management system)
composer-suite – composing shaders, particles, effects and game mechanics
triplex – scene editor for react-three-fiber
koestlich – UI component library for react-three-fiber

Usage Trend of the @react-three Family

Who is using Three-fiber

A small selection of companies and projects relying on three-fiber.

vercel (design agency)
basement (design agency)
studio freight (design agency)
14 islands (design agency)
ueno (design agency) — video
flux.ai (PCB builder)
colorful.app (modeller)
bezi (modeller)
readyplayer.me (avatar configurator)
zillow (real estate)
lumalabs.ai/genie (AI models)
skybox.blockadelabs (AI envmaps)
3dconfig (floor planer)
buerli.io (CAD)
getencube (CAD)
glowbuzzer (CAD) — video
triplex (editor) — video
theatrejs (editor) — video
How to contribute

If you like this project, please consider helping out. All contributions are welcome as well as donations to Opencollective, or in crypto BTC: 36fuguTPxGCNnYZSRdgdh6Ea94brCAjMbH, ETH: 0x6E3f79Ea1d0dcedeb33D3fC6c34d2B1f156F2682.

Backers

Thank you to all our backers! 🙏

Contributors

This project exists thanks to all the people who contribute.

About

🇨🇭 A React renderer for Three.js

docs.pmnd.rs/react-three-fiber
Topics
react threejs animation renderer fiber 3d
Resources
 Readme
License
 MIT license
 Activity
 Custom properties
Stars
 28k stars
Watchers
 214 watching
Forks
 1.6k forks
Report repository


Releases 112
v8.17.12
Latest
+ 111 releases


Sponsor this project
drcmda —
opencollective.com/react-three-fiber
Learn more about GitHub Sponsors


Used by 27.5k
+ 27,458


Contributors
213
+ 199 contributors


Languages
TypeScript
99.5%
 
Other
0.5%
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
  "title": "GitHub - pmndrs/react-three-fiber: 🇨🇭 A React renderer for Three.js",
  "description": "🇨🇭 A React renderer for Three.js. Contribute to pmndrs/react-three-fiber development by creating an account on GitHub.",
  "url": "https://github.com/pmndrs/react-three-fiber?screenshot=true",
  "content": "Skip to content\nNavigation Menu\nProduct\nSolutions\nResources\nOpen Source\nEnterprise\nPricing\nSign in\nSign up\npmndrs\n/\nreact-three-fiber\nPublic\n Sponsor\nNotifications\nFork 1.6k\n Star 28k\nCode\nIssues\n69\nPull requests\n16\nDiscussions\nActions\nProjects\nSecurity\nInsights\npmndrs/react-three-fiber\n master\nCode\nFolders and files\nName\tLast commit message\tLast commit date\n\nLatest commit\nCodyJasonBennett\nRELEASING: Releasing 2 package(s)\nec4f00b\n · \nHistory\n2,691 Commits\n\n\n.changeset\n\t\nRELEASING: Releasing 2 package(s)\n\t\n\n\n.codesandbox\n\t\ncsb: node 18 (#3157)\n\t\n\n\n.github\n\t\nchore: docs gh + dd links\n\t\n\n\n.husky\n\t\num, npx?\n\t\n\n\ndocs\n\t\nMerge pull request #3413 from tbtiberiu/fix/docs-sandpack-error\n\t\n\n\nexample\n\t\nfix(native): drop use-measure for react-dom peerdep (#3323)\n\t\n\n\npackages\n\t\nRELEASING: Releasing 2 package(s)\n\t\n\n\n.eslintignore\n\t\nchore(internals): [v6] use preconstruct\n\t\n\n\n.eslintrc.json\n\t\nchore: disable mixed imports rule\n\t\n\n\n.gitignore\n\t\nV8, react 18 beta (#1630)\n\t\n\n\n.prettierignore\n\t\nchore: Prettier CI/CD, remove deprecated options (#3260)\n\t\n\n\n.prettierrc\n\t\nchore: Prettier CI/CD, remove deprecated options (#3260)\n\t\n\n\nCONTRIBUTING.md\n\t\nclarify that yarn 1 is required, not just yarn (#2896)\n\t\n\n\nLICENSE\n\t\nUpdate LICENSE\n\t\n\n\nbabel.config.js\n\t\nUse new JSX runtime (#3256)\n\t\n\n\njest.config.js\n\t\nfeat: add ESLint package @react-three/eslint-plugin (#2698)\n\t\n\n\npackage.json\n\t\nchore: update docs for React 19 info\n\t\n\n\nreadme.md\n\t\nchore: move warnings to top of readme\n\t\n\n\ntsconfig.json\n\t\nUse new JSX runtime (#3256)\n\t\n\n\nyarn.lock\n\t\nfix(native): drop use-measure for react-dom peerdep (#3323)\n\t\nRepository files navigation\nREADME\nMIT license\n\nWarning\n\nR3F v8 is not compatible with React 19 or Next 15, which uses React 19. Use the R3F v9 RC instead which can be installed with @react-three/fiber@rc.\n\nNote\n\nWhile we work on R3F v9 you can track compatibility of different libraries and common workarounds here.\n\n@react-three/fiber\n\n      \n\nreact-three-fiber is a React renderer for threejs.\n\nBuild your scene declaratively with re-usable, self-contained components that react to state, are readily interactive and can participate in React's ecosystem.\n\nnpm install three @types/three @react-three/fiber\nDoes it have limitations?\n\nNone. Everything that works in Threejs will work here without exception.\n\nIs it slower than plain Threejs?\n\nNo. There is no overhead. Components render outside of React. It outperforms Threejs in scale due to React's scheduling abilities.\n\nCan it keep up with frequent feature updates to Threejs?\n\nYes. It merely expresses Threejs in JSX, <mesh /> dynamically turns into new THREE.Mesh(). If a new Threejs version adds, removes or changes features, it will be available to you instantly without depending on updates to this library.\n\nWhat does it look like?\nLet's make a re-usable component that has its own state, reacts to user-input and participates in the render-loop. (live demo).\t\nimport { createRoot } from 'react-dom/client'\nimport React, { useRef, useState } from 'react'\nimport { Canvas, useFrame } from '@react-three/fiber'\n\nfunction Box(props) {\n  // This reference gives us direct access to the THREE.Mesh object\n  const ref = useRef()\n  // Hold state for hovered and clicked events\n  const [hovered, hover] = useState(false)\n  const [clicked, click] = useState(false)\n  // Subscribe this component to the render-loop, rotate the mesh every frame\n  useFrame((state, delta) => (ref.current.rotation.x += delta))\n  // Return the view, these are regular Threejs elements expressed in JSX\n  return (\n    <mesh\n      {...props}\n      ref={ref}\n      scale={clicked ? 1.5 : 1}\n      onClick={(event) => click(!clicked)}\n      onPointerOver={(event) => hover(true)}\n      onPointerOut={(event) => hover(false)}>\n      <boxGeometry args={[1, 1, 1]} />\n      <meshStandardMaterial color={hovered ? 'hotpink' : 'orange'} />\n    </mesh>\n  )\n}\n\ncreateRoot(document.getElementById('root')).render(\n  <Canvas>\n    <ambientLight intensity={Math.PI / 2} />\n    <spotLight position={[10, 10, 10]} angle={0.15} penumbra={1} decay={0} intensity={Math.PI} />\n    <pointLight position={[-10, -10, -10]} decay={0} intensity={Math.PI} />\n    <Box position={[-1.2, 0, 0]} />\n    <Box position={[1.2, 0, 0]} />\n  </Canvas>,\n)\nShow TypeScript example\nShow React Native example\nDocumentation, tutorials, examples\n\nVisit docs.pmnd.rs\n\nFirst steps\n\nYou need to be versed in both React and Threejs before rushing into this. If you are unsure about React consult the official React docs, especially the section about hooks. As for Threejs, make sure you at least glance over the following links:\n\nMake sure you have a basic grasp of Threejs. Keep that site open.\nWhen you know what a scene is, a camera, mesh, geometry, material, fork the demo above.\nLook up the JSX elements that you see (mesh, ambientLight, etc), all threejs exports are native to three-fiber.\nTry changing some values, scroll through our API to see what the various settings and hooks do.\n\nSome helpful material:\n\nThreejs-docs and examples\nDiscover Threejs, especially the Tips and Tricks chapter for best practices\nBruno Simons Threejs Jouney, arguably the best learning resource, now includes a full R3F chapter\n\nEcosystem\n\nThere is a vibrant and extensive eco system around three-fiber, full of libraries, helpers and abstractions.\n\n@react-three/drei – useful helpers, this is an eco system in itself\n@react-three/gltfjsx – turns GLTFs into JSX components\n@react-three/postprocessing – post-processing effects\n@react-three/uikit – WebGL rendered UI components for three-fiber\n@react-three/test-renderer – for unit tests in node\n@react-three/offscreen – offscreen/worker canvas for react-three-fiber\n@react-three/flex – flexbox for react-three-fiber\n@react-three/xr – VR/AR controllers and events\n@react-three/csg – constructive solid geometry\n@react-three/rapier – 3D physics using Rapier\n@react-three/cannon – 3D physics using Cannon\n@react-three/p2 – 2D physics using P2\n@react-three/a11y – real a11y for your scene\n@react-three/gpu-pathtracer – realistic path tracing\ncreate-r3f-app next – nextjs starter\nlamina – layer based shader materials\nzustand – flux based state management\njotai – atoms based state management\nvaltio – proxy based state management\nreact-spring – a spring-physics-based animation library\nframer-motion-3d – framer motion, a popular animation library\nuse-gesture – mouse/touch gestures\nleva – create GUI controls in seconds\nmaath – a kitchen sink for math helpers\nminiplex – ECS (entity management system)\ncomposer-suite – composing shaders, particles, effects and game mechanics\ntriplex – scene editor for react-three-fiber\nkoestlich – UI component library for react-three-fiber\n\nUsage Trend of the @react-three Family\n\nWho is using Three-fiber\n\nA small selection of companies and projects relying on three-fiber.\n\nvercel (design agency)\nbasement (design agency)\nstudio freight (design agency)\n14 islands (design agency)\nueno (design agency) — video\nflux.ai (PCB builder)\ncolorful.app (modeller)\nbezi (modeller)\nreadyplayer.me (avatar configurator)\nzillow (real estate)\nlumalabs.ai/genie (AI models)\nskybox.blockadelabs (AI envmaps)\n3dconfig (floor planer)\nbuerli.io (CAD)\ngetencube (CAD)\nglowbuzzer (CAD) — video\ntriplex (editor) — video\ntheatrejs (editor) — video\nHow to contribute\n\nIf you like this project, please consider helping out. All contributions are welcome as well as donations to Opencollective, or in crypto BTC: 36fuguTPxGCNnYZSRdgdh6Ea94brCAjMbH, ETH: 0x6E3f79Ea1d0dcedeb33D3fC6c34d2B1f156F2682.\n\nBackers\n\nThank you to all our backers! 🙏\n\nContributors\n\nThis project exists thanks to all the people who contribute.\n\nAbout\n\n🇨🇭 A React renderer for Three.js\n\ndocs.pmnd.rs/react-three-fiber\nTopics\nreact threejs animation renderer fiber 3d\nResources\n Readme\nLicense\n MIT license\n Activity\n Custom properties\nStars\n 28k stars\nWatchers\n 214 watching\nForks\n 1.6k forks\nReport repository\n\n\nReleases 112\nv8.17.12\nLatest\n+ 111 releases\n\n\nSponsor this project\ndrcmda —\nopencollective.com/react-three-fiber\nLearn more about GitHub Sponsors\n\n\nUsed by 27.5k\n+ 27,458\n\n\nContributors\n213\n+ 199 contributors\n\n\nLanguages\nTypeScript\n99.5%\n \nOther\n0.5%\nFooter\n© 2025 GitHub, Inc.\nFooter navigation\nTerms\nPrivacy\nSecurity\nStatus\nDocs\nContact\nManage cookies\nDo not share my personal information",
  "usage": {
    "tokens": 2206
  }
}
```
