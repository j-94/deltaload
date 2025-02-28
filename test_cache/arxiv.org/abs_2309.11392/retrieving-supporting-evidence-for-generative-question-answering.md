---
title: Retrieving Supporting Evidence for Generative Question Answering
description: Abstract page for arXiv paper 2309.11392: Retrieving Supporting Evidence for Generative Question Answering
url: https://arxiv.org/abs/2309.11392
timestamp: 2025-01-20T15:49:29.142Z
domain: arxiv.org
path: abs_2309.11392
---

# Retrieving Supporting Evidence for Generative Question Answering


Abstract page for arXiv paper 2309.11392: Retrieving Supporting Evidence for Generative Question Answering


## Content

Skip to main content

In just 3 minutes help us improve arXiv:

Annual Global Survey
We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate
>
cs
>
arXiv:2309.11392

Help | Advanced Search

All fields
Title
Author
Abstract
Comments
Journal reference
ACM classification
MSC classification
Report number
arXiv identifier
DOI
ORCID
arXiv author ID
Help pages
Full text
Search
Computer Science > Information Retrieval
[Submitted on 20 Sep 2023]
Retrieving Supporting Evidence for Generative Question Answering
Siqing Huo, Negar Arabzadeh, Charles L. A. Clarke
Current large language models (LLMs) can exhibit near-human levels of performance on many natural language-based tasks, including open-domain question answering. Unfortunately, at this time, they also convincingly hallucinate incorrect answers, so that responses to questions must be verified against external sources before they can be accepted at face value. In this paper, we report two simple experiments to automatically validate generated answers against a corpus. We base our experiments on questions and passages from the MS MARCO (V1) test collection, and a retrieval pipeline consisting of sparse retrieval, dense retrieval and neural rerankers. In the first experiment, we validate the generated answer in its entirety. After presenting a question to an LLM and receiving a generated answer, we query the corpus with the combination of the question + generated answer. We then present the LLM with the combination of the question + generated answer + retrieved answer, prompting it to indicate if the generated answer can be supported by the retrieved answer. In the second experiment, we consider the generated answer at a more granular level, prompting the LLM to extract a list of factual statements from the answer and verifying each statement separately. We query the corpus with each factual statement and then present the LLM with the statement and the corresponding retrieved evidence. The LLM is prompted to indicate if the statement can be supported and make necessary edits using the retrieved material. With an accuracy of over 80%, we find that an LLM is capable of verifying its generated answer when a corpus of supporting material is provided. However, manual assessment of a random sample of questions reveals that incorrect generated answers are missed by this verification process. While this verification process can reduce hallucinations, it can not entirely eliminate them.
Comments:	arXiv admin note: text overlap with arXiv:2306.13781
Subjects:	Information Retrieval (cs.IR)
Cite as:	arXiv:2309.11392 [cs.IR]
 	(or arXiv:2309.11392v1 [cs.IR] for this version)
 	
https://doi.org/10.48550/arXiv.2309.11392
Focus to learn more

