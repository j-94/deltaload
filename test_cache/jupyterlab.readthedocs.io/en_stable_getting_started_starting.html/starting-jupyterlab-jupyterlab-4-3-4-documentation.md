---
title: Starting JupyterLab — JupyterLab 4.3.4 documentation
description: 
url: https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html
timestamp: 2025-01-20T15:48:30.602Z
domain: jupyterlab.readthedocs.io
path: en_stable_getting_started_starting.html
---

# Starting JupyterLab — JupyterLab 4.3.4 documentation



## Content

Starting JupyterLab — JupyterLab 4.3.4 documentation
===============         

[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html#main-content)

Back to top Ctrl+K

 [![Image 5: JupyterLab](https://jupyterlab.readthedocs.io/en/stable/_static/logo-rectangle.svg) ![Image 6: JupyterLab](https://jupyterlab.readthedocs.io/en/stable/_static/logo-rectangle-dark.svg)](https://jupyterlab.readthedocs.io/en/stable/index.html)

Choose version

*   [Get Started](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)
*   [User Guide](https://jupyterlab.readthedocs.io/en/stable/user/index.html)
*   [Develop Extensions](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html)
*   [Contribute](https://jupyterlab.readthedocs.io/en/stable/developer/contributing.html)
*   [Privacy policies](https://jupyterlab.readthedocs.io/en/stable/privacy_policies.html)

Search Ctrl+K

*   [![Image 7: jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/ "jupyter.org")
*   [GitHub](https://github.com/jupyterlab/jupyterlab "GitHub")
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17 "Discourse")
*   [Zulip](https://jupyter.zulipchat.com/channel/469762-jupyterlab "Zulip")

Search Ctrl+K

*   [Get Started](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)
*   [User Guide](https://jupyterlab.readthedocs.io/en/stable/user/index.html)
*   [Develop Extensions](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html)
*   [Contribute](https://jupyterlab.readthedocs.io/en/stable/developer/contributing.html)
*   [Privacy policies](https://jupyterlab.readthedocs.io/en/stable/privacy_policies.html)

*   [![Image 8: jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/ "jupyter.org")
*   [GitHub](https://github.com/jupyterlab/jupyterlab "GitHub")
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17 "Discourse")
*   [Zulip](https://jupyter.zulipchat.com/channel/469762-jupyterlab "Zulip")

Section Navigation

*   [Installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
*   [Starting JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html#)
*   [Reporting an issue](https://jupyterlab.readthedocs.io/en/stable/getting_started/issue.html)
*   [Frequently Asked Questions (FAQ)](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html)
*   [JupyterLab Changelog](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html)
*   [JupyterLab Accessibility Statement](https://jupyterlab.readthedocs.io/en/stable/getting_started/accessibility.html)
*   [Version lifecycle](https://jupyterlab.readthedocs.io/en/stable/getting_started/lifecycle.html)

*   [](https://jupyterlab.readthedocs.io/en/stable/index.html)
*   [Get Started](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)
*   Starting JupyterLab

Starting JupyterLab[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html#starting-jupyterlab "Link to this heading")
============================================================================================================================================

Start JupyterLab using:

jupyter lab

JupyterLab will open automatically in your browser.

If your notebook files are not in the current directory, you can pass your working directory path as argument when starting JupyterLab. Avoid running it from your root volume (e.g. `C:\` on Windows or `/` on Linux) to limit the risk of modifying system files.

Example:

#Windows Example
jupyter lab \--notebook-dir\=E:/ \--preferred-dir E:/Documents/Somewhere/Else
#Linux Example
jupyter lab \--notebook-dir\=/var/ \--preferred-dir /var/www/html/example-app/

You may access JupyterLab by entering the notebook server’s [URL](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#urls) into the browser. JupyterLab sessions always reside in a [workspace](https://jupyterlab.readthedocs.io/en/stable/user/workspaces.html#workspaces). The default workspace is the main `/lab` URL:

http(s)://<server:port\>/<lab-location\>/lab

Like the classic notebook, JupyterLab provides a way for users to copy URLs that [open a specific notebook or file](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#url-tree). Additionally, JupyterLab URLs are an advanced part of the user interface that allows for managing [workspaces](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#url-workspaces). To learn more about URLs in Jupyterlab, visit [JupyterLab URLs](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#urls).

JupyterLab runs on top of Jupyter Server, so see the [security section](https://jupyter-server.readthedocs.io/en/latest/operators/security.html) of Jupyter Server’s documentation for security-related information.

[previous Installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html "previous page")[next Reporting an issue](https://jupyterlab.readthedocs.io/en/stable/getting_started/issue.html "next page")

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.3.x/docs/source/getting_started/starting.rst)

### This Page

*   [Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/getting_started/starting.rst.txt)

© Copyright 2018-2025, Project Jupyter.  
The Jupyter Trademark is registered with the U.S. Patent & Trademark Office.

Built with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.16.1.

## Metadata

```json
{
  "title": "Starting JupyterLab — JupyterLab 4.3.4 documentation",
  "description": "",
  "url": "https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html",
  "content": "Starting JupyterLab — JupyterLab 4.3.4 documentation\n===============         \n\n[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html#main-content)\n\nBack to top Ctrl+K\n\n [![Image 5: JupyterLab](https://jupyterlab.readthedocs.io/en/stable/_static/logo-rectangle.svg) ![Image 6: JupyterLab](https://jupyterlab.readthedocs.io/en/stable/_static/logo-rectangle-dark.svg)](https://jupyterlab.readthedocs.io/en/stable/index.html)\n\nChoose version\n\n*   [Get Started](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)\n*   [User Guide](https://jupyterlab.readthedocs.io/en/stable/user/index.html)\n*   [Develop Extensions](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html)\n*   [Contribute](https://jupyterlab.readthedocs.io/en/stable/developer/contributing.html)\n*   [Privacy policies](https://jupyterlab.readthedocs.io/en/stable/privacy_policies.html)\n\nSearch Ctrl+K\n\n*   [![Image 7: jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/ \"jupyter.org\")\n*   [GitHub](https://github.com/jupyterlab/jupyterlab \"GitHub\")\n*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17 \"Discourse\")\n*   [Zulip](https://jupyter.zulipchat.com/channel/469762-jupyterlab \"Zulip\")\n\nSearch Ctrl+K\n\n*   [Get Started](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)\n*   [User Guide](https://jupyterlab.readthedocs.io/en/stable/user/index.html)\n*   [Develop Extensions](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html)\n*   [Contribute](https://jupyterlab.readthedocs.io/en/stable/developer/contributing.html)\n*   [Privacy policies](https://jupyterlab.readthedocs.io/en/stable/privacy_policies.html)\n\n*   [![Image 8: jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/ \"jupyter.org\")\n*   [GitHub](https://github.com/jupyterlab/jupyterlab \"GitHub\")\n*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17 \"Discourse\")\n*   [Zulip](https://jupyter.zulipchat.com/channel/469762-jupyterlab \"Zulip\")\n\nSection Navigation\n\n*   [Installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)\n*   [Starting JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html#)\n*   [Reporting an issue](https://jupyterlab.readthedocs.io/en/stable/getting_started/issue.html)\n*   [Frequently Asked Questions (FAQ)](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html)\n*   [JupyterLab Changelog](https://jupyterlab.readthedocs.io/en/stable/getting_started/changelog.html)\n*   [JupyterLab Accessibility Statement](https://jupyterlab.readthedocs.io/en/stable/getting_started/accessibility.html)\n*   [Version lifecycle](https://jupyterlab.readthedocs.io/en/stable/getting_started/lifecycle.html)\n\n*   [](https://jupyterlab.readthedocs.io/en/stable/index.html)\n*   [Get Started](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)\n*   Starting JupyterLab\n\nStarting JupyterLab[#](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html#starting-jupyterlab \"Link to this heading\")\n============================================================================================================================================\n\nStart JupyterLab using:\n\njupyter lab\n\nJupyterLab will open automatically in your browser.\n\nIf your notebook files are not in the current directory, you can pass your working directory path as argument when starting JupyterLab. Avoid running it from your root volume (e.g. `C:\\` on Windows or `/` on Linux) to limit the risk of modifying system files.\n\nExample:\n\n#Windows Example\njupyter lab \\--notebook-dir\\=E:/ \\--preferred-dir E:/Documents/Somewhere/Else\n#Linux Example\njupyter lab \\--notebook-dir\\=/var/ \\--preferred-dir /var/www/html/example-app/\n\nYou may access JupyterLab by entering the notebook server’s [URL](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#urls) into the browser. JupyterLab sessions always reside in a [workspace](https://jupyterlab.readthedocs.io/en/stable/user/workspaces.html#workspaces). The default workspace is the main `/lab` URL:\n\nhttp(s)://<server:port\\>/<lab-location\\>/lab\n\nLike the classic notebook, JupyterLab provides a way for users to copy URLs that [open a specific notebook or file](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#url-tree). Additionally, JupyterLab URLs are an advanced part of the user interface that allows for managing [workspaces](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#url-workspaces). To learn more about URLs in Jupyterlab, visit [JupyterLab URLs](https://jupyterlab.readthedocs.io/en/stable/user/urls.html#urls).\n\nJupyterLab runs on top of Jupyter Server, so see the [security section](https://jupyter-server.readthedocs.io/en/latest/operators/security.html) of Jupyter Server’s documentation for security-related information.\n\n[previous Installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html \"previous page\")[next Reporting an issue](https://jupyterlab.readthedocs.io/en/stable/getting_started/issue.html \"next page\")\n\n[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.3.x/docs/source/getting_started/starting.rst)\n\n### This Page\n\n*   [Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/getting_started/starting.rst.txt)\n\n© Copyright 2018-2025, Project Jupyter.  \nThe Jupyter Trademark is registered with the U.S. Patent & Trademark Office.\n\nBuilt with the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.16.1.",
  "usage": {
    "tokens": 1470
  }
}
```
