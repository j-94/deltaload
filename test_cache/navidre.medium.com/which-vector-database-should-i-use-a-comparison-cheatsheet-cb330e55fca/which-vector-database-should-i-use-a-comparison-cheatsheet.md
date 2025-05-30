---
title: Which Vector Database Should I Use? A Comparison Cheatsheet
description: Semantic search and retrieval-augmented generation (RAG) applications require systems to be able to save lots of embedding vectors (n-dimensional vectors, representing pieces of data) and also be…
url: https://navidre.medium.com/which-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca
timestamp: 2025-01-20T15:45:09.996Z
domain: navidre.medium.com
path: which-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca
---

# Which Vector Database Should I Use? A Comparison Cheatsheet


Semantic search and retrieval-augmented generation (RAG) applications require systems to be able to save lots of embedding vectors (n-dimensional vectors, representing pieces of data) and also be…


## Content

Which Vector Database Should I Use? A Comparison Cheatsheet | by Navid Rezaei | Medium
===============
 

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcb330e55fca&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&source=---top_nav_layout_nav----------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)

[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)

![Image 9](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

Which Vector Database Should I Use? A Comparison Cheatsheet
===========================================================

[![Image 10: Navid Rezaei](https://miro.medium.com/v2/resize:fill:88:88/1*_DALUa8EVjYpT12eSzFN-w.jpeg)](https://navidre.medium.com/?source=post_page---byline--cb330e55fca--------------------------------)

[Navid Rezaei](https://navidre.medium.com/?source=post_page---byline--cb330e55fca--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fa39f90dc9245&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&user=Navid+Rezaei&userId=a39f90dc9245&source=post_page-a39f90dc9245--byline--cb330e55fca---------------------post_header-----------)

3 min read

·

Jul 29, 2023

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fcb330e55fca&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&user=Navid+Rezaei&userId=a39f90dc9245&source=---header_actions--cb330e55fca---------------------clap_footer-----------)

\--

12

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcb330e55fca&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&source=---header_actions--cb330e55fca---------------------bookmark_footer-----------)

Listen

Share

Semantic search and retrieval-augmented generation (RAG) applications require systems to be able to save lots of embedding vectors (n-dimensional vectors, representing pieces of data) and also be able to retrieve the most relevant vectors with low latency. This requirement has resulted in emergence of many new vector databases. Choosing and relying on one can have long-term impacts and dependencies in your system. We ideally choose a vector database that can scale well, while keeping cost and latency low. Last but not least, the chosen vector database must adhere to the compliance requirements of the target application.

In this post, we try to summarize and compare all the well-known vector databases to make the decision between them easier. The comparison is an on-going work and the decision depends on the specific use cases.

![Image 11](https://miro.medium.com/v2/resize:fit:700/1*Qb16j6qZYfhK9sLgi3hWAA.png)

Screenshot of [TensorFlow embedding projector](https://projector.tensorflow.org/)

The comparison table is as follows. It is not a comprehensive comparison and may have errors. Please let me know if anything needs to be updated. Last update: Jul. 30, 2023.

Vector databases compared are: [Weaviate](https://weaviate.io/), [Pinecone](https://www.pinecone.io/), [pgvector](https://github.com/pgvector/pgvector), [Milvus](https://milvus.io/), [MongoDB](https://www.mongodb.com/), [Qdrant](https://qdrant.tech/), and [Chroma](https://www.trychroma.com/). The benchmark data is from [ANN Benchmarks](https://ann-benchmarks.com/).

The comparison is not exhaustive, more comparisons can be found here:

1.  A collaborative spreadsheet managed by the community: [https://docs.google.com/spreadsheets/d/1oAeF4Q7ILxxfInGJ8vTsBck3-2U9VV8idDf3hJOozNw/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1oAeF4Q7ILxxfInGJ8vTsBck3-2U9VV8idDf3hJOozNw/edit?usp=sharing).
2.  [VecDBs.com](https://www.vecdbs.com/) website (in-progress and to be open sourced): [https://www.vecdbs.com/](https://www.vecdbs.com/)

![Image 12](https://miro.medium.com/v2/resize:fit:700/1*fqiIXM6cHcOoEh_4WX0o1A.png)

Discussion
==========

Choosing a database to store vector formats is an important decision that can affect your architecture, compliance, and future costs. There are two general categories of vector databases: 1) Independent Vector Database and 2) Vector Search in Current Database. An example of an independent vector database is Pinecone and an example of vector search in the current database is pgvector on PostgreSQL.

Independent vector databases require that you maintain the embeddings independent of the original database. There could be some added benefits to this architecture. One should decide if these added benefits are worth the extra complexity and cost.

Another solution is to store the embeddings where your data already resides. This way, the complexity of the architecture is reduced, and you will not have extra compliance concerns. Last but not least, it seems to be a cost-effective solution. However, these solutions should be considered in terms of database queries per second (QPS).

Choosing between these two categories, a new vector database or vector search in the current database, is a decision that depends on application-specific factors. Hopefully, this collaborative comparison table could help with your decision!

Please follow me on Medium or social media to keep in contact:

[Twitter](https://twitter.com/navid_re) | [LinkedIn](https://www.linkedin.com/in/navidrezaei/) | [Medium](https://medium.com/@navidre)

![Image 13](https://miro.medium.com/v2/da:true/resize:fit:0/5c50caa54067fd622d2f0fac18392213bf92f6e2fae89b691e62bceb40885e74)

Sign up to discover human stories that deepen your understanding of the world.
------------------------------------------------------------------------------

Free
----

Distraction-free reading. No ads.

Organize your knowledge with lists and highlights.

Tell your story. Find your audience.

Sign up for free

Membership
----------

Read member-only stories

Support writers you read most

Earn money for your writing

Listen to audio narrations

Read offline with the Medium app

Try for $5/month

[AI](https://medium.com/tag/ai?source=post_page-----cb330e55fca--------------------------------)

[Vector Database](https://medium.com/tag/vector-database?source=post_page-----cb330e55fca--------------------------------)

[NLP](https://medium.com/tag/nlp?source=post_page-----cb330e55fca--------------------------------)

[Computer Vision](https://medium.com/tag/computer-vision?source=post_page-----cb330e55fca--------------------------------)

[Database](https://medium.com/tag/database?source=post_page-----cb330e55fca--------------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fcb330e55fca&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&user=Navid+Rezaei&userId=a39f90dc9245&source=---footer_actions--cb330e55fca---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fcb330e55fca&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&user=Navid+Rezaei&userId=a39f90dc9245&source=---footer_actions--cb330e55fca---------------------clap_footer-----------)

\--

12

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcb330e55fca&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&source=---footer_actions--cb330e55fca---------------------bookmark_footer-----------)

[![Image 14: Navid Rezaei](https://miro.medium.com/v2/resize:fill:96:96/1*_DALUa8EVjYpT12eSzFN-w.jpeg)](https://navidre.medium.com/?source=post_page---post_author_info--cb330e55fca--------------------------------)

[![Image 15: Navid Rezaei](https://miro.medium.com/v2/resize:fill:128:128/1*_DALUa8EVjYpT12eSzFN-w.jpeg)](https://navidre.medium.com/?source=post_page---post_author_info--cb330e55fca--------------------------------)

Follow

[Written by Navid Rezaei -----------------------](https://navidre.medium.com/?source=post_page---post_author_info--cb330e55fca--------------------------------)

[70 Followers](https://navidre.medium.com/followers?source=post_page---post_author_info--cb330e55fca--------------------------------)

·[12 Following](https://navidre.medium.com/following?source=post_page---post_author_info--cb330e55fca--------------------------------)

LinkedIn: [https://www.linkedin.com/in/navidrezaei/](https://www.linkedin.com/in/navidrezaei/) Twitter: [https://twitter.com/navid\_re](https://twitter.com/navid_re)

Follow

Responses (12)
--------------

[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--cb330e55fca--------------------------------)

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&source=---post_responses--cb330e55fca---------------------respond_sidebar-----------)

Also publish to my profile

Respond

Respond

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----cb330e55fca--------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----cb330e55fca--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----cb330e55fca--------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----cb330e55fca--------------------------------)

[Press](https://navidre.medium.com/pressinquiries@medium.com?source=post_page-----cb330e55fca--------------------------------)

[Blog](https://blog.medium.com/?source=post_page-----cb330e55fca--------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----cb330e55fca--------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cb330e55fca--------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----cb330e55fca--------------------------------)

[Teams](https://medium.com/business?source=post_page-----cb330e55fca--------------------------------)

## Metadata

```json
{
  "title": "Which Vector Database Should I Use? A Comparison Cheatsheet",
  "description": "Semantic search and retrieval-augmented generation (RAG) applications require systems to be able to save lots of embedding vectors (n-dimensional vectors, representing pieces of data) and also be…",
  "url": "https://navidre.medium.com/which-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca",
  "content": "Which Vector Database Should I Use? A Comparison Cheatsheet | by Navid Rezaei | Medium\n===============\n \n\n[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcb330e55fca&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&source=---top_nav_layout_nav----------------------------------)\n\nSign up\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n[](https://medium.com/?source=---top_nav_layout_nav----------------------------------)\n\n[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav-----------)\n\n[](https://medium.com/search?source=---top_nav_layout_nav----------------------------------)\n\nSign up\n\n[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&source=post_page---top_nav_layout_nav-----------------------global_nav-----------)\n\n![Image 9](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)\n\nWhich Vector Database Should I Use? A Comparison Cheatsheet\n===========================================================\n\n[![Image 10: Navid Rezaei](https://miro.medium.com/v2/resize:fill:88:88/1*_DALUa8EVjYpT12eSzFN-w.jpeg)](https://navidre.medium.com/?source=post_page---byline--cb330e55fca--------------------------------)\n\n[Navid Rezaei](https://navidre.medium.com/?source=post_page---byline--cb330e55fca--------------------------------)\n\n·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fa39f90dc9245&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&user=Navid+Rezaei&userId=a39f90dc9245&source=post_page-a39f90dc9245--byline--cb330e55fca---------------------post_header-----------)\n\n3 min read\n\n·\n\nJul 29, 2023\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fcb330e55fca&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&user=Navid+Rezaei&userId=a39f90dc9245&source=---header_actions--cb330e55fca---------------------clap_footer-----------)\n\n\\--\n\n12\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcb330e55fca&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&source=---header_actions--cb330e55fca---------------------bookmark_footer-----------)\n\nListen\n\nShare\n\nSemantic search and retrieval-augmented generation (RAG) applications require systems to be able to save lots of embedding vectors (n-dimensional vectors, representing pieces of data) and also be able to retrieve the most relevant vectors with low latency. This requirement has resulted in emergence of many new vector databases. Choosing and relying on one can have long-term impacts and dependencies in your system. We ideally choose a vector database that can scale well, while keeping cost and latency low. Last but not least, the chosen vector database must adhere to the compliance requirements of the target application.\n\nIn this post, we try to summarize and compare all the well-known vector databases to make the decision between them easier. The comparison is an on-going work and the decision depends on the specific use cases.\n\n![Image 11](https://miro.medium.com/v2/resize:fit:700/1*Qb16j6qZYfhK9sLgi3hWAA.png)\n\nScreenshot of [TensorFlow embedding projector](https://projector.tensorflow.org/)\n\nThe comparison table is as follows. It is not a comprehensive comparison and may have errors. Please let me know if anything needs to be updated. Last update: Jul. 30, 2023.\n\nVector databases compared are: [Weaviate](https://weaviate.io/), [Pinecone](https://www.pinecone.io/), [pgvector](https://github.com/pgvector/pgvector), [Milvus](https://milvus.io/), [MongoDB](https://www.mongodb.com/), [Qdrant](https://qdrant.tech/), and [Chroma](https://www.trychroma.com/). The benchmark data is from [ANN Benchmarks](https://ann-benchmarks.com/).\n\nThe comparison is not exhaustive, more comparisons can be found here:\n\n1.  A collaborative spreadsheet managed by the community: [https://docs.google.com/spreadsheets/d/1oAeF4Q7ILxxfInGJ8vTsBck3-2U9VV8idDf3hJOozNw/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1oAeF4Q7ILxxfInGJ8vTsBck3-2U9VV8idDf3hJOozNw/edit?usp=sharing).\n2.  [VecDBs.com](https://www.vecdbs.com/) website (in-progress and to be open sourced): [https://www.vecdbs.com/](https://www.vecdbs.com/)\n\n![Image 12](https://miro.medium.com/v2/resize:fit:700/1*fqiIXM6cHcOoEh_4WX0o1A.png)\n\nDiscussion\n==========\n\nChoosing a database to store vector formats is an important decision that can affect your architecture, compliance, and future costs. There are two general categories of vector databases: 1) Independent Vector Database and 2) Vector Search in Current Database. An example of an independent vector database is Pinecone and an example of vector search in the current database is pgvector on PostgreSQL.\n\nIndependent vector databases require that you maintain the embeddings independent of the original database. There could be some added benefits to this architecture. One should decide if these added benefits are worth the extra complexity and cost.\n\nAnother solution is to store the embeddings where your data already resides. This way, the complexity of the architecture is reduced, and you will not have extra compliance concerns. Last but not least, it seems to be a cost-effective solution. However, these solutions should be considered in terms of database queries per second (QPS).\n\nChoosing between these two categories, a new vector database or vector search in the current database, is a decision that depends on application-specific factors. Hopefully, this collaborative comparison table could help with your decision!\n\nPlease follow me on Medium or social media to keep in contact:\n\n[Twitter](https://twitter.com/navid_re) | [LinkedIn](https://www.linkedin.com/in/navidrezaei/) | [Medium](https://medium.com/@navidre)\n\n![Image 13](https://miro.medium.com/v2/da:true/resize:fit:0/5c50caa54067fd622d2f0fac18392213bf92f6e2fae89b691e62bceb40885e74)\n\nSign up to discover human stories that deepen your understanding of the world.\n------------------------------------------------------------------------------\n\nFree\n----\n\nDistraction-free reading. No ads.\n\nOrganize your knowledge with lists and highlights.\n\nTell your story. Find your audience.\n\nSign up for free\n\nMembership\n----------\n\nRead member-only stories\n\nSupport writers you read most\n\nEarn money for your writing\n\nListen to audio narrations\n\nRead offline with the Medium app\n\nTry for $5/month\n\n[AI](https://medium.com/tag/ai?source=post_page-----cb330e55fca--------------------------------)\n\n[Vector Database](https://medium.com/tag/vector-database?source=post_page-----cb330e55fca--------------------------------)\n\n[NLP](https://medium.com/tag/nlp?source=post_page-----cb330e55fca--------------------------------)\n\n[Computer Vision](https://medium.com/tag/computer-vision?source=post_page-----cb330e55fca--------------------------------)\n\n[Database](https://medium.com/tag/database?source=post_page-----cb330e55fca--------------------------------)\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fcb330e55fca&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&user=Navid+Rezaei&userId=a39f90dc9245&source=---footer_actions--cb330e55fca---------------------clap_footer-----------)\n\n\\--\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fcb330e55fca&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&user=Navid+Rezaei&userId=a39f90dc9245&source=---footer_actions--cb330e55fca---------------------clap_footer-----------)\n\n\\--\n\n12\n\n[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcb330e55fca&operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&source=---footer_actions--cb330e55fca---------------------bookmark_footer-----------)\n\n[![Image 14: Navid Rezaei](https://miro.medium.com/v2/resize:fill:96:96/1*_DALUa8EVjYpT12eSzFN-w.jpeg)](https://navidre.medium.com/?source=post_page---post_author_info--cb330e55fca--------------------------------)\n\n[![Image 15: Navid Rezaei](https://miro.medium.com/v2/resize:fill:128:128/1*_DALUa8EVjYpT12eSzFN-w.jpeg)](https://navidre.medium.com/?source=post_page---post_author_info--cb330e55fca--------------------------------)\n\nFollow\n\n[Written by Navid Rezaei -----------------------](https://navidre.medium.com/?source=post_page---post_author_info--cb330e55fca--------------------------------)\n\n[70 Followers](https://navidre.medium.com/followers?source=post_page---post_author_info--cb330e55fca--------------------------------)\n\n·[12 Following](https://navidre.medium.com/following?source=post_page---post_author_info--cb330e55fca--------------------------------)\n\nLinkedIn: [https://www.linkedin.com/in/navidrezaei/](https://www.linkedin.com/in/navidrezaei/) Twitter: [https://twitter.com/navid\\_re](https://twitter.com/navid_re)\n\nFollow\n\nResponses (12)\n--------------\n\n[](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page---post_responses--cb330e55fca--------------------------------)\n\n[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fnavidre.medium.com%2Fwhich-vector-database-should-i-use-a-comparison-cheatsheet-cb330e55fca&source=---post_responses--cb330e55fca---------------------respond_sidebar-----------)\n\nAlso publish to my profile\n\nRespond\n\nRespond\n\nSee all responses\n\n[Help](https://help.medium.com/hc/en-us?source=post_page-----cb330e55fca--------------------------------)\n\n[Status](https://medium.statuspage.io/?source=post_page-----cb330e55fca--------------------------------)\n\n[About](https://medium.com/about?autoplay=1&source=post_page-----cb330e55fca--------------------------------)\n\n[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----cb330e55fca--------------------------------)\n\n[Press](https://navidre.medium.com/pressinquiries@medium.com?source=post_page-----cb330e55fca--------------------------------)\n\n[Blog](https://blog.medium.com/?source=post_page-----cb330e55fca--------------------------------)\n\n[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----cb330e55fca--------------------------------)\n\n[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cb330e55fca--------------------------------)\n\n[Text to speech](https://speechify.com/medium?source=post_page-----cb330e55fca--------------------------------)\n\n[Teams](https://medium.com/business?source=post_page-----cb330e55fca--------------------------------)",
  "publishedTime": "2023-07-29T23:47:44.126Z",
  "usage": {
    "tokens": 3063
  }
}
```
