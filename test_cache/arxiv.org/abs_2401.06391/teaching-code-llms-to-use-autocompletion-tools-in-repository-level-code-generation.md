---
title: Teaching Code LLMs to Use Autocompletion Tools in Repository-Level Code Generation
description: Abstract page for arXiv paper 2401.06391: Teaching Code LLMs to Use Autocompletion Tools in Repository-Level Code Generation
url: https://arxiv.org/abs/2401.06391
timestamp: 2025-01-20T15:59:06.837Z
domain: arxiv.org
path: abs_2401.06391
---

# Teaching Code LLMs to Use Autocompletion Tools in Repository-Level Code Generation


Abstract page for arXiv paper 2401.06391: Teaching Code LLMs to Use Autocompletion Tools in Repository-Level Code Generation


## Content

Skip to main content

In just 3 minutes help us improve arXiv:

Annual Global Survey
We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate
>
cs
>
arXiv:2401.06391

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
[Submitted on 12 Jan 2024 (v1), last revised 18 Jul 2024 (this version, v3)]
Teaching Code LLMs to Use Autocompletion Tools in Repository-Level Code Generation
Chong Wang, Jian Zhang, Yebo Feng, Tianlin Li, Weisong Sun, Yang Liu, Xin Peng
Code large language models (LLMs) face limitations in repository-level code generation due to their lack of awareness of repository-level dependencies (e.g., user-defined attributes), resulting in dependency errors such as undefined-variable and no-member errors. In this work, we introduce ToolGen, an approach that integrates autocompletion tools into the code LLM generation process to address these dependencies. ToolGen comprises two main phases: Trigger Insertion and Model Fine-tuning (Offline), and Tool-integrated Code Generation (Online). During the offline phase, ToolGen augments functions within a given code corpus with a special mark token, indicating positions to trigger autocompletion tools. These augmented functions, along with their corresponding docstrings, are then used to fine-tune a selected code LLM. In the online phase, ToolGen iteratively generates functions by predicting tokens step-by-step using the fine-tuned LLM. Whenever a mark token is encountered, ToolGen invokes the autocompletion tool to suggest code completions and selects the most appropriate one.
We conduct comprehensive experiments to evaluate ToolGen's effectiveness in repository-level code generation. To facilitate this evaluation, we create a benchmark comprising 671 real-world code repositories and introduce two new dependency-based metrics: Dependency Coverage and Static Validity Rate. The results demonstrate that ToolGen significantly improves Dependency Coverage by 31.4% to 39.1% and Static Validity Rate by 44.9% to 57.7% across the three LLMs, while maintaining competitive or improved performance in widely recognized similarity metrics such as BLEU-4, CodeBLEU, Edit Similarity, and Exact Match. On the CoderEval dataset, ToolGen achieves improvements of 40.0% and 25.0% in Pass@1 for CodeT5 and CodeLlama, respectively.
Subjects:	Software Engineering (cs.SE)
Cite as:	arXiv:2401.06391 [cs.SE]
 	(or arXiv:2401.06391v3 [cs.SE] for this version)
 	
https://doi.org/10.48550/arXiv.2401.06391
Focus to learn more
Submission history
From: Chong Wang [view email]
[v1] Fri, 12 Jan 2024 06:03:56 UTC (1,137 KB)
[v2] Sun, 21 Jan 2024 08:41:09 UTC (1,026 KB)
[v3] Thu, 18 Jul 2024 07:04:38 UTC (2,162 KB)

Access Paper:
View PDF
HTML (experimental)
TeX Source
Other Formats
view license
Current browse context:
cs.SE
< prev   |   next >

