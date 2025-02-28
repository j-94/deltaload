---
title: L2MAC: Large Language Model Automatic Computer for Extensive Code Generation
description: Abstract page for arXiv paper 2310.02003: L2MAC: Large Language Model Automatic Computer for Extensive Code Generation
url: https://arxiv.org/abs/2310.02003
timestamp: 2025-01-20T15:49:26.640Z
domain: arxiv.org
path: abs_2310.02003
---

# L2MAC: Large Language Model Automatic Computer for Extensive Code Generation


Abstract page for arXiv paper 2310.02003: L2MAC: Large Language Model Automatic Computer for Extensive Code Generation


## Content

Skip to main content

In just 3 minutes help us improve arXiv:

Annual Global Survey
We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate
>
cs
>
arXiv:2310.02003

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
[Submitted on 2 Oct 2023 (v1), last revised 10 Apr 2024 (this version, v5)]
L2MAC: Large Language Model Automatic Computer for Extensive Code Generation
Samuel Holt, Max Ruiz Luyten, Mihaela van der Schaar
Transformer-based large language models (LLMs) are constrained by the fixed context window of the underlying transformer architecture, hindering their ability to produce long and coherent outputs. Memory-augmented LLMs are a promising solution, but current approaches cannot handle long output generation tasks since they (1) only focus on reading memory and reduce its evolution to the concatenation of new memories or (2) use very specialized memories that cannot adapt to other domains. This paper presents L2MAC, the first practical LLM-based general-purpose stored-program automatic computer (von Neumann architecture) framework, an LLM-based multi-agent system, for long and consistent output generation. Its memory has two components: the instruction registry, which is populated with a prompt program to solve the user-given task, and a file store, which will contain the final and intermediate outputs. Each instruction in turn is executed by a separate LLM agent, whose context is managed by a control unit capable of precise memory reading and writing to ensure effective interaction with the file store. These components enable L2MAC to generate extensive outputs, bypassing the constraints of the finite context window while producing outputs that fulfill a complex user-specified task. We empirically demonstrate that L2MAC achieves state-of-the-art performance in generating large codebases for system design tasks, significantly outperforming other coding methods in implementing the detailed user-specified task; we show that L2MAC works for general-purpose extensive text-based tasks, such as writing an entire book; and we provide valuable insights into L2MAC's performance improvement over existing methods.
Comments:	Published in The Twelfth International Conference on Learning Representations (ICLR), 2024. Copyright 2023 by the author(s)
Subjects:	Software Engineering (cs.SE); Artificial Intelligence (cs.AI); Machine Learning (cs.LG); Programming Languages (cs.PL)
ACM classes:	I.2.7; I.2.6; I.2.5; D.2.2; D.2.3; D.3.4
Cite as:	arXiv:2310.02003 [cs.SE]
 	(or arXiv:2310.02003v5 [cs.SE] for this version)
 	
https://doi.org/10.48550/arXiv.2310.02003
Focus to learn more
Submission history
From: Samuel Holt [view email]
[v1] Mon, 2 Oct 2023 16:55:19 UTC (4,216 KB)
[v2] Mon, 11 Dec 2023 06:55:32 UTC (7,468 KB)
[v3] Sat, 16 Mar 2024 01:42:40 UTC (7,823 KB)
[v4] Thu, 4 Apr 2024 01:53:27 UTC (7,904 KB)
[v5] Wed, 10 Apr 2024 13:38:30 UTC (7,916 KB)

Access Paper:
View PDF
HTML (experimental)
TeX Source
Other Formats
view license
Current browse context:
cs.SE
< prev   |   next >