Journal reference:	Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region (SIGIR-AP '23), November 26--28, 2023, Beijing, China
Related DOI:	
https://doi.org/10.1145/3624918.3625336
Focus to learn more
Submission history
From: Siqing Huo [view email]
[v1] Wed, 20 Sep 2023 15:16:42 UTC (608 KB)

Access Paper:
View PDF
TeX Source
Other Formats
view license
Current browse context:
cs.IR
< prev   |   next >

new | recent | 2023-09
Change to browse by:
cs

References & Citations
NASA ADS
Google Scholar
Semantic Scholar
Export BibTeX Citation
Bookmark
 
Bibliographic Tools
Bibliographic and Citation Tools
Bibliographic Explorer Toggle
Bibliographic Explorer (What is the Explorer?)
Connected Papers Toggle
Connected Papers (What is Connected Papers?)
Litmaps Toggle
Litmaps (What is Litmaps?)
scite.ai Toggle
scite Smart Citations (What are Smart Citations?)
Code, Data, Media
Demos
Related Papers
About arXivLabs
Which authors of this paper are endorsers? | Disable MathJax (What is MathJax?)
About
Help
Contact
Subscribe
Copyright
Privacy Policy
Web Accessibility Assistance

arXiv Operational Status 
Get status notifications via email or slack

## Metadata

```json
{
  "title": "Retrieving Supporting Evidence for Generative Question Answering",
  "description": "Abstract page for arXiv paper 2309.11392: Retrieving Supporting Evidence for Generative Question Answering",
  "url": "https://arxiv.org/abs/2309.11392",
  "content": "Skip to main content\n\nIn just 3 minutes help us improve arXiv:\n\nAnnual Global Survey\nWe gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.\nDonate\n>\ncs\n>\narXiv:2309.11392\n\nHelp | Advanced Search\n\nAll fields\nTitle\nAuthor\nAbstract\nComments\nJournal reference\nACM classification\nMSC classification\nReport number\narXiv identifier\nDOI\nORCID\narXiv author ID\nHelp pages\nFull text\nSearch\nComputer Science > Information Retrieval\n[Submitted on 20 Sep 2023]\nRetrieving Supporting Evidence for Generative Question Answering\nSiqing Huo, Negar Arabzadeh, Charles L. A. Clarke\nCurrent large language models (LLMs) can exhibit near-human levels of performance on many natural language-based tasks, including open-domain question answering. Unfortunately, at this time, they also convincingly hallucinate incorrect answers, so that responses to questions must be verified against external sources before they can be accepted at face value. In this paper, we report two simple experiments to automatically validate generated answers against a corpus. We base our experiments on questions and passages from the MS MARCO (V1) test collection, and a retrieval pipeline consisting of sparse retrieval, dense retrieval and neural rerankers. In the first experiment, we validate the generated answer in its entirety. After presenting a question to an LLM and receiving a generated answer, we query the corpus with the combination of the question + generated answer. We then present the LLM with the combination of the question + generated answer + retrieved answer, prompting it to indicate if the generated answer can be supported by the retrieved answer. In the second experiment, we consider the generated answer at a more granular level, prompting the LLM to extract a list of factual statements from the answer and verifying each statement separately. We query the corpus with each factual statement and then present the LLM with the statement and the corresponding retrieved evidence. The LLM is prompted to indicate if the statement can be supported and make necessary edits using the retrieved material. With an accuracy of over 80%, we find that an LLM is capable of verifying its generated answer when a corpus of supporting material is provided. However, manual assessment of a random sample of questions reveals that incorrect generated answers are missed by this verification process. While this verification process can reduce hallucinations, it can not entirely eliminate them.\nComments:\tarXiv admin note: text overlap with arXiv:2306.13781\nSubjects:\tInformation Retrieval (cs.IR)\nCite as:\tarXiv:2309.11392 [cs.IR]\n \t(or arXiv:2309.11392v1 [cs.IR] for this version)\n \t\nhttps://doi.org/10.48550/arXiv.2309.11392\nFocus to learn more\n\nJournal reference:\tAnnual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region (SIGIR-AP '23), November 26--28, 2023, Beijing, China\nRelated DOI:\t\nhttps://doi.org/10.1145/3624918.3625336\nFocus to learn more\nSubmission history\nFrom: Siqing Huo [view email]\n[v1] Wed, 20 Sep 2023 15:16:42 UTC (608 KB)\n\nAccess Paper:\nView PDF\nTeX Source\nOther Formats\nview license\nCurrent browse context:\ncs.IR\n< prev   |   next >\n\nnew | recent | 2023-09\nChange to browse by:\ncs\n\nReferences & Citations\nNASA ADS\nGoogle Scholar\nSemantic Scholar\nExport BibTeX Citation\nBookmark\n \nBibliographic Tools\nBibliographic and Citation Tools\nBibliographic Explorer Toggle\nBibliographic Explorer (What is the Explorer?)\nConnected Papers Toggle\nConnected Papers (What is Connected Papers?)\nLitmaps Toggle\nLitmaps (What is Litmaps?)\nscite.ai Toggle\nscite Smart Citations (What are Smart Citations?)\nCode, Data, Media\nDemos\nRelated Papers\nAbout arXivLabs\nWhich authors of this paper are endorsers? | Disable MathJax (What is MathJax?)\nAbout\nHelp\nContact\nSubscribe\nCopyright\nPrivacy Policy\nWeb Accessibility Assistance\n\narXiv Operational Status \nGet status notifications via email or slack",
  "usage": {
    "tokens": 916
  }
}
```
