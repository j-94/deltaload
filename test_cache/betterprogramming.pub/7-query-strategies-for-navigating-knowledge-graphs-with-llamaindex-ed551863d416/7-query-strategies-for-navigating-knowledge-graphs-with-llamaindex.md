---
title: 7 Query Strategies for Navigating Knowledge Graphs With LlamaIndex
description: There has been a lot of buzz around developing RAG (Retrieval Augmented Generation) pipelines powered by LLMs and Knowledge Graphs (KG) lately. In this article, let’s take a close look at Knowledge…
url: https://betterprogramming.pub/7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416
timestamp: 2025-01-20T15:45:18.719Z
domain: betterprogramming.pub
path: 7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416
---

# 7 Query Strategies for Navigating Knowledge Graphs With LlamaIndex


There has been a lot of buzz around developing RAG (Retrieval Augmented Generation) pipelines powered by LLMs and Knowledge Graphs (KG) lately. In this article, let’s take a close look at Knowledge…


## Content

7 Query Strategies for Navigating Knowledge Graphs With LlamaIndex | by Wenqi Glantz | Better Programming
===============
 

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fed551863d416&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)

[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

![Image 14](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

7 Query Strategies for Navigating Knowledge Graphs With LlamaIndex
==================================================================

Exploring NebulaGraph RAG Pipeline with the Philadelphia Phillies
-----------------------------------------------------------------

[![Image 15: Wenqi Glantz](https://miro.medium.com/v2/resize:fill:88:88/1*Ce4jOl6gjeebSiHsknN2-A.jpeg)](https://medium.com/@wenqiglantz?source=post_page---byline--ed551863d416--------------------------------)

[![Image 16: Better Programming](https://miro.medium.com/v2/resize:fill:48:48/1*QNoA3XlXLHz22zQazc0syg.png)](https://betterprogramming.pub/?source=post_page---byline--ed551863d416--------------------------------)

[Wenqi Glantz](https://medium.com/@wenqiglantz?source=post_page---byline--ed551863d416--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fce7cd5b8b74a&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=post_page-ce7cd5b8b74a--byline--ed551863d416---------------------post_header-----------)

Published in

[Better Programming](https://betterprogramming.pub/?source=post_page---byline--ed551863d416--------------------------------)

·

17 min read

·

Sep 29, 2023

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fbetter-programming%2Fed551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=---header_actions--ed551863d416---------------------clap_footer-----------)

\--

4

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fed551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=---header_actions--ed551863d416---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Ded551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=---header_actions--ed551863d416---------------------post_audio_button-----------)

Share

![Image 17](https://miro.medium.com/v2/resize:fit:700/1*rPlsuzX3viUjPt50-8UkWA.gif)

Sample graph generated by NebulaGraph

There has been a lot of buzz around developing RAG (Retrieval Augmented Generation) pipelines powered by LLMs and Knowledge Graphs (KG) lately. In this article, let’s take a close look at Knowledge Graphs by building an RAG pipeline for the Philadelphia Phillies using [LlamaIndex](https://www.llamaindex.ai/) and [NebulaGraph](https://www.nebula-graph.io/).

Use Case
========

We will use Knowledge Graph, specifically the open source NebulaGraph, to query information on the Philadelphia Phillies, the Major League Baseball team based in Philadelphia. My whole family are big fans of the Phillies!

We will use the [Wikipedia page of the Philadelphia Phillies](https://en.wikipedia.org/wiki/Philadelphia_Phillies) as one of our source documents. In addition, in light of the recent standing ovation event Philly fans organized for one of our favorite players, Trea Turner, we will use a [YouTube video](https://www.youtube.com/watch?v=k-HTQ8T7oVw) that comments on this great event as another part of our source documents.

Our high-level architectural diagram looks like this:

![Image 18](https://miro.medium.com/v2/resize:fit:495/1*X0JWZr8ToYvy2j8sYgLKUw.gif)

Diagram by author

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fbetter-programming%2Fed551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=---footer_actions--ed551863d416---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fbetter-programming%2Fed551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=---footer_actions--ed551863d416---------------------clap_footer-----------)

\--

4

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fed551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=---footer_actions--ed551863d416---------------------bookmark_footer-----------)

[![Image 19: Better Programming](https://miro.medium.com/v2/resize:fill:96:96/1*QNoA3XlXLHz22zQazc0syg.png)](https://betterprogramming.pub/?source=post_page---post_publication_info--ed551863d416--------------------------------)

[![Image 20: Better Programming](https://miro.medium.com/v2/resize:fill:128:128/1*QNoA3XlXLHz22zQazc0syg.png)](https://betterprogramming.pub/?source=post_page---post_publication_info--ed551863d416--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fbetter-programming&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&collection=Better+Programming&collectionId=d0b105d10f0a&source=post_page---post_publication_info--ed551863d416---------------------follow_profile-----------)

[Published in Better Programming -------------------------------](https://betterprogramming.pub/?source=post_page---post_publication_info--ed551863d416--------------------------------)

[220K Followers](https://betterprogramming.pub/followers?source=post_page---post_publication_info--ed551863d416--------------------------------)

·[Last published Nov 10, 2023](https://betterprogramming.pub/let-a-thousand-programming-publications-bloom-bf37baef8f27?source=post_page---post_publication_info--ed551863d416--------------------------------)

Advice for programmers.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fbetter-programming&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&collection=Better+Programming&collectionId=d0b105d10f0a&source=post_page---post_publication_info--ed551863d416---------------------follow_profile-----------)

[![Image 21: Wenqi Glantz](https://miro.medium.com/v2/resize:fill:96:96/1*Ce4jOl6gjeebSiHsknN2-A.jpeg)](https://medium.com/@wenqiglantz?source=post_page---post_author_info--ed551863d416--------------------------------)

[![Image 22: Wenqi Glantz](https://miro.medium.com/v2/resize:fill:128:128/1*Ce4jOl6gjeebSiHsknN2-A.jpeg)](https://medium.com/@wenqiglantz?source=post_page---post_author_info--ed551863d416--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fce7cd5b8b74a&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=post_page-ce7cd5b8b74a--post_author_info--ed551863d416---------------------follow_profile-----------)

[Written by Wenqi Glantz -----------------------](https://medium.com/@wenqiglantz?source=post_page---post_author_info--ed551863d416--------------------------------)

[8.5K Followers](https://medium.com/@wenqiglantz/followers?source=post_page---post_author_info--ed551863d416--------------------------------)

·[965 Following](https://medium.com/@wenqiglantz/following?source=post_page---post_author_info--ed551863d416--------------------------------)

Mom, wife, architect with a passion for technology and crafting quality products [linkedin.com/in/wenqi-glantz-b5448a5a/](http://linkedin.com/in/wenqi-glantz-b5448a5a/) [twitter.com/wenqi\_glantz](http://twitter.com/wenqi_glantz)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fce7cd5b8b74a&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=post_page-ce7cd5b8b74a--post_author_info--ed551863d416---------------------follow_profile-----------)

Responses (4)
-------------

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--ed551863d416--------------------------------)

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=---post_responses--ed551863d416---------------------respond_sidebar-----------)

Cancel

Respond

Respond

Also publish to my profile

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----ed551863d416--------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----ed551863d416--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ed551863d416--------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ed551863d416--------------------------------)

[Press](https://betterprogramming.pub/pressinquiries@medium.com?source=post_page-----ed551863d416--------------------------------)

[Blog](https://blog.medium.com/?source=post_page-----ed551863d416--------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ed551863d416--------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ed551863d416--------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ed551863d416--------------------------------)

[Teams](https://medium.com/business?source=post_page-----ed551863d416--------------------------------)

## Metadata

```json
{
  "title": "7 Query Strategies for Navigating Knowledge Graphs With LlamaIndex",
  "description": "There has been a lot of buzz around developing RAG (Retrieval Augmented Generation) pipelines powered by LLMs and Knowledge Graphs (KG) lately. In this article, let’s take a close look at Knowledge…",
  "url": "https://betterprogramming.pub/7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416",
  "content": "7 Query Strategies for Navigating Knowledge Graphs With LlamaIndex | by Wenqi Glantz | Better Programming\n===============\n \n\n[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fed551863d416&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)\n\n[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)\n\n[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n![Image 14](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)\n\nMember-only story\n\n7 Query Strategies for Navigating Knowledge Graphs With LlamaIndex\n==================================================================\n\nExploring NebulaGraph RAG Pipeline with the Philadelphia Phillies\n-----------------------------------------------------------------\n\n[![Image 15: Wenqi Glantz](https://miro.medium.com/v2/resize:fill:88:88/1*Ce4jOl6gjeebSiHsknN2-A.jpeg)](https://medium.com/@wenqiglantz?source=post_page---byline--ed551863d416--------------------------------)\n\n[![Image 16: Better Programming](https://miro.medium.com/v2/resize:fill:48:48/1*QNoA3XlXLHz22zQazc0syg.png)](https://betterprogramming.pub/?source=post_page---byline--ed551863d416--------------------------------)\n\n[Wenqi Glantz](https://medium.com/@wenqiglantz?source=post_page---byline--ed551863d416--------------------------------)\n\n·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fce7cd5b8b74a&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=post_page-ce7cd5b8b74a--byline--ed551863d416---------------------post_header-----------)\n\nPublished in\n\n[Better Programming](https://betterprogramming.pub/?source=post_page---byline--ed551863d416--------------------------------)\n\n·\n\n17 min read\n\n·\n\nSep 29, 2023\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fbetter-programming%2Fed551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=---header_actions--ed551863d416---------------------clap_footer-----------)\n\n\\--\n\n4\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fed551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=---header_actions--ed551863d416---------------------bookmark_footer-----------)\n\n[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Ded551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=---header_actions--ed551863d416---------------------post_audio_button-----------)\n\nShare\n\n![Image 17](https://miro.medium.com/v2/resize:fit:700/1*rPlsuzX3viUjPt50-8UkWA.gif)\n\nSample graph generated by NebulaGraph\n\nThere has been a lot of buzz around developing RAG (Retrieval Augmented Generation) pipelines powered by LLMs and Knowledge Graphs (KG) lately. In this article, let’s take a close look at Knowledge Graphs by building an RAG pipeline for the Philadelphia Phillies using [LlamaIndex](https://www.llamaindex.ai/) and [NebulaGraph](https://www.nebula-graph.io/).\n\nUse Case\n========\n\nWe will use Knowledge Graph, specifically the open source NebulaGraph, to query information on the Philadelphia Phillies, the Major League Baseball team based in Philadelphia. My whole family are big fans of the Phillies!\n\nWe will use the [Wikipedia page of the Philadelphia Phillies](https://en.wikipedia.org/wiki/Philadelphia_Phillies) as one of our source documents. In addition, in light of the recent standing ovation event Philly fans organized for one of our favorite players, Trea Turner, we will use a [YouTube video](https://www.youtube.com/watch?v=k-HTQ8T7oVw) that comments on this great event as another part of our source documents.\n\nOur high-level architectural diagram looks like this:\n\n![Image 18](https://miro.medium.com/v2/resize:fit:495/1*X0JWZr8ToYvy2j8sYgLKUw.gif)\n\nDiagram by author\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fbetter-programming%2Fed551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=---footer_actions--ed551863d416---------------------clap_footer-----------)\n\n\\--\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fbetter-programming%2Fed551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=---footer_actions--ed551863d416---------------------clap_footer-----------)\n\n\\--\n\n4\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fed551863d416&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=---footer_actions--ed551863d416---------------------bookmark_footer-----------)\n\n[![Image 19: Better Programming](https://miro.medium.com/v2/resize:fill:96:96/1*QNoA3XlXLHz22zQazc0syg.png)](https://betterprogramming.pub/?source=post_page---post_publication_info--ed551863d416--------------------------------)\n\n[![Image 20: Better Programming](https://miro.medium.com/v2/resize:fill:128:128/1*QNoA3XlXLHz22zQazc0syg.png)](https://betterprogramming.pub/?source=post_page---post_publication_info--ed551863d416--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fbetter-programming&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&collection=Better+Programming&collectionId=d0b105d10f0a&source=post_page---post_publication_info--ed551863d416---------------------follow_profile-----------)\n\n[Published in Better Programming -------------------------------](https://betterprogramming.pub/?source=post_page---post_publication_info--ed551863d416--------------------------------)\n\n[220K Followers](https://betterprogramming.pub/followers?source=post_page---post_publication_info--ed551863d416--------------------------------)\n\n·[Last published Nov 10, 2023](https://betterprogramming.pub/let-a-thousand-programming-publications-bloom-bf37baef8f27?source=post_page---post_publication_info--ed551863d416--------------------------------)\n\nAdvice for programmers.\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fbetter-programming&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&collection=Better+Programming&collectionId=d0b105d10f0a&source=post_page---post_publication_info--ed551863d416---------------------follow_profile-----------)\n\n[![Image 21: Wenqi Glantz](https://miro.medium.com/v2/resize:fill:96:96/1*Ce4jOl6gjeebSiHsknN2-A.jpeg)](https://medium.com/@wenqiglantz?source=post_page---post_author_info--ed551863d416--------------------------------)\n\n[![Image 22: Wenqi Glantz](https://miro.medium.com/v2/resize:fill:128:128/1*Ce4jOl6gjeebSiHsknN2-A.jpeg)](https://medium.com/@wenqiglantz?source=post_page---post_author_info--ed551863d416--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fce7cd5b8b74a&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=post_page-ce7cd5b8b74a--post_author_info--ed551863d416---------------------follow_profile-----------)\n\n[Written by Wenqi Glantz -----------------------](https://medium.com/@wenqiglantz?source=post_page---post_author_info--ed551863d416--------------------------------)\n\n[8.5K Followers](https://medium.com/@wenqiglantz/followers?source=post_page---post_author_info--ed551863d416--------------------------------)\n\n·[965 Following](https://medium.com/@wenqiglantz/following?source=post_page---post_author_info--ed551863d416--------------------------------)\n\nMom, wife, architect with a passion for technology and crafting quality products [linkedin.com/in/wenqi-glantz-b5448a5a/](http://linkedin.com/in/wenqi-glantz-b5448a5a/) [twitter.com/wenqi\\_glantz](http://twitter.com/wenqi_glantz)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fce7cd5b8b74a&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&user=Wenqi+Glantz&userId=ce7cd5b8b74a&source=post_page-ce7cd5b8b74a--post_author_info--ed551863d416---------------------follow_profile-----------)\n\nResponses (4)\n-------------\n\n[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--ed551863d416--------------------------------)\n\n[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2F7-query-strategies-for-navigating-knowledge-graphs-with-llamaindex-ed551863d416&source=---post_responses--ed551863d416---------------------respond_sidebar-----------)\n\nCancel\n\nRespond\n\nRespond\n\nAlso publish to my profile\n\nSee all responses\n\n[Help](https://help.medium.com/hc/en-us?source=post_page-----ed551863d416--------------------------------)\n\n[Status](https://medium.statuspage.io/?source=post_page-----ed551863d416--------------------------------)\n\n[About](https://medium.com/about?autoplay=1&source=post_page-----ed551863d416--------------------------------)\n\n[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ed551863d416--------------------------------)\n\n[Press](https://betterprogramming.pub/pressinquiries@medium.com?source=post_page-----ed551863d416--------------------------------)\n\n[Blog](https://blog.medium.com/?source=post_page-----ed551863d416--------------------------------)\n\n[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ed551863d416--------------------------------)\n\n[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ed551863d416--------------------------------)\n\n[Text to speech](https://speechify.com/medium?source=post_page-----ed551863d416--------------------------------)\n\n[Teams](https://medium.com/business?source=post_page-----ed551863d416--------------------------------)",
  "publishedTime": "2023-09-29T18:12:49.304Z",
  "usage": {
    "tokens": 3445
  }
}
```
