---
title: Aide - Your AI Programming Assistant
description: Code with the speed and knowledge of the best programmer you know. Aide is by your side.
url: https://aide.dev/
timestamp: 2025-01-20T16:13:44.198Z
domain: aide.dev
path: root
---

# Aide - Your AI Programming Assistant


Code with the speed and knowledge of the best programmer you know. Aide is by your side.


## Content

A proactive agent
-----------------

Aide proactively **proposes fixes** or asks to include files that may be missing in the context. Our agent can do so by **iterating on linter errors** and pulling in relevant context **using LSP tools**, like “Go to references”.

> What if LLMs could make edits across multiple files without breaking the logic? After a month of hacking, we tested our framework against [SWE-Bench Lite](https://www.swebench.com/) and (kinda shockingly) became the SOTA, resolving 43% of the issues.

![Image 16: Sandeep](https://aide.dev/_next/image?url=%2Fteam%2Fsandeep.jpeg&w=96&q=75)

Sandeep, CEO @ CodeStory

Developercontrol
----------------

Go ahead, do AI-edits on top of your coding session. We keep slim, VS Code-native checkpoints (we don’t use git) to **easily roll back** to previous states, in case the agent made any mistake.

Brainstorm, then edit.  
Or the other way around.
-------------------------------------------------

We try to make Aide feel like a real engineer to pair-program with. Chat about a problem by @’ting the file(s) and then jump into edits, or go from a smaller set of edits and discuss their side-effects.

Quick invoke
------------

Taking inspiration from MacOS spotlight, we created a floating widget you can invoke with CMD + K. If you have a text selection active, you quickly prompt a change for it.

Galaxy brain. Local-first.
--------------------------

We ship a binary called **sidecar** which takes care of preparing and sending prompts to LLMs, as well as giving them access to editor features. You get **full control** over the prompts and responses (unless you choose our subscription, sharing some data with us).

![Image 17: Placeholder](https://aide.dev/_next/image?url=%2Fsidecar-infographic.png&w=3840&q=75)

Other features
--------------

### Deep reasoning

Enforce and expose deep reasoning behind complex changes. Break down large tasks into smaller units of work that follow a logical flow.

### Blazing-fast edits

With prompt caching and multi-location editing, you will be amazed by how little time occurs between pressing enter and reviewing the changes.

### Context persistence

The editor listens to all events and changes made by both the developer and AI to keep a continuous context.

## Metadata

```json
{
  "title": "Aide - Your AI Programming Assistant",
  "description": "Code with the speed and knowledge of the best programmer you know. Aide is by your side.",
  "url": "https://aide.dev/",
  "content": "A proactive agent\n-----------------\n\nAide proactively **proposes fixes** or asks to include files that may be missing in the context. Our agent can do so by **iterating on linter errors** and pulling in relevant context **using LSP tools**, like “Go to references”.\n\n> What if LLMs could make edits across multiple files without breaking the logic? After a month of hacking, we tested our framework against [SWE-Bench Lite](https://www.swebench.com/) and (kinda shockingly) became the SOTA, resolving 43% of the issues.\n\n![Image 16: Sandeep](https://aide.dev/_next/image?url=%2Fteam%2Fsandeep.jpeg&w=96&q=75)\n\nSandeep, CEO @ CodeStory\n\nDevelopercontrol\n----------------\n\nGo ahead, do AI-edits on top of your coding session. We keep slim, VS Code-native checkpoints (we don’t use git) to **easily roll back** to previous states, in case the agent made any mistake.\n\nBrainstorm, then edit.  \nOr the other way around.\n-------------------------------------------------\n\nWe try to make Aide feel like a real engineer to pair-program with. Chat about a problem by @’ting the file(s) and then jump into edits, or go from a smaller set of edits and discuss their side-effects.\n\nQuick invoke\n------------\n\nTaking inspiration from MacOS spotlight, we created a floating widget you can invoke with CMD + K. If you have a text selection active, you quickly prompt a change for it.\n\nGalaxy brain. Local-first.\n--------------------------\n\nWe ship a binary called **sidecar** which takes care of preparing and sending prompts to LLMs, as well as giving them access to editor features. You get **full control** over the prompts and responses (unless you choose our subscription, sharing some data with us).\n\n![Image 17: Placeholder](https://aide.dev/_next/image?url=%2Fsidecar-infographic.png&w=3840&q=75)\n\nOther features\n--------------\n\n### Deep reasoning\n\nEnforce and expose deep reasoning behind complex changes. Break down large tasks into smaller units of work that follow a logical flow.\n\n### Blazing-fast edits\n\nWith prompt caching and multi-location editing, you will be amazed by how little time occurs between pressing enter and reviewing the changes.\n\n### Context persistence\n\nThe editor listens to all events and changes made by both the developer and AI to keep a continuous context.",
  "usage": {
    "tokens": 509
  }
}
```
