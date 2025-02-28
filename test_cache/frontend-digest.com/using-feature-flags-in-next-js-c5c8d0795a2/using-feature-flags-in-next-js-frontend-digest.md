---
title: Using Feature Flags in Next.js - Frontend Digest
description: Releasing features into production can be quite the thrill. Feature Flags can be an elegant solution as Feature Toggles are commonly used to test drive upcoming features internally. This article explains how to use Feature Flags in Next.js.
url: https://frontend-digest.com/using-feature-flags-in-next-js-c5c8d0795a2
timestamp: 2025-01-20T15:51:33.084Z
domain: frontend-digest.com
path: using-feature-flags-in-next-js-c5c8d0795a2
---

# Using Feature Flags in Next.js - Frontend Digest


Releasing features into production can be quite the thrill. Feature Flags can be an elegant solution as Feature Toggles are commonly used to test drive upcoming features internally. This article explains how to use Feature Flags in Next.js.


## Content

Using Feature Flags in Next.js. How to use Feature Flags to test drive… | by Dominik Ferber | Frontend Digest
===============
 

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc5c8d0795a2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)

[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)

[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

![Image 12](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Member-only story

Using Feature Flags in Next.js
==============================

How to release with confidence
------------------------------

[![Image 13: Dominik Ferber](https://miro.medium.com/v2/resize:fill:88:88/1*MTPqn8a9MxLikmbsJm907Q.jpeg)](https://medium.com/@dferber90?source=post_page---byline--c5c8d0795a2--------------------------------)

[![Image 14: Frontend Digest](https://miro.medium.com/v2/resize:fill:48:48/1*s7I1XqcdBhD7NzIdPNUSRQ.png)](https://frontend-digest.com/?source=post_page---byline--c5c8d0795a2--------------------------------)

[Dominik Ferber](https://medium.com/@dferber90?source=post_page---byline--c5c8d0795a2--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5f79bc607ab9&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=post_page-5f79bc607ab9--byline--c5c8d0795a2---------------------post_header-----------)

Published in

[Frontend Digest](https://frontend-digest.com/?source=post_page---byline--c5c8d0795a2--------------------------------)

·

10 min read

·

Sep 21, 2020

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ffrontend-digest%2Fc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=---header_actions--c5c8d0795a2---------------------clap_footer-----------)

\--

3

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=---header_actions--c5c8d0795a2---------------------bookmark_footer-----------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=---header_actions--c5c8d0795a2---------------------post_audio_button-----------)

Share

![Image 15](https://miro.medium.com/v2/resize:fit:700/0*UmnjmMzi7i5C6Ccs)

Photo by [Victor Grabarczyk](https://unsplash.com/@victor_vector?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Releasing features into production can be quite the thrill. Surely you’ve tested the feature you’ve been working on locally to ensure that it works as expected. Or you might have even used a preview deployment to your staging environment, on which your PO or a dedicated testing team took the feature for a ride.

But there’s still this uncertainty when going live: _Will it work in production?_

_And what do we do if it doesn’t?_

This article shows how to use feature flags to release with confidence, and how to set feature flags up in Next.js.

Releasing with confidence
=========================

Feature Flags allow you to do many cool things. The most important for the topic at hand is that they allow you to define who can access new features. That way, you can publish features for your team members only.

They can then ensure the feature you’ve been working works as expected, before you turn the new feature on for everyone. And if you later discover something’s wrong, you can even turn the feature off for everyone.

This setup allows you to take your changes for a test ride before opening it up to your users. Feature Flags aren’t only useful for big releases, you can use the same…

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ffrontend-digest%2Fc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=---footer_actions--c5c8d0795a2---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ffrontend-digest%2Fc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=---footer_actions--c5c8d0795a2---------------------clap_footer-----------)

\--

3

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=---footer_actions--c5c8d0795a2---------------------bookmark_footer-----------)

[![Image 16: Frontend Digest](https://miro.medium.com/v2/resize:fill:96:96/1*s7I1XqcdBhD7NzIdPNUSRQ.png)](https://frontend-digest.com/?source=post_page---post_publication_info--c5c8d0795a2--------------------------------)

[![Image 17: Frontend Digest](https://miro.medium.com/v2/resize:fill:128:128/1*s7I1XqcdBhD7NzIdPNUSRQ.png)](https://frontend-digest.com/?source=post_page---post_publication_info--c5c8d0795a2--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ffrontend-digest&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&collection=Frontend+Digest&collectionId=ca3e4733c82d&source=post_page---post_publication_info--c5c8d0795a2---------------------follow_profile-----------)

[Published in Frontend Digest ----------------------------](https://frontend-digest.com/?source=post_page---post_publication_info--c5c8d0795a2--------------------------------)

[2.7K Followers](https://frontend-digest.com/followers?source=post_page---post_publication_info--c5c8d0795a2--------------------------------)

·[Last published Feb 25, 2023](https://frontend-digest.com/how-to-import-third-party-scripts-into-nextjs-d2f353a6226f?source=post_page---post_publication_info--c5c8d0795a2--------------------------------)

Anything and everything frontend. JavaScript, CSS and HTML.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ffrontend-digest&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&collection=Frontend+Digest&collectionId=ca3e4733c82d&source=post_page---post_publication_info--c5c8d0795a2---------------------follow_profile-----------)

[![Image 18: Dominik Ferber](https://miro.medium.com/v2/resize:fill:96:96/1*MTPqn8a9MxLikmbsJm907Q.jpeg)](https://medium.com/@dferber90?source=post_page---post_author_info--c5c8d0795a2--------------------------------)

[![Image 19: Dominik Ferber](https://miro.medium.com/v2/resize:fill:128:128/1*MTPqn8a9MxLikmbsJm907Q.jpeg)](https://medium.com/@dferber90?source=post_page---post_author_info--c5c8d0795a2--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5f79bc607ab9&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=post_page-5f79bc607ab9--post_author_info--c5c8d0795a2---------------------follow_profile-----------)

[Written by Dominik Ferber -------------------------](https://medium.com/@dferber90?source=post_page---post_author_info--c5c8d0795a2--------------------------------)

[318 Followers](https://medium.com/@dferber90/followers?source=post_page---post_author_info--c5c8d0795a2--------------------------------)

·[80 Following](https://medium.com/@dferber90/following?source=post_page---post_author_info--c5c8d0795a2--------------------------------)

Next.js Consultant. I also build [happykit.dev](http://happykit.dev/)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5f79bc607ab9&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=post_page-5f79bc607ab9--post_author_info--c5c8d0795a2---------------------follow_profile-----------)

Responses (3)
-------------

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--c5c8d0795a2--------------------------------)

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=---post_responses--c5c8d0795a2---------------------respond_sidebar-----------)

Cancel

Respond

Respond

Also publish to my profile

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----c5c8d0795a2--------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----c5c8d0795a2--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----c5c8d0795a2--------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c5c8d0795a2--------------------------------)

[Press](https://frontend-digest.com/pressinquiries@medium.com?source=post_page-----c5c8d0795a2--------------------------------)

[Blog](https://blog.medium.com/?source=post_page-----c5c8d0795a2--------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c5c8d0795a2--------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c5c8d0795a2--------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----c5c8d0795a2--------------------------------)

[Teams](https://medium.com/business?source=post_page-----c5c8d0795a2--------------------------------)

## Metadata

```json
{
  "title": "Using Feature Flags in Next.js - Frontend Digest",
  "description": "Releasing features into production can be quite the thrill. Feature Flags can be an elegant solution as Feature Toggles are commonly used to test drive upcoming features internally. This article explains how to use Feature Flags in Next.js.",
  "url": "https://frontend-digest.com/using-feature-flags-in-next-js-c5c8d0795a2",
  "content": "Using Feature Flags in Next.js. How to use Feature Flags to test drive… | by Dominik Ferber | Frontend Digest\n===============\n \n\n[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc5c8d0795a2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)\n\n[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)\n\n[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)\n\n[Sign up](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n![Image 12](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)\n\nMember-only story\n\nUsing Feature Flags in Next.js\n==============================\n\nHow to release with confidence\n------------------------------\n\n[![Image 13: Dominik Ferber](https://miro.medium.com/v2/resize:fill:88:88/1*MTPqn8a9MxLikmbsJm907Q.jpeg)](https://medium.com/@dferber90?source=post_page---byline--c5c8d0795a2--------------------------------)\n\n[![Image 14: Frontend Digest](https://miro.medium.com/v2/resize:fill:48:48/1*s7I1XqcdBhD7NzIdPNUSRQ.png)](https://frontend-digest.com/?source=post_page---byline--c5c8d0795a2--------------------------------)\n\n[Dominik Ferber](https://medium.com/@dferber90?source=post_page---byline--c5c8d0795a2--------------------------------)\n\n·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5f79bc607ab9&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=post_page-5f79bc607ab9--byline--c5c8d0795a2---------------------post_header-----------)\n\nPublished in\n\n[Frontend Digest](https://frontend-digest.com/?source=post_page---byline--c5c8d0795a2--------------------------------)\n\n·\n\n10 min read\n\n·\n\nSep 21, 2020\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ffrontend-digest%2Fc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=---header_actions--c5c8d0795a2---------------------clap_footer-----------)\n\n\\--\n\n3\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=---header_actions--c5c8d0795a2---------------------bookmark_footer-----------)\n\n[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=---header_actions--c5c8d0795a2---------------------post_audio_button-----------)\n\nShare\n\n![Image 15](https://miro.medium.com/v2/resize:fit:700/0*UmnjmMzi7i5C6Ccs)\n\nPhoto by [Victor Grabarczyk](https://unsplash.com/@victor_vector?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)\n\nReleasing features into production can be quite the thrill. Surely you’ve tested the feature you’ve been working on locally to ensure that it works as expected. Or you might have even used a preview deployment to your staging environment, on which your PO or a dedicated testing team took the feature for a ride.\n\nBut there’s still this uncertainty when going live: _Will it work in production?_\n\n_And what do we do if it doesn’t?_\n\nThis article shows how to use feature flags to release with confidence, and how to set feature flags up in Next.js.\n\nReleasing with confidence\n=========================\n\nFeature Flags allow you to do many cool things. The most important for the topic at hand is that they allow you to define who can access new features. That way, you can publish features for your team members only.\n\nThey can then ensure the feature you’ve been working works as expected, before you turn the new feature on for everyone. And if you later discover something’s wrong, you can even turn the feature off for everyone.\n\nThis setup allows you to take your changes for a test ride before opening it up to your users. Feature Flags aren’t only useful for big releases, you can use the same…\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ffrontend-digest%2Fc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=---footer_actions--c5c8d0795a2---------------------clap_footer-----------)\n\n\\--\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Ffrontend-digest%2Fc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=---footer_actions--c5c8d0795a2---------------------clap_footer-----------)\n\n\\--\n\n3\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc5c8d0795a2&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=---footer_actions--c5c8d0795a2---------------------bookmark_footer-----------)\n\n[![Image 16: Frontend Digest](https://miro.medium.com/v2/resize:fill:96:96/1*s7I1XqcdBhD7NzIdPNUSRQ.png)](https://frontend-digest.com/?source=post_page---post_publication_info--c5c8d0795a2--------------------------------)\n\n[![Image 17: Frontend Digest](https://miro.medium.com/v2/resize:fill:128:128/1*s7I1XqcdBhD7NzIdPNUSRQ.png)](https://frontend-digest.com/?source=post_page---post_publication_info--c5c8d0795a2--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ffrontend-digest&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&collection=Frontend+Digest&collectionId=ca3e4733c82d&source=post_page---post_publication_info--c5c8d0795a2---------------------follow_profile-----------)\n\n[Published in Frontend Digest ----------------------------](https://frontend-digest.com/?source=post_page---post_publication_info--c5c8d0795a2--------------------------------)\n\n[2.7K Followers](https://frontend-digest.com/followers?source=post_page---post_publication_info--c5c8d0795a2--------------------------------)\n\n·[Last published Feb 25, 2023](https://frontend-digest.com/how-to-import-third-party-scripts-into-nextjs-d2f353a6226f?source=post_page---post_publication_info--c5c8d0795a2--------------------------------)\n\nAnything and everything frontend. JavaScript, CSS and HTML.\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Ffrontend-digest&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&collection=Frontend+Digest&collectionId=ca3e4733c82d&source=post_page---post_publication_info--c5c8d0795a2---------------------follow_profile-----------)\n\n[![Image 18: Dominik Ferber](https://miro.medium.com/v2/resize:fill:96:96/1*MTPqn8a9MxLikmbsJm907Q.jpeg)](https://medium.com/@dferber90?source=post_page---post_author_info--c5c8d0795a2--------------------------------)\n\n[![Image 19: Dominik Ferber](https://miro.medium.com/v2/resize:fill:128:128/1*MTPqn8a9MxLikmbsJm907Q.jpeg)](https://medium.com/@dferber90?source=post_page---post_author_info--c5c8d0795a2--------------------------------)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5f79bc607ab9&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=post_page-5f79bc607ab9--post_author_info--c5c8d0795a2---------------------follow_profile-----------)\n\n[Written by Dominik Ferber -------------------------](https://medium.com/@dferber90?source=post_page---post_author_info--c5c8d0795a2--------------------------------)\n\n[318 Followers](https://medium.com/@dferber90/followers?source=post_page---post_author_info--c5c8d0795a2--------------------------------)\n\n·[80 Following](https://medium.com/@dferber90/following?source=post_page---post_author_info--c5c8d0795a2--------------------------------)\n\nNext.js Consultant. I also build [happykit.dev](http://happykit.dev/)\n\n[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F5f79bc607ab9&operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&user=Dominik+Ferber&userId=5f79bc607ab9&source=post_page-5f79bc607ab9--post_author_info--c5c8d0795a2---------------------follow_profile-----------)\n\nResponses (3)\n-------------\n\n[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--c5c8d0795a2--------------------------------)\n\n[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Ffrontend-digest.com%2Fusing-feature-flags-in-next-js-c5c8d0795a2&source=---post_responses--c5c8d0795a2---------------------respond_sidebar-----------)\n\nCancel\n\nRespond\n\nRespond\n\nAlso publish to my profile\n\nSee all responses\n\n[Help](https://help.medium.com/hc/en-us?source=post_page-----c5c8d0795a2--------------------------------)\n\n[Status](https://medium.statuspage.io/?source=post_page-----c5c8d0795a2--------------------------------)\n\n[About](https://medium.com/about?autoplay=1&source=post_page-----c5c8d0795a2--------------------------------)\n\n[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----c5c8d0795a2--------------------------------)\n\n[Press](https://frontend-digest.com/pressinquiries@medium.com?source=post_page-----c5c8d0795a2--------------------------------)\n\n[Blog](https://blog.medium.com/?source=post_page-----c5c8d0795a2--------------------------------)\n\n[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----c5c8d0795a2--------------------------------)\n\n[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----c5c8d0795a2--------------------------------)\n\n[Text to speech](https://speechify.com/medium?source=post_page-----c5c8d0795a2--------------------------------)\n\n[Teams](https://medium.com/business?source=post_page-----c5c8d0795a2--------------------------------)",
  "publishedTime": "2020-09-21T11:22:08.795Z",
  "usage": {
    "tokens": 3450
  }
}
```
