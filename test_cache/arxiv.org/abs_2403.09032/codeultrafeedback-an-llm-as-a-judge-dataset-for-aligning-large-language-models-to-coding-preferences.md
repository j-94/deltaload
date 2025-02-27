---
title: CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences
description: Abstract page for arXiv paper 2403.09032: CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences
url: https://arxiv.org/abs/2403.09032
timestamp: 2025-01-20T15:59:57.494Z
domain: arxiv.org
path: abs_2403.09032
---

# CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences


Abstract page for arXiv paper 2403.09032: CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences


## Content

Skip to main content

In just 3 minutes help us improve arXiv:

Annual Global Survey
We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate
>
cs
>
arXiv:2403.09032

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
[Submitted on 14 Mar 2024 (v1), last revised 27 Dec 2024 (this version, v3)]
CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences
Martin Weyssow, Aton Kamanda, Xin Zhou, Houari Sahraoui
Evaluating the alignment of large language models (LLMs) with user-defined coding preferences is a challenging endeavour that requires a deep assessment of LLMs' outputs. Existing methods and benchmarks rely primarily on automated metrics and static analysis tools, which often fail to capture the nuances of user instructions and LLM outputs. To address this gap, we propose using the LLM-as-a-Judge methodology to evaluate the alignment of LLMs with coding preferences. Based on this approach, we present CodeUltraFeedback, a comprehensive dataset designed to facilitate the evaluation and improvement of LLM alignment. CodeUltraFeedback consists of 10,000 coding instructions, each annotated with four responses generated from a diverse pool of 14 LLMs. These responses are ranked based on five distinct coding preferences using GPT-3.5 as a judge, providing both numerical scores and detailed textual feedback. Our analysis of CodeUltraFeedback reveals that responses from GPT-3.5 and GPT-4 are generally preferred over those from open-weight LLMs, highlighting significant differences in alignment between closed and open-weight models. In turn, we explore the usage of CodeUltraFeedback as feedback data to fine-tune and align CodeLlama-7B-Instruct using supervised fine-tuning (SFT) and reinforcement learning from AI feedback (RLAIF) with direct preference optimization (DPO). The resulting aligned CodeLlama-7B-Instruct model outperforms larger LLMs in terms of alignment with coding preferences and shows improved functional correctness on the HumanEval+ benchmark compared to the original instruct model. Therefore, our contributions bridge the gap in preference tuning of LLMs for code and set the stage for further advancements in model alignment and RLAIF in automated software engineering.
Subjects:	Software Engineering (cs.SE); Computation and Language (cs.CL); Machine Learning (cs.LG)
Cite as:	arXiv:2403.09032 [cs.SE]
 	(or arXiv:2403.09032v3 [cs.SE] for this version)
 	
https://doi.org/10.48550/arXiv.2403.09032
Focus to learn more
Submission history
From: Martin Weyssow [view email]
[v1] Thu, 14 Mar 2024 01:51:35 UTC (999 KB)
[v2] Wed, 7 Aug 2024 07:20:23 UTC (1,454 KB)
[v3] Fri, 27 Dec 2024 05:13:23 UTC (1,737 KB)

Access Paper:
View PDF
HTML (experimental)
TeX Source
Other Formats
view license
Current browse context:
cs.SE
< prev   |   next >

