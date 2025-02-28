---
title: Deploy Command
description: sidekick deploy With your application deployed, it’s super simple to deploy a new version. This command will:
Make a new image of your application Check for updates in your env file and if so, re-encrypt it and sync it to server Deploy the new version without losing any traffic. Input This command does not require any input. It will use the same app config that was saved in sidekick.yml file during running launch command.
url: https://www.sidekickdeploy.com/docs/command/deploy/
timestamp: 2025-01-20T16:14:04.772Z
domain: www.sidekickdeploy.com
path: docs_command_deploy
---

# Deploy Command


sidekick deploy With your application deployed, it’s super simple to deploy a new version. This command will:
Make a new image of your application Check for updates in your env file and if so, re-encrypt it and sync it to server Deploy the new version without losing any traffic. Input This command does not require any input. It will use the same app config that was saved in sidekick.yml file during running launch command.


## Content

Deploy Command – Sidekick
===============

[Sidekick](https://www.sidekickdeploy.com/) [Docs](https://www.sidekickdeploy.com/docs/introduction "Docs") [About](https://www.sidekickdeploy.com/about "About") [Contact ↗](https://github.com/mightymoud "Contact ↗")

 CTRL K

[GitHub](https://github.com/mightymoud/sidekick "GitHub") [Twitter](https://twitter.com/mightymoud "Twitter")

 CTRL K

*   [Docs](https://www.sidekickdeploy.com/docs/)
    
    *   [Introduction](https://www.sidekickdeploy.com/docs/introduction/)
        
        *   [What Is Sidekick](https://www.sidekickdeploy.com/docs/introduction/what-is-sidekick/)
        *   [Get Started](https://www.sidekickdeploy.com/docs/introduction/get-started/)
        
    *   [Commands](https://www.sidekickdeploy.com/docs/command/)
        
        *   [Init Command](https://www.sidekickdeploy.com/docs/command/init/)
        *   [Launch Command](https://www.sidekickdeploy.com/docs/command/launch/)
        *   [Deploy Command](https://www.sidekickdeploy.com/docs/command/deploy/)
            
            *   [Input](https://www.sidekickdeploy.com/docs/command/deploy/#input)
            *   [Gotchas](https://www.sidekickdeploy.com/docs/command/deploy/#gotchas)
            *   [What does Sidekick do when I run this?](https://www.sidekickdeploy.com/docs/command/deploy/#what-does-sidekick-do-when-i-run-this)
            *   [Changelog](https://www.sidekickdeploy.com/docs/command/deploy/#changelog)
            
            *   [Preview](https://www.sidekickdeploy.com/docs/command/deploy/preview/)
            
        
    *   [Ethos](https://www.sidekickdeploy.com/docs/ethos/)
        
        *   [Principles](https://www.sidekickdeploy.com/docs/ethos/principles/)
        *   [Vision](https://www.sidekickdeploy.com/docs/ethos/vision/)
        *   [Why Sidekick](https://www.sidekickdeploy.com/docs/ethos/why-sidekick/)
        
    *   [Design](https://www.sidekickdeploy.com/docs/design/)
        
        *   [Docker Images](https://www.sidekickdeploy.com/docs/design/docker-images/)
        *   [Secrets](https://www.sidekickdeploy.com/docs/design/secrets/)
        *   [Reverse Proxy](https://www.sidekickdeploy.com/docs/design/reverse-proxy/)
        *   [Security](https://www.sidekickdeploy.com/docs/design/security/)
        
    
*   [About](https://www.sidekickdeploy.com/about/)

*   [Introduction](https://www.sidekickdeploy.com/docs/introduction/)
    
    *   [What Is Sidekick](https://www.sidekickdeploy.com/docs/introduction/what-is-sidekick/)
    *   [Get Started](https://www.sidekickdeploy.com/docs/introduction/get-started/)
    
*   [Commands](https://www.sidekickdeploy.com/docs/command/)
    
    *   [Init Command](https://www.sidekickdeploy.com/docs/command/init/)
    *   [Launch Command](https://www.sidekickdeploy.com/docs/command/launch/)
    *   [Deploy Command](https://www.sidekickdeploy.com/docs/command/deploy/)
        
        *   [Preview](https://www.sidekickdeploy.com/docs/command/deploy/preview/)
        
    
*   [Ethos](https://www.sidekickdeploy.com/docs/ethos/)
    
    *   [Principles](https://www.sidekickdeploy.com/docs/ethos/principles/)
    *   [Vision](https://www.sidekickdeploy.com/docs/ethos/vision/)
    *   [Why Sidekick](https://www.sidekickdeploy.com/docs/ethos/why-sidekick/)
    
*   [Design](https://www.sidekickdeploy.com/docs/design/)
    
    *   [Docker Images](https://www.sidekickdeploy.com/docs/design/docker-images/)
    *   [Secrets](https://www.sidekickdeploy.com/docs/design/secrets/)
    *   [Reverse Proxy](https://www.sidekickdeploy.com/docs/design/reverse-proxy/)
    *   [Security](https://www.sidekickdeploy.com/docs/design/security/)
    

LightDark

On this page

*   [Input](https://www.sidekickdeploy.com/docs/command/deploy/#input)
*   [Gotchas](https://www.sidekickdeploy.com/docs/command/deploy/#gotchas)
*   [What does Sidekick do when I run this?](https://www.sidekickdeploy.com/docs/command/deploy/#what-does-sidekick-do-when-i-run-this)
*   [Changelog](https://www.sidekickdeploy.com/docs/command/deploy/#changelog)

Scroll to top

[Docs](https://www.sidekickdeploy.com/docs/)

[Commands](https://www.sidekickdeploy.com/docs/command/)

Deploy Command

Deploy Command
==============

![Image 3: Hero image](https://raw.githubusercontent.com/MightyMoud/sidekick/main/demo/imgs/deploy.png)

```bash
sidekick deploy
```

With your application deployed, it’s super simple to deploy a new version. This command will:

*   Make a new image of your application
*   Check for updates in your env file and if so, re-encrypt it and sync it to server
*   Deploy the new version without losing any traffic.

Input[](https://www.sidekickdeploy.com/docs/command/deploy/#input)
------------------------------------------------------------------

This command does not require any input. It will use the same app config that was saved in `sidekick.yml` file during running `launch` command.

Gotchas[](https://www.sidekickdeploy.com/docs/command/deploy/#gotchas)
----------------------------------------------------------------------

*   Sidekick will check for updates in your env file and will re-encrypt its content if it has changed
*   Sidekick will save the docker image in a file and use `scp` to move that to your VPS then load it up. Make sure your VPS has enough space.

What does Sidekick do when I run this?[](https://www.sidekickdeploy.com/docs/command/deploy/#what-does-sidekick-do-when-i-run-this)
-----------------------------------------------------------------------------------------------------------------------------------

*   Build your docker image locally for linux
*   Compare your latest env file checksum for changes from last time you deployed your application.
*   If your env file has changed, sidekick will re-encrypt it and replace the encrypted.env file on your server.
*   Deploy the new version with zero downtime deploys so you don’t miss any traffic.

Changelog[](https://www.sidekickdeploy.com/docs/command/deploy/#changelog)
--------------------------------------------------------------------------

NA

[Preview](https://www.sidekickdeploy.com/docs/command/deploy/preview/ "Preview")

© 2024 Sidekick

## Metadata

```json
{
  "title": "Deploy Command",
  "description": "sidekick deploy With your application deployed, it’s super simple to deploy a new version. This command will:\nMake a new image of your application Check for updates in your env file and if so, re-encrypt it and sync it to server Deploy the new version without losing any traffic. Input This command does not require any input. It will use the same app config that was saved in sidekick.yml file during running launch command.",
  "url": "https://www.sidekickdeploy.com/docs/command/deploy/",
  "content": "Deploy Command – Sidekick\n===============\n\n[Sidekick](https://www.sidekickdeploy.com/) [Docs](https://www.sidekickdeploy.com/docs/introduction \"Docs\") [About](https://www.sidekickdeploy.com/about \"About\") [Contact ↗](https://github.com/mightymoud \"Contact ↗\")\n\n CTRL K\n\n[GitHub](https://github.com/mightymoud/sidekick \"GitHub\") [Twitter](https://twitter.com/mightymoud \"Twitter\")\n\n CTRL K\n\n*   [Docs](https://www.sidekickdeploy.com/docs/)\n    \n    *   [Introduction](https://www.sidekickdeploy.com/docs/introduction/)\n        \n        *   [What Is Sidekick](https://www.sidekickdeploy.com/docs/introduction/what-is-sidekick/)\n        *   [Get Started](https://www.sidekickdeploy.com/docs/introduction/get-started/)\n        \n    *   [Commands](https://www.sidekickdeploy.com/docs/command/)\n        \n        *   [Init Command](https://www.sidekickdeploy.com/docs/command/init/)\n        *   [Launch Command](https://www.sidekickdeploy.com/docs/command/launch/)\n        *   [Deploy Command](https://www.sidekickdeploy.com/docs/command/deploy/)\n            \n            *   [Input](https://www.sidekickdeploy.com/docs/command/deploy/#input)\n            *   [Gotchas](https://www.sidekickdeploy.com/docs/command/deploy/#gotchas)\n            *   [What does Sidekick do when I run this?](https://www.sidekickdeploy.com/docs/command/deploy/#what-does-sidekick-do-when-i-run-this)\n            *   [Changelog](https://www.sidekickdeploy.com/docs/command/deploy/#changelog)\n            \n            *   [Preview](https://www.sidekickdeploy.com/docs/command/deploy/preview/)\n            \n        \n    *   [Ethos](https://www.sidekickdeploy.com/docs/ethos/)\n        \n        *   [Principles](https://www.sidekickdeploy.com/docs/ethos/principles/)\n        *   [Vision](https://www.sidekickdeploy.com/docs/ethos/vision/)\n        *   [Why Sidekick](https://www.sidekickdeploy.com/docs/ethos/why-sidekick/)\n        \n    *   [Design](https://www.sidekickdeploy.com/docs/design/)\n        \n        *   [Docker Images](https://www.sidekickdeploy.com/docs/design/docker-images/)\n        *   [Secrets](https://www.sidekickdeploy.com/docs/design/secrets/)\n        *   [Reverse Proxy](https://www.sidekickdeploy.com/docs/design/reverse-proxy/)\n        *   [Security](https://www.sidekickdeploy.com/docs/design/security/)\n        \n    \n*   [About](https://www.sidekickdeploy.com/about/)\n\n*   [Introduction](https://www.sidekickdeploy.com/docs/introduction/)\n    \n    *   [What Is Sidekick](https://www.sidekickdeploy.com/docs/introduction/what-is-sidekick/)\n    *   [Get Started](https://www.sidekickdeploy.com/docs/introduction/get-started/)\n    \n*   [Commands](https://www.sidekickdeploy.com/docs/command/)\n    \n    *   [Init Command](https://www.sidekickdeploy.com/docs/command/init/)\n    *   [Launch Command](https://www.sidekickdeploy.com/docs/command/launch/)\n    *   [Deploy Command](https://www.sidekickdeploy.com/docs/command/deploy/)\n        \n        *   [Preview](https://www.sidekickdeploy.com/docs/command/deploy/preview/)\n        \n    \n*   [Ethos](https://www.sidekickdeploy.com/docs/ethos/)\n    \n    *   [Principles](https://www.sidekickdeploy.com/docs/ethos/principles/)\n    *   [Vision](https://www.sidekickdeploy.com/docs/ethos/vision/)\n    *   [Why Sidekick](https://www.sidekickdeploy.com/docs/ethos/why-sidekick/)\n    \n*   [Design](https://www.sidekickdeploy.com/docs/design/)\n    \n    *   [Docker Images](https://www.sidekickdeploy.com/docs/design/docker-images/)\n    *   [Secrets](https://www.sidekickdeploy.com/docs/design/secrets/)\n    *   [Reverse Proxy](https://www.sidekickdeploy.com/docs/design/reverse-proxy/)\n    *   [Security](https://www.sidekickdeploy.com/docs/design/security/)\n    \n\nLightDark\n\nOn this page\n\n*   [Input](https://www.sidekickdeploy.com/docs/command/deploy/#input)\n*   [Gotchas](https://www.sidekickdeploy.com/docs/command/deploy/#gotchas)\n*   [What does Sidekick do when I run this?](https://www.sidekickdeploy.com/docs/command/deploy/#what-does-sidekick-do-when-i-run-this)\n*   [Changelog](https://www.sidekickdeploy.com/docs/command/deploy/#changelog)\n\nScroll to top\n\n[Docs](https://www.sidekickdeploy.com/docs/)\n\n[Commands](https://www.sidekickdeploy.com/docs/command/)\n\nDeploy Command\n\nDeploy Command\n==============\n\n![Image 3: Hero image](https://raw.githubusercontent.com/MightyMoud/sidekick/main/demo/imgs/deploy.png)\n\n```bash\nsidekick deploy\n```\n\nWith your application deployed, it’s super simple to deploy a new version. This command will:\n\n*   Make a new image of your application\n*   Check for updates in your env file and if so, re-encrypt it and sync it to server\n*   Deploy the new version without losing any traffic.\n\nInput[](https://www.sidekickdeploy.com/docs/command/deploy/#input)\n------------------------------------------------------------------\n\nThis command does not require any input. It will use the same app config that was saved in `sidekick.yml` file during running `launch` command.\n\nGotchas[](https://www.sidekickdeploy.com/docs/command/deploy/#gotchas)\n----------------------------------------------------------------------\n\n*   Sidekick will check for updates in your env file and will re-encrypt its content if it has changed\n*   Sidekick will save the docker image in a file and use `scp` to move that to your VPS then load it up. Make sure your VPS has enough space.\n\nWhat does Sidekick do when I run this?[](https://www.sidekickdeploy.com/docs/command/deploy/#what-does-sidekick-do-when-i-run-this)\n-----------------------------------------------------------------------------------------------------------------------------------\n\n*   Build your docker image locally for linux\n*   Compare your latest env file checksum for changes from last time you deployed your application.\n*   If your env file has changed, sidekick will re-encrypt it and replace the encrypted.env file on your server.\n*   Deploy the new version with zero downtime deploys so you don’t miss any traffic.\n\nChangelog[](https://www.sidekickdeploy.com/docs/command/deploy/#changelog)\n--------------------------------------------------------------------------\n\nNA\n\n[Preview](https://www.sidekickdeploy.com/docs/command/deploy/preview/ \"Preview\")\n\n© 2024 Sidekick",
  "usage": {
    "tokens": 1457
  }
}
```
