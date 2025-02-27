---
title: CodeChain: Improving Code Generation through Modular Self-Revision
description: Code generation using large language models (LLMs) has shown promising results recently. However, when evaluated on complex programming tasks, current LLMs still fall short compared to human…
url: https://medium.com/@raphael.mansuy/codechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3
timestamp: 2025-01-20T15:54:18.179Z
domain: medium.com
path: @raphael.mansuy_codechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3
---

# CodeChain: Improving Code Generation through Modular Self-Revision


Code generation using large language models (LLMs) has shown promising results recently. However, when evaluated on complex programming tasks, current LLMs still fall short compared to human…


## Content

CodeChain: Improving Code Generation through Modular Self-Revision | by Raphael Mansuy | Medium
===============
 

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5d0fed59bba3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&source=---top_nav_layout_nav----------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)

[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

![Image 8](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

CodeChain: Improving Code Generation through Modular Self-Revision
==================================================================

[![Image 9: Raphael Mansuy](https://miro.medium.com/v2/resize:fill:88:88/1*S7SBJ3PHbV-cttihRUwdag.jpeg)](https://medium.com/@raphael.mansuy?source=post_page---byline--5d0fed59bba3--------------------------------)

[Raphael Mansuy](https://medium.com/@raphael.mansuy?source=post_page---byline--5d0fed59bba3--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fab5e81bdeb7a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&user=Raphael+Mansuy&userId=ab5e81bdeb7a&source=post_page-ab5e81bdeb7a--byline--5d0fed59bba3---------------------post_header-----------)

4 min read

·

Oct 16, 2023

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F5d0fed59bba3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&user=Raphael+Mansuy&userId=ab5e81bdeb7a&source=---header_actions--5d0fed59bba3---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F5d0fed59bba3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&source=---header_actions--5d0fed59bba3---------------------bookmark_footer-----------)

Share

Code generation using large language models (LLMs) has shown promising results recently. However, when evaluated on complex programming tasks, current LLMs still fall short compared to human developers. A key reason is LLMs’ tendency to generate monolithic code blocks, lacking the modularization and abstraction that experienced programmers utilize.

To address this, the paper “CodeChain: Towards Modular Code Generation through Chain of Self-Revisions with Representative Sub-Modules” introduces a novel framework called CodeChain that elicits modular code generation through iterative self-revision.

![Image 10](https://miro.medium.com/v2/resize:fit:700/1*3beH_97oBnIY1HpcbsaW9A.png)

The Coding Lama

The Limitations of Current LLMs in Code Generation
==================================================

LLMs like Codex, AlphaCode, and CodeParrot can generate syntactically correct programs and solve simple coding tasks. However, their performance significantly drops on more complex problems from benchmarks like APPS and CodeContests.

For instance, Codex only achieves 0.92% pass@1 on APPS. The key limitations are:

*   Monolithic generation: LLMs tend to generate solutions as one big code block, without decomposing them into logical sub-tasks and sub-modules.
*   Independent sampling: LLMs generate many candidate solutions independently…

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F5d0fed59bba3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&user=Raphael+Mansuy&userId=ab5e81bdeb7a&source=---footer_actions--5d0fed59bba3---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F5d0fed59bba3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&user=Raphael+Mansuy&userId=ab5e81bdeb7a&source=---footer_actions--5d0fed59bba3---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F5d0fed59bba3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&source=---footer_actions--5d0fed59bba3---------------------bookmark_footer-----------)

[![Image 11: Raphael Mansuy](https://miro.medium.com/v2/resize:fill:96:96/1*S7SBJ3PHbV-cttihRUwdag.jpeg)](https://medium.com/@raphael.mansuy?source=post_page---post_author_info--5d0fed59bba3--------------------------------)

[![Image 12: Raphael Mansuy](https://miro.medium.com/v2/resize:fill:128:128/1*S7SBJ3PHbV-cttihRUwdag.jpeg)](https://medium.com/@raphael.mansuy?source=post_page---post_author_info--5d0fed59bba3--------------------------------)

Follow

[Written by Raphael Mansuy -------------------------](https://medium.com/@raphael.mansuy?source=post_page---post_author_info--5d0fed59bba3--------------------------------)

[841 Followers](https://medium.com/@raphael.mansuy/followers?source=post_page---post_author_info--5d0fed59bba3--------------------------------)

·[2K Following](https://medium.com/@raphael.mansuy/following?source=post_page---post_author_info--5d0fed59bba3--------------------------------)

AI, Data Architecture & Data Engineering 👉 Follow me for deep dives on data-engineering and AI ! Books Author.

Follow

No responses yet
----------------

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--5d0fed59bba3--------------------------------)

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&source=---post_responses--5d0fed59bba3---------------------respond_sidebar-----------)

Also publish to my profile

Respond

Respond

[Help](https://help.medium.com/hc/en-us?source=post_page-----5d0fed59bba3--------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----5d0fed59bba3--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----5d0fed59bba3--------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----5d0fed59bba3--------------------------------)

[Press](https://medium.com/@raphael.mansuy/pressinquiries@medium.com?source=post_page-----5d0fed59bba3--------------------------------)

[Blog](https://blog.medium.com/?source=post_page-----5d0fed59bba3--------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----5d0fed59bba3--------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----5d0fed59bba3--------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----5d0fed59bba3--------------------------------)

[Teams](https://medium.com/business?source=post_page-----5d0fed59bba3--------------------------------)

## Metadata

```json
{
  "title": "CodeChain: Improving Code Generation through Modular Self-Revision",
  "description": "Code generation using large language models (LLMs) has shown promising results recently. However, when evaluated on complex programming tasks, current LLMs still fall short compared to human…",
  "url": "https://medium.com/@raphael.mansuy/codechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3",
  "content": "CodeChain: Improving Code Generation through Modular Self-Revision | by Raphael Mansuy | Medium\n===============\n \n\n[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5d0fed59bba3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&source=---top_nav_layout_nav----------------------------------)\n\nSign up\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)\n\n[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)\n\n[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)\n\nSign up\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n![Image 8](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)\n\nMember-only story\n\nCodeChain: Improving Code Generation through Modular Self-Revision\n==================================================================\n\n[![Image 9: Raphael Mansuy](https://miro.medium.com/v2/resize:fill:88:88/1*S7SBJ3PHbV-cttihRUwdag.jpeg)](https://medium.com/@raphael.mansuy?source=post_page---byline--5d0fed59bba3--------------------------------)\n\n[Raphael Mansuy](https://medium.com/@raphael.mansuy?source=post_page---byline--5d0fed59bba3--------------------------------)\n\n·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fab5e81bdeb7a&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&user=Raphael+Mansuy&userId=ab5e81bdeb7a&source=post_page-ab5e81bdeb7a--byline--5d0fed59bba3---------------------post_header-----------)\n\n4 min read\n\n·\n\nOct 16, 2023\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F5d0fed59bba3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&user=Raphael+Mansuy&userId=ab5e81bdeb7a&source=---header_actions--5d0fed59bba3---------------------clap_footer-----------)\n\n\\--\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F5d0fed59bba3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&source=---header_actions--5d0fed59bba3---------------------bookmark_footer-----------)\n\nShare\n\nCode generation using large language models (LLMs) has shown promising results recently. However, when evaluated on complex programming tasks, current LLMs still fall short compared to human developers. A key reason is LLMs’ tendency to generate monolithic code blocks, lacking the modularization and abstraction that experienced programmers utilize.\n\nTo address this, the paper “CodeChain: Towards Modular Code Generation through Chain of Self-Revisions with Representative Sub-Modules” introduces a novel framework called CodeChain that elicits modular code generation through iterative self-revision.\n\n![Image 10](https://miro.medium.com/v2/resize:fit:700/1*3beH_97oBnIY1HpcbsaW9A.png)\n\nThe Coding Lama\n\nThe Limitations of Current LLMs in Code Generation\n==================================================\n\nLLMs like Codex, AlphaCode, and CodeParrot can generate syntactically correct programs and solve simple coding tasks. However, their performance significantly drops on more complex problems from benchmarks like APPS and CodeContests.\n\nFor instance, Codex only achieves 0.92% pass@1 on APPS. The key limitations are:\n\n*   Monolithic generation: LLMs tend to generate solutions as one big code block, without decomposing them into logical sub-tasks and sub-modules.\n*   Independent sampling: LLMs generate many candidate solutions independently…\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F5d0fed59bba3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&user=Raphael+Mansuy&userId=ab5e81bdeb7a&source=---footer_actions--5d0fed59bba3---------------------clap_footer-----------)\n\n\\--\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2F5d0fed59bba3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&user=Raphael+Mansuy&userId=ab5e81bdeb7a&source=---footer_actions--5d0fed59bba3---------------------clap_footer-----------)\n\n\\--\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F5d0fed59bba3&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&source=---footer_actions--5d0fed59bba3---------------------bookmark_footer-----------)\n\n[![Image 11: Raphael Mansuy](https://miro.medium.com/v2/resize:fill:96:96/1*S7SBJ3PHbV-cttihRUwdag.jpeg)](https://medium.com/@raphael.mansuy?source=post_page---post_author_info--5d0fed59bba3--------------------------------)\n\n[![Image 12: Raphael Mansuy](https://miro.medium.com/v2/resize:fill:128:128/1*S7SBJ3PHbV-cttihRUwdag.jpeg)](https://medium.com/@raphael.mansuy?source=post_page---post_author_info--5d0fed59bba3--------------------------------)\n\nFollow\n\n[Written by Raphael Mansuy -------------------------](https://medium.com/@raphael.mansuy?source=post_page---post_author_info--5d0fed59bba3--------------------------------)\n\n[841 Followers](https://medium.com/@raphael.mansuy/followers?source=post_page---post_author_info--5d0fed59bba3--------------------------------)\n\n·[2K Following](https://medium.com/@raphael.mansuy/following?source=post_page---post_author_info--5d0fed59bba3--------------------------------)\n\nAI, Data Architecture & Data Engineering 👉 Follow me for deep dives on data-engineering and AI ! Books Author.\n\nFollow\n\nNo responses yet\n----------------\n\n[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--5d0fed59bba3--------------------------------)\n\n[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40raphael.mansuy%2Fcodechain-improving-code-generation-through-modular-self-revision-5d0fed59bba3&source=---post_responses--5d0fed59bba3---------------------respond_sidebar-----------)\n\nAlso publish to my profile\n\nRespond\n\nRespond\n\n[Help](https://help.medium.com/hc/en-us?source=post_page-----5d0fed59bba3--------------------------------)\n\n[Status](https://medium.statuspage.io/?source=post_page-----5d0fed59bba3--------------------------------)\n\n[About](https://medium.com/about?autoplay=1&source=post_page-----5d0fed59bba3--------------------------------)\n\n[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----5d0fed59bba3--------------------------------)\n\n[Press](https://medium.com/@raphael.mansuy/pressinquiries@medium.com?source=post_page-----5d0fed59bba3--------------------------------)\n\n[Blog](https://blog.medium.com/?source=post_page-----5d0fed59bba3--------------------------------)\n\n[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----5d0fed59bba3--------------------------------)\n\n[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----5d0fed59bba3--------------------------------)\n\n[Text to speech](https://speechify.com/medium?source=post_page-----5d0fed59bba3--------------------------------)\n\n[Teams](https://medium.com/business?source=post_page-----5d0fed59bba3--------------------------------)",
  "publishedTime": "2023-10-16T06:50:30.781Z",
  "usage": {
    "tokens": 2346
  }
}
```
