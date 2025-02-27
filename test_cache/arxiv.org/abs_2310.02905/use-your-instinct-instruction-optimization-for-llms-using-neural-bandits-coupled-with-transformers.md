---
title: Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers
description: Abstract page for arXiv paper 2310.02905: Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers
url: https://arxiv.org/abs/2310.02905
timestamp: 2025-01-20T15:46:24.848Z
domain: arxiv.org
path: abs_2310.02905
---

# Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers


Abstract page for arXiv paper 2310.02905: Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers


## Content

Skip to main content

In just 3 minutes help us improve arXiv:

Annual Global Survey
We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate
>
cs
>
arXiv:2310.02905

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
Computer Science > Machine Learning
[Submitted on 2 Oct 2023 (v1), last revised 23 Jun 2024 (this version, v3)]
Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers
Xiaoqiang Lin, Zhaoxuan Wu, Zhongxiang Dai, Wenyang Hu, Yao Shu, See-Kiong Ng, Patrick Jaillet, Bryan Kian Hsiang Low
Large language models (LLMs) have shown remarkable instruction-following capabilities and achieved impressive performances in various applications. However, the performances of LLMs depend heavily on the instructions given to them, which are typically manually tuned with substantial human efforts. Recent work has used the query-efficient Bayesian optimization (BO) algorithm to automatically optimize the instructions given to black-box LLMs. However, BO usually falls short when optimizing highly sophisticated (e.g., high-dimensional) objective functions, such as the functions mapping an instruction to the performance of an LLM. This is mainly due to the limited expressive power of the Gaussian process (GP) which is used by BO as a surrogate to model the objective function. Meanwhile, it has been repeatedly shown that neural networks (NNs), especially pre-trained transformers, possess strong expressive power and can model highly complex functions. So, we adopt a neural bandit algorithm which replaces the GP in BO by an NN surrogate to optimize instructions for black-box LLMs. More importantly, the neural bandit algorithm allows us to naturally couple the NN surrogate with the hidden representation learned by a pre-trained transformer (i.e., an open-source LLM), which significantly boosts its performance. These motivate us to propose our INSTruction optimization usIng Neural bandits Coupled with Transformers (INSTINCT) algorithm. We perform instruction optimization for ChatGPT and use extensive experiments to show that INSTINCT consistently outperforms baselines in different tasks, e.g., various instruction induction tasks and the task of improving zero-shot chain-of-thought instructions. Our code is available at this https URL.
Comments:	Accepted to ICML 2024
Subjects:	Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:	arXiv:2310.02905 [cs.LG]
 	(or arXiv:2310.02905v3 [cs.LG] for this version)
 	
https://doi.org/10.48550/arXiv.2310.02905
Focus to learn more
Submission history
From: Zhongxiang Dai [view email]
[v1] Mon, 2 Oct 2023 02:01:16 UTC (1,300 KB)
[v2] Fri, 31 May 2024 16:27:53 UTC (1,729 KB)
[v3] Sun, 23 Jun 2024 23:59:53 UTC (1,730 KB)

Access Paper:
View PDF
HTML (experimental)
TeX Source
Other Formats
view license
Current browse context:
cs.LG
< prev   |   next >

new | recent | 2023-10
Change to browse by:
cs
cs.AI
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
  "title": "Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers",
  "description": "Abstract page for arXiv paper 2310.02905: Use Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers",
  "url": "https://arxiv.org/abs/2310.02905",
  "content": "Skip to main content\n\nIn just 3 minutes help us improve arXiv:\n\nAnnual Global Survey\nWe gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.\nDonate\n>\ncs\n>\narXiv:2310.02905\n\nHelp | Advanced Search\n\nAll fields\nTitle\nAuthor\nAbstract\nComments\nJournal reference\nACM classification\nMSC classification\nReport number\narXiv identifier\nDOI\nORCID\narXiv author ID\nHelp pages\nFull text\nSearch\nComputer Science > Machine Learning\n[Submitted on 2 Oct 2023 (v1), last revised 23 Jun 2024 (this version, v3)]\nUse Your INSTINCT: INSTruction optimization for LLMs usIng Neural bandits Coupled with Transformers\nXiaoqiang Lin, Zhaoxuan Wu, Zhongxiang Dai, Wenyang Hu, Yao Shu, See-Kiong Ng, Patrick Jaillet, Bryan Kian Hsiang Low\nLarge language models (LLMs) have shown remarkable instruction-following capabilities and achieved impressive performances in various applications. However, the performances of LLMs depend heavily on the instructions given to them, which are typically manually tuned with substantial human efforts. Recent work has used the query-efficient Bayesian optimization (BO) algorithm to automatically optimize the instructions given to black-box LLMs. However, BO usually falls short when optimizing highly sophisticated (e.g., high-dimensional) objective functions, such as the functions mapping an instruction to the performance of an LLM. This is mainly due to the limited expressive power of the Gaussian process (GP) which is used by BO as a surrogate to model the objective function. Meanwhile, it has been repeatedly shown that neural networks (NNs), especially pre-trained transformers, possess strong expressive power and can model highly complex functions. So, we adopt a neural bandit algorithm which replaces the GP in BO by an NN surrogate to optimize instructions for black-box LLMs. More importantly, the neural bandit algorithm allows us to naturally couple the NN surrogate with the hidden representation learned by a pre-trained transformer (i.e., an open-source LLM), which significantly boosts its performance. These motivate us to propose our INSTruction optimization usIng Neural bandits Coupled with Transformers (INSTINCT) algorithm. We perform instruction optimization for ChatGPT and use extensive experiments to show that INSTINCT consistently outperforms baselines in different tasks, e.g., various instruction induction tasks and the task of improving zero-shot chain-of-thought instructions. Our code is available at this https URL.\nComments:\tAccepted to ICML 2024\nSubjects:\tMachine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)\nCite as:\tarXiv:2310.02905 [cs.LG]\n \t(or arXiv:2310.02905v3 [cs.LG] for this version)\n \t\nhttps://doi.org/10.48550/arXiv.2310.02905\nFocus to learn more\nSubmission history\nFrom: Zhongxiang Dai [view email]\n[v1] Mon, 2 Oct 2023 02:01:16 UTC (1,300 KB)\n[v2] Fri, 31 May 2024 16:27:53 UTC (1,729 KB)\n[v3] Sun, 23 Jun 2024 23:59:53 UTC (1,730 KB)\n\nAccess Paper:\nView PDF\nHTML (experimental)\nTeX Source\nOther Formats\nview license\nCurrent browse context:\ncs.LG\n< prev   |   next >\n\nnew | recent | 2023-10\nChange to browse by:\ncs\ncs.AI\ncs.CL\n\nReferences & Citations\nNASA ADS\nGoogle Scholar\nSemantic Scholar\nExport BibTeX Citation\nBookmark\n \nBibliographic Tools\nBibliographic and Citation Tools\nBibliographic Explorer Toggle\nBibliographic Explorer (What is the Explorer?)\nConnected Papers Toggle\nConnected Papers (What is Connected Papers?)\nLitmaps Toggle\nLitmaps (What is Litmaps?)\nscite.ai Toggle\nscite Smart Citations (What are Smart Citations?)\nCode, Data, Media\nDemos\nRelated Papers\nAbout arXivLabs\nWhich authors of this paper are endorsers? | Disable MathJax (What is MathJax?)\nAbout\nHelp\nContact\nSubscribe\nCopyright\nPrivacy Policy\nWeb Accessibility Assistance\n\narXiv Operational Status \nGet status notifications via email or slack",
  "usage": {
    "tokens": 938
  }
}
```
