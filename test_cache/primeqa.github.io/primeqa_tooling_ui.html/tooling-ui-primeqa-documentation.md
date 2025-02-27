---
title: Tooling UI — PrimeQA documentation
description: 
url: https://primeqa.github.io/primeqa/tooling_ui.html
timestamp: 2025-01-20T15:57:50.712Z
domain: primeqa.github.io
path: primeqa_tooling_ui.html
---

# Tooling UI — PrimeQA documentation



## Content

![Image 8](https://primeqa.github.io/primeqa/_static/img/PrimeQA.png)

[![Image 9: LICENSE|Apache2.0](https://img.shields.io/github/license/saltstack/salt?color=blue)](https://www.apache.org/licenses/LICENSE-2.0.txt)

### ✔️ Getting Started

*   [Repository](https://github.com/primeqa/primeqa-ui)
    
*   This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app)
    

### ✅ Prerequisites

*   [Yarn](https://classic.yarnpkg.com/en/docs/install)
    

### 🧩 Setup Local Environment

*   Dowload all necessary packages to build and deploy the application: `yarn install`
    
*   Open `.env` files and set `REACT_APP_API_URL` to point to services:
    
    *   local: [http://localhost:{PORT}](http://localhost:%7BPORT%7D)
        

### 💻 Run Locally

*   Run the app in the __development mode__: `yarn start`
    
*   Open [http://localhost:8888](http://localhost:8888/) to view it in the browser.
    

### 💻 Setup & Run Docker

This allows us to run the build in a node image and server the app using an nginx image.  
The final Docker image will just contain the build folder and nothing else  
(the project files were only used by to build the project in the builder layer, which then gets thrown away)  
it’s just an intermmediary step.

*   `docker build . -t primeqa_ui`
    
*   `docker run --rm --name primeqa_ui -d -p 82:82 primeqa_ui:$(cat VERSION)`
    
    *   82 -\> public port to access
        
    *   82 -\> container expose port
        
*   stop container: `docker stop  primeqa_ui`
    
*   remove container: `docker rm primeqa_ui`
    
*   remove image: `docker rmi primeqa_ui`

## Metadata

```json
{
  "title": "Tooling UI — PrimeQA documentation",
  "description": "",
  "url": "https://primeqa.github.io/primeqa/tooling_ui.html",
  "content": "![Image 8](https://primeqa.github.io/primeqa/_static/img/PrimeQA.png)\n\n[![Image 9: LICENSE|Apache2.0](https://img.shields.io/github/license/saltstack/salt?color=blue)](https://www.apache.org/licenses/LICENSE-2.0.txt)\n\n### ✔️ Getting Started\n\n*   [Repository](https://github.com/primeqa/primeqa-ui)\n    \n*   This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app)\n    \n\n### ✅ Prerequisites\n\n*   [Yarn](https://classic.yarnpkg.com/en/docs/install)\n    \n\n### 🧩 Setup Local Environment\n\n*   Dowload all necessary packages to build and deploy the application: `yarn install`\n    \n*   Open `.env` files and set `REACT_APP_API_URL` to point to services:\n    \n    *   local: [http://localhost:{PORT}](http://localhost:%7BPORT%7D)\n        \n\n### 💻 Run Locally\n\n*   Run the app in the __development mode__: `yarn start`\n    \n*   Open [http://localhost:8888](http://localhost:8888/) to view it in the browser.\n    \n\n### 💻 Setup & Run Docker\n\nThis allows us to run the build in a node image and server the app using an nginx image.  \nThe final Docker image will just contain the build folder and nothing else  \n(the project files were only used by to build the project in the builder layer, which then gets thrown away)  \nit’s just an intermmediary step.\n\n*   `docker build . -t primeqa_ui`\n    \n*   `docker run --rm --name primeqa_ui -d -p 82:82 primeqa_ui:$(cat VERSION)`\n    \n    *   82 -\\> public port to access\n        \n    *   82 -\\> container expose port\n        \n*   stop container: `docker stop  primeqa_ui`\n    \n*   remove container: `docker rm primeqa_ui`\n    \n*   remove image: `docker rmi primeqa_ui`",
  "usage": {
    "tokens": 447
  }
}
```
