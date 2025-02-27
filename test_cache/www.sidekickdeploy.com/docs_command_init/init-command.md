---
title: Init Command
description: sidekick init This command is meant to setup your VPS and prepare it for hosting your applications. This command will run multiple commands on the VPS following best practices.
Once this command is done your VPS will have the following installed:
Docker Sops Age Traefik Curl Vim Input ℹ️ New in V0.6.1 - You can now pass inputs as flags and skip this step completely. When running this command you will be prompted to enter two values:
url: https://www.sidekickdeploy.com/docs/command/init/
timestamp: 2025-01-20T16:14:05.558Z
domain: www.sidekickdeploy.com
path: docs_command_init
---

# Init Command


sidekick init This command is meant to setup your VPS and prepare it for hosting your applications. This command will run multiple commands on the VPS following best practices.
Once this command is done your VPS will have the following installed:
Docker Sops Age Traefik Curl Vim Input ℹ️ New in V0.6.1 - You can now pass inputs as flags and skip this step completely. When running this command you will be prompted to enter two values:


## Content

![Image 3: Hero image](https://raw.githubusercontent.com/MightyMoud/sidekick/main/demo/imgs/init.png)

This command is meant to setup your VPS and prepare it for hosting your applications. This command will run multiple commands on the VPS following best practices.

Once this command is done your VPS will have the following installed:

*   Docker
*   Sops
*   Age
*   Traefik
*   Curl
*   Vim

Input[](https://www.sidekickdeploy.com/docs/command/init/#input)
----------------------------------------------------------------

New in V0.6.1 - You can now pass inputs as flags and skip this step completely.

When running this command you will be prompted to enter two values:

*   IP address of your VPS.
*   An email address to use for auto TLS certs.

After this you will be shown the randomart and fingerprint of your VPS’s public key. This is a crucial step in the authentication process. Once approved Sidekick will add the Address/public key pair to `known_hosts` on your system. This will allow you and Sidekick to login faster using SSH to your server.

The full list of bash commands that will run can be viewed on [Github](https://github.com/MightyMoud/sidekick/blob/main/utils/stages.go).

If you run this command once more and enter a different IP Address, Sidekick will warn you that you are overriding the current config with a prompt. You can also skip that prompt by passing `-y` flag.

So for short quick use, you can do this:

**Which SSH key will Sidekick use to login?**

Flags[](https://www.sidekickdeploy.com/docs/command/init/#flags)
----------------------------------------------------------------

*   `--server` or `-s` - provides the server ip address
*   `--email` or `-e` - provides the email address for TLS certs
*   `--yes` or `-y` - override the confirmation prompts when trying to setup a new server when an old server is already setup

Gotchas[](https://www.sidekickdeploy.com/docs/command/init/#gotchas)
--------------------------------------------------------------------

*   Sidekick will use `root` user by default to SSH into your VPS for the first time.
*   Sidekick will disable `root` SSH login during this command. You can re-login using `sidekick@ip` later if you want.

What does Sidekick do when I run this?[](https://www.sidekickdeploy.com/docs/command/init/#what-does-sidekick-do-when-i-run-this)
---------------------------------------------------------------------------------------------------------------------------------

*   Check if `brew` is installed and if not will throw an error
*   Install `sops` locally on your machine for use later
*   Login with `root` user
*   Make a new user `sidekick` and grant sudo access
*   Logout from `root` and login with `sidekick`
*   Disable login with `root` user - security best practice
*   Update and upgrade your Ubuntu system
*   Install `sops` & `age` on your server.
*   Use `age` to make secret and public keys to use later.
*   Send public key back to your host machine to be used later for encryption
*   Install Docker
*   Add `sidekick` user to docker group
*   Setup Traefik and TSL certs on your VPS

During this setup Sidekick will clone this [repo](https://www.github.com/mightymoud/sidekick-traefik) to your VPS.

Changelog[](https://www.sidekickdeploy.com/docs/command/init/#changelog)
------------------------------------------------------------------------

*   V0.6.4 - Added a new step to check if `brew` is present and install `sops` locally.
*   V0.6.1 - Added default ssh keys use.
*   V0.6.1 - Added flags to skip input step.
*   V0.6.0 - Added host key validation prompt with randomart and key fingerprint.
*   V0.6.0 - Moved away from using a docker registry to host images.

## Metadata

```json
{
  "title": "Init Command",
  "description": "sidekick init This command is meant to setup your VPS and prepare it for hosting your applications. This command will run multiple commands on the VPS following best practices.\nOnce this command is done your VPS will have the following installed:\nDocker Sops Age Traefik Curl Vim Input ℹ️ New in V0.6.1 - You can now pass inputs as flags and skip this step completely. When running this command you will be prompted to enter two values:",
  "url": "https://www.sidekickdeploy.com/docs/command/init/",
  "content": "![Image 3: Hero image](https://raw.githubusercontent.com/MightyMoud/sidekick/main/demo/imgs/init.png)\n\nThis command is meant to setup your VPS and prepare it for hosting your applications. This command will run multiple commands on the VPS following best practices.\n\nOnce this command is done your VPS will have the following installed:\n\n*   Docker\n*   Sops\n*   Age\n*   Traefik\n*   Curl\n*   Vim\n\nInput[](https://www.sidekickdeploy.com/docs/command/init/#input)\n----------------------------------------------------------------\n\nNew in V0.6.1 - You can now pass inputs as flags and skip this step completely.\n\nWhen running this command you will be prompted to enter two values:\n\n*   IP address of your VPS.\n*   An email address to use for auto TLS certs.\n\nAfter this you will be shown the randomart and fingerprint of your VPS’s public key. This is a crucial step in the authentication process. Once approved Sidekick will add the Address/public key pair to `known_hosts` on your system. This will allow you and Sidekick to login faster using SSH to your server.\n\nThe full list of bash commands that will run can be viewed on [Github](https://github.com/MightyMoud/sidekick/blob/main/utils/stages.go).\n\nIf you run this command once more and enter a different IP Address, Sidekick will warn you that you are overriding the current config with a prompt. You can also skip that prompt by passing `-y` flag.\n\nSo for short quick use, you can do this:\n\n**Which SSH key will Sidekick use to login?**\n\nFlags[](https://www.sidekickdeploy.com/docs/command/init/#flags)\n----------------------------------------------------------------\n\n*   `--server` or `-s` - provides the server ip address\n*   `--email` or `-e` - provides the email address for TLS certs\n*   `--yes` or `-y` - override the confirmation prompts when trying to setup a new server when an old server is already setup\n\nGotchas[](https://www.sidekickdeploy.com/docs/command/init/#gotchas)\n--------------------------------------------------------------------\n\n*   Sidekick will use `root` user by default to SSH into your VPS for the first time.\n*   Sidekick will disable `root` SSH login during this command. You can re-login using `sidekick@ip` later if you want.\n\nWhat does Sidekick do when I run this?[](https://www.sidekickdeploy.com/docs/command/init/#what-does-sidekick-do-when-i-run-this)\n---------------------------------------------------------------------------------------------------------------------------------\n\n*   Check if `brew` is installed and if not will throw an error\n*   Install `sops` locally on your machine for use later\n*   Login with `root` user\n*   Make a new user `sidekick` and grant sudo access\n*   Logout from `root` and login with `sidekick`\n*   Disable login with `root` user - security best practice\n*   Update and upgrade your Ubuntu system\n*   Install `sops` & `age` on your server.\n*   Use `age` to make secret and public keys to use later.\n*   Send public key back to your host machine to be used later for encryption\n*   Install Docker\n*   Add `sidekick` user to docker group\n*   Setup Traefik and TSL certs on your VPS\n\nDuring this setup Sidekick will clone this [repo](https://www.github.com/mightymoud/sidekick-traefik) to your VPS.\n\nChangelog[](https://www.sidekickdeploy.com/docs/command/init/#changelog)\n------------------------------------------------------------------------\n\n*   V0.6.4 - Added a new step to check if `brew` is present and install `sops` locally.\n*   V0.6.1 - Added default ssh keys use.\n*   V0.6.1 - Added flags to skip input step.\n*   V0.6.0 - Added host key validation prompt with randomart and key fingerprint.\n*   V0.6.0 - Moved away from using a docker registry to host images.",
  "publishedTime": "2024-09-25T20:30:56+09:00",
  "usage": {
    "tokens": 857
  }
}
```
