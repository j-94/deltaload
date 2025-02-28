---
title: Attention Sorting Combats Recency Bias In Long Context Language Models
description: Abstract page for arXiv paper 2310.01427: Attention Sorting Combats Recency Bias In Long Context Language Models
url: https://arxiv.org/abs/2310.01427
timestamp: 2025-01-20T15:46:20.906Z
domain: arxiv.org
path: abs_2310.01427
---

# Attention Sorting Combats Recency Bias In Long Context Language Models


Abstract page for arXiv paper 2310.01427: Attention Sorting Combats Recency Bias In Long Context Language Models


## Content

Skip to main content

In just 3 minutes help us improve arXiv:

Annual Global Survey
We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate
>
cs
>
arXiv:2310.01427

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
Computer Science > Computation and Language
[Submitted on 28 Sep 2023]
Attention Sorting Combats Recency Bias In Long Context Language Models
Alexander Peysakhovich, Adam Lerer
Current language models often fail to incorporate long contexts efficiently during generation. We show that a major contributor to this issue are attention priors that are likely learned during pre-training: relevant information located earlier in context is attended to less on average. Yet even when models fail to use the information from a relevant document in their response, they still pay preferential attention to that document compared to an irrelevant document at the same position. We leverage this fact to introduce ``attention sorting'': perform one step of decoding, sort documents by the attention they receive (highest attention going last), repeat the process, generate the answer with the newly sorted context. We find that attention sorting improves performance of long context models. Our findings highlight some challenges in using off-the-shelf language models for retrieval augmented generation.
Subjects:	Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
Cite as:	arXiv:2310.01427 [cs.CL]
 	(or arXiv:2310.01427v1 [cs.CL] for this version)
 	
https://doi.org/10.48550/arXiv.2310.01427
Focus to learn more
Submission history
From: Alexander Peysakhovich [view email]
[v1] Thu, 28 Sep 2023 05:19:06 UTC (463 KB)

Access Paper:
View PDF
TeX Source
Other Formats
view license
Current browse context:
cs.CL
< prev   |   next >

new | recent | 2023-10
Change to browse by:
cs
cs.AI

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
  "title": "Attention Sorting Combats Recency Bias In Long Context Language Models",
  "description": "Abstract page for arXiv paper 2310.01427: Attention Sorting Combats Recency Bias In Long Context Language Models",
  "url": "https://arxiv.org/abs/2310.01427",
  "content": "Skip to main content\n\nIn just 3 minutes help us improve arXiv:\n\nAnnual Global Survey\nWe gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.\nDonate\n>\ncs\n>\narXiv:2310.01427\n\nHelp | Advanced Search\n\nAll fields\nTitle\nAuthor\nAbstract\nComments\nJournal reference\nACM classification\nMSC classification\nReport number\narXiv identifier\nDOI\nORCID\narXiv author ID\nHelp pages\nFull text\nSearch\nComputer Science > Computation and Language\n[Submitted on 28 Sep 2023]\nAttention Sorting Combats Recency Bias In Long Context Language Models\nAlexander Peysakhovich, Adam Lerer\nCurrent language models often fail to incorporate long contexts efficiently during generation. We show that a major contributor to this issue are attention priors that are likely learned during pre-training: relevant information located earlier in context is attended to less on average. Yet even when models fail to use the information from a relevant document in their response, they still pay preferential attention to that document compared to an irrelevant document at the same position. We leverage this fact to introduce ``attention sorting'': perform one step of decoding, sort documents by the attention they receive (highest attention going last), repeat the process, generate the answer with the newly sorted context. We find that attention sorting improves performance of long context models. Our findings highlight some challenges in using off-the-shelf language models for retrieval augmented generation.\nSubjects:\tComputation and Language (cs.CL); Artificial Intelligence (cs.AI)\nCite as:\tarXiv:2310.01427 [cs.CL]\n \t(or arXiv:2310.01427v1 [cs.CL] for this version)\n \t\nhttps://doi.org/10.48550/arXiv.2310.01427\nFocus to learn more\nSubmission history\nFrom: Alexander Peysakhovich [view email]\n[v1] Thu, 28 Sep 2023 05:19:06 UTC (463 KB)\n\nAccess Paper:\nView PDF\nTeX Source\nOther Formats\nview license\nCurrent browse context:\ncs.CL\n< prev   |   next >\n\nnew | recent | 2023-10\nChange to browse by:\ncs\ncs.AI\n\nReferences & Citations\nNASA ADS\nGoogle Scholar\nSemantic Scholar\nExport BibTeX Citation\nBookmark\n \nBibliographic Tools\nBibliographic and Citation Tools\nBibliographic Explorer Toggle\nBibliographic Explorer (What is the Explorer?)\nConnected Papers Toggle\nConnected Papers (What is Connected Papers?)\nLitmaps Toggle\nLitmaps (What is Litmaps?)\nscite.ai Toggle\nscite Smart Citations (What are Smart Citations?)\nCode, Data, Media\nDemos\nRelated Papers\nAbout arXivLabs\nWhich authors of this paper are endorsers? | Disable MathJax (What is MathJax?)\nAbout\nHelp\nContact\nSubscribe\nCopyright\nPrivacy Policy\nWeb Accessibility Assistance\n\narXiv Operational Status \nGet status notifications via email or slack",
  "usage": {
    "tokens": 634
  }
}
```
