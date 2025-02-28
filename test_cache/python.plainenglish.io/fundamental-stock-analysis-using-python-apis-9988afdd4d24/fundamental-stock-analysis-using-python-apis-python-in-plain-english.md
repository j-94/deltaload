---
title: Fundamental Stock Analysis Using Python APIs - Python in Plain English
description: Disclaimer: The information provided here is for informational purposes only and is not intended to be personal financial, investment, or other advice.
url: https://python.plainenglish.io/fundamental-stock-analysis-using-python-apis-9988afdd4d24
timestamp: 2025-01-20T15:54:49.051Z
domain: python.plainenglish.io
path: fundamental-stock-analysis-using-python-apis-9988afdd4d24
---

# Fundamental Stock Analysis Using Python APIs - Python in Plain English


Disclaimer: The information provided here is for informational purposes only and is not intended to be personal financial, investment, or other advice.


## Content

Fundamental Stock Analysis Using Python APIs | by Sugath Mudali | Python in Plain English
===============
 

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9988afdd4d24&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)

[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

![Image 10](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

Fundamental Stock Analysis Using Python APIs
============================================

[![Image 11: Sugath Mudali](https://miro.medium.com/v2/resize:fill:88:88/1*c1GqB08k2_DBv3pZn0jsYA.jpeg)](https://medium.com/@sugath.mudali?source=post_page---byline--9988afdd4d24--------------------------------)

[![Image 12: Python in Plain English](https://miro.medium.com/v2/resize:fill:48:48/1*VA3oGfprJgj5fRsTjXp6fA@2x.png)](https://python.plainenglish.io/?source=post_page---byline--9988afdd4d24--------------------------------)

[Sugath Mudali](https://medium.com/@sugath.mudali?source=post_page---byline--9988afdd4d24--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff54d3df0bb58&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=post_page-f54d3df0bb58--byline--9988afdd4d24---------------------post_header-----------)

Published in

[Python in Plain English](https://python.plainenglish.io/?source=post_page---byline--9988afdd4d24--------------------------------)

·

8 min read

·

Nov 7, 2023

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=---header_actions--9988afdd4d24---------------------clap_footer-----------)

\--

12

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=---header_actions--9988afdd4d24---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=---header_actions--9988afdd4d24---------------------post_audio_button-----------)

Share

This article will look at 10 fundamental indicators for stock selection.

**_Disclaimer:_** _The information provided here is for informational purposes only and is not intended to be personal financial, investment, or other advice._

**Key indicators:**

1.  [**EPS**](https://www.investopedia.com/terms/e/eps.asp) **(Earnings Per Share) —** portion of a company’s profit that is assigned to each share of its stock
2.  [**P/E**](https://www.investopedia.com/terms/p/price-earningsratio.asp) **(Price to Earnings) —** relationship between the stock price of a company and its per-share earnings. It helps investors determine if a stock is undervalued or overvalued relative to others in the same sector.
3.  [**PEG**](https://www.investopedia.com/terms/p/pegratio.asp) **(Projected Earnings Growth) —** calculated by dividing a stock’s P/E by its projected 12-month forward revenue growth rate. In general, a PEG lower than 1 is a good sign, and a PEG higher than 2 indicates that a stock may be overpriced
4.  [**FCFY**](https://www.investopedia.com/articles/fundamental-analysis/09/free-cash-flow-yield.asp) **(Free Cash Flow Yield) —** a financial solvency ratio that compares the free cash flow per share a company is expected to earn against its market value per share. A lower ratio indicates a less attractive investment opportunity.
5.  [**PB**](https://www.investopedia.com/terms/p/price-to-bookratio.asp) **(Price to Book) —** a ratio of 1 indicates the company’s shares are trading in line with its book value. A P/B higher than 1 suggests the company is trading at a premium to book value, and a P/B lower than 1 indicates a stock that may be undervalued relative to the company’s assets.
6.  [**ROE**](https://www.investopedia.com/terms/r/returnonequity.asp) **(Return on Equity) —** provides a way for investors to evaluate how…

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=---footer_actions--9988afdd4d24---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=---footer_actions--9988afdd4d24---------------------clap_footer-----------)

\--

12

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=---footer_actions--9988afdd4d24---------------------bookmark_footer-----------)

[![Image 13: Python in Plain English](https://miro.medium.com/v2/resize:fill:96:96/1*VA3oGfprJgj5fRsTjXp6fA@2x.png)](https://python.plainenglish.io/?source=post_page---post_publication_info--9988afdd4d24--------------------------------)

[![Image 14: Python in Plain English](https://miro.medium.com/v2/resize:fill:128:128/1*VA3oGfprJgj5fRsTjXp6fA@2x.png)](https://python.plainenglish.io/?source=post_page---post_publication_info--9988afdd4d24--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fpython-in-plain-english&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&collection=Python+in+Plain+English&collectionId=78073def27b8&source=post_page---post_publication_info--9988afdd4d24---------------------follow_profile-----------)

[Published in Python in Plain English ------------------------------------](https://python.plainenglish.io/?source=post_page---post_publication_info--9988afdd4d24--------------------------------)

[38K Followers](https://python.plainenglish.io/followers?source=post_page---post_publication_info--9988afdd4d24--------------------------------)

·[Last published 8 hours ago](https://python.plainenglish.io/unlock-your-future-a-step-by-step-guide-to-the-best-free-coding-resources-in-2025-1639b7c342e4?source=post_page---post_publication_info--9988afdd4d24--------------------------------)

New Python content every day. Follow to join our 3.5M+ monthly readers.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fpython-in-plain-english&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&collection=Python+in+Plain+English&collectionId=78073def27b8&source=post_page---post_publication_info--9988afdd4d24---------------------follow_profile-----------)

[![Image 15: Sugath Mudali](https://miro.medium.com/v2/resize:fill:96:96/1*c1GqB08k2_DBv3pZn0jsYA.jpeg)](https://medium.com/@sugath.mudali?source=post_page---post_author_info--9988afdd4d24--------------------------------)

[![Image 16: Sugath Mudali](https://miro.medium.com/v2/resize:fill:128:128/1*c1GqB08k2_DBv3pZn0jsYA.jpeg)](https://medium.com/@sugath.mudali?source=post_page---post_author_info--9988afdd4d24--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff54d3df0bb58&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=post_page-f54d3df0bb58--post_author_info--9988afdd4d24---------------------follow_profile-----------)

[Written by Sugath Mudali ------------------------](https://medium.com/@sugath.mudali?source=post_page---post_author_info--9988afdd4d24--------------------------------)

[1.1K Followers](https://medium.com/@sugath.mudali/followers?source=post_page---post_author_info--9988afdd4d24--------------------------------)

·[2 Following](https://medium.com/@sugath.mudali/following?source=post_page---post_author_info--9988afdd4d24--------------------------------)

Software Architect. Data Science & Cloud enthusiast. Opinions are my own.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff54d3df0bb58&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=post_page-f54d3df0bb58--post_author_info--9988afdd4d24---------------------follow_profile-----------)

Responses (12)
--------------

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--9988afdd4d24--------------------------------)

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=---post_responses--9988afdd4d24---------------------respond_sidebar-----------)

Cancel

Respond

Respond

Also publish to my profile

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----9988afdd4d24--------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----9988afdd4d24--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----9988afdd4d24--------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----9988afdd4d24--------------------------------)

[Press](https://python.plainenglish.io/pressinquiries@medium.com?source=post_page-----9988afdd4d24--------------------------------)

[Blog](https://blog.medium.com/?source=post_page-----9988afdd4d24--------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----9988afdd4d24--------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----9988afdd4d24--------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----9988afdd4d24--------------------------------)

[Teams](https://medium.com/business?source=post_page-----9988afdd4d24--------------------------------)

## Metadata

```json
{
  "title": "Fundamental Stock Analysis Using Python APIs - Python in Plain English",
  "description": "Disclaimer: The information provided here is for informational purposes only and is not intended to be personal financial, investment, or other advice.",
  "url": "https://python.plainenglish.io/fundamental-stock-analysis-using-python-apis-9988afdd4d24",
  "content": "Fundamental Stock Analysis Using Python APIs | by Sugath Mudali | Python in Plain English\n===============\n \n\n[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9988afdd4d24&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)\n\n[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)\n\n[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n![Image 10](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)\n\nMember-only story\n\nFundamental Stock Analysis Using Python APIs\n============================================\n\n[![Image 11: Sugath Mudali](https://miro.medium.com/v2/resize:fill:88:88/1*c1GqB08k2_DBv3pZn0jsYA.jpeg)](https://medium.com/@sugath.mudali?source=post_page---byline--9988afdd4d24--------------------------------)\n\n[![Image 12: Python in Plain English](https://miro.medium.com/v2/resize:fill:48:48/1*VA3oGfprJgj5fRsTjXp6fA@2x.png)](https://python.plainenglish.io/?source=post_page---byline--9988afdd4d24--------------------------------)\n\n[Sugath Mudali](https://medium.com/@sugath.mudali?source=post_page---byline--9988afdd4d24--------------------------------)\n\n·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff54d3df0bb58&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=post_page-f54d3df0bb58--byline--9988afdd4d24---------------------post_header-----------)\n\nPublished in\n\n[Python in Plain English](https://python.plainenglish.io/?source=post_page---byline--9988afdd4d24--------------------------------)\n\n·\n\n8 min read\n\n·\n\nNov 7, 2023\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=---header_actions--9988afdd4d24---------------------clap_footer-----------)\n\n\\--\n\n12\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=---header_actions--9988afdd4d24---------------------bookmark_footer-----------)\n\n[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=---header_actions--9988afdd4d24---------------------post_audio_button-----------)\n\nShare\n\nThis article will look at 10 fundamental indicators for stock selection.\n\n**_Disclaimer:_** _The information provided here is for informational purposes only and is not intended to be personal financial, investment, or other advice._\n\n**Key indicators:**\n\n1.  [**EPS**](https://www.investopedia.com/terms/e/eps.asp) **(Earnings Per Share) —** portion of a company’s profit that is assigned to each share of its stock\n2.  [**P/E**](https://www.investopedia.com/terms/p/price-earningsratio.asp) **(Price to Earnings) —** relationship between the stock price of a company and its per-share earnings. It helps investors determine if a stock is undervalued or overvalued relative to others in the same sector.\n3.  [**PEG**](https://www.investopedia.com/terms/p/pegratio.asp) **(Projected Earnings Growth) —** calculated by dividing a stock’s P/E by its projected 12-month forward revenue growth rate. In general, a PEG lower than 1 is a good sign, and a PEG higher than 2 indicates that a stock may be overpriced\n4.  [**FCFY**](https://www.investopedia.com/articles/fundamental-analysis/09/free-cash-flow-yield.asp) **(Free Cash Flow Yield) —** a financial solvency ratio that compares the free cash flow per share a company is expected to earn against its market value per share. A lower ratio indicates a less attractive investment opportunity.\n5.  [**PB**](https://www.investopedia.com/terms/p/price-to-bookratio.asp) **(Price to Book) —** a ratio of 1 indicates the company’s shares are trading in line with its book value. A P/B higher than 1 suggests the company is trading at a premium to book value, and a P/B lower than 1 indicates a stock that may be undervalued relative to the company’s assets.\n6.  [**ROE**](https://www.investopedia.com/terms/r/returnonequity.asp) **(Return on Equity) —** provides a way for investors to evaluate how…\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=---footer_actions--9988afdd4d24---------------------clap_footer-----------)\n\n\\--\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fpython-in-plain-english%2F9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=---footer_actions--9988afdd4d24---------------------clap_footer-----------)\n\n\\--\n\n12\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F9988afdd4d24&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=---footer_actions--9988afdd4d24---------------------bookmark_footer-----------)\n\n[![Image 13: Python in Plain English](https://miro.medium.com/v2/resize:fill:96:96/1*VA3oGfprJgj5fRsTjXp6fA@2x.png)](https://python.plainenglish.io/?source=post_page---post_publication_info--9988afdd4d24--------------------------------)\n\n[![Image 14: Python in Plain English](https://miro.medium.com/v2/resize:fill:128:128/1*VA3oGfprJgj5fRsTjXp6fA@2x.png)](https://python.plainenglish.io/?source=post_page---post_publication_info--9988afdd4d24--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fpython-in-plain-english&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&collection=Python+in+Plain+English&collectionId=78073def27b8&source=post_page---post_publication_info--9988afdd4d24---------------------follow_profile-----------)\n\n[Published in Python in Plain English ------------------------------------](https://python.plainenglish.io/?source=post_page---post_publication_info--9988afdd4d24--------------------------------)\n\n[38K Followers](https://python.plainenglish.io/followers?source=post_page---post_publication_info--9988afdd4d24--------------------------------)\n\n·[Last published 8 hours ago](https://python.plainenglish.io/unlock-your-future-a-step-by-step-guide-to-the-best-free-coding-resources-in-2025-1639b7c342e4?source=post_page---post_publication_info--9988afdd4d24--------------------------------)\n\nNew Python content every day. Follow to join our 3.5M+ monthly readers.\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fpython-in-plain-english&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&collection=Python+in+Plain+English&collectionId=78073def27b8&source=post_page---post_publication_info--9988afdd4d24---------------------follow_profile-----------)\n\n[![Image 15: Sugath Mudali](https://miro.medium.com/v2/resize:fill:96:96/1*c1GqB08k2_DBv3pZn0jsYA.jpeg)](https://medium.com/@sugath.mudali?source=post_page---post_author_info--9988afdd4d24--------------------------------)\n\n[![Image 16: Sugath Mudali](https://miro.medium.com/v2/resize:fill:128:128/1*c1GqB08k2_DBv3pZn0jsYA.jpeg)](https://medium.com/@sugath.mudali?source=post_page---post_author_info--9988afdd4d24--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff54d3df0bb58&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=post_page-f54d3df0bb58--post_author_info--9988afdd4d24---------------------follow_profile-----------)\n\n[Written by Sugath Mudali ------------------------](https://medium.com/@sugath.mudali?source=post_page---post_author_info--9988afdd4d24--------------------------------)\n\n[1.1K Followers](https://medium.com/@sugath.mudali/followers?source=post_page---post_author_info--9988afdd4d24--------------------------------)\n\n·[2 Following](https://medium.com/@sugath.mudali/following?source=post_page---post_author_info--9988afdd4d24--------------------------------)\n\nSoftware Architect. Data Science & Cloud enthusiast. Opinions are my own.\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff54d3df0bb58&operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&user=Sugath+Mudali&userId=f54d3df0bb58&source=post_page-f54d3df0bb58--post_author_info--9988afdd4d24---------------------follow_profile-----------)\n\nResponses (12)\n--------------\n\n[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--9988afdd4d24--------------------------------)\n\n[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fpython.plainenglish.io%2Ffundamental-stock-analysis-using-python-apis-9988afdd4d24&source=---post_responses--9988afdd4d24---------------------respond_sidebar-----------)\n\nCancel\n\nRespond\n\nRespond\n\nAlso publish to my profile\n\nSee all responses\n\n[Help](https://help.medium.com/hc/en-us?source=post_page-----9988afdd4d24--------------------------------)\n\n[Status](https://medium.statuspage.io/?source=post_page-----9988afdd4d24--------------------------------)\n\n[About](https://medium.com/about?autoplay=1&source=post_page-----9988afdd4d24--------------------------------)\n\n[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----9988afdd4d24--------------------------------)\n\n[Press](https://python.plainenglish.io/pressinquiries@medium.com?source=post_page-----9988afdd4d24--------------------------------)\n\n[Blog](https://blog.medium.com/?source=post_page-----9988afdd4d24--------------------------------)\n\n[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----9988afdd4d24--------------------------------)\n\n[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----9988afdd4d24--------------------------------)\n\n[Text to speech](https://speechify.com/medium?source=post_page-----9988afdd4d24--------------------------------)\n\n[Teams](https://medium.com/business?source=post_page-----9988afdd4d24--------------------------------)",
  "publishedTime": "2023-11-07T07:54:46.275Z",
  "usage": {
    "tokens": 3597
  }
}
```
