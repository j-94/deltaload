---
title: Advanced Prompt Engineering - Towards Data Science
description: The popularization of large language models (LLMs) has completely shifted how we solve problems as humans. In prior years, solving any task (e.g., reformatting a document or classifying a sentence)…
url: https://towardsdatascience.com/advanced-prompt-engineering-f07f9e55fe01
timestamp: 2025-01-20T15:44:03.723Z
domain: towardsdatascience.com
path: advanced-prompt-engineering-f07f9e55fe01
---

# Advanced Prompt Engineering - Towards Data Science


The popularization of large language models (LLMs) has completely shifted how we solve problems as humans. In prior years, solving any task (e.g., reformatting a document or classifying a sentence)…


## Content

Advanced Prompt Engineering. What to do when few-shot learning isn’t… | by Cameron R. Wolfe, Ph.D. | Towards Data Science
===============
 

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff07f9e55fe01&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)

[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

![Image 14](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

Advanced Prompt Engineering
===========================

What to do when few-shot learning isn’t enough…
-----------------------------------------------

[![Image 15: Cameron R. Wolfe, Ph.D.](https://miro.medium.com/v2/resize:fill:88:88/1*JhmKo3dvmoRoEfnoU02oSQ.jpeg)](https://wolfecameron.medium.com/?source=post_page---byline--f07f9e55fe01--------------------------------)

[![Image 16: Towards Data Science](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---byline--f07f9e55fe01--------------------------------)

[Cameron R. Wolfe, Ph.D.](https://wolfecameron.medium.com/?source=post_page---byline--f07f9e55fe01--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F28aa6026c553&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=post_page-28aa6026c553--byline--f07f9e55fe01---------------------post_header-----------)

Published in

[Towards Data Science](https://towardsdatascience.com/?source=post_page---byline--f07f9e55fe01--------------------------------)

·

17 min read

·

Aug 7, 2023

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Ff07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=---header_actions--f07f9e55fe01---------------------clap_footer-----------)

\--

14

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=---header_actions--f07f9e55fe01---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Df07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=---header_actions--f07f9e55fe01---------------------post_audio_button-----------)

Share

![Image 17](https://miro.medium.com/v2/resize:fit:700/1*d6yWsvLaLTfieYQP5lQf6w.jpeg)

(Photo by [Mike Tinnion](https://unsplash.com/@m15ky?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/3ym6i13Y9LU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))

The popularization of large language models (LLMs) has completely shifted how we solve problems as humans. In prior years, solving any task (e.g., reformatting a document or classifying a sentence) with a computer would require a program (i.e., a set of commands precisely written according to some programming language) to be created. With LLMs, solving such problems requires no more than a textual prompt. For example, we can prompt an LLM to reformat any document via a prompt similar to the one shown below.

![Image 18](https://miro.medium.com/v2/resize:fit:700/0*lMIZ4748GIlHZPvM.png)

Using prompting to reformat an XML document (created by author)

As demonstrated in the example above, the generic text-to-text format of LLMs makes it easy for us to solve a wide variety of problems. We first saw a glimpse of this potential with the proposal of [GPT-3](https://cameronrwolfe.substack.com/p/language-model-scaling-laws-and-gpt) \[18\], showing that sufficiently-large language models can use [few-shot learning](https://cameronrwolfe.substack.com/i/117151147/few-shot-learning) to solve many tasks with surprising accuracy. However, as the research surrounding LLMs progressed, we began to move beyond these basic (but still very effective!) prompting techniques like zero/few-shot learning.

[Instruction-following LLMs](https://cameronrwolfe.substack.com/i/117151147/instruction-prompting) (e.g., [InstructGPT](https://cameronrwolfe.substack.com/i/93578656/training-language-models-to-follow-instructions-with-human-feedback) and [ChatGPT](https://openai.com/blog/chatgpt)) led us to explore whether language models could…

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Ff07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=---footer_actions--f07f9e55fe01---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Ff07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=---footer_actions--f07f9e55fe01---------------------clap_footer-----------)

\--

14

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=---footer_actions--f07f9e55fe01---------------------bookmark_footer-----------)

[![Image 19: Towards Data Science](https://miro.medium.com/v2/resize:fill:96:96/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---post_publication_info--f07f9e55fe01--------------------------------)

[![Image 20: Towards Data Science](https://miro.medium.com/v2/resize:fill:128:128/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---post_publication_info--f07f9e55fe01--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--f07f9e55fe01---------------------follow_profile-----------)

[Published in Towards Data Science ---------------------------------](https://towardsdatascience.com/?source=post_page---post_publication_info--f07f9e55fe01--------------------------------)

[793K Followers](https://towardsdatascience.com/followers?source=post_page---post_publication_info--f07f9e55fe01--------------------------------)

·[Last published 2 hours ago](https://towardsdatascience.com/detecting-hallucination-in-rag-ecaf251a6633?source=post_page---post_publication_info--f07f9e55fe01--------------------------------)

Your home for data science and AI. The world’s leading publication for data science, data analytics, data engineering, machine learning, and artificial intelligence professionals.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--f07f9e55fe01---------------------follow_profile-----------)

[![Image 21: Cameron R. Wolfe, Ph.D.](https://miro.medium.com/v2/resize:fill:96:96/1*JhmKo3dvmoRoEfnoU02oSQ.jpeg)](https://wolfecameron.medium.com/?source=post_page---post_author_info--f07f9e55fe01--------------------------------)

[![Image 22: Cameron R. Wolfe, Ph.D.](https://miro.medium.com/v2/resize:fill:128:128/1*JhmKo3dvmoRoEfnoU02oSQ.jpeg)](https://wolfecameron.medium.com/?source=post_page---post_author_info--f07f9e55fe01--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F28aa6026c553&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=post_page-28aa6026c553--post_author_info--f07f9e55fe01---------------------follow_profile-----------)

[Written by Cameron R. Wolfe, Ph.D. ----------------------------------](https://wolfecameron.medium.com/?source=post_page---post_author_info--f07f9e55fe01--------------------------------)

[5K Followers](https://wolfecameron.medium.com/followers?source=post_page---post_author_info--f07f9e55fe01--------------------------------)

·[7 Following](https://medium.com/@wolfecameron/following?source=post_page---post_author_info--f07f9e55fe01--------------------------------)

Director of AI @ Rebuy • Deep Learning Ph.D. • I make AI understandable

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F28aa6026c553&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=post_page-28aa6026c553--post_author_info--f07f9e55fe01---------------------follow_profile-----------)

Responses (14)
--------------

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--f07f9e55fe01--------------------------------)

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=---post_responses--f07f9e55fe01---------------------respond_sidebar-----------)

Cancel

Respond

Respond

Also publish to my profile

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----f07f9e55fe01--------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----f07f9e55fe01--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----f07f9e55fe01--------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f07f9e55fe01--------------------------------)

[Press](https://towardsdatascience.com/pressinquiries@medium.com?source=post_page-----f07f9e55fe01--------------------------------)

[Blog](https://blog.medium.com/?source=post_page-----f07f9e55fe01--------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f07f9e55fe01--------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f07f9e55fe01--------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----f07f9e55fe01--------------------------------)

[Teams](https://medium.com/business?source=post_page-----f07f9e55fe01--------------------------------)

## Metadata

```json
{
  "title": "Advanced Prompt Engineering - Towards Data Science",
  "description": "The popularization of large language models (LLMs) has completely shifted how we solve problems as humans. In prior years, solving any task (e.g., reformatting a document or classifying a sentence)…",
  "url": "https://towardsdatascience.com/advanced-prompt-engineering-f07f9e55fe01",
  "content": "Advanced Prompt Engineering. What to do when few-shot learning isn’t… | by Cameron R. Wolfe, Ph.D. | Towards Data Science\n===============\n \n\n[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff07f9e55fe01&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)\n\n[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)\n\n[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n![Image 14](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)\n\nMember-only story\n\nAdvanced Prompt Engineering\n===========================\n\nWhat to do when few-shot learning isn’t enough…\n-----------------------------------------------\n\n[![Image 15: Cameron R. Wolfe, Ph.D.](https://miro.medium.com/v2/resize:fill:88:88/1*JhmKo3dvmoRoEfnoU02oSQ.jpeg)](https://wolfecameron.medium.com/?source=post_page---byline--f07f9e55fe01--------------------------------)\n\n[![Image 16: Towards Data Science](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---byline--f07f9e55fe01--------------------------------)\n\n[Cameron R. Wolfe, Ph.D.](https://wolfecameron.medium.com/?source=post_page---byline--f07f9e55fe01--------------------------------)\n\n·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F28aa6026c553&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=post_page-28aa6026c553--byline--f07f9e55fe01---------------------post_header-----------)\n\nPublished in\n\n[Towards Data Science](https://towardsdatascience.com/?source=post_page---byline--f07f9e55fe01--------------------------------)\n\n·\n\n17 min read\n\n·\n\nAug 7, 2023\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Ff07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=---header_actions--f07f9e55fe01---------------------clap_footer-----------)\n\n\\--\n\n14\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=---header_actions--f07f9e55fe01---------------------bookmark_footer-----------)\n\n[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Df07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=---header_actions--f07f9e55fe01---------------------post_audio_button-----------)\n\nShare\n\n![Image 17](https://miro.medium.com/v2/resize:fit:700/1*d6yWsvLaLTfieYQP5lQf6w.jpeg)\n\n(Photo by [Mike Tinnion](https://unsplash.com/@m15ky?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/3ym6i13Y9LU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))\n\nThe popularization of large language models (LLMs) has completely shifted how we solve problems as humans. In prior years, solving any task (e.g., reformatting a document or classifying a sentence) with a computer would require a program (i.e., a set of commands precisely written according to some programming language) to be created. With LLMs, solving such problems requires no more than a textual prompt. For example, we can prompt an LLM to reformat any document via a prompt similar to the one shown below.\n\n![Image 18](https://miro.medium.com/v2/resize:fit:700/0*lMIZ4748GIlHZPvM.png)\n\nUsing prompting to reformat an XML document (created by author)\n\nAs demonstrated in the example above, the generic text-to-text format of LLMs makes it easy for us to solve a wide variety of problems. We first saw a glimpse of this potential with the proposal of [GPT-3](https://cameronrwolfe.substack.com/p/language-model-scaling-laws-and-gpt) \\[18\\], showing that sufficiently-large language models can use [few-shot learning](https://cameronrwolfe.substack.com/i/117151147/few-shot-learning) to solve many tasks with surprising accuracy. However, as the research surrounding LLMs progressed, we began to move beyond these basic (but still very effective!) prompting techniques like zero/few-shot learning.\n\n[Instruction-following LLMs](https://cameronrwolfe.substack.com/i/117151147/instruction-prompting) (e.g., [InstructGPT](https://cameronrwolfe.substack.com/i/93578656/training-language-models-to-follow-instructions-with-human-feedback) and [ChatGPT](https://openai.com/blog/chatgpt)) led us to explore whether language models could…\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Ff07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=---footer_actions--f07f9e55fe01---------------------clap_footer-----------)\n\n\\--\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2Ff07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=---footer_actions--f07f9e55fe01---------------------clap_footer-----------)\n\n\\--\n\n14\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff07f9e55fe01&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=---footer_actions--f07f9e55fe01---------------------bookmark_footer-----------)\n\n[![Image 19: Towards Data Science](https://miro.medium.com/v2/resize:fill:96:96/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---post_publication_info--f07f9e55fe01--------------------------------)\n\n[![Image 20: Towards Data Science](https://miro.medium.com/v2/resize:fill:128:128/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---post_publication_info--f07f9e55fe01--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--f07f9e55fe01---------------------follow_profile-----------)\n\n[Published in Towards Data Science ---------------------------------](https://towardsdatascience.com/?source=post_page---post_publication_info--f07f9e55fe01--------------------------------)\n\n[793K Followers](https://towardsdatascience.com/followers?source=post_page---post_publication_info--f07f9e55fe01--------------------------------)\n\n·[Last published 2 hours ago](https://towardsdatascience.com/detecting-hallucination-in-rag-ecaf251a6633?source=post_page---post_publication_info--f07f9e55fe01--------------------------------)\n\nYour home for data science and AI. The world’s leading publication for data science, data analytics, data engineering, machine learning, and artificial intelligence professionals.\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--f07f9e55fe01---------------------follow_profile-----------)\n\n[![Image 21: Cameron R. Wolfe, Ph.D.](https://miro.medium.com/v2/resize:fill:96:96/1*JhmKo3dvmoRoEfnoU02oSQ.jpeg)](https://wolfecameron.medium.com/?source=post_page---post_author_info--f07f9e55fe01--------------------------------)\n\n[![Image 22: Cameron R. Wolfe, Ph.D.](https://miro.medium.com/v2/resize:fill:128:128/1*JhmKo3dvmoRoEfnoU02oSQ.jpeg)](https://wolfecameron.medium.com/?source=post_page---post_author_info--f07f9e55fe01--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F28aa6026c553&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=post_page-28aa6026c553--post_author_info--f07f9e55fe01---------------------follow_profile-----------)\n\n[Written by Cameron R. Wolfe, Ph.D. ----------------------------------](https://wolfecameron.medium.com/?source=post_page---post_author_info--f07f9e55fe01--------------------------------)\n\n[5K Followers](https://wolfecameron.medium.com/followers?source=post_page---post_author_info--f07f9e55fe01--------------------------------)\n\n·[7 Following](https://medium.com/@wolfecameron/following?source=post_page---post_author_info--f07f9e55fe01--------------------------------)\n\nDirector of AI @ Rebuy • Deep Learning Ph.D. • I make AI understandable\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F28aa6026c553&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&user=Cameron+R.+Wolfe%2C+Ph.D.&userId=28aa6026c553&source=post_page-28aa6026c553--post_author_info--f07f9e55fe01---------------------follow_profile-----------)\n\nResponses (14)\n--------------\n\n[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--f07f9e55fe01--------------------------------)\n\n[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fadvanced-prompt-engineering-f07f9e55fe01&source=---post_responses--f07f9e55fe01---------------------respond_sidebar-----------)\n\nCancel\n\nRespond\n\nRespond\n\nAlso publish to my profile\n\nSee all responses\n\n[Help](https://help.medium.com/hc/en-us?source=post_page-----f07f9e55fe01--------------------------------)\n\n[Status](https://medium.statuspage.io/?source=post_page-----f07f9e55fe01--------------------------------)\n\n[About](https://medium.com/about?autoplay=1&source=post_page-----f07f9e55fe01--------------------------------)\n\n[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f07f9e55fe01--------------------------------)\n\n[Press](https://towardsdatascience.com/pressinquiries@medium.com?source=post_page-----f07f9e55fe01--------------------------------)\n\n[Blog](https://blog.medium.com/?source=post_page-----f07f9e55fe01--------------------------------)\n\n[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f07f9e55fe01--------------------------------)\n\n[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f07f9e55fe01--------------------------------)\n\n[Text to speech](https://speechify.com/medium?source=post_page-----f07f9e55fe01--------------------------------)\n\n[Teams](https://medium.com/business?source=post_page-----f07f9e55fe01--------------------------------)",
  "publishedTime": "2023-08-07T14:24:08.329Z",
  "usage": {
    "tokens": 3658
  }
}
```
