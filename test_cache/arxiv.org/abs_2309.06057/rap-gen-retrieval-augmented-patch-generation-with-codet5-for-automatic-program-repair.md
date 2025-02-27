---
title: RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 for Automatic Program Repair
description: Abstract page for arXiv paper 2309.06057: RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 for Automatic Program Repair
url: https://arxiv.org/abs/2309.06057
timestamp: 2025-01-20T15:46:05.036Z
domain: arxiv.org
path: abs_2309.06057
---

# RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 for Automatic Program Repair


Abstract page for arXiv paper 2309.06057: RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 for Automatic Program Repair


## Content

Skip to main content

In just 3 minutes help us improve arXiv:

Annual Global Survey
We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate
>
cs
>
arXiv:2309.06057

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
[Submitted on 12 Sep 2023]
RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 for Automatic Program Repair
Weishi Wang, Yue Wang, Shafiq Joty, Steven C.H. Hoi
Automatic program repair (APR) is crucial to reduce manual debugging efforts for developers and improve software reliability. While conventional search-based techniques typically rely on heuristic rules or a redundancy assumption to mine fix patterns, recent years have witnessed the surge of deep learning (DL) based approaches to automate the program repair process in a data-driven manner. However, their performance is often limited by a fixed set of parameters to model the highly complex search space of APR. To ease such burden on the parametric models, in this work, we propose a novel Retrieval-Augmented Patch Generation framework (RAP-Gen) by explicitly leveraging relevant fix patterns retrieved from a codebase of previous bug-fix pairs. Specifically, we build a hybrid patch retriever to account for both lexical and semantic matching based on the raw source code in a language-agnostic manner, which does not rely on any code-specific features. In addition, we adapt a code-aware language model CodeT5 as our foundation model to facilitate both patch retrieval and generation tasks in a unified manner. We adopt a stage-wise approach where the patch retriever first retrieves a relevant external bug-fix pair to augment the buggy input for the CodeT5 patch generator, which synthesizes a ranked list of repair patch candidates. Notably, RAP-Gen is a generic APR framework that can flexibly integrate different patch retrievers and generators to repair various types of bugs. We thoroughly evaluate RAP-Gen on three benchmarks in two programming languages, including the TFix benchmark in JavaScript, and Code Refinement and Defects4J benchmarks in Java, where the bug localization information may or may not be provided. Experimental results show that RAP-Gen significantly outperforms previous state-of-the-art approaches on all benchmarks, e.g., repairing 15 more bugs on 818 Defects4J bugs.
Comments:	FSE 2023, Long paper
Subjects:	Software Engineering (cs.SE); Computation and Language (cs.CL)
Cite as:	arXiv:2309.06057 [cs.SE]
 	(or arXiv:2309.06057v1 [cs.SE] for this version)
 	
https://doi.org/10.48550/arXiv.2309.06057
Focus to learn more
Submission history
From: Yue Wang [view email]
[v1] Tue, 12 Sep 2023 08:52:56 UTC (1,045 KB)

Access Paper:
View PDF
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
  "title": "RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 for Automatic Program Repair",
  "description": "Abstract page for arXiv paper 2309.06057: RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 for Automatic Program Repair",
  "url": "https://arxiv.org/abs/2309.06057",
  "content": "Skip to main content\n\nIn just 3 minutes help us improve arXiv:\n\nAnnual Global Survey\nWe gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.\nDonate\n>\ncs\n>\narXiv:2309.06057\n\nHelp | Advanced Search\n\nAll fields\nTitle\nAuthor\nAbstract\nComments\nJournal reference\nACM classification\nMSC classification\nReport number\narXiv identifier\nDOI\nORCID\narXiv author ID\nHelp pages\nFull text\nSearch\nComputer Science > Software Engineering\n[Submitted on 12 Sep 2023]\nRAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 for Automatic Program Repair\nWeishi Wang, Yue Wang, Shafiq Joty, Steven C.H. Hoi\nAutomatic program repair (APR) is crucial to reduce manual debugging efforts for developers and improve software reliability. While conventional search-based techniques typically rely on heuristic rules or a redundancy assumption to mine fix patterns, recent years have witnessed the surge of deep learning (DL) based approaches to automate the program repair process in a data-driven manner. However, their performance is often limited by a fixed set of parameters to model the highly complex search space of APR. To ease such burden on the parametric models, in this work, we propose a novel Retrieval-Augmented Patch Generation framework (RAP-Gen) by explicitly leveraging relevant fix patterns retrieved from a codebase of previous bug-fix pairs. Specifically, we build a hybrid patch retriever to account for both lexical and semantic matching based on the raw source code in a language-agnostic manner, which does not rely on any code-specific features. In addition, we adapt a code-aware language model CodeT5 as our foundation model to facilitate both patch retrieval and generation tasks in a unified manner. We adopt a stage-wise approach where the patch retriever first retrieves a relevant external bug-fix pair to augment the buggy input for the CodeT5 patch generator, which synthesizes a ranked list of repair patch candidates. Notably, RAP-Gen is a generic APR framework that can flexibly integrate different patch retrievers and generators to repair various types of bugs. We thoroughly evaluate RAP-Gen on three benchmarks in two programming languages, including the TFix benchmark in JavaScript, and Code Refinement and Defects4J benchmarks in Java, where the bug localization information may or may not be provided. Experimental results show that RAP-Gen significantly outperforms previous state-of-the-art approaches on all benchmarks, e.g., repairing 15 more bugs on 818 Defects4J bugs.\nComments:\tFSE 2023, Long paper\nSubjects:\tSoftware Engineering (cs.SE); Computation and Language (cs.CL)\nCite as:\tarXiv:2309.06057 [cs.SE]\n \t(or arXiv:2309.06057v1 [cs.SE] for this version)\n \t\nhttps://doi.org/10.48550/arXiv.2309.06057\nFocus to learn more\nSubmission history\nFrom: Yue Wang [view email]\n[v1] Tue, 12 Sep 2023 08:52:56 UTC (1,045 KB)\n\nAccess Paper:\nView PDF\nTeX Source\nOther Formats\nview license\nCurrent browse context:\ncs.SE\n< prev   |   next >\n\nnew | recent | 2023-09\nChange to browse by:\ncs\ncs.CL\n\nReferences & Citations\nNASA ADS\nGoogle Scholar\nSemantic Scholar\nExport BibTeX Citation\nBookmark\n \nBibliographic Tools\nBibliographic and Citation Tools\nBibliographic Explorer Toggle\nBibliographic Explorer (What is the Explorer?)\nConnected Papers Toggle\nConnected Papers (What is Connected Papers?)\nLitmaps Toggle\nLitmaps (What is Litmaps?)\nscite.ai Toggle\nscite Smart Citations (What are Smart Citations?)\nCode, Data, Media\nDemos\nRelated Papers\nAbout arXivLabs\nWhich authors of this paper are endorsers? | Disable MathJax (What is MathJax?)\nAbout\nHelp\nContact\nSubscribe\nCopyright\nPrivacy Policy\nWeb Accessibility Assistance\n\narXiv Operational Status \nGet status notifications via email or slack",
  "usage": {
    "tokens": 871
  }
}
```
