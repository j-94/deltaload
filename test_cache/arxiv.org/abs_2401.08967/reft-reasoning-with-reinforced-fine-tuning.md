---
title: ReFT: Reasoning with Reinforced Fine-Tuning
description: Abstract page for arXiv paper 2401.08967: ReFT: Reasoning with Reinforced Fine-Tuning
url: https://arxiv.org/abs/2401.08967
timestamp: 2025-01-20T15:54:49.190Z
domain: arxiv.org
path: abs_2401.08967
---

# ReFT: Reasoning with Reinforced Fine-Tuning


Abstract page for arXiv paper 2401.08967: ReFT: Reasoning with Reinforced Fine-Tuning


## Content

Skip to main content

In just 3 minutes help us improve arXiv:

Annual Global Survey
We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate
>
cs
>
arXiv:2401.08967

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
[Submitted on 17 Jan 2024 (v1), last revised 13 Dec 2024 (this version, v3)]
ReFT: Reasoning with Reinforced Fine-Tuning
Trung Quoc Luong, Xinbo Zhang, Zhanming Jie, Peng Sun, Xiaoran Jin, Hang Li
One way to enhance the reasoning capability of Large Language Models (LLMs) is to conduct Supervised Fine-Tuning (SFT) using Chain-of-Thought (CoT) annotations. This approach does not show sufficiently strong generalization ability, however, because the training only relies on the given CoT data. In math problem-solving, for example, there is usually only one annotated reasoning path for each question in the training data. Intuitively, it would be better for the algorithm to learn from multiple annotated reasoning paths given a question. To address this issue, we propose a simple yet effective approach called Reinforced Fine-Tuning (ReFT) to enhance the generalizability of learning LLMs for reasoning, with math problem-solving as an example. ReFT first warmups the model with SFT, and then employs on-line reinforcement learning, specifically the PPO algorithm in this paper, to further fine-tune the model, where an abundance of reasoning paths are automatically sampled given the question and the rewards are naturally derived from the ground-truth answers. Extensive experiments on GSM8K, MathQA, and SVAMP datasets show that ReFT significantly outperforms SFT, and the performance can be potentially further boosted by combining inference-time strategies such as majority voting and re-ranking. Note that ReFT obtains the improvement by learning from the same training questions as SFT, without relying on extra or augmented training questions. This indicates a superior generalization ability for ReFT.
Comments:	ACL 2024 main conference; adjust with reviewer comments; 13 pages
Subjects:	Computation and Language (cs.CL)
Cite as:	arXiv:2401.08967 [cs.CL]
 	(or arXiv:2401.08967v3 [cs.CL] for this version)
 	
https://doi.org/10.48550/arXiv.2401.08967
Focus to learn more
Submission history
From: Zhanming Jie [view email]
[v1] Wed, 17 Jan 2024 04:43:21 UTC (3,687 KB)
[v2] Thu, 27 Jun 2024 15:29:15 UTC (5,080 KB)
[v3] Fri, 13 Dec 2024 04:44:11 UTC (5,080 KB)

Access Paper:
View PDF
TeX Source
Other Formats
view license
Current browse context:
cs.CL
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
  "title": "ReFT: Reasoning with Reinforced Fine-Tuning",
  "description": "Abstract page for arXiv paper 2401.08967: ReFT: Reasoning with Reinforced Fine-Tuning",
  "url": "https://arxiv.org/abs/2401.08967",
  "content": "Skip to main content\n\nIn just 3 minutes help us improve arXiv:\n\nAnnual Global Survey\nWe gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.\nDonate\n>\ncs\n>\narXiv:2401.08967\n\nHelp | Advanced Search\n\nAll fields\nTitle\nAuthor\nAbstract\nComments\nJournal reference\nACM classification\nMSC classification\nReport number\narXiv identifier\nDOI\nORCID\narXiv author ID\nHelp pages\nFull text\nSearch\nComputer Science > Computation and Language\n[Submitted on 17 Jan 2024 (v1), last revised 13 Dec 2024 (this version, v3)]\nReFT: Reasoning with Reinforced Fine-Tuning\nTrung Quoc Luong, Xinbo Zhang, Zhanming Jie, Peng Sun, Xiaoran Jin, Hang Li\nOne way to enhance the reasoning capability of Large Language Models (LLMs) is to conduct Supervised Fine-Tuning (SFT) using Chain-of-Thought (CoT) annotations. This approach does not show sufficiently strong generalization ability, however, because the training only relies on the given CoT data. In math problem-solving, for example, there is usually only one annotated reasoning path for each question in the training data. Intuitively, it would be better for the algorithm to learn from multiple annotated reasoning paths given a question. To address this issue, we propose a simple yet effective approach called Reinforced Fine-Tuning (ReFT) to enhance the generalizability of learning LLMs for reasoning, with math problem-solving as an example. ReFT first warmups the model with SFT, and then employs on-line reinforcement learning, specifically the PPO algorithm in this paper, to further fine-tune the model, where an abundance of reasoning paths are automatically sampled given the question and the rewards are naturally derived from the ground-truth answers. Extensive experiments on GSM8K, MathQA, and SVAMP datasets show that ReFT significantly outperforms SFT, and the performance can be potentially further boosted by combining inference-time strategies such as majority voting and re-ranking. Note that ReFT obtains the improvement by learning from the same training questions as SFT, without relying on extra or augmented training questions. This indicates a superior generalization ability for ReFT.\nComments:\tACL 2024 main conference; adjust with reviewer comments; 13 pages\nSubjects:\tComputation and Language (cs.CL)\nCite as:\tarXiv:2401.08967 [cs.CL]\n \t(or arXiv:2401.08967v3 [cs.CL] for this version)\n \t\nhttps://doi.org/10.48550/arXiv.2401.08967\nFocus to learn more\nSubmission history\nFrom: Zhanming Jie [view email]\n[v1] Wed, 17 Jan 2024 04:43:21 UTC (3,687 KB)\n[v2] Thu, 27 Jun 2024 15:29:15 UTC (5,080 KB)\n[v3] Fri, 13 Dec 2024 04:44:11 UTC (5,080 KB)\n\nAccess Paper:\nView PDF\nTeX Source\nOther Formats\nview license\nCurrent browse context:\ncs.CL\n< prev   |   next >\n\nnew | recent | 2024-01\nChange to browse by:\ncs\n\nReferences & Citations\nNASA ADS\nGoogle Scholar\nSemantic Scholar\nExport BibTeX Citation\nBookmark\n \nBibliographic Tools\nBibliographic and Citation Tools\nBibliographic Explorer Toggle\nBibliographic Explorer (What is the Explorer?)\nConnected Papers Toggle\nConnected Papers (What is Connected Papers?)\nLitmaps Toggle\nLitmaps (What is Litmaps?)\nscite.ai Toggle\nscite Smart Citations (What are Smart Citations?)\nCode, Data, Media\nDemos\nRelated Papers\nAbout arXivLabs\nWhich authors of this paper are endorsers? | Disable MathJax (What is MathJax?)\nAbout\nHelp\nContact\nSubscribe\nCopyright\nPrivacy Policy\nWeb Accessibility Assistance\n\narXiv Operational Status \nGet status notifications via email or slack",
  "usage": {
    "tokens": 871
  }
}
```
