---
title: Segment Anything 3D for Point Clouds: Complete Guide | Towards Data Science
description: Build a Semantic Segmentation Application for 3D Point Clouds with the Segment Anything Model (SAM) and Python. Bonus: Code for 2D to 3D Projections.
url: https://towardsdatascience.com/segment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18
timestamp: 2025-01-20T16:02:17.954Z
domain: towardsdatascience.com
path: segment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18
---

# Segment Anything 3D for Point Clouds: Complete Guide | Towards Data Science


Build a Semantic Segmentation Application for 3D Point Clouds with the Segment Anything Model (SAM) and Python. Bonus: Code for 2D to 3D Projections.


## Content

Segment Anything 3D for Point Clouds: Complete Guide | Towards Data Science
===============
 

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F80c06be99a18&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)

[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

![Image 12](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

3D Python
---------

Segment Anything 3D for Point Clouds: Complete Guide (SAM 3D)
=============================================================

How to build a semantic segmentation application for 3D point clouds leveraging SAM and Python. Bonus: code for projections and relationships between 3D points and 2D pixels.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[![Image 13: Florent Poux, Ph.D.](https://miro.medium.com/v2/resize:fill:44:44/1*2y0Pd7Oe-EFBIIVYNHG9iQ.jpeg)](https://medium.com/@florentpoux?source=post_page---byline--80c06be99a18--------------------------------)

[![Image 14: Towards Data Science](https://miro.medium.com/v2/resize:fill:24:24/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---byline--80c06be99a18--------------------------------)

[Florent Poux, Ph.D.](https://medium.com/@florentpoux?source=post_page---byline--80c06be99a18--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8ba7bf4ad784&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=post_page-8ba7bf4ad784--byline--80c06be99a18---------------------post_header-----------)

Published in

[Towards Data Science](https://towardsdatascience.com/?source=post_page---byline--80c06be99a18--------------------------------)

·

27 min read

·

Dec 13, 2023

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=---header_actions--80c06be99a18---------------------clap_footer-----------)

\--

9

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=---header_actions--80c06be99a18---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=---header_actions--80c06be99a18---------------------post_audio_button-----------)

Share

![Image 15: The Segment Anything Model for 3D Environments. We will detect objects in indoor spaces using 3D point cloud datasets. Credit goes to Mimatelier, the talented illustrator who created this image.](https://miro.medium.com/v2/resize:fit:700/1*WshbnvXhbNyTQqxeYPTIQA.png)

The Segment Anything Model for 3D Environments. We will detect objects in indoor spaces using 3D point cloud datasets. Credit goes to [Mimatelier](https://linktr.ee/mimatelier), the talented illustrator who created this image.

Technological leaps are just plain crazy, especially looking at Artificial Intelligence (AI) applied to 3D challenges. Having the ability to leverage the latest cutting-edge research for advanced 3D applications is very empowering. Especially when looking at bringing human-level reasoning capabilities to a computer, there is a clear need to extract a formalized meaning from the 3D entities that we observe.

> In this tutorial, we are here to make sure that we can bind amazing AI advancements with 3D applications that make use of 3D Point Clouds. — _🐲_ **Florent & Ville**

This is no easy feat, but once mastered, the fusion of 3D point clouds and deep learning gives birth to new dimensions of understanding and interpreting our visual world.

Among these advancements, the Segment Anything Model is a recent beacon of innovation, especially for full automation without supervision.

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=---footer_actions--80c06be99a18---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=---footer_actions--80c06be99a18---------------------clap_footer-----------)

\--

9

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=---footer_actions--80c06be99a18---------------------bookmark_footer-----------)

[![Image 16: Towards Data Science](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---post_publication_info--80c06be99a18--------------------------------)

[![Image 17: Towards Data Science](https://miro.medium.com/v2/resize:fill:64:64/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---post_publication_info--80c06be99a18--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--80c06be99a18---------------------follow_profile-----------)

[Published in Towards Data Science ---------------------------------](https://towardsdatascience.com/?source=post_page---post_publication_info--80c06be99a18--------------------------------)

[793K Followers](https://towardsdatascience.com/followers?source=post_page---post_publication_info--80c06be99a18--------------------------------)

·[Last published 3 hours ago](https://towardsdatascience.com/detecting-hallucination-in-rag-ecaf251a6633?source=post_page---post_publication_info--80c06be99a18--------------------------------)

Your home for data science and AI. The world’s leading publication for data science, data analytics, data engineering, machine learning, and artificial intelligence professionals.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--80c06be99a18---------------------follow_profile-----------)

[![Image 18: Florent Poux, Ph.D.](https://miro.medium.com/v2/resize:fill:48:48/1*2y0Pd7Oe-EFBIIVYNHG9iQ.jpeg)](https://medium.com/@florentpoux?source=post_page---post_author_info--80c06be99a18--------------------------------)

[![Image 19: Florent Poux, Ph.D.](https://miro.medium.com/v2/resize:fill:64:64/1*2y0Pd7Oe-EFBIIVYNHG9iQ.jpeg)](https://medium.com/@florentpoux?source=post_page---post_author_info--80c06be99a18--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8ba7bf4ad784&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=post_page-8ba7bf4ad784--post_author_info--80c06be99a18---------------------follow_profile-----------)

[Written by Florent Poux, Ph.D. ------------------------------](https://medium.com/@florentpoux?source=post_page---post_author_info--80c06be99a18--------------------------------)

[3.9K Followers](https://medium.com/@florentpoux/followers?source=post_page---post_author_info--80c06be99a18--------------------------------)

·[26 Following](https://medium.com/@florentpoux/following?source=post_page---post_author_info--80c06be99a18--------------------------------)

🏆 Director of Science | 3D Data + Spatial AI. [https://learngeodata.eu](https://learngeodata.eu/) (💻 + 📦 + 📙 + ▶️)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8ba7bf4ad784&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=post_page-8ba7bf4ad784--post_author_info--80c06be99a18---------------------follow_profile-----------)

Responses (9)
-------------

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--80c06be99a18--------------------------------)

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=---post_responses--80c06be99a18---------------------respond_sidebar-----------)

Cancel

Respond

Respond

Also publish to my profile

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----80c06be99a18--------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----80c06be99a18--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----80c06be99a18--------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----80c06be99a18--------------------------------)

[Press](https://towardsdatascience.com/pressinquiries@medium.com?source=post_page-----80c06be99a18--------------------------------)

[Blog](https://blog.medium.com/?source=post_page-----80c06be99a18--------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----80c06be99a18--------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----80c06be99a18--------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----80c06be99a18--------------------------------)

[Teams](https://medium.com/business?source=post_page-----80c06be99a18--------------------------------)

## Metadata

```json
{
  "title": "Segment Anything 3D for Point Clouds: Complete Guide | Towards Data Science",
  "description": "Build a Semantic Segmentation Application for 3D Point Clouds with the Segment Anything Model (SAM) and Python. Bonus: Code for 2D to 3D Projections.",
  "url": "https://towardsdatascience.com/segment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18",
  "content": "Segment Anything 3D for Point Clouds: Complete Guide | Towards Data Science\n===============\n \n\n[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F80c06be99a18&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)\n\n[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)\n\n[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n![Image 12](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)\n\nMember-only story\n\n3D Python\n---------\n\nSegment Anything 3D for Point Clouds: Complete Guide (SAM 3D)\n=============================================================\n\nHow to build a semantic segmentation application for 3D point clouds leveraging SAM and Python. Bonus: code for projections and relationships between 3D points and 2D pixels.\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n[![Image 13: Florent Poux, Ph.D.](https://miro.medium.com/v2/resize:fill:44:44/1*2y0Pd7Oe-EFBIIVYNHG9iQ.jpeg)](https://medium.com/@florentpoux?source=post_page---byline--80c06be99a18--------------------------------)\n\n[![Image 14: Towards Data Science](https://miro.medium.com/v2/resize:fill:24:24/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---byline--80c06be99a18--------------------------------)\n\n[Florent Poux, Ph.D.](https://medium.com/@florentpoux?source=post_page---byline--80c06be99a18--------------------------------)\n\n·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8ba7bf4ad784&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=post_page-8ba7bf4ad784--byline--80c06be99a18---------------------post_header-----------)\n\nPublished in\n\n[Towards Data Science](https://towardsdatascience.com/?source=post_page---byline--80c06be99a18--------------------------------)\n\n·\n\n27 min read\n\n·\n\nDec 13, 2023\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=---header_actions--80c06be99a18---------------------clap_footer-----------)\n\n\\--\n\n9\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=---header_actions--80c06be99a18---------------------bookmark_footer-----------)\n\n[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=---header_actions--80c06be99a18---------------------post_audio_button-----------)\n\nShare\n\n![Image 15: The Segment Anything Model for 3D Environments. We will detect objects in indoor spaces using 3D point cloud datasets. Credit goes to Mimatelier, the talented illustrator who created this image.](https://miro.medium.com/v2/resize:fit:700/1*WshbnvXhbNyTQqxeYPTIQA.png)\n\nThe Segment Anything Model for 3D Environments. We will detect objects in indoor spaces using 3D point cloud datasets. Credit goes to [Mimatelier](https://linktr.ee/mimatelier), the talented illustrator who created this image.\n\nTechnological leaps are just plain crazy, especially looking at Artificial Intelligence (AI) applied to 3D challenges. Having the ability to leverage the latest cutting-edge research for advanced 3D applications is very empowering. Especially when looking at bringing human-level reasoning capabilities to a computer, there is a clear need to extract a formalized meaning from the 3D entities that we observe.\n\n> In this tutorial, we are here to make sure that we can bind amazing AI advancements with 3D applications that make use of 3D Point Clouds. — _🐲_ **Florent & Ville**\n\nThis is no easy feat, but once mastered, the fusion of 3D point clouds and deep learning gives birth to new dimensions of understanding and interpreting our visual world.\n\nAmong these advancements, the Segment Anything Model is a recent beacon of innovation, especially for full automation without supervision.\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=---footer_actions--80c06be99a18---------------------clap_footer-----------)\n\n\\--\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ftowards-data-science%2F80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=---footer_actions--80c06be99a18---------------------clap_footer-----------)\n\n\\--\n\n9\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F80c06be99a18&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=---footer_actions--80c06be99a18---------------------bookmark_footer-----------)\n\n[![Image 16: Towards Data Science](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---post_publication_info--80c06be99a18--------------------------------)\n\n[![Image 17: Towards Data Science](https://miro.medium.com/v2/resize:fill:64:64/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---post_publication_info--80c06be99a18--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--80c06be99a18---------------------follow_profile-----------)\n\n[Published in Towards Data Science ---------------------------------](https://towardsdatascience.com/?source=post_page---post_publication_info--80c06be99a18--------------------------------)\n\n[793K Followers](https://towardsdatascience.com/followers?source=post_page---post_publication_info--80c06be99a18--------------------------------)\n\n·[Last published 3 hours ago](https://towardsdatascience.com/detecting-hallucination-in-rag-ecaf251a6633?source=post_page---post_publication_info--80c06be99a18--------------------------------)\n\nYour home for data science and AI. The world’s leading publication for data science, data analytics, data engineering, machine learning, and artificial intelligence professionals.\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ftowards-data-science&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&collection=Towards+Data+Science&collectionId=7f60cf5620c9&source=post_page---post_publication_info--80c06be99a18---------------------follow_profile-----------)\n\n[![Image 18: Florent Poux, Ph.D.](https://miro.medium.com/v2/resize:fill:48:48/1*2y0Pd7Oe-EFBIIVYNHG9iQ.jpeg)](https://medium.com/@florentpoux?source=post_page---post_author_info--80c06be99a18--------------------------------)\n\n[![Image 19: Florent Poux, Ph.D.](https://miro.medium.com/v2/resize:fill:64:64/1*2y0Pd7Oe-EFBIIVYNHG9iQ.jpeg)](https://medium.com/@florentpoux?source=post_page---post_author_info--80c06be99a18--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8ba7bf4ad784&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=post_page-8ba7bf4ad784--post_author_info--80c06be99a18---------------------follow_profile-----------)\n\n[Written by Florent Poux, Ph.D. ------------------------------](https://medium.com/@florentpoux?source=post_page---post_author_info--80c06be99a18--------------------------------)\n\n[3.9K Followers](https://medium.com/@florentpoux/followers?source=post_page---post_author_info--80c06be99a18--------------------------------)\n\n·[26 Following](https://medium.com/@florentpoux/following?source=post_page---post_author_info--80c06be99a18--------------------------------)\n\n🏆 Director of Science | 3D Data + Spatial AI. [https://learngeodata.eu](https://learngeodata.eu/) (💻 + 📦 + 📙 + ▶️)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8ba7bf4ad784&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&user=Florent+Poux%2C+Ph.D.&userId=8ba7bf4ad784&source=post_page-8ba7bf4ad784--post_author_info--80c06be99a18---------------------follow_profile-----------)\n\nResponses (9)\n-------------\n\n[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--80c06be99a18--------------------------------)\n\n[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Fsegment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18&source=---post_responses--80c06be99a18---------------------respond_sidebar-----------)\n\nCancel\n\nRespond\n\nRespond\n\nAlso publish to my profile\n\nSee all responses\n\n[Help](https://help.medium.com/hc/en-us?source=post_page-----80c06be99a18--------------------------------)\n\n[Status](https://medium.statuspage.io/?source=post_page-----80c06be99a18--------------------------------)\n\n[About](https://medium.com/about?autoplay=1&source=post_page-----80c06be99a18--------------------------------)\n\n[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----80c06be99a18--------------------------------)\n\n[Press](https://towardsdatascience.com/pressinquiries@medium.com?source=post_page-----80c06be99a18--------------------------------)\n\n[Blog](https://blog.medium.com/?source=post_page-----80c06be99a18--------------------------------)\n\n[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----80c06be99a18--------------------------------)\n\n[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----80c06be99a18--------------------------------)\n\n[Text to speech](https://speechify.com/medium?source=post_page-----80c06be99a18--------------------------------)\n\n[Teams](https://medium.com/business?source=post_page-----80c06be99a18--------------------------------)",
  "publishedTime": "2023-12-13T00:51:01.307Z",
  "usage": {
    "tokens": 3693
  }
}
```