new | recent | 2024-03
Change to browse by:
cs
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
  "title": "CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences",
  "description": "Abstract page for arXiv paper 2403.09032: CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences",
  "url": "https://arxiv.org/abs/2403.09032",
  "content": "Skip to main content\n\nIn just 3 minutes help us improve arXiv:\n\nAnnual Global Survey\nWe gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.\nDonate\n>\ncs\n>\narXiv:2403.09032\n\nHelp | Advanced Search\n\nAll fields\nTitle\nAuthor\nAbstract\nComments\nJournal reference\nACM classification\nMSC classification\nReport number\narXiv identifier\nDOI\nORCID\narXiv author ID\nHelp pages\nFull text\nSearch\nComputer Science > Software Engineering\n[Submitted on 14 Mar 2024 (v1), last revised 27 Dec 2024 (this version, v3)]\nCodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences\nMartin Weyssow, Aton Kamanda, Xin Zhou, Houari Sahraoui\nEvaluating the alignment of large language models (LLMs) with user-defined coding preferences is a challenging endeavour that requires a deep assessment of LLMs' outputs. Existing methods and benchmarks rely primarily on automated metrics and static analysis tools, which often fail to capture the nuances of user instructions and LLM outputs. To address this gap, we propose using the LLM-as-a-Judge methodology to evaluate the alignment of LLMs with coding preferences. Based on this approach, we present CodeUltraFeedback, a comprehensive dataset designed to facilitate the evaluation and improvement of LLM alignment. CodeUltraFeedback consists of 10,000 coding instructions, each annotated with four responses generated from a diverse pool of 14 LLMs. These responses are ranked based on five distinct coding preferences using GPT-3.5 as a judge, providing both numerical scores and detailed textual feedback. Our analysis of CodeUltraFeedback reveals that responses from GPT-3.5 and GPT-4 are generally preferred over those from open-weight LLMs, highlighting significant differences in alignment between closed and open-weight models. In turn, we explore the usage of CodeUltraFeedback as feedback data to fine-tune and align CodeLlama-7B-Instruct using supervised fine-tuning (SFT) and reinforcement learning from AI feedback (RLAIF) with direct preference optimization (DPO). The resulting aligned CodeLlama-7B-Instruct model outperforms larger LLMs in terms of alignment with coding preferences and shows improved functional correctness on the HumanEval+ benchmark compared to the original instruct model. Therefore, our contributions bridge the gap in preference tuning of LLMs for code and set the stage for further advancements in model alignment and RLAIF in automated software engineering.\nSubjects:\tSoftware Engineering (cs.SE); Computation and Language (cs.CL); Machine Learning (cs.LG)\nCite as:\tarXiv:2403.09032 [cs.SE]\n \t(or arXiv:2403.09032v3 [cs.SE] for this version)\n \t\nhttps://doi.org/10.48550/arXiv.2403.09032\nFocus to learn more\nSubmission history\nFrom: Martin Weyssow [view email]\n[v1] Thu, 14 Mar 2024 01:51:35 UTC (999 KB)\n[v2] Wed, 7 Aug 2024 07:20:23 UTC (1,454 KB)\n[v3] Fri, 27 Dec 2024 05:13:23 UTC (1,737 KB)\n\nAccess Paper:\nView PDF\nHTML (experimental)\nTeX Source\nOther Formats\nview license\nCurrent browse context:\ncs.SE\n< prev   |   next >\n\nnew | recent | 2024-03\nChange to browse by:\ncs\ncs.CL\ncs.LG\n\nReferences & Citations\nNASA ADS\nGoogle Scholar\nSemantic Scholar\nExport BibTeX Citation\nBookmark\n \nBibliographic Tools\nBibliographic and Citation Tools\nBibliographic Explorer Toggle\nBibliographic Explorer (What is the Explorer?)\nConnected Papers Toggle\nConnected Papers (What is Connected Papers?)\nLitmaps Toggle\nLitmaps (What is Litmaps?)\nscite.ai Toggle\nscite Smart Citations (What are Smart Citations?)\nCode, Data, Media\nDemos\nRelated Papers\nAbout arXivLabs\nWhich authors of this paper are endorsers? | Disable MathJax (What is MathJax?)\nAbout\nHelp\nContact\nSubscribe\nCopyright\nPrivacy Policy\nWeb Accessibility Assistance\n\narXiv Operational Status \nGet status notifications via email or slack",
  "usage": {
    "tokens": 932
  }
}
```
