---
title: An Algo Trading Strategy which made +8,371%: A Python Case Study
description: There is literally no point in going after traditional algo trading strategies like SMA crossover or RSI threshold breakout strategy as it has proven to be obsolete given their simplistic nature and…
url: https://levelup.gitconnected.com/an-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc
timestamp: 2025-01-20T15:56:34.985Z
domain: levelup.gitconnected.com
path: an-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc
---

# An Algo Trading Strategy which made +8,371%: A Python Case Study


There is literally no point in going after traditional algo trading strategies like SMA crossover or RSI threshold breakout strategy as it has proven to be obsolete given their simplistic nature and…


## Content

An Algo Trading Strategy which made +8,371%: A Python Case Study | by Nikhil Adithyan | Level Up Coding
===============
 

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F58ed12a492dc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)

[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

![Image 12](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

An Algo Trading Strategy which made +8,371%: A Python Case Study
================================================================

Backtesting of a simple breakout trading strategy with APIs and Python
----------------------------------------------------------------------

[![Image 13: Nikhil Adithyan](https://miro.medium.com/v2/resize:fill:88:88/1*oGeikU0oge-OyJ88-On8QQ.jpeg)](https://nikhiladithyan.medium.com/?source=post_page---byline--58ed12a492dc--------------------------------)

[![Image 14: Level Up Coding](https://miro.medium.com/v2/resize:fill:48:48/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---byline--58ed12a492dc--------------------------------)

[Nikhil Adithyan](https://nikhiladithyan.medium.com/?source=post_page---byline--58ed12a492dc--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fe10ad955760c&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=post_page-e10ad955760c--byline--58ed12a492dc---------------------post_header-----------)

Published in

[Level Up Coding](https://levelup.gitconnected.com/?source=post_page---byline--58ed12a492dc--------------------------------)

·

7 min read

·

Nov 28, 2023

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=---header_actions--58ed12a492dc---------------------clap_footer-----------)

\--

55

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=---header_actions--58ed12a492dc---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=---header_actions--58ed12a492dc---------------------post_audio_button-----------)

Share

![Image 15](https://miro.medium.com/v2/resize:fit:700/0*NVcgICnCBFvG0gM7)

Photo by [Behnam Norouzi](https://unsplash.com/@behy_studio?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Introduction
============

There is literally no point in going after traditional algo trading strategies like SMA crossover or RSI threshold breakout strategy as it has proven to be obsolete given their simplistic nature and more importantly, the massive volume of participants who are trying to implement them in the market.

So instead of embracing those strategies, it’s time to try something new. In this article, we’ll be using Python and [Benzinga’s APIs](https://www.benzinga.com/apis/?utm_source=nikhil_medium&utm_medium=organic&utm_campaign=apisblog&utm_term=benzingaapis&utm_content=body) to construct and backtest a new trading strategy that will help us beat the market.

With that being said, let’s dive into the article!

The Trading Strategy
====================

Before moving to the coding part, it’s essential to have a good background on the strategy we’re going to build in this article. Our trading strategy follows the principle of simplicity yet a very effective breakout strategy.

**We enter the market if:** the stock’s current high exceeds the 50-week high

**We exit the market if:** the stock’s current low sinks below the 40-week low

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=---footer_actions--58ed12a492dc---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=---footer_actions--58ed12a492dc---------------------clap_footer-----------)

\--

55

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=---footer_actions--58ed12a492dc---------------------bookmark_footer-----------)

[![Image 16: Level Up Coding](https://miro.medium.com/v2/resize:fill:96:96/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---post_publication_info--58ed12a492dc--------------------------------)

[![Image 17: Level Up Coding](https://miro.medium.com/v2/resize:fill:128:128/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---post_publication_info--58ed12a492dc--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fgitconnected&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&collection=Level+Up+Coding&collectionId=5517fd7b58a6&source=post_page---post_publication_info--58ed12a492dc---------------------follow_profile-----------)

[Published in Level Up Coding ----------------------------](https://levelup.gitconnected.com/?source=post_page---post_publication_info--58ed12a492dc--------------------------------)

[192K Followers](https://levelup.gitconnected.com/followers?source=post_page---post_publication_info--58ed12a492dc--------------------------------)

·[Last published 19 hours ago](https://levelup.gitconnected.com/the-dream-machine-decoding-why-llms-hallucinate-reality-fea8846a5bc5?source=post_page---post_publication_info--58ed12a492dc--------------------------------)

Coding tutorials and news. The developer homepage [gitconnected.com](http://gitconnected.com/) && [skilled.dev](http://skilled.dev/) && [levelup.dev](http://levelup.dev/)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fgitconnected&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&collection=Level+Up+Coding&collectionId=5517fd7b58a6&source=post_page---post_publication_info--58ed12a492dc---------------------follow_profile-----------)

[![Image 18: Nikhil Adithyan](https://miro.medium.com/v2/resize:fill:96:96/1*oGeikU0oge-OyJ88-On8QQ.jpeg)](https://nikhiladithyan.medium.com/?source=post_page---post_author_info--58ed12a492dc--------------------------------)

[![Image 19: Nikhil Adithyan](https://miro.medium.com/v2/resize:fill:128:128/1*oGeikU0oge-OyJ88-On8QQ.jpeg)](https://nikhiladithyan.medium.com/?source=post_page---post_author_info--58ed12a492dc--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fe10ad955760c&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=post_page-e10ad955760c--post_author_info--58ed12a492dc---------------------follow_profile-----------)

[Written by Nikhil Adithyan --------------------------](https://nikhiladithyan.medium.com/?source=post_page---post_author_info--58ed12a492dc--------------------------------)

[11.4K Followers](https://nikhiladithyan.medium.com/followers?source=post_page---post_author_info--58ed12a492dc--------------------------------)

·[54 Following](https://medium.com/@nikhiladithyan/following?source=post_page---post_author_info--58ed12a492dc--------------------------------)

Founder @BacktestZone ([https://www.backtestzone.com/](https://www.backtestzone.com/)), a no-code backtesting platform | Top Writer | Connect with me on LinkedIn: [https://bit.ly/3yNuwCJ](https://bit.ly/3yNuwCJ)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fe10ad955760c&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=post_page-e10ad955760c--post_author_info--58ed12a492dc---------------------follow_profile-----------)

Responses (55)
--------------

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--58ed12a492dc--------------------------------)

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=---post_responses--58ed12a492dc---------------------respond_sidebar-----------)

Cancel

Respond

Respond

Also publish to my profile

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----58ed12a492dc--------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----58ed12a492dc--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----58ed12a492dc--------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----58ed12a492dc--------------------------------)

[Press](https://levelup.gitconnected.com/pressinquiries@medium.com?source=post_page-----58ed12a492dc--------------------------------)

[Blog](https://blog.medium.com/?source=post_page-----58ed12a492dc--------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----58ed12a492dc--------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----58ed12a492dc--------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----58ed12a492dc--------------------------------)

[Teams](https://medium.com/business?source=post_page-----58ed12a492dc--------------------------------)

## Metadata

```json
{
  "title": "An Algo Trading Strategy which made +8,371%: A Python Case Study",
  "description": "There is literally no point in going after traditional algo trading strategies like SMA crossover or RSI threshold breakout strategy as it has proven to be obsolete given their simplistic nature and…",
  "url": "https://levelup.gitconnected.com/an-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc",
  "content": "An Algo Trading Strategy which made +8,371%: A Python Case Study | by Nikhil Adithyan | Level Up Coding\n===============\n \n\n[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F58ed12a492dc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)\n\n[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)\n\n[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n![Image 12](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)\n\nMember-only story\n\nAn Algo Trading Strategy which made +8,371%: A Python Case Study\n================================================================\n\nBacktesting of a simple breakout trading strategy with APIs and Python\n----------------------------------------------------------------------\n\n[![Image 13: Nikhil Adithyan](https://miro.medium.com/v2/resize:fill:88:88/1*oGeikU0oge-OyJ88-On8QQ.jpeg)](https://nikhiladithyan.medium.com/?source=post_page---byline--58ed12a492dc--------------------------------)\n\n[![Image 14: Level Up Coding](https://miro.medium.com/v2/resize:fill:48:48/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---byline--58ed12a492dc--------------------------------)\n\n[Nikhil Adithyan](https://nikhiladithyan.medium.com/?source=post_page---byline--58ed12a492dc--------------------------------)\n\n·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fe10ad955760c&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=post_page-e10ad955760c--byline--58ed12a492dc---------------------post_header-----------)\n\nPublished in\n\n[Level Up Coding](https://levelup.gitconnected.com/?source=post_page---byline--58ed12a492dc--------------------------------)\n\n·\n\n7 min read\n\n·\n\nNov 28, 2023\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=---header_actions--58ed12a492dc---------------------clap_footer-----------)\n\n\\--\n\n55\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=---header_actions--58ed12a492dc---------------------bookmark_footer-----------)\n\n[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=---header_actions--58ed12a492dc---------------------post_audio_button-----------)\n\nShare\n\n![Image 15](https://miro.medium.com/v2/resize:fit:700/0*NVcgICnCBFvG0gM7)\n\nPhoto by [Behnam Norouzi](https://unsplash.com/@behy_studio?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)\n\nIntroduction\n============\n\nThere is literally no point in going after traditional algo trading strategies like SMA crossover or RSI threshold breakout strategy as it has proven to be obsolete given their simplistic nature and more importantly, the massive volume of participants who are trying to implement them in the market.\n\nSo instead of embracing those strategies, it’s time to try something new. In this article, we’ll be using Python and [Benzinga’s APIs](https://www.benzinga.com/apis/?utm_source=nikhil_medium&utm_medium=organic&utm_campaign=apisblog&utm_term=benzingaapis&utm_content=body) to construct and backtest a new trading strategy that will help us beat the market.\n\nWith that being said, let’s dive into the article!\n\nThe Trading Strategy\n====================\n\nBefore moving to the coding part, it’s essential to have a good background on the strategy we’re going to build in this article. Our trading strategy follows the principle of simplicity yet a very effective breakout strategy.\n\n**We enter the market if:** the stock’s current high exceeds the 50-week high\n\n**We exit the market if:** the stock’s current low sinks below the 40-week low\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=---footer_actions--58ed12a492dc---------------------clap_footer-----------)\n\n\\--\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fgitconnected%2F58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=---footer_actions--58ed12a492dc---------------------clap_footer-----------)\n\n\\--\n\n55\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F58ed12a492dc&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=---footer_actions--58ed12a492dc---------------------bookmark_footer-----------)\n\n[![Image 16: Level Up Coding](https://miro.medium.com/v2/resize:fill:96:96/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---post_publication_info--58ed12a492dc--------------------------------)\n\n[![Image 17: Level Up Coding](https://miro.medium.com/v2/resize:fill:128:128/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://levelup.gitconnected.com/?source=post_page---post_publication_info--58ed12a492dc--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fgitconnected&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&collection=Level+Up+Coding&collectionId=5517fd7b58a6&source=post_page---post_publication_info--58ed12a492dc---------------------follow_profile-----------)\n\n[Published in Level Up Coding ----------------------------](https://levelup.gitconnected.com/?source=post_page---post_publication_info--58ed12a492dc--------------------------------)\n\n[192K Followers](https://levelup.gitconnected.com/followers?source=post_page---post_publication_info--58ed12a492dc--------------------------------)\n\n·[Last published 19 hours ago](https://levelup.gitconnected.com/the-dream-machine-decoding-why-llms-hallucinate-reality-fea8846a5bc5?source=post_page---post_publication_info--58ed12a492dc--------------------------------)\n\nCoding tutorials and news. The developer homepage [gitconnected.com](http://gitconnected.com/) && [skilled.dev](http://skilled.dev/) && [levelup.dev](http://levelup.dev/)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fgitconnected&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&collection=Level+Up+Coding&collectionId=5517fd7b58a6&source=post_page---post_publication_info--58ed12a492dc---------------------follow_profile-----------)\n\n[![Image 18: Nikhil Adithyan](https://miro.medium.com/v2/resize:fill:96:96/1*oGeikU0oge-OyJ88-On8QQ.jpeg)](https://nikhiladithyan.medium.com/?source=post_page---post_author_info--58ed12a492dc--------------------------------)\n\n[![Image 19: Nikhil Adithyan](https://miro.medium.com/v2/resize:fill:128:128/1*oGeikU0oge-OyJ88-On8QQ.jpeg)](https://nikhiladithyan.medium.com/?source=post_page---post_author_info--58ed12a492dc--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fe10ad955760c&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=post_page-e10ad955760c--post_author_info--58ed12a492dc---------------------follow_profile-----------)\n\n[Written by Nikhil Adithyan --------------------------](https://nikhiladithyan.medium.com/?source=post_page---post_author_info--58ed12a492dc--------------------------------)\n\n[11.4K Followers](https://nikhiladithyan.medium.com/followers?source=post_page---post_author_info--58ed12a492dc--------------------------------)\n\n·[54 Following](https://medium.com/@nikhiladithyan/following?source=post_page---post_author_info--58ed12a492dc--------------------------------)\n\nFounder @BacktestZone ([https://www.backtestzone.com/](https://www.backtestzone.com/)), a no-code backtesting platform | Top Writer | Connect with me on LinkedIn: [https://bit.ly/3yNuwCJ](https://bit.ly/3yNuwCJ)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fe10ad955760c&operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&user=Nikhil+Adithyan&userId=e10ad955760c&source=post_page-e10ad955760c--post_author_info--58ed12a492dc---------------------follow_profile-----------)\n\nResponses (55)\n--------------\n\n[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--58ed12a492dc--------------------------------)\n\n[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Flevelup.gitconnected.com%2Fan-algo-trading-strategy-which-made-8-371-a-python-case-study-58ed12a492dc&source=---post_responses--58ed12a492dc---------------------respond_sidebar-----------)\n\nCancel\n\nRespond\n\nRespond\n\nAlso publish to my profile\n\nSee all responses\n\n[Help](https://help.medium.com/hc/en-us?source=post_page-----58ed12a492dc--------------------------------)\n\n[Status](https://medium.statuspage.io/?source=post_page-----58ed12a492dc--------------------------------)\n\n[About](https://medium.com/about?autoplay=1&source=post_page-----58ed12a492dc--------------------------------)\n\n[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----58ed12a492dc--------------------------------)\n\n[Press](https://levelup.gitconnected.com/pressinquiries@medium.com?source=post_page-----58ed12a492dc--------------------------------)\n\n[Blog](https://blog.medium.com/?source=post_page-----58ed12a492dc--------------------------------)\n\n[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----58ed12a492dc--------------------------------)\n\n[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----58ed12a492dc--------------------------------)\n\n[Text to speech](https://speechify.com/medium?source=post_page-----58ed12a492dc--------------------------------)\n\n[Teams](https://medium.com/business?source=post_page-----58ed12a492dc--------------------------------)",
  "publishedTime": "2023-11-28T20:54:51.453Z",
  "usage": {
    "tokens": 3579
  }
}
```
