---
title: Announcing All Hands Online (Beta)
description: Today we're excited to announce our official hosted version of the OpenHands AI software developer! Learn about our new features including GitHub integration and improved multi-session support.
url: https://www.all-hands.dev/blog/announcing-all-hands-online-beta
timestamp: 2025-01-20T16:14:30.904Z
domain: www.all-hands.dev
path: blog_announcing-all-hands-online-beta
---

# Announcing All Hands Online (Beta)


Today we're excited to announce our official hosted version of the OpenHands AI software developer! Learn about our new features including GitHub integration and improved multi-session support.


## Content

Today we're excited to announce something we've been working hard for for the past couple months: we now have an official hosted version of the OpenHands AI software developer!

OpenHands is an open source project for software development agents, and now [boasts the strongest AI software development agent in the world](https://www.all-hands.dev/blog/openhands-codeact-21-an-open-state-of-the-art-software-development-agent), resolving over 50% of real github issues on the standard SWE-Bench Verified benchmark. OpenHands will always remain open source and free for every developer to run locally, but at the same time, spinning up the software and development sandboxes on your computer has been a major pain point for users. Now all you have to do is go to app.all-hands.dev and get to work within seconds!

We're doing a gradual rollout to ensure we can scale up to meet demand. We've already invited our core open source maintainers, and will be adding more users over the coming weeks. We expect to have a fully open release in early 2025.

If you'd like to join the waitlist, you can [sign up](https://www.all-hands.dev/join-waitlist) at all-hands.dev. In the meantime, you can also go over to the [GitHub repo](https://github.com/All-Hands-AI/OpenHands) and download it yourself, as always. We will also be prioritizing waitlist access to OpenHands contributors, so this is as good a time as ever to start contributing!

New UI
------

We've completely redesigned the OpenHands interface to be more intuitive and easier to use. The new UI includes:

*   A cleaner, more modern look
*   Better organization of conversations and projects
*   Improved visibility into what the agent is doing
*   More intuitive navigation

![Image 6: New OpenHands UI](https://www.all-hands.dev/assets/blog/20241104-beta-rollout/new-ui.png)

Huge thanks to Paul Bloch for his work on the designs here, and to Stephan Psaras for his implementation.

Github Integration
------------------

One of the tricky things about the hosted version of OpenHands is that we don't have access to your local filesystem. So if you want to work with an existing project, you need a way to get all that code into OpenHands.

One way to do this is by uploading a .zip archive of your codebase. But most of us are comfortable with GitHub, so we built an integration that allows you to connect any GitHub repo into OpenHands:

![Image 7: GitHub Integration](https://www.all-hands.dev/assets/blog/20241104-beta-rollout/github-integration.png)

Once you connect a project, OpenHands will automatically clone that project for you. It will also provide the agent with a GitHub token which allows it to push changes and create pull requests.

We have plans for an even deeper GitHub integration in the near future, like showing the PR status inside the UI. We'd love for OpenHands to automatically detect when the CI checks failed, and fix the issue for you!

Improved Robustness for Multi-session Support
---------------------------------------------

The trickiest thing about moving to a hosted version of OpenHands was creating a highly available, multi-tenant application.

OpenHands has grown organically as an open source project, and was only ever run by single users on their own laptop. If multiple users tried to connect to the same server, often there would be problems. It was easy for one user's error to crash or freeze the entire application!

We did a bunch of refactoring to mitigate these problems. We've incorporated threading and async logic where appropriate to ensure that no single user can lock up the server, making the application much more reliable.

We also got rid of a few antipatterns inside of OpenHands that don't work well in a cloud native environment. In particular, we stopped storing any application state in-memory, so that we can have multiple instances of OpenHands serving users, without worrying about which user connects to which instance. We can even kill the instance you're connected to without interrupting your session–you'll automatically reconnect to a new instance without noticing.

Many thanks to Tim O'Farrell for his work on making our application server more robust.

Future Plans
------------

This is just the start for OpenHands: we've got a lot of great features in development now. In particular, we're working on support for having multiple conversations simultaneously, adding the ability to extend and customize the agent's behavior, and a deeper GitHub integration. And as always we're working hard on making our core agent better and better, so it can take on even bigger issues with higher accuracy.

Stay tuned!

## Metadata

```json
{
  "title": "Announcing All Hands Online (Beta)",
  "description": "Today we're excited to announce our official hosted version of the OpenHands AI software developer! Learn about our new features including GitHub integration and improved multi-session support.",
  "url": "https://www.all-hands.dev/blog/announcing-all-hands-online-beta",
  "content": "Today we're excited to announce something we've been working hard for for the past couple months: we now have an official hosted version of the OpenHands AI software developer!\n\nOpenHands is an open source project for software development agents, and now [boasts the strongest AI software development agent in the world](https://www.all-hands.dev/blog/openhands-codeact-21-an-open-state-of-the-art-software-development-agent), resolving over 50% of real github issues on the standard SWE-Bench Verified benchmark. OpenHands will always remain open source and free for every developer to run locally, but at the same time, spinning up the software and development sandboxes on your computer has been a major pain point for users. Now all you have to do is go to app.all-hands.dev and get to work within seconds!\n\nWe're doing a gradual rollout to ensure we can scale up to meet demand. We've already invited our core open source maintainers, and will be adding more users over the coming weeks. We expect to have a fully open release in early 2025.\n\nIf you'd like to join the waitlist, you can [sign up](https://www.all-hands.dev/join-waitlist) at all-hands.dev. In the meantime, you can also go over to the [GitHub repo](https://github.com/All-Hands-AI/OpenHands) and download it yourself, as always. We will also be prioritizing waitlist access to OpenHands contributors, so this is as good a time as ever to start contributing!\n\nNew UI\n------\n\nWe've completely redesigned the OpenHands interface to be more intuitive and easier to use. The new UI includes:\n\n*   A cleaner, more modern look\n*   Better organization of conversations and projects\n*   Improved visibility into what the agent is doing\n*   More intuitive navigation\n\n![Image 6: New OpenHands UI](https://www.all-hands.dev/assets/blog/20241104-beta-rollout/new-ui.png)\n\nHuge thanks to Paul Bloch for his work on the designs here, and to Stephan Psaras for his implementation.\n\nGithub Integration\n------------------\n\nOne of the tricky things about the hosted version of OpenHands is that we don't have access to your local filesystem. So if you want to work with an existing project, you need a way to get all that code into OpenHands.\n\nOne way to do this is by uploading a .zip archive of your codebase. But most of us are comfortable with GitHub, so we built an integration that allows you to connect any GitHub repo into OpenHands:\n\n![Image 7: GitHub Integration](https://www.all-hands.dev/assets/blog/20241104-beta-rollout/github-integration.png)\n\nOnce you connect a project, OpenHands will automatically clone that project for you. It will also provide the agent with a GitHub token which allows it to push changes and create pull requests.\n\nWe have plans for an even deeper GitHub integration in the near future, like showing the PR status inside the UI. We'd love for OpenHands to automatically detect when the CI checks failed, and fix the issue for you!\n\nImproved Robustness for Multi-session Support\n---------------------------------------------\n\nThe trickiest thing about moving to a hosted version of OpenHands was creating a highly available, multi-tenant application.\n\nOpenHands has grown organically as an open source project, and was only ever run by single users on their own laptop. If multiple users tried to connect to the same server, often there would be problems. It was easy for one user's error to crash or freeze the entire application!\n\nWe did a bunch of refactoring to mitigate these problems. We've incorporated threading and async logic where appropriate to ensure that no single user can lock up the server, making the application much more reliable.\n\nWe also got rid of a few antipatterns inside of OpenHands that don't work well in a cloud native environment. In particular, we stopped storing any application state in-memory, so that we can have multiple instances of OpenHands serving users, without worrying about which user connects to which instance. We can even kill the instance you're connected to without interrupting your session–you'll automatically reconnect to a new instance without noticing.\n\nMany thanks to Tim O'Farrell for his work on making our application server more robust.\n\nFuture Plans\n------------\n\nThis is just the start for OpenHands: we've got a lot of great features in development now. In particular, we're working on support for having multiple conversations simultaneously, adding the ability to extend and customize the agent's behavior, and a deeper GitHub integration. And as always we're working hard on making our core agent better and better, so it can take on even bigger issues with higher accuracy.\n\nStay tuned!",
  "usage": {
    "tokens": 970
  }
}
```
