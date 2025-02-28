---
title: We can all be AI engineers – and we can do it with open source models
description: The barriers to AI engineering are crumbling fast
url: https://blog.helix.ml/p/we-can-all-be-ai-engineers?utm_source=tldrai
timestamp: 2025-01-20T16:18:03.241Z
domain: blog.helix.ml
path: p_we-can-all-be-ai-engineers
---

# We can all be AI engineers – and we can do it with open source models


The barriers to AI engineering are crumbling fast


## Content

[![Image 12](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b127cec-2c23-4484-997e-120a7f35f435_1344x768.webp)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b127cec-2c23-4484-997e-120a7f35f435_1344x768.webp)

A couple of weeks ago, I gave a talk at [Hannah Foxwell’s](https://www.linkedin.com/in/hannah-foxwell/) amazing AI for the Rest of Us conference about something that's been brewing in my mind after years of working in DevOps, MLOps, and now GenAI: the barriers to AI engineering are crumbling fast. The tools have gotten good enough that if you can handle an IDE and push some YAML to git, you're already qualified.

Having lived through the evolution from DevOps (ClusterHQ) to MLOps (Dotscience) and now diving deep into GenAI with HelixML, I keep seeing the same pattern: complex tools get simpler, workflows get standardized, and suddenly what seemed like rocket science becomes just... more engineering.

Building an AI application comes down to six building blocks:

1.  **Models**: Just mathematical functions. Complex ones, sure, but at their core, they're just turning words into numbers and back again.
    
2.  **Prompts**: Telling the model what to do in plain English. Sometimes you need to be really explicit - like talking to a toddler.
    
3.  **Knowledge**: Your AI's personal knowledge base. Documents, websites, whatever you need it to learn from.
    
4.  **Integrations**: This is where it gets interesting - connecting your AI to real business systems through APIs.
    
5.  **Tests**: Because nobody wants their AI going sideways in production. Yes, you can test AI apps, and you absolutely should.
    
6.  **Deployment**: Running it on a server. For example, versioning the entire app above in a yaml file and [using Flux to manage deployment to K8s and Helix](https://blog.helix.ml/p/announcing-helix-14-cicd-for-cloud).
    

Here's where my DevOps background kicks in. You know all those tools you're already using? Git? CI/CD pipelines? They work for AI apps too. I demonstrated this live in the talk by building a Jira integration that could write code based on ticket descriptions.

The secret sauce? Something we're calling an "[AISpec](https://aispec.org/)" - a YAML file that pulls all these pieces together in a way that feels natural to anyone who's worked with modern infrastructure tools.

This bit's important: when you use open source models, your data stays yours. It doesn't end up training someone else's model. For companies worried about GDPR or other national, regional or corporate regulation, this is crucial. You can run everything locally, in your own infrastructure, with your data staying right where your legal team wants it.

If you're reading this thinking "show me the code," I've got you covered. Here’s a complete reference architecture you can set up to do this stuff yourself: **[https://github.com/helixml/genai-cicd-ref](https://github.com/helixml/genai-cicd-ref)**

And here’s a complete tutorial of using and setting up the reference architecture:

The main thing I want you to take away is this: if you can handle version control and basic deployment workflows, you can build production-ready AI applications. The tools are there. The models are there. And they're getting better every day.

Check out [aispec.org](https://aispec.org/) if you want to dig into the standard format we're proposing for all this. Or if you want to chat about any of this, [find me on LinkedIn](https://www.linkedin.com/in/luke-marsden-71b3789/) or drop me an email at [luke@helix.ml](mailto:luke@helix.ml).

This is about making AI engineering accessible to everyone who knows how to ship code. No PhD required, no magic - just solid engineering practices applied to these powerful new tools.

#### Discussion about this post

## Metadata

```json
{
  "title": "We can all be AI engineers – and we can do it with open source models",
  "description": "The barriers to AI engineering are crumbling fast",
  "url": "https://blog.helix.ml/p/we-can-all-be-ai-engineers",
  "content": "[![Image 12](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b127cec-2c23-4484-997e-120a7f35f435_1344x768.webp)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b127cec-2c23-4484-997e-120a7f35f435_1344x768.webp)\n\nA couple of weeks ago, I gave a talk at [Hannah Foxwell’s](https://www.linkedin.com/in/hannah-foxwell/) amazing AI for the Rest of Us conference about something that's been brewing in my mind after years of working in DevOps, MLOps, and now GenAI: the barriers to AI engineering are crumbling fast. The tools have gotten good enough that if you can handle an IDE and push some YAML to git, you're already qualified.\n\nHaving lived through the evolution from DevOps (ClusterHQ) to MLOps (Dotscience) and now diving deep into GenAI with HelixML, I keep seeing the same pattern: complex tools get simpler, workflows get standardized, and suddenly what seemed like rocket science becomes just... more engineering.\n\nBuilding an AI application comes down to six building blocks:\n\n1.  **Models**: Just mathematical functions. Complex ones, sure, but at their core, they're just turning words into numbers and back again.\n    \n2.  **Prompts**: Telling the model what to do in plain English. Sometimes you need to be really explicit - like talking to a toddler.\n    \n3.  **Knowledge**: Your AI's personal knowledge base. Documents, websites, whatever you need it to learn from.\n    \n4.  **Integrations**: This is where it gets interesting - connecting your AI to real business systems through APIs.\n    \n5.  **Tests**: Because nobody wants their AI going sideways in production. Yes, you can test AI apps, and you absolutely should.\n    \n6.  **Deployment**: Running it on a server. For example, versioning the entire app above in a yaml file and [using Flux to manage deployment to K8s and Helix](https://blog.helix.ml/p/announcing-helix-14-cicd-for-cloud).\n    \n\nHere's where my DevOps background kicks in. You know all those tools you're already using? Git? CI/CD pipelines? They work for AI apps too. I demonstrated this live in the talk by building a Jira integration that could write code based on ticket descriptions.\n\nThe secret sauce? Something we're calling an \"[AISpec](https://aispec.org/)\" - a YAML file that pulls all these pieces together in a way that feels natural to anyone who's worked with modern infrastructure tools.\n\nThis bit's important: when you use open source models, your data stays yours. It doesn't end up training someone else's model. For companies worried about GDPR or other national, regional or corporate regulation, this is crucial. You can run everything locally, in your own infrastructure, with your data staying right where your legal team wants it.\n\nIf you're reading this thinking \"show me the code,\" I've got you covered. Here’s a complete reference architecture you can set up to do this stuff yourself: **[https://github.com/helixml/genai-cicd-ref](https://github.com/helixml/genai-cicd-ref)**\n\nAnd here’s a complete tutorial of using and setting up the reference architecture:\n\nThe main thing I want you to take away is this: if you can handle version control and basic deployment workflows, you can build production-ready AI applications. The tools are there. The models are there. And they're getting better every day.\n\nCheck out [aispec.org](https://aispec.org/) if you want to dig into the standard format we're proposing for all this. Or if you want to chat about any of this, [find me on LinkedIn](https://www.linkedin.com/in/luke-marsden-71b3789/) or drop me an email at [luke@helix.ml](mailto:luke@helix.ml).\n\nThis is about making AI engineering accessible to everyone who knows how to ship code. No PhD required, no magic - just solid engineering practices applied to these powerful new tools.\n\n#### Discussion about this post",
  "publishedTime": "2024-11-12T13:57:11+00:00",
  "usage": {
    "tokens": 982
  }
}
```
