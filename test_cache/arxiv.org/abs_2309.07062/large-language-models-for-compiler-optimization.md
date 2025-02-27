---
title: Large Language Models for Compiler Optimization
description: Abstract page for arXiv paper 2309.07062: Large Language Models for Compiler Optimization
url: https://arxiv.org/abs/2309.07062
timestamp: 2025-01-20T15:46:01.021Z
domain: arxiv.org
path: abs_2309.07062
---

# Large Language Models for Compiler Optimization


Abstract page for arXiv paper 2309.07062: Large Language Models for Compiler Optimization


## Content

Skip to main content

In just 3 minutes help us improve arXiv:

Annual Global Survey
We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate
>
cs
>
arXiv:2309.07062

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
Computer Science > Programming Languages
[Submitted on 11 Sep 2023]
Large Language Models for Compiler Optimization
Chris Cummins, Volker Seeker, Dejan Grubisic, Mostafa Elhoushi, Youwei Liang, Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Kim Hazelwood, Gabriel Synnaeve, Hugh Leather
We explore the novel application of Large Language Models to code optimization. We present a 7B-parameter transformer model trained from scratch to optimize LLVM assembly for code size. The model takes as input unoptimized assembly and outputs a list of compiler options to best optimize the program. Crucially, during training, we ask the model to predict the instruction counts before and after optimization, and the optimized code itself. These auxiliary learning tasks significantly improve the optimization performance of the model and improve the model's depth of understanding.
We evaluate on a large suite of test programs. Our approach achieves a 3.0% improvement in reducing instruction counts over the compiler, outperforming two state-of-the-art baselines that require thousands of compilations. Furthermore, the model shows surprisingly strong code reasoning abilities, generating compilable code 91% of the time and perfectly emulating the output of the compiler 70% of the time.
Subjects:	Programming Languages (cs.PL); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)
Cite as:	arXiv:2309.07062 [cs.PL]
 	(or arXiv:2309.07062v1 [cs.PL] for this version)
 	
https://doi.org/10.48550/arXiv.2309.07062
Focus to learn more
Submission history
From: Chris Cummins [view email]
[v1] Mon, 11 Sep 2023 22:11:46 UTC (4,757 KB)

Access Paper:
View PDF
TeX Source
Other Formats
view license
Current browse context:
cs.PL
< prev   |   next >

new | recent | 2023-09
Change to browse by:
cs
cs.AI
cs.CL
cs.LG

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
  "title": "Large Language Models for Compiler Optimization",
  "description": "Abstract page for arXiv paper 2309.07062: Large Language Models for Compiler Optimization",
  "url": "https://arxiv.org/abs/2309.07062",
  "content": "Skip to main content\n\nIn just 3 minutes help us improve arXiv:\n\nAnnual Global Survey\nWe gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.\nDonate\n>\ncs\n>\narXiv:2309.07062\n\nHelp | Advanced Search\n\nAll fields\nTitle\nAuthor\nAbstract\nComments\nJournal reference\nACM classification\nMSC classification\nReport number\narXiv identifier\nDOI\nORCID\narXiv author ID\nHelp pages\nFull text\nSearch\nComputer Science > Programming Languages\n[Submitted on 11 Sep 2023]\nLarge Language Models for Compiler Optimization\nChris Cummins, Volker Seeker, Dejan Grubisic, Mostafa Elhoushi, Youwei Liang, Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Kim Hazelwood, Gabriel Synnaeve, Hugh Leather\nWe explore the novel application of Large Language Models to code optimization. We present a 7B-parameter transformer model trained from scratch to optimize LLVM assembly for code size. The model takes as input unoptimized assembly and outputs a list of compiler options to best optimize the program. Crucially, during training, we ask the model to predict the instruction counts before and after optimization, and the optimized code itself. These auxiliary learning tasks significantly improve the optimization performance of the model and improve the model's depth of understanding.\nWe evaluate on a large suite of test programs. Our approach achieves a 3.0% improvement in reducing instruction counts over the compiler, outperforming two state-of-the-art baselines that require thousands of compilations. Furthermore, the model shows surprisingly strong code reasoning abilities, generating compilable code 91% of the time and perfectly emulating the output of the compiler 70% of the time.\nSubjects:\tProgramming Languages (cs.PL); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Machine Learning (cs.LG)\nCite as:\tarXiv:2309.07062 [cs.PL]\n \t(or arXiv:2309.07062v1 [cs.PL] for this version)\n \t\nhttps://doi.org/10.48550/arXiv.2309.07062\nFocus to learn more\nSubmission history\nFrom: Chris Cummins [view email]\n[v1] Mon, 11 Sep 2023 22:11:46 UTC (4,757 KB)\n\nAccess Paper:\nView PDF\nTeX Source\nOther Formats\nview license\nCurrent browse context:\ncs.PL\n< prev   |   next >\n\nnew | recent | 2023-09\nChange to browse by:\ncs\ncs.AI\ncs.CL\ncs.LG\n\nReferences & Citations\nNASA ADS\nGoogle Scholar\nSemantic Scholar\nExport BibTeX Citation\nBookmark\n \nBibliographic Tools\nBibliographic and Citation Tools\nBibliographic Explorer Toggle\nBibliographic Explorer (What is the Explorer?)\nConnected Papers Toggle\nConnected Papers (What is Connected Papers?)\nLitmaps Toggle\nLitmaps (What is Litmaps?)\nscite.ai Toggle\nscite Smart Citations (What are Smart Citations?)\nCode, Data, Media\nDemos\nRelated Papers\nAbout arXivLabs\nWhich authors of this paper are endorsers? | Disable MathJax (What is MathJax?)\nAbout\nHelp\nContact\nSubscribe\nCopyright\nPrivacy Policy\nWeb Accessibility Assistance\n\narXiv Operational Status \nGet status notifications via email or slack",
  "usage": {
    "tokens": 720
  }
}
```
