---
title: Hot or Cold? Adaptive Temperature Sampling for Code Generation with Large Language Models
description: Abstract page for arXiv paper 2309.02772: Hot or Cold? Adaptive Temperature Sampling for Code Generation with Large Language Models
url: https://arxiv.org/abs/2309.02772
timestamp: 2025-01-20T15:46:03.579Z
domain: arxiv.org
path: abs_2309.02772
---

# Hot or Cold? Adaptive Temperature Sampling for Code Generation with Large Language Models


Abstract page for arXiv paper 2309.02772: Hot or Cold? Adaptive Temperature Sampling for Code Generation with Large Language Models


## Content

Skip to main content

In just 3 minutes help us improve arXiv:

Annual Global Survey
We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate
>
cs
>
arXiv:2309.02772

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
Computer Science > Software Engineering
[Submitted on 6 Sep 2023 (v1), last revised 28 Dec 2023 (this version, v3)]
Hot or Cold? Adaptive Temperature Sampling for Code Generation with Large Language Models
Yuqi Zhu, Jia Li, Ge Li, YunFei Zhao, Jia Li, Zhi Jin, Hong Mei
Recently, Large Language Models (LLMs) have shown impressive abilities in code generation. However, existing LLMs' decoding strategies are designed for Natural Language (NL) generation, overlooking the differences between NL and programming languages (PL). Due to this oversight, a better decoding strategy for code generation remains an open question. In this paper, we conduct the first systematic study to explore a decoding strategy specialized in code generation. With an analysis of loss distributions of code tokens, we find that code tokens can be divided into two categories: challenging tokens that are difficult to predict and confident tokens that can be easily inferred. Among them, the challenging tokens mainly appear at the beginning of a code block. Inspired by the above findings, we propose a simple yet effective method: Adaptive Temperature (AdapT) sampling, which dynamically adjusts the temperature coefficient when decoding different tokens. We apply a larger temperature when sampling for challenging tokens, allowing LLMs to explore diverse choices. We employ a smaller temperature for confident tokens avoiding the influence of tail randomness noises. We apply AdapT sampling to LLMs with different sizes and conduct evaluations on two popular datasets. Results show that AdapT sampling significantly outperforms state-of-the-art decoding strategy.
Comments:	This paper is accepted by AAAI 2024
Subjects:	Software Engineering (cs.SE); Computation and Language (cs.CL)
Cite as:	arXiv:2309.02772 [cs.SE]
 	(or arXiv:2309.02772v3 [cs.SE] for this version)
 	
https://doi.org/10.48550/arXiv.2309.02772
Focus to learn more
Submission history
From: Yuqi Zhu [view email]
[v1] Wed, 6 Sep 2023 06:27:33 UTC (5,076 KB)
[v2] Sat, 14 Oct 2023 09:27:51 UTC (5,076 KB)
[v3] Thu, 28 Dec 2023 10:54:36 UTC (7,687 KB)

Access Paper:
View PDF
HTML (experimental)
TeX Source
Other Formats
view license
Current browse context:
cs.SE
< prev   |   next >

new | recent | 2023-09
Change to browse by:
cs
cs.CL

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
  "title": "Hot or Cold? Adaptive Temperature Sampling for Code Generation with Large Language Models",
  "description": "Abstract page for arXiv paper 2309.02772: Hot or Cold? Adaptive Temperature Sampling for Code Generation with Large Language Models",
  "url": "https://arxiv.org/abs/2309.02772",
  "content": "Skip to main content\n\nIn just 3 minutes help us improve arXiv:\n\nAnnual Global Survey\nWe gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.\nDonate\n>\ncs\n>\narXiv:2309.02772\n\nHelp | Advanced Search\n\nAll fields\nTitle\nAuthor\nAbstract\nComments\nJournal reference\nACM classification\nMSC classification\nReport number\narXiv identifier\nDOI\nORCID\narXiv author ID\nHelp pages\nFull text\nSearch\nComputer Science > Software Engineering\n[Submitted on 6 Sep 2023 (v1), last revised 28 Dec 2023 (this version, v3)]\nHot or Cold? Adaptive Temperature Sampling for Code Generation with Large Language Models\nYuqi Zhu, Jia Li, Ge Li, YunFei Zhao, Jia Li, Zhi Jin, Hong Mei\nRecently, Large Language Models (LLMs) have shown impressive abilities in code generation. However, existing LLMs' decoding strategies are designed for Natural Language (NL) generation, overlooking the differences between NL and programming languages (PL). Due to this oversight, a better decoding strategy for code generation remains an open question. In this paper, we conduct the first systematic study to explore a decoding strategy specialized in code generation. With an analysis of loss distributions of code tokens, we find that code tokens can be divided into two categories: challenging tokens that are difficult to predict and confident tokens that can be easily inferred. Among them, the challenging tokens mainly appear at the beginning of a code block. Inspired by the above findings, we propose a simple yet effective method: Adaptive Temperature (AdapT) sampling, which dynamically adjusts the temperature coefficient when decoding different tokens. We apply a larger temperature when sampling for challenging tokens, allowing LLMs to explore diverse choices. We employ a smaller temperature for confident tokens avoiding the influence of tail randomness noises. We apply AdapT sampling to LLMs with different sizes and conduct evaluations on two popular datasets. Results show that AdapT sampling significantly outperforms state-of-the-art decoding strategy.\nComments:\tThis paper is accepted by AAAI 2024\nSubjects:\tSoftware Engineering (cs.SE); Computation and Language (cs.CL)\nCite as:\tarXiv:2309.02772 [cs.SE]\n \t(or arXiv:2309.02772v3 [cs.SE] for this version)\n \t\nhttps://doi.org/10.48550/arXiv.2309.02772\nFocus to learn more\nSubmission history\nFrom: Yuqi Zhu [view email]\n[v1] Wed, 6 Sep 2023 06:27:33 UTC (5,076 KB)\n[v2] Sat, 14 Oct 2023 09:27:51 UTC (5,076 KB)\n[v3] Thu, 28 Dec 2023 10:54:36 UTC (7,687 KB)\n\nAccess Paper:\nView PDF\nHTML (experimental)\nTeX Source\nOther Formats\nview license\nCurrent browse context:\ncs.SE\n< prev   |   next >\n\nnew | recent | 2023-09\nChange to browse by:\ncs\ncs.CL\n\nReferences & Citations\nNASA ADS\nGoogle Scholar\nSemantic Scholar\nExport BibTeX Citation\nBookmark\n \nBibliographic Tools\nBibliographic and Citation Tools\nBibliographic Explorer Toggle\nBibliographic Explorer (What is the Explorer?)\nConnected Papers Toggle\nConnected Papers (What is Connected Papers?)\nLitmaps Toggle\nLitmaps (What is Litmaps?)\nscite.ai Toggle\nscite Smart Citations (What are Smart Citations?)\nCode, Data, Media\nDemos\nRelated Papers\nAbout arXivLabs\nWhich authors of this paper are endorsers? | Disable MathJax (What is MathJax?)\nAbout\nHelp\nContact\nSubscribe\nCopyright\nPrivacy Policy\nWeb Accessibility Assistance\n\narXiv Operational Status \nGet status notifications via email or slack",
  "usage": {
    "tokens": 825
  }
}
```
