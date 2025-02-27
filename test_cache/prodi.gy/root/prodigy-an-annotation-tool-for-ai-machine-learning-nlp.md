---
title: Prodigy  · An annotation tool for AI, Machine Learning & NLP
description: A downloadable annotation tool for LLMs, NLP and computer vision tasks such as named entity recognition, text classification, object detection, image segmentation, evaluation and more.
url: https://prodi.gy/
timestamp: 2025-01-20T15:49:52.459Z
domain: prodi.gy
path: root
---

# Prodigy  · An annotation tool for AI, Machine Learning & NLP


A downloadable annotation tool for LLMs, NLP and computer vision tasks such as named entity recognition, text classification, object detection, image segmentation, evaluation and more.


## Content

Build AI systems that  
do exactly what **you** want
----------------------------------------------------

A modern data development experience  
from the makers of[](https://spacy.io/)
------------------------------------------------------------------------------

`prodigyner.llm.correctnews_articles./config.cfg./news.jsonl`

This live demo requires JavaScript to be enabled.

Efficiently define, train and evaluate
--------------------------------------

Prodigy is an extensible annotation tool that gives you a new way to build custom AI systems. Define your classification scheme with real-world examples rather than just prompts, and let powerful models assist – no machine learning experience required.

`prodigytrain./information_extraction--ner news_ner--textcat news_textcat=========== Training pipeline ===========48% | ████████████████`

Take back **control**
---------------------

Prodigy runs entirely under your control, making it suitable for even the strictest privacy requirements. You can download it and run it locally right out of the box, or adapt it to serve your infrastructure needs. The models you produce are yours as well, with absolutely no lock-in.

```
@prodigy.recipe(    "my_custom_recipe"    dataset=Arg(help="dataset to save answers to"),    source=Arg("--source", help="data to load"),    label=Arg("--label", "-l", help="comma-separated label(s)"),)def recipe(dataset: str, source: str, dataset: List[str]):    ...
```

#### Terminal

`prodigymy_custom_recipeannotations./samples.jsonl--label PERSON,PRODUCT`

Built for **customization** and extension
-----------------------------------------

Prodigy lets you define fully custom data feeds and interfaces, letting the computer work instead of the human. By breaking down tasks into smaller pieces and automating whatever you can, you can make annotation over [10× as efficient](https://explosion.ai/blog/sp-global-commodities).

*   [](https://prodi.gy/industries/banking-finance#case-study)
*   [](https://prodi.gy/industries/media-content-creation#case-study)

Real-world case studies
-----------------------

What others say
---------------

> [![Image 21](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_chris.jpg&w=96&q=75) ### Christopher Ewen Senior Product Manager](https://prodi.gy/industries/banking-finance#case-study)

> ![Image 22](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_ahalterman.jpg&w=96&q=75)
> 
> ### Andy Halterman
> 
> Researcher
> 
> A lack of labeled data held geoparsing back for years. It took a week to fix that with Prodigy.

> [![Image 23](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_india.jpg&w=96&q=75) ### India Kerle Data Scientist](https://prodi.gy/industries/research-education#case-study)

> [![Image 24](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_anna.png&w=96&q=75) ### Anna Vissens Lead Data Scientist](https://prodi.gy/industries/media-content-creation#case-study)

> [![Image 25](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_cheyanne.png&w=96&q=75) ### Cheyanne Baird NLP Research Scientist](https://prodi.gy/industries/conversation-insights#case-study)

> ### Raphael Cohen
> 
> Head of Research
> 
> Prodigy is by far the best ROI we had on any tool!

> ![Image 26](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_daniel.jpg&w=96&q=75)
> 
> ### Daniel Bourke
> 
> Founder
> 
> We love Prodigy! I've tried many data labelling tools and chose Prodigy specifically for the simplicity. Image folder plus text file to database is perfect for our needs. If a model is one of our main products, good data is basically the same as good code.

> ### Antonio Polo de Alvarado
> 
> ML Engineer
> 
> I have been working with Prodigy these last few weeks and I can say that it is probably (if not the best) one of the best NLP tools.

> ![Image 27](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_rebecca.jpg&w=96&q=75)
> 
> ### Rebecca Bilbro
> 
> Founder & CTO
> 
> Prodigy’s interface is incredibly intuitive! It elevates data labeling to a first-order concern in the ML workflow, enables us to collaborate on measures of inter-rater reliability and makes the labeling options super unambiguous for data annotators.

Frequently Asked Questions
--------------------------

What makes Prodigy different from other annotation solutions?Prodigy is a downloadable developer tool for creating training and evaluation data for machine learning models. You can use Prodigy to build custom AI systems specific to your use case that you can own and control. Prodigy is a Python package and library that includes a web application. You can customize Prodigy with your own Python functions, and mix and match frontend components to make your own annotation experience.

Prodigy integrates tighly with spaCy, but can also be used with any other libraries and tools. The library includes a range of pre-built workflows and command-line commands for various common tasks, and components for implementing your own workflow scripts. Your scripts can specify how the data is loaded and saved and even define custom HTML and JavaScript. The web application is optimized for fast, intuitive and efficient annotation.

Is our data really private? How does it work?Prodigy runs entirely on your own machines and never “phones home” or connects to our or any third-party servers. Once installed, you can even operate it on an entirely air-gapped machine without internet connection. All data and models you use and create stay entirely private and under your control.

Which models can I use and train with Prodigy?Prodigy lets you train any models you can train in Python. It comes with first-class support for our NLP library [spaCy](https://spacy.io/) via the built-in [` train`](https://prodi.gy/teams/recipes/train) recipe, as well as plugins for using and training [Hugging Face models](https://prodi.gy/docs/plugins#hf). It also integrates with the major [Large Language Model (LLM)](https://prodi.gy/docs/large-language-models) API providers out-of-the-box.

All data you create is accessible via a convenient [Python API](https://prodi.gy/docs/database#database) and command-line interface, making it easy to implement training for custom models with standard libraries like [PyTorch](https://pytorch.org/) or [TensorFlow](https://www.tensorflow.org/), both in the cloud, as well as in local setups or environments like [Jupyter](https://jupyter.org/).

How customizable are Prodigy’s workflows and interfaces?Prodigy allows for extensive customization. A range of built-in settings makes it easy for non-experts to customize the experience, and the developer API and SDK lets you integrate the tool into your existing workflows and build powerful extensions for custom use cases.

At the core of Prodigy’s developer experience are "recipes", Python functions that describe a workflow. Recipes can implement custom data processing and model training logic, integrate with third-party or internal libraries and tools and provide reusable workflows for your team that can be run without requiring programming or machine learning expertise. Prodigy also allows combining interfaces to build fully custom solutions, as well as implementing your own interactive interfaces with HTML, CSS and JavaScript.

What expertise does my team need to use Prodigy?Prodigy is designed as a developer tool and assumes basic familiarity with the Python programming language and the command line. We also provide extensive [documentation](https://prodi.gy/docs) and examples to help you get started. Once you’ve set up an annotation task, the web application makes it easy for anyone to create annotations, no programming experience required.

Which cloud providers does Prodigy support?Prodigy provides a standard Python web server and application that can be deployed on any cloud provider of your choice, including entirely on-premise. You can read more about deployment options and instructions [here](https://prodi.gy/docs/deployment).

Do you have special offers for researchers and universities?We’re always happy to support [research projects](https://prodi.gy/industries/research-education), and researchers at degree-granting academic institutions can apply for an interim license to use Prodigy for free. To claim your research license, [email us](mailto:contact@explosion.ai?subject=Prodigy%20Research%20License) and include your university details.

## Metadata

```json
{
  "title": "Prodigy  · An annotation tool for AI, Machine Learning & NLP",
  "description": "A downloadable annotation tool for LLMs, NLP and computer vision tasks such as named entity recognition, text classification, object detection, image segmentation, evaluation and more.",
  "url": "https://prodi.gy/",
  "content": "Build AI systems that  \ndo exactly what **you** want\n----------------------------------------------------\n\nA modern data development experience  \nfrom the makers of[](https://spacy.io/)\n------------------------------------------------------------------------------\n\n`prodigyner.llm.correctnews_articles./config.cfg./news.jsonl`\n\nThis live demo requires JavaScript to be enabled.\n\nEfficiently define, train and evaluate\n--------------------------------------\n\nProdigy is an extensible annotation tool that gives you a new way to build custom AI systems. Define your classification scheme with real-world examples rather than just prompts, and let powerful models assist – no machine learning experience required.\n\n`prodigytrain./information_extraction--ner news_ner--textcat news_textcat=========== Training pipeline ===========48% | ████████████████`\n\nTake back **control**\n---------------------\n\nProdigy runs entirely under your control, making it suitable for even the strictest privacy requirements. You can download it and run it locally right out of the box, or adapt it to serve your infrastructure needs. The models you produce are yours as well, with absolutely no lock-in.\n\n```\n@prodigy.recipe(    \"my_custom_recipe\"    dataset=Arg(help=\"dataset to save answers to\"),    source=Arg(\"--source\", help=\"data to load\"),    label=Arg(\"--label\", \"-l\", help=\"comma-separated label(s)\"),)def recipe(dataset: str, source: str, dataset: List[str]):    ...\n```\n\n#### Terminal\n\n`prodigymy_custom_recipeannotations./samples.jsonl--label PERSON,PRODUCT`\n\nBuilt for **customization** and extension\n-----------------------------------------\n\nProdigy lets you define fully custom data feeds and interfaces, letting the computer work instead of the human. By breaking down tasks into smaller pieces and automating whatever you can, you can make annotation over [10× as efficient](https://explosion.ai/blog/sp-global-commodities).\n\n*   [](https://prodi.gy/industries/banking-finance#case-study)\n*   [](https://prodi.gy/industries/media-content-creation#case-study)\n\nReal-world case studies\n-----------------------\n\nWhat others say\n---------------\n\n> [![Image 21](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_chris.jpg&w=96&q=75) ### Christopher Ewen Senior Product Manager](https://prodi.gy/industries/banking-finance#case-study)\n\n> ![Image 22](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_ahalterman.jpg&w=96&q=75)\n> \n> ### Andy Halterman\n> \n> Researcher\n> \n> A lack of labeled data held geoparsing back for years. It took a week to fix that with Prodigy.\n\n> [![Image 23](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_india.jpg&w=96&q=75) ### India Kerle Data Scientist](https://prodi.gy/industries/research-education#case-study)\n\n> [![Image 24](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_anna.png&w=96&q=75) ### Anna Vissens Lead Data Scientist](https://prodi.gy/industries/media-content-creation#case-study)\n\n> [![Image 25](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_cheyanne.png&w=96&q=75) ### Cheyanne Baird NLP Research Scientist](https://prodi.gy/industries/conversation-insights#case-study)\n\n> ### Raphael Cohen\n> \n> Head of Research\n> \n> Prodigy is by far the best ROI we had on any tool!\n\n> ![Image 26](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_daniel.jpg&w=96&q=75)\n> \n> ### Daniel Bourke\n> \n> Founder\n> \n> We love Prodigy! I've tried many data labelling tools and chose Prodigy specifically for the simplicity. Image folder plus text file to database is perfect for our needs. If a model is one of our main products, good data is basically the same as good code.\n\n> ### Antonio Polo de Alvarado\n> \n> ML Engineer\n> \n> I have been working with Prodigy these last few weeks and I can say that it is probably (if not the best) one of the best NLP tools.\n\n> ![Image 27](https://prodi.gy/_next/image?url=%2Flanding%2Ftestimonial_rebecca.jpg&w=96&q=75)\n> \n> ### Rebecca Bilbro\n> \n> Founder & CTO\n> \n> Prodigy’s interface is incredibly intuitive! It elevates data labeling to a first-order concern in the ML workflow, enables us to collaborate on measures of inter-rater reliability and makes the labeling options super unambiguous for data annotators.\n\nFrequently Asked Questions\n--------------------------\n\nWhat makes Prodigy different from other annotation solutions?Prodigy is a downloadable developer tool for creating training and evaluation data for machine learning models. You can use Prodigy to build custom AI systems specific to your use case that you can own and control. Prodigy is a Python package and library that includes a web application. You can customize Prodigy with your own Python functions, and mix and match frontend components to make your own annotation experience.\n\nProdigy integrates tighly with spaCy, but can also be used with any other libraries and tools. The library includes a range of pre-built workflows and command-line commands for various common tasks, and components for implementing your own workflow scripts. Your scripts can specify how the data is loaded and saved and even define custom HTML and JavaScript. The web application is optimized for fast, intuitive and efficient annotation.\n\nIs our data really private? How does it work?Prodigy runs entirely on your own machines and never “phones home” or connects to our or any third-party servers. Once installed, you can even operate it on an entirely air-gapped machine without internet connection. All data and models you use and create stay entirely private and under your control.\n\nWhich models can I use and train with Prodigy?Prodigy lets you train any models you can train in Python. It comes with first-class support for our NLP library [spaCy](https://spacy.io/) via the built-in [` train`](https://prodi.gy/teams/recipes/train) recipe, as well as plugins for using and training [Hugging Face models](https://prodi.gy/docs/plugins#hf). It also integrates with the major [Large Language Model (LLM)](https://prodi.gy/docs/large-language-models) API providers out-of-the-box.\n\nAll data you create is accessible via a convenient [Python API](https://prodi.gy/docs/database#database) and command-line interface, making it easy to implement training for custom models with standard libraries like [PyTorch](https://pytorch.org/) or [TensorFlow](https://www.tensorflow.org/), both in the cloud, as well as in local setups or environments like [Jupyter](https://jupyter.org/).\n\nHow customizable are Prodigy’s workflows and interfaces?Prodigy allows for extensive customization. A range of built-in settings makes it easy for non-experts to customize the experience, and the developer API and SDK lets you integrate the tool into your existing workflows and build powerful extensions for custom use cases.\n\nAt the core of Prodigy’s developer experience are \"recipes\", Python functions that describe a workflow. Recipes can implement custom data processing and model training logic, integrate with third-party or internal libraries and tools and provide reusable workflows for your team that can be run without requiring programming or machine learning expertise. Prodigy also allows combining interfaces to build fully custom solutions, as well as implementing your own interactive interfaces with HTML, CSS and JavaScript.\n\nWhat expertise does my team need to use Prodigy?Prodigy is designed as a developer tool and assumes basic familiarity with the Python programming language and the command line. We also provide extensive [documentation](https://prodi.gy/docs) and examples to help you get started. Once you’ve set up an annotation task, the web application makes it easy for anyone to create annotations, no programming experience required.\n\nWhich cloud providers does Prodigy support?Prodigy provides a standard Python web server and application that can be deployed on any cloud provider of your choice, including entirely on-premise. You can read more about deployment options and instructions [here](https://prodi.gy/docs/deployment).\n\nDo you have special offers for researchers and universities?We’re always happy to support [research projects](https://prodi.gy/industries/research-education), and researchers at degree-granting academic institutions can apply for an interim license to use Prodigy for free. To claim your research license, [email us](mailto:contact@explosion.ai?subject=Prodigy%20Research%20License) and include your university details.",
  "usage": {
    "tokens": 1907
  }
}
```
