---
title: Data Systems Group (DSG) @ MIT
description: The main website of the Data Systems Group (DSG) at MIT.
url: https://dsg.csail.mit.edu/projects/brad/
timestamp: 2025-01-20T16:19:37.424Z
domain: dsg.csail.mit.edu
path: projects_brad
---

# Data Systems Group (DSG) @ MIT


The main website of the Data Systems Group (DSG) at MIT.


## Content

BRAD: Simplifying Cloud Data Processing with Learned Automated Data Meshes
--------------------------------------------------------------------------

The last decade of database research has led to the prevalence of specialized systems for different workloads. Consequently, organizations often rely on a combination of specialized systems, organized in a Data Mesh. Data meshes present significant challenges for system administrators, including picking the right system for each workload, moving data between systems, maintaining consistency, and correctly configuring each system. Many non-expert end users (e.g., data analysts or app developers) either cannot solve their business problems, or suffer from sub-optimal performance or cost due to this complexity. We envision BRAD, a cloud system that automatically integrates and manages data and systems into an instance-optimized data mesh, allowing users to efficiently store and query data under a unified data model (i.e., relational tables) without knowledge of underlying system details. With machine learning, BRAD automatically deduces the strengths and weaknesses of each engine through a combination of offline training and online probing. Then, BRAD uses these insights to route queries to the most suitable (combination of) system(s) for efficient execution. Furthermore, BRAD automates configuration tuning, resource scaling, and data migration across component systems, and makes recommendations for more impactful decisions, such as adding or removing systems. As such, BRAD exemplifies a new class of systems that utilize machine learning and the cloud to make complex data processing more accessible to end users, raising numerous new problems in database systems, machine learning, and the cloud.

[Read the Paper (VLDB 2024)](https://doi.org/10.14778/3681954.3682026) | [Read the Extended Version (arXiv)](https://doi.org/10.48550/arxiv.2407.15363) | [View BibTeX](https://dsg.csail.mit.edu/projects/brad/#)

[Read the Vision Paper (VLDB 2023)](https://doi.org/10.14778/3611479.3611526) | [View BibTeX](https://dsg.csail.mit.edu/projects/brad/#)

[Check out the Code](https://github.com/mitdbg/brad/)

### Project Participants

Markos Markakis, Ziniu Wu, Amadou Ngom, Tim Kraska, Tianyu Li, Samuel Madden, Geoffrey Yu, Ferdinand Kossmann

(Participant order is randomized.)

## Metadata

```json
{
  "title": "Data Systems Group (DSG) @ MIT",
  "description": "The main website of the Data Systems Group (DSG) at MIT.",
  "url": "https://dsg.csail.mit.edu/projects/brad/",
  "content": "BRAD: Simplifying Cloud Data Processing with Learned Automated Data Meshes\n--------------------------------------------------------------------------\n\nThe last decade of database research has led to the prevalence of specialized systems for different workloads. Consequently, organizations often rely on a combination of specialized systems, organized in a Data Mesh. Data meshes present significant challenges for system administrators, including picking the right system for each workload, moving data between systems, maintaining consistency, and correctly configuring each system. Many non-expert end users (e.g., data analysts or app developers) either cannot solve their business problems, or suffer from sub-optimal performance or cost due to this complexity. We envision BRAD, a cloud system that automatically integrates and manages data and systems into an instance-optimized data mesh, allowing users to efficiently store and query data under a unified data model (i.e., relational tables) without knowledge of underlying system details. With machine learning, BRAD automatically deduces the strengths and weaknesses of each engine through a combination of offline training and online probing. Then, BRAD uses these insights to route queries to the most suitable (combination of) system(s) for efficient execution. Furthermore, BRAD automates configuration tuning, resource scaling, and data migration across component systems, and makes recommendations for more impactful decisions, such as adding or removing systems. As such, BRAD exemplifies a new class of systems that utilize machine learning and the cloud to make complex data processing more accessible to end users, raising numerous new problems in database systems, machine learning, and the cloud.\n\n[Read the Paper (VLDB 2024)](https://doi.org/10.14778/3681954.3682026) | [Read the Extended Version (arXiv)](https://doi.org/10.48550/arxiv.2407.15363) | [View BibTeX](https://dsg.csail.mit.edu/projects/brad/#)\n\n[Read the Vision Paper (VLDB 2023)](https://doi.org/10.14778/3611479.3611526) | [View BibTeX](https://dsg.csail.mit.edu/projects/brad/#)\n\n[Check out the Code](https://github.com/mitdbg/brad/)\n\n### Project Participants\n\nMarkos Markakis, Ziniu Wu, Amadou Ngom, Tim Kraska, Tianyu Li, Samuel Madden, Geoffrey Yu, Ferdinand Kossmann\n\n(Participant order is randomized.)",
  "usage": {
    "tokens": 498
  }
}
```
