---
title: MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use
description: Abstract page for arXiv paper 2310.03128: MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use
url: https://arxiv.org/abs/2310.03128#:~:text=version%2C%20v2)%5D-,MetaTool%20Benchmark%20for%20Large%20Language%20Models%3A%20Deciding%20Whether%20to,Tools%20and%20Which%20to%20Use&text=Large%20language%20models%20(LLMs)%20have,tool%20utilization%20ability%20of%20LLMs.
timestamp: 2025-01-20T15:49:53.830Z
domain: arxiv.org
path: abs_2310.03128
---

# MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use


Abstract page for arXiv paper 2310.03128: MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use


## Content

Skip to main content

In just 3 minutes help us improve arXiv:

Annual Global Survey
We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.
Donate
>
cs
>
arXiv:2310.03128

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
[Submitted on 4 Oct 2023 (v1), last revised 4 Dec 2024 (this version, v6)]
MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use
Yue Huang, Jiawen Shi, Yuan Li, Chenrui Fan, Siyuan Wu, Qihui Zhang, Yixin Liu, Pan Zhou, Yao Wan, Neil Zhenqiang Gong, Lichao Sun
Large language models (LLMs) have garnered significant attention due to their impressive natural language processing (NLP) capabilities. Recently, many studies have focused on the tool utilization ability of LLMs. They primarily investigated how LLMs effectively collaborate with given specific tools. However, in scenarios where LLMs serve as intelligent agents, as seen in applications like AutoGPT and MetaGPT, LLMs are expected to engage in intricate decision-making processes that involve deciding whether to employ a tool and selecting the most suitable tool(s) from a collection of available tools to fulfill user requests. Therefore, in this paper, we introduce MetaTool, a benchmark designed to evaluate whether LLMs have tool usage awareness and can correctly choose tools. Specifically, we create a dataset called ToolE within the benchmark. This dataset contains various types of user queries in the form of prompts that trigger LLMs to use tools, including both single-tool and multi-tool scenarios. Subsequently, we set the tasks for both tool usage awareness and tool selection. We define four subtasks from different perspectives in tool selection, including tool selection with similar choices, tool selection in specific scenarios, tool selection with possible reliability issues, and multi-tool selection. We conduct experiments involving eight popular LLMs and find that the majority of them still struggle to effectively select tools, highlighting the existing gaps between LLMs and genuine intelligent agents. However, through the error analysis, we found there is still significant room for improvement. Finally, we conclude with insights for tool developers -- we strongly recommend that tool developers choose an appropriate rewrite model for generating new descriptions based on the downstream LLM the tool will apply to. Our code is in this https URL.
Subjects:	Software Engineering (cs.SE); Computation and Language (cs.CL)
Cite as:	arXiv:2310.03128 [cs.SE]
 	(or arXiv:2310.03128v6 [cs.SE] for this version)
 	
