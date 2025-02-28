---
title: Mito: Using pandas as a spreadsheet - Towards Data Science
description: Spreadsheets are a great solution to inspect new data, get a first grasp of their content and interact with them quickly and visually. However, when these tasks are to be performed frequently — as…
url: https://towardsdatascience.com/mito-using-pandas-as-a-spreadsheet-within-jupyter-lab-6a6bd04310a8
timestamp: 2025-01-20T15:48:26.530Z
domain: towardsdatascience.com
path: mito-using-pandas-as-a-spreadsheet-within-jupyter-lab-6a6bd04310a8
---

# Mito: Using pandas as a spreadsheet - Towards Data Science


Spreadsheets are a great solution to inspect new data, get a first grasp of their content and interact with them quickly and visually. However, when these tasks are to be performed frequently — as…


## Content

Review of the _mitosheet_ python package
----------------------------------------

[![Image 39: Luca Clissa](https://miro.medium.com/v2/resize:fill:88:88/1*wPQ1cGdbMxg5HvT5-OerOw.png)](https://medium.com/@luca.clissa?source=post_page---byline--6a6bd04310a8--------------------------------)

[![Image 40: Towards Data Science](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---byline--6a6bd04310a8--------------------------------)

![Image 41](https://miro.medium.com/v2/resize:fit:700/0*ORT67DoO9izFx5UU)

Photo by [Isaac Smith](https://unsplash.com/@isaacmsmith?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Spreadsheets are a great solution to inspect new data, get a first grasp of their content and interact with them quickly and visually. However, when these tasks are to be performed frequently — as for typical workflows in data science projects — the advantage of spreadsheets-based tools like [Excel](https://www.microsoft.com/it-it/microsoft-365/excel) or [Google Sheets](https://www.google.com/intl/it/sheets/about/) is capped by the burden of manually repeating the same operations multiple times.

Programming languages offer a convenient alternative to automate the latter part, although possibly requiring some itching in the first pass through the data depending on the language and the user proficiency.

In this article we’re going to explore [**Mito**](https://www.trymito.io/), _a spreadsheet-like interface for pandas dataframes based on python_. In particular, I’ll guide you through its installation and main features, assessing the completeness, effectiveness and ease of use of Mito’s functionalities on a scale from 1 to 5.

> **_Disclaimer_**_: This post is sponsored. However, it presents a critical and honest appraisal of the library and its performances._

What is Mito?
-------------

[Mito is an open-source python library](https://github.com/mito-ds/monorepo) that combines the _intuitive and visual_ aspects of spreadsheets with the benefits of programming to _handle larger datasets_, provide _timely elaborations_ and create _repeatable processes_ easily.

In brief, Mito is a **Jupyter Lab interface** that allows users to **handle** data **as in a spreadsheet** while **automatically generating the corresponding python code** in the cell below.

Who’s for?
----------

Mito is just the perfect tool for old-school spreadsheet users — e.g. **Excel practitioners** —in transition to a programming-oriented paradigm.

However, I would recommend Mito also to python programmers like me that get bored by copy-pasting the same boilerplate code for exploratory data analysis. I believe this is a convenient tool for **exploratory data analysis,** and a **good starting** point to quickly set up the bulk of the code and then apply some custom adjustments here and there.

Installation
------------

The installation is pretty simple and requires just a [few steps](https://docs.trymito.io/getting-started/installing-mito) well described in the [documentation](https://docs.trymito.io/), e.g. for _conda_:

\# this article uses mitosheet version '0.1.392'  
conda create -n mitoenv python=3.8  
conda activate mitoenv  
python -m pip install mitoinstaller  
python -m mitoinstaller install

I had a try on my _ubuntu 20.04_ platform and managed to succeed almost without a blink. Actually, I couldn’t complete `python -m pip install mitoinstaller` immediately as some dependencies weren’t resolved:

(mitoenv) luca@ASUS-ROG:~/workspace/blog\_mito$ python -m pip install mitoinstaller  
Collecting mitoinstaller  
  Downloading mitoinstaller-0.0.122.tar.gz (14 kB)  
  Preparing metadata (setup.py) ... done  
Collecting analytics-python  
  Downloading analytics\_python-1.4.0-py2.py3-none-any.whl (15 kB)  
Requirement already satisfied: colorama in /home/luca/.local/lib/python3.8/site-packages (from mitoinstaller) (0.4.4)  
Collecting termcolor  
  Using cached termcolor-1.1.0.tar.gz (3.9 kB)  
  Preparing metadata (setup.py) ... done  
Collecting monotonic\>\=1.5  
  Downloading monotonic-1.6-py2.py3-none-any.whl (8.2 kB)  
Collecting backoff==1.10.0  
  Downloading backoff-1.10.0-py2.py3-none-any.whl (31 kB)  
Requirement already satisfied: python-dateutil\>2.1 in /home/luca/.local/lib/python3.8/site-packages (from analytics-python-\>mitoinstaller) (2.8.1)  
Collecting six\>\=1.5  
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)  
Collecting requests<3.0,\>\=2.7  
  Downloading requests-2.27.1-py2.py3-none-any.whl (63 kB)  
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.1/63.1 KB 605.1 kB/s eta 0:00:00  
Collecting certifi\>\=2017.4.17  
  Downloading certifi-2021.10.8-py2.py3-none-any.whl (149 kB)  
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 149.2/149.2 KB 1.1 MB/s eta 0:00:00  
Collecting urllib3<1.27,\>\=1.21.1  
  Downloading urllib3-1.26.8-py2.py3-none-any.whl (138 kB)  
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 138.7/138.7 KB 1.4 MB/s eta 0:00:00  
Collecting charset-normalizer~=2.0.0  
  Downloading charset\_normalizer-2.0.12-py3-none-any.whl (39 kB)  
Collecting idna<4,\>\=2.5  
  Downloading idna-3.3-py3-none-any.whl (61 kB)  
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 KB 1.6 MB/s eta 0:00:00  
Building wheels for collected packages: mitoinstaller, termcolor  
  Building wheel for mitoinstaller (setup.py) ... done  
  Created wheel for mitoinstaller: filename=mitoinstaller-0.0.122-py3-none-any.whl size=19809 sha256=68b55bfd4dbc4f916f6cd1a19500aefdfab6f25f86737c2ae7c258264eff410f  
  Stored in directory: /home/luca/.cache/pip/wheels/46/c6/8a/8b77ea33ddac40eff0b3e1847f84789d316e557e48bb0bc110  
  Building wheel for termcolor (setup.py) ... done  
  Created wheel for termcolor: filename=termcolor-1.1.0-py3-none-any.whl size=4848 sha256=84532fa74eca34fbe56efd5665ff9c8ebce197dc2a32254a19f145f97d6da515  
  Stored in directory: /home/luca/.cache/pip/wheels/a0/16/9c/5473df82468f958445479c59e784896fa24f4a5fc024b0f501  
Successfully built mitoinstaller termcolor  
Installing collected packages: termcolor, monotonic, certifi, urllib3, six, idna, charset-normalizer, backoff, requests, analytics-python, mitoinstaller  
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.  
requests-oauthlib 1.3.0 requires oauthlib\>\=3.0.0, which is not installed.  
pandas 1.2.2 requires pytz\>\=2017.3, which is not installed.  
oauth2client 4.1.3 requires httplib2\>\=0.9.1, which is not installed.  
moto 1.3.16.dev122 requires MarkupSafe<2.0, which is not installed.  
moto 1.3.16.dev122 requires more-itertools, which is not installed.  
moto 1.3.16.dev122 requires pytz, which is not installed.  
moto 1.3.16.dev122 requires zipp, which is not installed.  
google-api-core 1.26.3 requires packaging\>\=14.3, which is not installed.  
google-api-core 1.26.3 requires pytz, which is not installed.  
Successfully installed analytics-python-1.4.0 backoff-1.10.0 certifi-2021.10.8 charset-normalizer-2.0.12 idna-3.3 mitoinstaller-0.0.122 monotonic-1.6 requests-2.27.1 six-1.16.0 termcolor-1.1.0 urllib3-1.26.8

which led me to the following error when running `python -m mitoinstaller install`:

(mitoenv) luca@ASUS-ROG:~/workspace/blog\_mito$ python -m mitoinstaller install  
Starting install...  
Create mito user  
Upgrade mitoinstaller  
Check dependencies  
Remove mitosheet3 if present  
Install mitosheet  
Create import mito startup file  
Creating a Mitosheet starter notebook  
Start JupyterLab  
Traceback (most recent call last):  
  File "/home/luca/anaconda3/envs/mitoenv/bin/jupyter-lab", line 5, in <module\>  
    from jupyterlab.labapp import main  
  File "/home/luca/anaconda3/envs/mitoenv/lib/python3.8/site-packages/jupyterlab/labapp.py", line 13, in <module\>  
    from jupyter\_server.serverapp import flags  
  File "/home/luca/anaconda3/envs/mitoenv/lib/python3.8/site-packages/jupyter\_server/serverapp.py", line 38, in <module\>  
    from jinja2 import Environment, FileSystemLoader  
  File "/home/luca/.local/lib/python3.8/site-packages/jinja2/\_\_init\_\_.py", line 12, in <module\>  
    from .environment import Environment  
  File "/home/luca/.local/lib/python3.8/site-packages/jinja2/environment.py", line 25, in <module\>  
    from .defaults import BLOCK\_END\_STRING  
  File "/home/luca/.local/lib/python3.8/site-packages/jinja2/defaults.py", line 3, in <module\>  
    from .filters import FILTERS as DEFAULT\_FILTERS  # noqa: F401  
  File "/home/luca/.local/lib/python3.8/site-packages/jinja2/filters.py", line 13, in <module\>  
    from markupsafe import soft\_unicode  
ImportError: cannot import name 'soft\_unicode' from 'markupsafe' (/home/luca/anaconda3/envs/mitoenv/lib/python3.8/site-packages/markupsafe/\_\_init\_\_.py)

However, this may depend on my local configuration and was easily fixed by installing missing dependencies singularly:

pip install mitoinstaller  
pip install requests-oauthlib  
pip install oauth2client  
pip install pandas  
pip install moto  
pip install google-api-core

**Rate: 4 / 5** ⭐⭐⭐⭐

**Functionalities**
-------------------

Mito provides most (almost all) spreadsheets functionalities in a very intuitive and efficient manner.

Import data
-----------

Mito supports importing data from _csv_ and _xlsx_ files. The import itself is as easy as importing the _mitosheet_ package and running `mitosheet.sheet(). `The first time the user is asked to register and choose the desired [plan](https://www.trymito.io/plans). After that, you can simply follow a neat graphical interface to select data files to import.

![Image 42](https://miro.medium.com/v2/resize:fit:700/1*drcnCq_UUlg38kN2cP1BWg.gif)

**Data import.** Image by the author

Alternatively, Mito supports also pandas dataframe for each sheet as `mitosheet.sheet(df1, df2)`.

A minor limitation is that you can’t customize data type at import for _csv_ files — you can fix it later with data formatting though.

**Rate: 4 / 5** ⭐⭐⭐⭐

Check values and distributions
------------------------------

The first step of every data science project is to explore the data, check the values and explore variables’ distribution. With Mito this is real quick and intuitive.

![Image 43](https://miro.medium.com/v2/resize:fit:700/1*qIVqmk-rcB_MscKlnIa6kQ.gif)

**Data values and distribution.** Image by the author

My experience was very smooth for different kinds of data types and it covered all the use cases I can think of. A sound thumbs-up for this util!

**Rate: 5 / 5** ⭐⭐⭐⭐⭐

**Filter and sort**
-------------------

Filtering and sorting are also very common operations when dealing with data. Mito allows filtering both based on conditions and by directly excluding unwanted values.

![Image 44](https://miro.medium.com/v2/resize:fit:700/1*g0cgb1uux0s0nreBEQGwoA.gif)

**Filtering.** Image by the author

Sorting is also effective, although ordering based on multiple columns is not natively supported. A possible workaround is to concatenate such variables and sort by the resulting column.

**Rate: 4 / 5** ⭐⭐⭐⭐

Formatting
----------

Nice data formatting is key for visual exploration. Mito provides plenty of options to arrange their content for any need.

![Image 45](https://miro.medium.com/v2/resize:fit:700/1*Bq5aVlHbwoe1yQHsLW3Y3Q.gif)

**Data formatting.** Image by the author

**Rate: 5 / 5** ⭐⭐⭐⭐⭐

**Data types**
--------------

Handling data types is often needed during pre-processing in order to prepare the data appropriately for the following analysis pipeline. Mito does a nice job also in this respect, balancing the initial lack of customization during data import.

![Image 46](https://miro.medium.com/v2/resize:fit:700/1*VuXg8zd5dReTSNHt1OA_cQ.gif)

**Data types.** Image by the author

Apart from standard data types like `int` , `float`, `str` and `bool` , I tested Mito against one of the biggest data scientists’ nightmares: _dates._ The conversion from string to `datetime` is seamless, and you can play around with Excel formulas for more customization. Nicely done!

**Rate: 5 / 5** ⭐⭐⭐⭐⭐

Data manipulation
-----------------

Mito supports several kinds of data manipulation exploiting the most used Excel formulas. _Adding and deleting columns_, as well as _editing_ single cells or entire variables are just a few clicks away.

![Image 47](https://miro.medium.com/v2/resize:fit:700/1*j_oL4uDPmuLvEuhJhFfr8w.gif)

**Data manipulation.** Image by the author

I really appreciated the nice interface with suggestions as you type commands, plus the `Search Functionality` box in the top-right corner.

However, I didn’t manage to replicate one of Excel’s killer features: **dragging formulas**. That’s a pity and I think it should be one of the top priorities for future developments.

Also, added columns are not editable cell-wise — which means you can just edit new columns as a bulk. Again, this misses out on the convenience of Excel.

**Rate: 3 / 5** ⭐⭐⭐

Merge
-----

Mito supports multiple options for merging sheets, including _left/right/inner/outer joins_, and _lookups_, all nicely explained in the drop-down menu.

![Image 48](https://miro.medium.com/v2/resize:fit:700/1*18ohNFkIWF6gAssH9aEAvQ.gif)

**Merge.** Image by the author

Another great feature is the ability to quickly select the key variable and the columns to keep from each table. I really enjoyed that!

On the downsides, **multi-key merges** are not natively supported. However, the documentation covers this use case:

> If you want to use multiple columns as the merge key, try creating a new column and using the CONCAT function to combine all of the columns into one. Then, select that new column as the merge key!

Also, I didn’t manage to merge two sheets vertically — analogous of pandas `.concat()` —, for which an external pass is needed.

**Rate: 4 / 5** ⭐⭐⭐⭐

Dedup
-----

This is one of the things I always have to google when I need it. De-duplicate repeated rows with Mito is just a couple of clicks. It supports the combination of multiple columns and provides different options for the values to keep: _first, last, none_.

![Image 49](https://miro.medium.com/v2/resize:fit:700/1*TEPfaUU0ZM6SR0cl3YKHYA.gif)

**Dedup.** Image by the author

**Rate: 5 / 5** ⭐⭐⭐⭐⭐

Graphs
------

This is probably one of the top features I would look for in a tool like this. Mito does a nice job with this functionality and supports a wide choice of plot types including bar charts, line trends, boxplots and violin plots, heatmaps and more.

![Image 50](https://miro.medium.com/v2/resize:fit:700/1*R57kYIvkcvqra1TPq4YwDw.gif)

**Line charts.** Image by the author

![Image 51](https://miro.medium.com/v2/resize:fit:700/1*QO_LaSkvXbLvLaHAGiwFJA.gif)

**Distribution charts.** Image by the author

The flow through the interface is very smooth and the results are decent, with a bonus for the use of _plotly_ for interactive charts. Unfortunately, it is not possible to alter their appearance but that’s not a great concern for explorative analysis. Plus, the generated code can be leveraged as a basis for quick adaptations to the desired looks.

> But does Mito have the **WOW-factor**?

Univariate graphs are nice and functional, definitely a strong thumbs up!

The result is a bit less effective for multivariate plots though. Mito handles some functionalities but fails to represent the same information by groups.

![Image 52](https://miro.medium.com/v2/resize:fit:700/1*F0oy31qS-SPFQz61KVLx8Q.gif)

**Boxplot by multiple groups.** Image by the author

In the above example, the auto-generated code simply concatenates the values in the X-axis which is somewhat not intuitive in my opinion:

I think a better way to handle this would be adding the second x-variable as the _color argument_ instead:

Overall, a great solution for quick exploration that works in most of the common use cases. For more articulate needs and styling there’s some room for improvement.

**Rate: 4 / 5** ⭐⭐⭐⭐

Pivot table
-----------

Pivot tables are a way to summarize findings by means of aggregate statistics. Mito allows doing this very smoothly in an Excel-like fashion.

![Image 53](https://miro.medium.com/v2/resize:fit:700/1*l3n50yds6NimOBme6naafQ.gif)

**Pivot table.** Image by the author

The interface is really intuitive and supports all the aggregation functions you can think of. The formatting utils can then be used to better visualize the results or refine the output for later export and sharing.

Adding a choice on how to handle missing values would be a nice add-on for future developments.

**Rate: 5 / 5** ⭐⭐⭐⭐⭐

![Image 54](https://miro.medium.com/v2/resize:fit:700/0*V9VI1IN_hhV1pw5e)

Photo by [Sherman Yang](https://unsplash.com/@emp_creative?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Final thoughts
--------------

All in all Mito is a mature tool and does a great job, enabling the users to inspect the data visually and interact with them intuitively and efficiently. It covers pretty much all of the **most common use cases for exploratory data analysis** like checking values and distributions, editing and formatting data, merging sheets, creating pivot tables, and various kinds of plotting. All the operations are tracked and automatically converted to python code that performs the actions on the underlying pandas dataframes.

I appreciated the order of the generated code and the fact it contains comments to guide the users through it. Also, it is well optimized to exploit fast pandas implementations — e.g. it uses `.at()` instead of `.loc()` to set the value of a cell efficiently as per [pandas documentation](https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.at.html#pandas.DataFrame.at).

Also, a bonus goes for the **easy installation**, the **spot and comprehensive** [**documentation**](https://docs.trymito.io/) — which I found helpful while exploring the library — and the availability of a [**Discord channel**](https://discord.com/channels/885865606203736104/885865606748966924) **for assistance** — I got a reply even during the weekend!

In terms of limitations, I encountered two major missing features: the Excel-fashion _formula dragging_ and the possibility to _edit created columns cell-wise_ — instead of column-wise.

As further extensions or enrichment, I would love the possibility to _merge_ sheets _on multiple keys_ straight away rather than creating a concatenated key right for the purpose.  
Also, it would be nice to have an _automatic refresh_ of graphs or pivot tables _after filtering_.  
Finally, _multivariate plots_ are still incomplete. I think their enhancement may be the missing piece to finalize the tool for end-to-end data exploration within Mito.

Resources
---------

To give it a try, here are some link to more resources:

**Website:** [https://www.trymito.io/](https://www.trymito.io/)  
**YouTube:** [https://www.youtube.com/channel/UCN9o\_0m1fwCjigfIpnKr0oA/featured](https://www.youtube.com/channel/UCN9o_0m1fwCjigfIpnKr0oA/featured)  
**Github:** [https://github.com/mito-ds/monorepo](https://github.com/mito-ds/monorepo)

That’s all for this time! If you _liked this article_ and you’re interested in more _data analysis contents_, then **check my** [**stories**](https://medium.com/@luca.clissa) and **let me know what you think!**

## Metadata

```json
{
  "title": "Mito: Using pandas as a spreadsheet - Towards Data Science",
  "description": "Spreadsheets are a great solution to inspect new data, get a first grasp of their content and interact with them quickly and visually. However, when these tasks are to be performed frequently — as…",
  "url": "https://towardsdatascience.com/mito-using-pandas-as-a-spreadsheet-within-jupyter-lab-6a6bd04310a8",
  "content": "Review of the _mitosheet_ python package\n----------------------------------------\n\n[![Image 39: Luca Clissa](https://miro.medium.com/v2/resize:fill:88:88/1*wPQ1cGdbMxg5HvT5-OerOw.png)](https://medium.com/@luca.clissa?source=post_page---byline--6a6bd04310a8--------------------------------)\n\n[![Image 40: Towards Data Science](https://miro.medium.com/v2/resize:fill:48:48/1*CJe3891yB1A1mzMdqemkdg.jpeg)](https://towardsdatascience.com/?source=post_page---byline--6a6bd04310a8--------------------------------)\n\n![Image 41](https://miro.medium.com/v2/resize:fit:700/0*ORT67DoO9izFx5UU)\n\nPhoto by [Isaac Smith](https://unsplash.com/@isaacmsmith?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)\n\nSpreadsheets are a great solution to inspect new data, get a first grasp of their content and interact with them quickly and visually. However, when these tasks are to be performed frequently — as for typical workflows in data science projects — the advantage of spreadsheets-based tools like [Excel](https://www.microsoft.com/it-it/microsoft-365/excel) or [Google Sheets](https://www.google.com/intl/it/sheets/about/) is capped by the burden of manually repeating the same operations multiple times.\n\nProgramming languages offer a convenient alternative to automate the latter part, although possibly requiring some itching in the first pass through the data depending on the language and the user proficiency.\n\nIn this article we’re going to explore [**Mito**](https://www.trymito.io/), _a spreadsheet-like interface for pandas dataframes based on python_. In particular, I’ll guide you through its installation and main features, assessing the completeness, effectiveness and ease of use of Mito’s functionalities on a scale from 1 to 5.\n\n> **_Disclaimer_**_: This post is sponsored. However, it presents a critical and honest appraisal of the library and its performances._\n\nWhat is Mito?\n-------------\n\n[Mito is an open-source python library](https://github.com/mito-ds/monorepo) that combines the _intuitive and visual_ aspects of spreadsheets with the benefits of programming to _handle larger datasets_, provide _timely elaborations_ and create _repeatable processes_ easily.\n\nIn brief, Mito is a **Jupyter Lab interface** that allows users to **handle** data **as in a spreadsheet** while **automatically generating the corresponding python code** in the cell below.\n\nWho’s for?\n----------\n\nMito is just the perfect tool for old-school spreadsheet users — e.g. **Excel practitioners** —in transition to a programming-oriented paradigm.\n\nHowever, I would recommend Mito also to python programmers like me that get bored by copy-pasting the same boilerplate code for exploratory data analysis. I believe this is a convenient tool for **exploratory data analysis,** and a **good starting** point to quickly set up the bulk of the code and then apply some custom adjustments here and there.\n\nInstallation\n------------\n\nThe installation is pretty simple and requires just a [few steps](https://docs.trymito.io/getting-started/installing-mito) well described in the [documentation](https://docs.trymito.io/), e.g. for _conda_:\n\n\\# this article uses mitosheet version '0.1.392'  \nconda create -n mitoenv python=3.8  \nconda activate mitoenv  \npython -m pip install mitoinstaller  \npython -m mitoinstaller install\n\nI had a try on my _ubuntu 20.04_ platform and managed to succeed almost without a blink. Actually, I couldn’t complete `python -m pip install mitoinstaller` immediately as some dependencies weren’t resolved:\n\n(mitoenv) luca@ASUS-ROG:~/workspace/blog\\_mito$ python -m pip install mitoinstaller  \nCollecting mitoinstaller  \n  Downloading mitoinstaller-0.0.122.tar.gz (14 kB)  \n  Preparing metadata (setup.py) ... done  \nCollecting analytics-python  \n  Downloading analytics\\_python-1.4.0-py2.py3-none-any.whl (15 kB)  \nRequirement already satisfied: colorama in /home/luca/.local/lib/python3.8/site-packages (from mitoinstaller) (0.4.4)  \nCollecting termcolor  \n  Using cached termcolor-1.1.0.tar.gz (3.9 kB)  \n  Preparing metadata (setup.py) ... done  \nCollecting monotonic\\>\\=1.5  \n  Downloading monotonic-1.6-py2.py3-none-any.whl (8.2 kB)  \nCollecting backoff==1.10.0  \n  Downloading backoff-1.10.0-py2.py3-none-any.whl (31 kB)  \nRequirement already satisfied: python-dateutil\\>2.1 in /home/luca/.local/lib/python3.8/site-packages (from analytics-python-\\>mitoinstaller) (2.8.1)  \nCollecting six\\>\\=1.5  \n  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)  \nCollecting requests<3.0,\\>\\=2.7  \n  Downloading requests-2.27.1-py2.py3-none-any.whl (63 kB)  \n     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.1/63.1 KB 605.1 kB/s eta 0:00:00  \nCollecting certifi\\>\\=2017.4.17  \n  Downloading certifi-2021.10.8-py2.py3-none-any.whl (149 kB)  \n     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 149.2/149.2 KB 1.1 MB/s eta 0:00:00  \nCollecting urllib3<1.27,\\>\\=1.21.1  \n  Downloading urllib3-1.26.8-py2.py3-none-any.whl (138 kB)  \n     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 138.7/138.7 KB 1.4 MB/s eta 0:00:00  \nCollecting charset-normalizer~=2.0.0  \n  Downloading charset\\_normalizer-2.0.12-py3-none-any.whl (39 kB)  \nCollecting idna<4,\\>\\=2.5  \n  Downloading idna-3.3-py3-none-any.whl (61 kB)  \n     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 KB 1.6 MB/s eta 0:00:00  \nBuilding wheels for collected packages: mitoinstaller, termcolor  \n  Building wheel for mitoinstaller (setup.py) ... done  \n  Created wheel for mitoinstaller: filename=mitoinstaller-0.0.122-py3-none-any.whl size=19809 sha256=68b55bfd4dbc4f916f6cd1a19500aefdfab6f25f86737c2ae7c258264eff410f  \n  Stored in directory: /home/luca/.cache/pip/wheels/46/c6/8a/8b77ea33ddac40eff0b3e1847f84789d316e557e48bb0bc110  \n  Building wheel for termcolor (setup.py) ... done  \n  Created wheel for termcolor: filename=termcolor-1.1.0-py3-none-any.whl size=4848 sha256=84532fa74eca34fbe56efd5665ff9c8ebce197dc2a32254a19f145f97d6da515  \n  Stored in directory: /home/luca/.cache/pip/wheels/a0/16/9c/5473df82468f958445479c59e784896fa24f4a5fc024b0f501  \nSuccessfully built mitoinstaller termcolor  \nInstalling collected packages: termcolor, monotonic, certifi, urllib3, six, idna, charset-normalizer, backoff, requests, analytics-python, mitoinstaller  \nERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.  \nrequests-oauthlib 1.3.0 requires oauthlib\\>\\=3.0.0, which is not installed.  \npandas 1.2.2 requires pytz\\>\\=2017.3, which is not installed.  \noauth2client 4.1.3 requires httplib2\\>\\=0.9.1, which is not installed.  \nmoto 1.3.16.dev122 requires MarkupSafe<2.0, which is not installed.  \nmoto 1.3.16.dev122 requires more-itertools, which is not installed.  \nmoto 1.3.16.dev122 requires pytz, which is not installed.  \nmoto 1.3.16.dev122 requires zipp, which is not installed.  \ngoogle-api-core 1.26.3 requires packaging\\>\\=14.3, which is not installed.  \ngoogle-api-core 1.26.3 requires pytz, which is not installed.  \nSuccessfully installed analytics-python-1.4.0 backoff-1.10.0 certifi-2021.10.8 charset-normalizer-2.0.12 idna-3.3 mitoinstaller-0.0.122 monotonic-1.6 requests-2.27.1 six-1.16.0 termcolor-1.1.0 urllib3-1.26.8\n\nwhich led me to the following error when running `python -m mitoinstaller install`:\n\n(mitoenv) luca@ASUS-ROG:~/workspace/blog\\_mito$ python -m mitoinstaller install  \nStarting install...  \nCreate mito user  \nUpgrade mitoinstaller  \nCheck dependencies  \nRemove mitosheet3 if present  \nInstall mitosheet  \nCreate import mito startup file  \nCreating a Mitosheet starter notebook  \nStart JupyterLab  \nTraceback (most recent call last):  \n  File \"/home/luca/anaconda3/envs/mitoenv/bin/jupyter-lab\", line 5, in <module\\>  \n    from jupyterlab.labapp import main  \n  File \"/home/luca/anaconda3/envs/mitoenv/lib/python3.8/site-packages/jupyterlab/labapp.py\", line 13, in <module\\>  \n    from jupyter\\_server.serverapp import flags  \n  File \"/home/luca/anaconda3/envs/mitoenv/lib/python3.8/site-packages/jupyter\\_server/serverapp.py\", line 38, in <module\\>  \n    from jinja2 import Environment, FileSystemLoader  \n  File \"/home/luca/.local/lib/python3.8/site-packages/jinja2/\\_\\_init\\_\\_.py\", line 12, in <module\\>  \n    from .environment import Environment  \n  File \"/home/luca/.local/lib/python3.8/site-packages/jinja2/environment.py\", line 25, in <module\\>  \n    from .defaults import BLOCK\\_END\\_STRING  \n  File \"/home/luca/.local/lib/python3.8/site-packages/jinja2/defaults.py\", line 3, in <module\\>  \n    from .filters import FILTERS as DEFAULT\\_FILTERS  # noqa: F401  \n  File \"/home/luca/.local/lib/python3.8/site-packages/jinja2/filters.py\", line 13, in <module\\>  \n    from markupsafe import soft\\_unicode  \nImportError: cannot import name 'soft\\_unicode' from 'markupsafe' (/home/luca/anaconda3/envs/mitoenv/lib/python3.8/site-packages/markupsafe/\\_\\_init\\_\\_.py)\n\nHowever, this may depend on my local configuration and was easily fixed by installing missing dependencies singularly:\n\npip install mitoinstaller  \npip install requests-oauthlib  \npip install oauth2client  \npip install pandas  \npip install moto  \npip install google-api-core\n\n**Rate: 4 / 5** ⭐⭐⭐⭐\n\n**Functionalities**\n-------------------\n\nMito provides most (almost all) spreadsheets functionalities in a very intuitive and efficient manner.\n\nImport data\n-----------\n\nMito supports importing data from _csv_ and _xlsx_ files. The import itself is as easy as importing the _mitosheet_ package and running `mitosheet.sheet(). `The first time the user is asked to register and choose the desired [plan](https://www.trymito.io/plans). After that, you can simply follow a neat graphical interface to select data files to import.\n\n![Image 42](https://miro.medium.com/v2/resize:fit:700/1*drcnCq_UUlg38kN2cP1BWg.gif)\n\n**Data import.** Image by the author\n\nAlternatively, Mito supports also pandas dataframe for each sheet as `mitosheet.sheet(df1, df2)`.\n\nA minor limitation is that you can’t customize data type at import for _csv_ files — you can fix it later with data formatting though.\n\n**Rate: 4 / 5** ⭐⭐⭐⭐\n\nCheck values and distributions\n------------------------------\n\nThe first step of every data science project is to explore the data, check the values and explore variables’ distribution. With Mito this is real quick and intuitive.\n\n![Image 43](https://miro.medium.com/v2/resize:fit:700/1*qIVqmk-rcB_MscKlnIa6kQ.gif)\n\n**Data values and distribution.** Image by the author\n\nMy experience was very smooth for different kinds of data types and it covered all the use cases I can think of. A sound thumbs-up for this util!\n\n**Rate: 5 / 5** ⭐⭐⭐⭐⭐\n\n**Filter and sort**\n-------------------\n\nFiltering and sorting are also very common operations when dealing with data. Mito allows filtering both based on conditions and by directly excluding unwanted values.\n\n![Image 44](https://miro.medium.com/v2/resize:fit:700/1*g0cgb1uux0s0nreBEQGwoA.gif)\n\n**Filtering.** Image by the author\n\nSorting is also effective, although ordering based on multiple columns is not natively supported. A possible workaround is to concatenate such variables and sort by the resulting column.\n\n**Rate: 4 / 5** ⭐⭐⭐⭐\n\nFormatting\n----------\n\nNice data formatting is key for visual exploration. Mito provides plenty of options to arrange their content for any need.\n\n![Image 45](https://miro.medium.com/v2/resize:fit:700/1*Bq5aVlHbwoe1yQHsLW3Y3Q.gif)\n\n**Data formatting.** Image by the author\n\n**Rate: 5 / 5** ⭐⭐⭐⭐⭐\n\n**Data types**\n--------------\n\nHandling data types is often needed during pre-processing in order to prepare the data appropriately for the following analysis pipeline. Mito does a nice job also in this respect, balancing the initial lack of customization during data import.\n\n![Image 46](https://miro.medium.com/v2/resize:fit:700/1*VuXg8zd5dReTSNHt1OA_cQ.gif)\n\n**Data types.** Image by the author\n\nApart from standard data types like `int` , `float`, `str` and `bool` , I tested Mito against one of the biggest data scientists’ nightmares: _dates._ The conversion from string to `datetime` is seamless, and you can play around with Excel formulas for more customization. Nicely done!\n\n**Rate: 5 / 5** ⭐⭐⭐⭐⭐\n\nData manipulation\n-----------------\n\nMito supports several kinds of data manipulation exploiting the most used Excel formulas. _Adding and deleting columns_, as well as _editing_ single cells or entire variables are just a few clicks away.\n\n![Image 47](https://miro.medium.com/v2/resize:fit:700/1*j_oL4uDPmuLvEuhJhFfr8w.gif)\n\n**Data manipulation.** Image by the author\n\nI really appreciated the nice interface with suggestions as you type commands, plus the `Search Functionality` box in the top-right corner.\n\nHowever, I didn’t manage to replicate one of Excel’s killer features: **dragging formulas**. That’s a pity and I think it should be one of the top priorities for future developments.\n\nAlso, added columns are not editable cell-wise — which means you can just edit new columns as a bulk. Again, this misses out on the convenience of Excel.\n\n**Rate: 3 / 5** ⭐⭐⭐\n\nMerge\n-----\n\nMito supports multiple options for merging sheets, including _left/right/inner/outer joins_, and _lookups_, all nicely explained in the drop-down menu.\n\n![Image 48](https://miro.medium.com/v2/resize:fit:700/1*18ohNFkIWF6gAssH9aEAvQ.gif)\n\n**Merge.** Image by the author\n\nAnother great feature is the ability to quickly select the key variable and the columns to keep from each table. I really enjoyed that!\n\nOn the downsides, **multi-key merges** are not natively supported. However, the documentation covers this use case:\n\n> If you want to use multiple columns as the merge key, try creating a new column and using the CONCAT function to combine all of the columns into one. Then, select that new column as the merge key!\n\nAlso, I didn’t manage to merge two sheets vertically — analogous of pandas `.concat()` —, for which an external pass is needed.\n\n**Rate: 4 / 5** ⭐⭐⭐⭐\n\nDedup\n-----\n\nThis is one of the things I always have to google when I need it. De-duplicate repeated rows with Mito is just a couple of clicks. It supports the combination of multiple columns and provides different options for the values to keep: _first, last, none_.\n\n![Image 49](https://miro.medium.com/v2/resize:fit:700/1*TEPfaUU0ZM6SR0cl3YKHYA.gif)\n\n**Dedup.** Image by the author\n\n**Rate: 5 / 5** ⭐⭐⭐⭐⭐\n\nGraphs\n------\n\nThis is probably one of the top features I would look for in a tool like this. Mito does a nice job with this functionality and supports a wide choice of plot types including bar charts, line trends, boxplots and violin plots, heatmaps and more.\n\n![Image 50](https://miro.medium.com/v2/resize:fit:700/1*R57kYIvkcvqra1TPq4YwDw.gif)\n\n**Line charts.** Image by the author\n\n![Image 51](https://miro.medium.com/v2/resize:fit:700/1*QO_LaSkvXbLvLaHAGiwFJA.gif)\n\n**Distribution charts.** Image by the author\n\nThe flow through the interface is very smooth and the results are decent, with a bonus for the use of _plotly_ for interactive charts. Unfortunately, it is not possible to alter their appearance but that’s not a great concern for explorative analysis. Plus, the generated code can be leveraged as a basis for quick adaptations to the desired looks.\n\n> But does Mito have the **WOW-factor**?\n\nUnivariate graphs are nice and functional, definitely a strong thumbs up!\n\nThe result is a bit less effective for multivariate plots though. Mito handles some functionalities but fails to represent the same information by groups.\n\n![Image 52](https://miro.medium.com/v2/resize:fit:700/1*F0oy31qS-SPFQz61KVLx8Q.gif)\n\n**Boxplot by multiple groups.** Image by the author\n\nIn the above example, the auto-generated code simply concatenates the values in the X-axis which is somewhat not intuitive in my opinion:\n\nI think a better way to handle this would be adding the second x-variable as the _color argument_ instead:\n\nOverall, a great solution for quick exploration that works in most of the common use cases. For more articulate needs and styling there’s some room for improvement.\n\n**Rate: 4 / 5** ⭐⭐⭐⭐\n\nPivot table\n-----------\n\nPivot tables are a way to summarize findings by means of aggregate statistics. Mito allows doing this very smoothly in an Excel-like fashion.\n\n![Image 53](https://miro.medium.com/v2/resize:fit:700/1*l3n50yds6NimOBme6naafQ.gif)\n\n**Pivot table.** Image by the author\n\nThe interface is really intuitive and supports all the aggregation functions you can think of. The formatting utils can then be used to better visualize the results or refine the output for later export and sharing.\n\nAdding a choice on how to handle missing values would be a nice add-on for future developments.\n\n**Rate: 5 / 5** ⭐⭐⭐⭐⭐\n\n![Image 54](https://miro.medium.com/v2/resize:fit:700/0*V9VI1IN_hhV1pw5e)\n\nPhoto by [Sherman Yang](https://unsplash.com/@emp_creative?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)\n\nFinal thoughts\n--------------\n\nAll in all Mito is a mature tool and does a great job, enabling the users to inspect the data visually and interact with them intuitively and efficiently. It covers pretty much all of the **most common use cases for exploratory data analysis** like checking values and distributions, editing and formatting data, merging sheets, creating pivot tables, and various kinds of plotting. All the operations are tracked and automatically converted to python code that performs the actions on the underlying pandas dataframes.\n\nI appreciated the order of the generated code and the fact it contains comments to guide the users through it. Also, it is well optimized to exploit fast pandas implementations — e.g. it uses `.at()` instead of `.loc()` to set the value of a cell efficiently as per [pandas documentation](https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.at.html#pandas.DataFrame.at).\n\nAlso, a bonus goes for the **easy installation**, the **spot and comprehensive** [**documentation**](https://docs.trymito.io/) — which I found helpful while exploring the library — and the availability of a [**Discord channel**](https://discord.com/channels/885865606203736104/885865606748966924) **for assistance** — I got a reply even during the weekend!\n\nIn terms of limitations, I encountered two major missing features: the Excel-fashion _formula dragging_ and the possibility to _edit created columns cell-wise_ — instead of column-wise.\n\nAs further extensions or enrichment, I would love the possibility to _merge_ sheets _on multiple keys_ straight away rather than creating a concatenated key right for the purpose.  \nAlso, it would be nice to have an _automatic refresh_ of graphs or pivot tables _after filtering_.  \nFinally, _multivariate plots_ are still incomplete. I think their enhancement may be the missing piece to finalize the tool for end-to-end data exploration within Mito.\n\nResources\n---------\n\nTo give it a try, here are some link to more resources:\n\n**Website:** [https://www.trymito.io/](https://www.trymito.io/)  \n**YouTube:** [https://www.youtube.com/channel/UCN9o\\_0m1fwCjigfIpnKr0oA/featured](https://www.youtube.com/channel/UCN9o_0m1fwCjigfIpnKr0oA/featured)  \n**Github:** [https://github.com/mito-ds/monorepo](https://github.com/mito-ds/monorepo)\n\nThat’s all for this time! If you _liked this article_ and you’re interested in more _data analysis contents_, then **check my** [**stories**](https://medium.com/@luca.clissa) and **let me know what you think!**",
  "publishedTime": "2022-03-16T14:19:26.533Z",
  "usage": {
    "tokens": 5406
  }
}
```