new | recent | 2024-01
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
  "title": "Teaching Code LLMs to Use Autocompletion Tools in Repository-Level Code Generation",
  "description": "Abstract page for arXiv paper 2401.06391: Teaching Code LLMs to Use Autocompletion Tools in Repository-Level Code Generation",
  "url": "https://arxiv.org/abs/2401.06391",
  "content": "Skip to main content\n\nIn just 3 minutes help us improve arXiv:\n\nAnnual Global Survey\nWe gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.\nDonate\n>\ncs\n>\narXiv:2401.06391\n\nHelp | Advanced Search\n\nAll fields\nTitle\nAuthor\nAbstract\nComments\nJournal reference\nACM classification\nMSC classification\nReport number\narXiv identifier\nDOI\nORCID\narXiv author ID\nHelp pages\nFull text\nSearch\nComputer Science > Software Engineering\n[Submitted on 12 Jan 2024 (v1), last revised 18 Jul 2024 (this version, v3)]\nTeaching Code LLMs to Use Autocompletion Tools in Repository-Level Code Generation\nChong Wang, Jian Zhang, Yebo Feng, Tianlin Li, Weisong Sun, Yang Liu, Xin Peng\nCode large language models (LLMs) face limitations in repository-level code generation due to their lack of awareness of repository-level dependencies (e.g., user-defined attributes), resulting in dependency errors such as undefined-variable and no-member errors. In this work, we introduce ToolGen, an approach that integrates autocompletion tools into the code LLM generation process to address these dependencies. ToolGen comprises two main phases: Trigger Insertion and Model Fine-tuning (Offline), and Tool-integrated Code Generation (Online). During the offline phase, ToolGen augments functions within a given code corpus with a special mark token, indicating positions to trigger autocompletion tools. These augmented functions, along with their corresponding docstrings, are then used to fine-tune a selected code LLM. In the online phase, ToolGen iteratively generates functions by predicting tokens step-by-step using the fine-tuned LLM. Whenever a mark token is encountered, ToolGen invokes the autocompletion tool to suggest code completions and selects the most appropriate one.\nWe conduct comprehensive experiments to evaluate ToolGen's effectiveness in repository-level code generation. To facilitate this evaluation, we create a benchmark comprising 671 real-world code repositories and introduce two new dependency-based metrics: Dependency Coverage and Static Validity Rate. The results demonstrate that ToolGen significantly improves Dependency Coverage by 31.4% to 39.1% and Static Validity Rate by 44.9% to 57.7% across the three LLMs, while maintaining competitive or improved performance in widely recognized similarity metrics such as BLEU-4, CodeBLEU, Edit Similarity, and Exact Match. On the CoderEval dataset, ToolGen achieves improvements of 40.0% and 25.0% in Pass@1 for CodeT5 and CodeLlama, respectively.\nSubjects:\tSoftware Engineering (cs.SE)\nCite as:\tarXiv:2401.06391 [cs.SE]\n \t(or arXiv:2401.06391v3 [cs.SE] for this version)\n \t\nhttps://doi.org/10.48550/arXiv.2401.06391\nFocus to learn more\nSubmission history\nFrom: Chong Wang [view email]\n[v1] Fri, 12 Jan 2024 06:03:56 UTC (1,137 KB)\n[v2] Sun, 21 Jan 2024 08:41:09 UTC (1,026 KB)\n[v3] Thu, 18 Jul 2024 07:04:38 UTC (2,162 KB)\n\nAccess Paper:\nView PDF\nHTML (experimental)\nTeX Source\nOther Formats\nview license\nCurrent browse context:\ncs.SE\n< prev   |   next >\n\nnew | recent | 2024-01\nChange to browse by:\ncs\n\nReferences & Citations\nNASA ADS\nGoogle Scholar\nSemantic Scholar\nExport BibTeX Citation\nBookmark\n \nBibliographic Tools\nBibliographic and Citation Tools\nBibliographic Explorer Toggle\nBibliographic Explorer (What is the Explorer?)\nConnected Papers Toggle\nConnected Papers (What is Connected Papers?)\nLitmaps Toggle\nLitmaps (What is Litmaps?)\nscite.ai Toggle\nscite Smart Citations (What are Smart Citations?)\nCode, Data, Media\nDemos\nRelated Papers\nAbout arXivLabs\nWhich authors of this paper are endorsers? | Disable MathJax (What is MathJax?)\nAbout\nHelp\nContact\nSubscribe\nCopyright\nPrivacy Policy\nWeb Accessibility Assistance\n\narXiv Operational Status \nGet status notifications via email or slack",
  "usage": {
    "tokens": 926
  }
}
```