new | recent | 2023-10
Change to browse by:
cs
cs.AI
cs.LG
cs.PL

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
  "title": "L2MAC: Large Language Model Automatic Computer for Extensive Code Generation",
  "description": "Abstract page for arXiv paper 2310.02003: L2MAC: Large Language Model Automatic Computer for Extensive Code Generation",
  "url": "https://arxiv.org/abs/2310.02003",
  "content": "Skip to main content\n\nIn just 3 minutes help us improve arXiv:\n\nAnnual Global Survey\nWe gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.\nDonate\n>\ncs\n>\narXiv:2310.02003\n\nHelp | Advanced Search\n\nAll fields\nTitle\nAuthor\nAbstract\nComments\nJournal reference\nACM classification\nMSC classification\nReport number\narXiv identifier\nDOI\nORCID\narXiv author ID\nHelp pages\nFull text\nSearch\nComputer Science > Software Engineering\n[Submitted on 2 Oct 2023 (v1), last revised 10 Apr 2024 (this version, v5)]\nL2MAC: Large Language Model Automatic Computer for Extensive Code Generation\nSamuel Holt, Max Ruiz Luyten, Mihaela van der Schaar\nTransformer-based large language models (LLMs) are constrained by the fixed context window of the underlying transformer architecture, hindering their ability to produce long and coherent outputs. Memory-augmented LLMs are a promising solution, but current approaches cannot handle long output generation tasks since they (1) only focus on reading memory and reduce its evolution to the concatenation of new memories or (2) use very specialized memories that cannot adapt to other domains. This paper presents L2MAC, the first practical LLM-based general-purpose stored-program automatic computer (von Neumann architecture) framework, an LLM-based multi-agent system, for long and consistent output generation. Its memory has two components: the instruction registry, which is populated with a prompt program to solve the user-given task, and a file store, which will contain the final and intermediate outputs. Each instruction in turn is executed by a separate LLM agent, whose context is managed by a control unit capable of precise memory reading and writing to ensure effective interaction with the file store. These components enable L2MAC to generate extensive outputs, bypassing the constraints of the finite context window while producing outputs that fulfill a complex user-specified task. We empirically demonstrate that L2MAC achieves state-of-the-art performance in generating large codebases for system design tasks, significantly outperforming other coding methods in implementing the detailed user-specified task; we show that L2MAC works for general-purpose extensive text-based tasks, such as writing an entire book; and we provide valuable insights into L2MAC's performance improvement over existing methods.\nComments:\tPublished in The Twelfth International Conference on Learning Representations (ICLR), 2024. Copyright 2023 by the author(s)\nSubjects:\tSoftware Engineering (cs.SE); Artificial Intelligence (cs.AI); Machine Learning (cs.LG); Programming Languages (cs.PL)\nACM classes:\tI.2.7; I.2.6; I.2.5; D.2.2; D.2.3; D.3.4\nCite as:\tarXiv:2310.02003 [cs.SE]\n \t(or arXiv:2310.02003v5 [cs.SE] for this version)\n \t\nhttps://doi.org/10.48550/arXiv.2310.02003\nFocus to learn more\nSubmission history\nFrom: Samuel Holt [view email]\n[v1] Mon, 2 Oct 2023 16:55:19 UTC (4,216 KB)\n[v2] Mon, 11 Dec 2023 06:55:32 UTC (7,468 KB)\n[v3] Sat, 16 Mar 2024 01:42:40 UTC (7,823 KB)\n[v4] Thu, 4 Apr 2024 01:53:27 UTC (7,904 KB)\n[v5] Wed, 10 Apr 2024 13:38:30 UTC (7,916 KB)\n\nAccess Paper:\nView PDF\nHTML (experimental)\nTeX Source\nOther Formats\nview license\nCurrent browse context:\ncs.SE\n< prev   |   next >\n\nnew | recent | 2023-10\nChange to browse by:\ncs\ncs.AI\ncs.LG\ncs.PL\n\nReferences & Citations\nNASA ADS\nGoogle Scholar\nSemantic Scholar\nExport BibTeX Citation\nBookmark\n \nBibliographic Tools\nBibliographic and Citation Tools\nBibliographic Explorer Toggle\nBibliographic Explorer (What is the Explorer?)\nConnected Papers Toggle\nConnected Papers (What is Connected Papers?)\nLitmaps Toggle\nLitmaps (What is Litmaps?)\nscite.ai Toggle\nscite Smart Citations (What are Smart Citations?)\nCode, Data, Media\nDemos\nRelated Papers\nAbout arXivLabs\nWhich authors of this paper are endorsers? | Disable MathJax (What is MathJax?)\nAbout\nHelp\nContact\nSubscribe\nCopyright\nPrivacy Policy\nWeb Accessibility Assistance\n\narXiv Operational Status \nGet status notifications via email or slack",
  "usage": {
    "tokens": 1011
  }
}
```