https://doi.org/10.48550/arXiv.2310.03128
Focus to learn more
Submission history
From: Yue Huang [view email]
[v1] Wed, 4 Oct 2023 19:39:26 UTC (6,814 KB)
[v2] Thu, 12 Oct 2023 14:37:55 UTC (6,814 KB)
[v3] Mon, 23 Oct 2023 18:28:56 UTC (6,814 KB)
[v4] Thu, 18 Jan 2024 18:57:10 UTC (6,830 KB)
[v5] Fri, 23 Feb 2024 13:19:52 UTC (6,832 KB)
[v6] Wed, 4 Dec 2024 19:49:02 UTC (6,832 KB)

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
  "title": "MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use",
  "description": "Abstract page for arXiv paper 2310.03128: MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use",
  "url": "https://arxiv.org/abs/2310.03128",
  "content": "Skip to main content\n\nIn just 3 minutes help us improve arXiv:\n\nAnnual Global Survey\nWe gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors.\nDonate\n>\ncs\n>\narXiv:2310.03128\n\nHelp | Advanced Search\n\nAll fields\nTitle\nAuthor\nAbstract\nComments\nJournal reference\nACM classification\nMSC classification\nReport number\narXiv identifier\nDOI\nORCID\narXiv author ID\nHelp pages\nFull text\nSearch\nComputer Science > Software Engineering\n[Submitted on 4 Oct 2023 (v1), last revised 4 Dec 2024 (this version, v6)]\nMetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use\nYue Huang, Jiawen Shi, Yuan Li, Chenrui Fan, Siyuan Wu, Qihui Zhang, Yixin Liu, Pan Zhou, Yao Wan, Neil Zhenqiang Gong, Lichao Sun\nLarge language models (LLMs) have garnered significant attention due to their impressive natural language processing (NLP) capabilities. Recently, many studies have focused on the tool utilization ability of LLMs. They primarily investigated how LLMs effectively collaborate with given specific tools. However, in scenarios where LLMs serve as intelligent agents, as seen in applications like AutoGPT and MetaGPT, LLMs are expected to engage in intricate decision-making processes that involve deciding whether to employ a tool and selecting the most suitable tool(s) from a collection of available tools to fulfill user requests. Therefore, in this paper, we introduce MetaTool, a benchmark designed to evaluate whether LLMs have tool usage awareness and can correctly choose tools. Specifically, we create a dataset called ToolE within the benchmark. This dataset contains various types of user queries in the form of prompts that trigger LLMs to use tools, including both single-tool and multi-tool scenarios. Subsequently, we set the tasks for both tool usage awareness and tool selection. We define four subtasks from different perspectives in tool selection, including tool selection with similar choices, tool selection in specific scenarios, tool selection with possible reliability issues, and multi-tool selection. We conduct experiments involving eight popular LLMs and find that the majority of them still struggle to effectively select tools, highlighting the existing gaps between LLMs and genuine intelligent agents. However, through the error analysis, we found there is still significant room for improvement. Finally, we conclude with insights for tool developers -- we strongly recommend that tool developers choose an appropriate rewrite model for generating new descriptions based on the downstream LLM the tool will apply to. Our code is in this https URL.\nSubjects:\tSoftware Engineering (cs.SE); Computation and Language (cs.CL)\nCite as:\tarXiv:2310.03128 [cs.SE]\n \t(or arXiv:2310.03128v6 [cs.SE] for this version)\n \t\nhttps://doi.org/10.48550/arXiv.2310.03128\nFocus to learn more\nSubmission history\nFrom: Yue Huang [view email]\n[v1] Wed, 4 Oct 2023 19:39:26 UTC (6,814 KB)\n[v2] Thu, 12 Oct 2023 14:37:55 UTC (6,814 KB)\n[v3] Mon, 23 Oct 2023 18:28:56 UTC (6,814 KB)\n[v4] Thu, 18 Jan 2024 18:57:10 UTC (6,830 KB)\n[v5] Fri, 23 Feb 2024 13:19:52 UTC (6,832 KB)\n[v6] Wed, 4 Dec 2024 19:49:02 UTC (6,832 KB)\n\nAccess Paper:\nView PDF\nHTML (experimental)\nTeX Source\nOther Formats\nview license\nCurrent browse context:\ncs.SE\n< prev   |   next >\n\nnew | recent | 2023-10\nChange to browse by:\ncs\ncs.CL\n\nReferences & Citations\nNASA ADS\nGoogle Scholar\nSemantic Scholar\nExport BibTeX Citation\nBookmark\n \nBibliographic Tools\nBibliographic and Citation Tools\nBibliographic Explorer Toggle\nBibliographic Explorer (What is the Explorer?)\nConnected Papers Toggle\nConnected Papers (What is Connected Papers?)\nLitmaps Toggle\nLitmaps (What is Litmaps?)\nscite.ai Toggle\nscite Smart Citations (What are Smart Citations?)\nCode, Data, Media\nDemos\nRelated Papers\nAbout arXivLabs\nWhich authors of this paper are endorsers? | Disable MathJax (What is MathJax?)\nAbout\nHelp\nContact\nSubscribe\nCopyright\nPrivacy Policy\nWeb Accessibility Assistance\n\narXiv Operational Status \nGet status notifications via email or slack",
  "usage": {
    "tokens": 1006
  }
}
```
