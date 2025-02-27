---
title: Using Large language models like GPT to do Q&A over papers (II) — using Perplexity.ai (free) over CORE, Scite.ai, Semantic Scholar etc domains
description: Summary : In this blog post, I delve into the use of Perplexity.ai, a startup that combines search engine results with GPT-3 results like Bing’s new chatbot. But instead of letting it get results…
url: https://aarontay.medium.com/using-large-language-models-like-gpt-to-do-q-a-over-papers-ii-using-perplexity-ai-15684629f02b
timestamp: 2025-01-20T15:41:56.258Z
domain: aarontay.medium.com
path: using-large-language-models-like-gpt-to-do-q-a-over-papers-ii-using-perplexity-ai-15684629f02b
---

# Using Large language models like GPT to do Q&A over papers (II) — using Perplexity.ai (free) over CORE, Scite.ai, Semantic Scholar etc domains


Summary : In this blog post, I delve into the use of Perplexity.ai, a startup that combines search engine results with GPT-3 results like Bing’s new chatbot. But instead of letting it get results…


## Content

[![Image 83: Aaron Tay](https://miro.medium.com/v2/resize:fill:44:44/0*nvlIFawVEcFLbCxY.jpg)](https://medium.com/@aarontay?source=post_page---byline--15684629f02b--------------------------------)

[![Image 84: Academic librarians and open access](https://miro.medium.com/v2/resize:fill:24:24/1*LLTh-8I_JetOtI1WUzClKA.jpeg)](https://medium.com/a-academic-librarians-thoughts-on-open-access?source=post_page---byline--15684629f02b--------------------------------)

_Summary : In this blog post, I delve into the use of Perplexity.ai,_ [_a startup that combines search engine results with GPT-3 results_](https://gpt3demo.com/apps/perplexity-ai) _like Bing’s new chatbot. But instead of letting it get results from all over the net, I test with a few examples what happens if you restrict the results, so it gets results only from domains that include only academic content such as Google Scholar (scholar.google.com), CORE (core.ac.uk), Semantic Scholar (semanticscholar.org/), Scite (scite.ai) and Google books(books.google.com/)._

_Effectively, you are now querying papers directly for answers using the power of state of art — large language models (LLMs). The results are amazing! Among other things, this technique is able to find seminal papers, answer direct questions on the paper that first coined a certain term etc._

_Interestingly, two of these domains scite.ai and semanticscholar.org have specialized tools that already apply LLMs on their content. In the case of_ [_scite.ai there is a beta “Ask a question feature”_](https://twitter.com/scite/status/1626706467272130567?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1626706467272130567%7Ctwgr%5Ed0bfe8fdf636e7df3c960eb10071d5229c5d3b5b%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext2Fhtmlkey%3Da19fcc184b9711e1b4764040d3dc5c07schema%3Dtwitterurl%3Dhttp3A%2F%2Ftwitter.com%2Fscite%2Fstatus%2F1626706467272130567image%3D) _, while_ [_elicit.org does the same over Semantic Scholar data._](https://elicit.org/)

_When the results from these specialized tools are compared against the simplistic idea of restricting results to specific domain in Perplexity, Perplexity shockingly does a lot better in these few examples! I speculate in the blog post why this is so._

_All in all, I am nearly sold, it isn’t perfect but Perplexity does amazingly well for a task that it wasn’t designed for. And this isn’t just about Perplexity, I expect with a bit more fine tuning and tweaks this way of using LLMs will become the standard in the next few years for search._

Introduction
------------

In [part I, I shared about how the latest Large Language Models are being combined with search engine technology to create real Q&A systems](https://medium.com/@aarontay/using-the-latest-large-language-models-like-gpt-to-do-q-a-over-webpages-or-papers-i-dd22b7671d7e).

Unlike past promises of semantic search, _this seems like the real deal_. The latest generation of language models particularly the transformer based models like BERT and GPT which use tricks like self-attention and masked self-attention really seem to be able to “understand” text.

They combine the state of art capabilities of LLMs to do Natural Language processing with the information retrieval capabilities of traditional search engines.

Roughly speaking, when you do a query it looks up the top N promising documents, then tries to see which parts of the top N document might best match the query (embeddings are used!). The top passages which are deemed to likely answer the query are then passed over to the LLM (e.g. ChatGPT, GPT3.5-davinci model, OPT, BLOOM) which then use these passages to answer the question.

If you are interested in knowing [more how LLM technology is combined with traditional search technology please refer to my last post](https://medium.com/@aarontay/using-the-latest-large-language-models-like-gpt-to-do-q-a-over-webpages-or-papers-i-dd22b7671d7e)

Examples of search engines that work in such a way **currently at time of writing** includes general search systems like Microsoft’s Bing+Chatbot — so called Sydney (limited release at time of writing), Google’s Bard (not released at time of writing) and other commercial systems like [you.com](http://you.com/) and [Perplexity.ai](http://perplexity.ai/)

> I’m going to stick my head out to make a prediction that in 3–5 years times, such search engines will be the norm!

These systems will find results from the general web but you might prefer one that works closer to Google Scholar and extracts results only from academic papers when doing academic research.

Academic search + Large Language models
---------------------------------------

Take the example below.

While the example above looks good, you notice the sources are domains like [womenshealthmag.com](https://www.womenshealthmag.com/) and [naturalnews.com](https://naturalnews.com/) which aren’t the best sites you want your evidence to come from. ([Clinicaltrials.gov](https://clinicaltrials.gov/) is much better).

While [OpenAI’s WebGPT](https://openai.com/blog/webgpt/) (unreleased) was trained to try to learn which websites are reputable and search accordingly(the model has full access to a BING api which it can use to send queries and extract from webpages), this might not be something in the current Bing model.

One obvious idea in the case of doing academic queries is to do this search only over academic websites/papers.

> In practice, if you looking for health type evidence, it might even be better to just do the query over Systematic reviews and meta-analysis!

If so your choices include tools like [elicit.org](https://clinicaltrials.gov/) , [scite.ai](http://scite.ai/), [scispace](https://typeset.io/) do.

Below shows an example of Elicit.org query which extracts answers from papers available in the Semantic Scholar Corpus.

![Image 85](https://miro.medium.com/v2/resize:fit:700/0*Z2FcZYwWeQb2o6c6.png)

[Elicit query can you use google scholar alone for systematic reviews?](https://elicit.org/search?q=can+you+use+google+scholar+standalone+for+systematic+reviews%3F&token=01GT8Z09AYSFDJQG4SB24MA3Q1)

See my post on [Q&A academic systems — Elicit.org, Scispace, Consensus.app, Scite.ai and Galactica](https://musingsaboutlibrarianship.blogspot.com/2022/11/q-academic-systems-elicitorg-scispace.html).

Rolling your own search + large language model
----------------------------------------------

Or you can consider building your own! See [here](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb), [here](https://github.com/openai/openai-cookbook/blob/main/apps/web-crawl-q-and-a/web-qa.ipynb), [here](https://simonwillison.net/2023/Jan/13/semantic-search-answers/) ,[here](https://github.com/shauryr/S2QA) but all this require a bit of know how and either cost some money if you use OpenAI and other paid APIs for state of art embeddings or need a fairly powerful computer to run opensource LLMs like T5.

In this blog post, I will show you how using [Perplexity.ai](http://perplexity.ai/) or [You.com](http://you.com/) you can have a feel of how such a system will work for your use case without paying a cent or knowing a line of code.

> Obviously, Bing+Chatbot might work as well, but as of time of writing I don’t have access to it.

As noted in the last blog, the trick is simply restricting the queries to a specific domain. In my example, I wanted to do a Q&A over my library website so I simply did\*

**site:smu.edu.sg <query\>**

\*I assume it honors the site operator….

![Image 86](https://miro.medium.com/v2/resize:fit:700/0*rl5lJLdEgN1DsxuY.png)

[Perplexity search — restricted to my University site.](https://www.perplexity.ai/?s=c&uuid=5a84b6da-000b-4ba9-b2de-bb6d662e2770)

You get similar results using the [Perplexity Chrome extension](https://chrome.google.com/webstore/detail/perplexity/hlgbcneanomplepojfcnclggenpcoldo) by going to a specific domain (e.g. your website) and selecting “This domain”

![Image 87](https://miro.medium.com/v2/resize:fit:433/0*HR-Vb3d2U5bQKbu0.png)

Using “this domain” option with Perplexity Chrome extension

You get similar results with You.com

![Image 88](https://miro.medium.com/v2/resize:fit:700/0*wonkcm__8wFBemV4.png)

[Using you.com on smu.edu.sg domain](https://you.com/search?q=site%3Asmu.edu.sg+how+many+books+can+you+borrow+as+an+undergraduate%3F&fromSearchBar=true&tbm=youchat) (it got the answer wrong!)

The results aren’t always perfect, for example it can get confused by tables, but this is something that can be worked around by parsing the table etc.

What happens if you do it over only academic content?
-----------------------------------------------------

I was toying with the idea of it answering research questions as a library chatbot and I shot it the question

**site:smu.edu.sg what are good datasets for ceo renumeration**

And I was amazed it gave an excellent answer.

![Image 89](https://miro.medium.com/v2/resize:fit:700/1*xANeGnB-E4drctYWi7LYNg.png)

[Askng Perplexity a research question restricted to smu.edu.sg](https://www.perplexity.ai/?s=c&uuid=4814b3a4-7295-4c04-876a-53b06c29b094)

How did it do that? A lot of it was simply the fact that our institutional repository was hosting a lot of papers in finance and accounting on the same domain and Perplexity was extracting the answer from there! (Our ResearchGuides on the same domain helps too sometimes)

This led me to think, could I do the same trick over domains with a ton of papers? Sure I could do it on domains for preprint servers like [Arxiv.org](https://arxiv.org/) but that would be domain specific. Publisher sites like [wiley.com](https://www.wiley.com/) might work but that would be too publisher specific.

In the end I thought of the following

1.  Google Scholar ([scholar.google.com](http://scholar.google.com/))
2.  CORE ([core.ac.uk](https://core.ac.uk/))
3.  Semantic Scholar ([semanticscholar.org/](https://www.semanticscholar.org/me/research))
4.  Scite —([scite.ai](http://scite.ai/))
5.  Google books — ([books.google.com/](https://books.google.com/))

After some testing, Perplexity.ai seems to have a large index than You.com so I will show results only from perplexity.

1\. Restricting to Google Scholar ([scholar.google.com](http://scholar.google.com/))
------------------------------------------------------------------------------------

A natural idea was to try this on the largest single source of academic content — Google Scholar.

In my first query I asked about the result from [one of my old published papers](https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.20755)

**site:scholar.google.com is accuracy of Wikipedia articles correlated with edit age?**

![Image 90](https://miro.medium.com/v2/resize:fit:700/1*1Od7aC7_-F6TGw01GRpQdA.png)

[https://www.perplexity.ai/?s=c&uuid=08c1d2a9-9fc9-4788-be70-cd3ba088868b](https://www.perplexity.ai/?s=c&uuid=08c1d2a9-9fc9-4788-be70-cd3ba088868b)

Perplexity did very well and correctly found the paper — Improving Wikipedia’s accuracy: Is edit age a solution? that had the result. The last sentence might not be correct though.

What is interesting is that the sources given when linked on goes to the [Google Scholar profile of the two authors including mine.](https://scholar.google.com/citations?hl=en&user=F9_kHm0AAAAJ&inst=14102473421921925766) I have a suspicion it is drawing own from [the brief record with title , abstract like this page](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=F9_kHm0AAAAJ&citation_for_view=F9_kHm0AAAAJ%3Au-x6o8ySG0sC&inst=14102473421921925766) as Google Scholar does not itself host full text.

You certainly can ask questions about metadata

![Image 91](https://miro.medium.com/v2/resize:fit:700/1*v8MeTuCzvfAzU1lNDmjZhA.png)

[https://www.perplexity.ai/?s=u&uuid=37662a7c-dd81-4550-b9d5-ce2499362a86](https://www.perplexity.ai/?s=u&uuid=37662a7c-dd81-4550-b9d5-ce2499362a86)

Here’s some evidence it is only using title/abstract and not full-text when asked

**site:scholar.google.com what are seminal papers on deep learning.**

> You might be interested in [my recent blog post on methods for finding seminal papers](https://musingsaboutlibrarianship.blogspot.com/2023/02/identifying-seminal-papers-some-methods.html)

The response was as follows

![Image 92](https://miro.medium.com/v2/resize:fit:700/1*YvAfaXSxybeZe-kJ1Y6jrw.png)

[https://www.perplexity.ai/?s=c&uuid=2d9ac2b0-c3a5-46e8-9416-93b2b6bd7910](https://www.perplexity.ai/?s=c&uuid=2d9ac2b0-c3a5-46e8-9416-93b2b6bd7910)

The papers suggested seemed odd to me even though I’m not a deep learning specialist. But when I looked at [one of the papers suggested](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=80MfVJ8AAAAJ&citation_for_view=80MfVJ8AAAAJ%3AqjMakFHDy7sC&inst=14102473421921925766), you can see it is picking it up from the abstract where it mentions “seminal segmentation”.

Similarly asking which paper coined the term bronze OA gets zero answers.

![Image 93](https://miro.medium.com/v2/resize:fit:700/1*hIXbYkKKn3wXCZ--vWxM3g.png)

[https://www.perplexity.ai/?s=u&uuid=8c5ae915-d405-4d30-9fbc-2e98e1048a18](https://www.perplexity.ai/?s=u&uuid=8c5ae915-d405-4d30-9fbc-2e98e1048a18)

**Preliminary Conclusion — In general, this technique works only if the content you are looking for is in the title, abstract or other metadata. Can we do better with domains with full-text?**

2\. Restricting to CORE (core.ac.uk) Domain
-------------------------------------------

But what if I wanted to search full-text of papers for answers? Unfortunately, we don’t quite live in a world of full open-access.

That said one of the largest aggregator of Open academic content I know of is the CORE service at [core.ac.uk](https://core.ac.uk/).

![Image 94](https://miro.medium.com/v2/resize:fit:700/1*MxutSfIvav8VicZXs2kJ0w.png)

[Core Service](https://core.ac.uk/)

More importantly, unlike other aggregators like [BASE (Bielefeld Academic Search Engine)](https://www.base-search.net/) Core _actually harvests and hosts full text of papers on their domain_, so hopefully the full-text can be used by Perplexity to answer queries.

First let’s try asking the question on seminal papers on deep learning

![Image 95](https://miro.medium.com/v2/resize:fit:700/1*ivrBWaHxioc1iygHENIIoA.png)

[https://www.perplexity.ai/?s=u&uuid=4710eaa8-6f35-4625-9afc-cf83c02853ef](https://www.perplexity.ai/?s=u&uuid=4710eaa8-6f35-4625-9afc-cf83c02853ef)

I’m not expert enough to judge if this answer is good, but checking the sources you can see it is picking up some answers from not just the abstract but also the full text ([e.g. source 5](https://core.ac.uk/download/pdf/158246434.pdf))

![Image 96](https://miro.medium.com/v2/resize:fit:700/1*i9C1oIS74ZN_i2XAvtqsdw.png)

[Perplexity picks up seminal papers using full-text of paper indexed by CORE — source 5](https://core.ac.uk/download/pdf/158246434.pdf)

After some testing, it seems [asking for “Seminal works”](https://www.perplexity.ai/?s=c&uuid=7906a3d5-463f-4678-be42-6511f1f7fc80) instead of papers might give better results.

![Image 97](https://miro.medium.com/v2/resize:fit:700/1*y7qFWrvxVj5JzIdwi0YhJw.png)

[https://www.perplexity.ai/?s=c&uuid=7906a3d5-463f-4678-be42-6511f1f7fc80](https://www.perplexity.ai/?s=c&uuid=7906a3d5-463f-4678-be42-6511f1f7fc80)

Here are other attempts to find seminal papers. The results look fairly decent (though not perfect particularly as it goes on) to my untrained eyes.

![Image 98](https://miro.medium.com/v2/resize:fit:700/1*j50ecDrfetRT0M37dXfNbw.png)

[https://www.perplexity.ai/?s=u&uuid=7b0e6e23-4c69-44cd-b83b-0b8b2d8a7cf2](https://www.perplexity.ai/?s=u&uuid=7b0e6e23-4c69-44cd-b83b-0b8b2d8a7cf2)

Again, changing the query to ask about seminal works instead of seminal papers make a difference. This shows how sensitive these searches are to different queries , which is characteristic of LLMs.

![Image 99](https://miro.medium.com/v2/resize:fit:700/1*Vn8K139xDyI2O0UaZ4Y6ew.png)

[https://www.perplexity.ai/?s=u&uuid=991f2edd-db8f-4082-9fa1-ed14224d4d1b](https://www.perplexity.ai/?s=u&uuid=991f2edd-db8f-4082-9fa1-ed14224d4d1b)

Let’s try asking the question that Perplexity failed when restricting to Google Scholar — which paper first coined the term Bronze OA?

![Image 100](https://miro.medium.com/v2/resize:fit:700/1*fMxyDrdqiHsoZamZoOJ_RQ.png)

[https://www.perplexity.ai/?s=c&uuid=af8b3f88-fec3-4936-8588-73912af5a349](https://www.perplexity.ai/?s=c&uuid=af8b3f88-fec3-4936-8588-73912af5a349)

As far as I know this answer is correct. At the very least it was extracted from [source 1](https://core.ac.uk/download/pdf/345178270.pdf) — that believes this is so and is citing the Piwowar et al. (2018)

**Preliminary Conclusion — In general, this technique looks to be really powerful, and it seems to be really looking into full-text of papers! But like any LLM prompts it can be sensitive to the phrasing you use.**

3\. Restricting to Semantic Scholar ([semanticscholar.org/](https://www.semanticscholar.org/me/research))
---------------------------------------------------------------------------------------------------------

The other major source of open access data (both metadata and full-text) is Semantic Scholar. In fact, it is the source used by Elicit.org and [many other tools that need a source of scholarly paper data](https://musingsaboutlibrarianship.blogspot.com/p/list-of-innovative-literature-mapping.html).

You might bebetter off using [Elicit.org](http://elicit.org/) here, since they use the same source but use LLMs in a far more refined manner, but I was curious to see the difference.

let’s try to find seminal works.

The results don’t look as good if I ask for “[seminal paper](https://www.perplexity.ai/?s=u&uuid=8b81bb66-1e88-48ec-b830-9381f322c4e4)s” rather than “[Seminal works](https://www.perplexity.ai/?s=u&uuid=5c0d18ec-46e1-4ca4-8d1c-d636547fc679)” for unknown reasons.

![Image 101](https://miro.medium.com/v2/resize:fit:700/1*irNe8yYMNZ8yiq1AMjf8Qg.png)

[https://www.perplexity.ai/?s=u&uuid=5c0d18ec-46e1-4ca4-8d1c-d636547fc679](https://www.perplexity.ai/?s=u&uuid=5c0d18ec-46e1-4ca4-8d1c-d636547fc679)

For comparison, you might want to try the same queries on Elicit.org, which uses also Semantic Scholar as data with large language models to extract answers.

Here’s a comparison when I use elicit.org to ask for seminal works.

![Image 102](https://miro.medium.com/v2/resize:fit:700/1*LccijvZeb4xoUMr-LbR_Ew.png)

[Using elicit to ask for seminal papers](https://elicit.org/search?q=what+are+seminal+works+on+theory+of+the+firm%3F&token=01GTA50Z37PPA55KB46MGAMHXG)

Interestingly, the answers look worse in Elicit.org. I speculate that because Elicit is trying to rank papers to find seminal works, its top 4 papers which it uses to generate answers are quite old and do not tend to mention other seminal works?

Perplexity restricted to Semantic Scholar also passes the test when I ask which paper first coined the term bronze OA as it is able to look into full-text of papers.

![Image 103](https://miro.medium.com/v2/resize:fit:700/1*yGHWBPwOqbQ81vaVa0m63A.png)

[https://www.perplexity.ai/?s=u&uuid=1c9fb150-8670-44f1-bf91-03dbcecbfead](https://www.perplexity.ai/?s=u&uuid=1c9fb150-8670-44f1-bf91-03dbcecbfead)

When we try the same query in Elicit.org , it totally fails.

![Image 104](https://miro.medium.com/v2/resize:fit:700/1*oGXBnZ5R4wF_pqoNTv7lhA.png)

[Elicit query on which paper first coined the term bronze OA](https://elicit.org/search?q=which+paper+first+coined+the+term+%22bronze+oa%22%3F&token=01GTA58HG2XKCSVMKM7VHAGG2T)

Here you can see the obvious problem. Elicit.org’s sematic search has totally failed to find the right papers at all. My guess is it’s ignoring the quotes for “bronze OA” and gets into trouble.

[Changing the query to say “bronze open access” gets slightly better results but is still nowhere as good.](https://elicit.org/search?q=which+paper+first+coined+the+term+%22bronze+open+access%22%3F&token=01GTA5FAET6PAD82BS5JA1M4NG)

**Preliminary Conclusion — In general restricting perplexity to answers from** [semanticscholar.org/](https://www.semanticscholar.org/me/research) is gives similar results to restricting answers to [core.ac.uk](http://core.ac.uk/) domain and both seem to be able to extract answers from full text.

Given [Elicit.org](http://elicit.org/) is using Semantic Scholar data with LLM technology, it is natural to compare the results there with this technique.

Interestingly, for the few queries I tested, Perplexity restricted to Semantic Scholar domain trounces elicit.

My theory is as such. Elicit.org generates results from the top 4 results while Perplexity from the top 10. But more importantly, Perplexity probably is using a “dumber” keyword search, while Elicit is doing a smarter semantic type search to find documents.

Ironically this hurts certain type of searches. For example, when I use Perplexity it probably just does a keyword search (which matches full-text) and looks for documents that mention paper XYZ is seminal and surfaces those. Elicit.org is probably smarter, and tries to actually find seminal papers….

For whatever reason for the few use cases I tried, elicit.org’s more semantic searches are surfacing far worse results than Perplexity’s, and given the worse results, the LLM is unable to extract good answers.

4\. Restricting to scite ([scite.ai](http://scholar.google.com/))
-----------------------------------------------------------------

The next domain I tried with Perplexity is using scite.ai. This is a interesting search index that doesn't have full-text. What they have besides the usual metadata is [citation citance or statements.](https://help.scite.ai/en-us/article/how-does-citation-statement-search-work-13tnvx7/)

They have recently launched in beta a [“Ask a question” feature that essentially uses LLMs to extract answers](https://www.linkedin.com/feed/update/urn:li:activity:7020861658109501440/)… but not from full-text, instead they use [citation citance or statements.](https://help.scite.ai/en-us/article/how-does-citation-statement-search-work-13tnvx7/) If you think about it is just a special part of the full-text aka the sentences around citations.

Are the results better? Let’s try again with perplexity limited to scite.ai

![Image 105](https://miro.medium.com/v2/resize:fit:700/1*VE0OuXgvnh_4iejd2MWJVQ.png)

[https://www.perplexity.ai/?s=c&uuid=a76ee219-f4c3-48df-b0ed-238ea99a4de3](https://www.perplexity.ai/?s=c&uuid=a76ee219-f4c3-48df-b0ed-238ea99a4de3)

Here’s a s[imilar search asking for seminal works on deep learning using scite’s beta feature](https://www.perplexity.ai/?s=c&uuid=e1b58dc8-980f-4022-97e7-5f4ac8fd214b)

As mentioned above, scite.ai has it’s own beta “Ask a question” feature that is using GPT-3 to extract answers. How does it match up for the same query?

Not very well in my opinion.

![Image 106](https://miro.medium.com/v2/resize:fit:700/1*u4RfMuBgLMFO_vqRAcmeSA.png)

[https://scite.ai/search?mode=question-answering&q=what%20are%20some%20seminal%20works%20on%20theory%20of%20the%20firm%3F](https://scite.ai/search?mode=question-answering&q=what+are+some+seminal+works+on+theory+of+the+firm%3F)

Now let’s try Perplexity on the question — which paper first coined the term bronze OA. As before this is restricted to the scite.ai domain.

![Image 107](https://miro.medium.com/v2/resize:fit:700/1*uwnYuAafG9ZsYDyazYikbw.png)

[https://www.perplexity.ai/?s=u&uuid=0a2e339e-89f2-4a62-8f7c-6442ac3c052b](https://www.perplexity.ai/?s=u&uuid=0a2e339e-89f2-4a62-8f7c-6442ac3c052b)

So it failed for the specific question on which paper first coined the term bronze OA. It’s unclear why since the same type of query worked when restricting on the domain core.ac.uk. Maybe the papers available was different?

For what’s it worth using the scite.ai’s beta ask a question feature, [also did not do well.](https://scite.ai/search?mode=question-answering&q=which+paper+first+coined+the+term+%22bronze+oa%22%3F)

![Image 108](https://miro.medium.com/v2/resize:fit:700/1*TdgLQVIJJITizl9CMNnVwQ.png)

[https://scite.ai/search?mode=question-answering&q=which%20paper%20first%20coined%20the%20phrase%20%22bronze%20oa%22%3F](https://scite.ai/search?mode=question-answering&q=which+paper+first+coined+the+phrase+%22bronze+oa%22%3F)

**Preliminary Conclusion —It's hard to say what’s going on. It seems to be able to identify seminal works to some extent, but in my few examples, restricting to scite.ai domain doesn’t seem to do as well as to say core.ac.uk**

I’m guessing because each article paper comes with citation statements, it can see how other papers are describing the paper itself. For example, a seminal paper like [Coase(1937) will have a scite.ai page](https://scite.ai/reports/the-nature-of-the-firm-6p6W9E) listing not just the metadata of the paper but also include citation statements from other papers saying it is a seminal work and this is picked up by perplexity.

Why it can’t find Piwowar (2018) as the paper that coined Bronze OA is unclear to me, [as there is a scite page for it.](https://scite.ai/reports/the-state-of-oa-a-b2AZ2gN) Is it simply the lack of a citation statement in scite saying so?

Similar to the Semantic Scholar case, for some reason the results I get using perplexity restricted to scite domain seem superior to using specialized search systems that use these sources. In this case, Perplexity restricted to scite.ai gives better results than scite.ai’s build-in ask a question feature!

This feels surprising because you would expect a specialized tool like elicit.org or scite.ai to work better than a tool like perplexity that was never designed for this use case.

Then again Scite.ai’s feature is still in beta and while elicit has been working with OpenAI for almost as long as Perplexity (1 year+), it focused more on extraction of article properties (e.g. population sample, sample size, region of study etc) and the generative answer part was added fairly recently.

5\. Restricting to Google books (books.google.com)
--------------------------------------------------

Let’s now switch to books, in particular let’s restrict results to books.google.com

![Image 109](https://miro.medium.com/v2/resize:fit:700/1*jr8BKeF5zzu8MukSJN43sw.png)

[https://www.perplexity.ai/?s=u&uuid=fda982fc-3217-4872-9a55-63796d05d3e8](https://www.perplexity.ai/?s=u&uuid=fda982fc-3217-4872-9a55-63796d05d3e8)

In first test query, I see the sources it points to are pages like

Some of these books have preview versions available, is Perplexity able to “See” them?

Probably. Take the query below.

![Image 110](https://miro.medium.com/v2/resize:fit:700/1*Jgb9lPPn1h5MVIVNZF5wJA.png)

[https://www.perplexity.ai/?s=u&uuid=5d9c66bd-1f08-4ef4-9289-87957a5f11f8](https://www.perplexity.ai/?s=u&uuid=5d9c66bd-1f08-4ef4-9289-87957a5f11f8)

You can see in the sources, sentences found by Perplexity, and when you check google books , you will notice there are from within Preview versions of books.

In the example below, I looked at the first source and searched within the book “It is clear that Darwin did not sail directly from Christian orthodoxy to atheistic materialism.” and you can see the hit.

![Image 111](https://miro.medium.com/v2/resize:fit:700/1*CXJJzxV3zhWmKgumTUlVAw.png)

[https://books.google.com.sg/books?redir\_esc=y&id=0TA81BTW3dIC&q=It+is+clear+that+Darwin+did+not+sail+directly+from+Christian+orthodoxy+to+atheistic+materialism.#v=snippet&q=It%20is%20clear%20that%20Darwin%20did%20not%20sail%20directly%20from%20Christian%20orthodoxy%20to%20atheistic%20materialism.&f=false](https://books.google.com.sg/books?redir_esc=y&id=0TA81BTW3dIC&q=It+is+clear+that+Darwin+did+not+sail+directly+from+Christian+orthodoxy+to+atheistic+materialism.#v=snippet&q=It%20is%20clear%20that%20Darwin%20did%20not%20sail%20directly%20from%20Christian%20orthodoxy%20to%20atheistic%20materialism.&f=false)

All this seems very good, but when I try to work the other way, where I search for something that is available in Google book preview , Perplexity can’t seem to find the answer.

I suspect this has to do with the way Perplexity works . My guess is for googlebooks it doesnt have all the google book previews indexed…but if you hit the right pages, it can extract the results?

Perplexity — how it works
-------------------------

Perplexity [has precious little information on how it works.](https://www.perplexity.ai/about) we do know it [uses or used OpenAI’s GPT-3 (similar to Elicit)](https://gpt3demo.com/apps/perplexity-ai) , but we don’t how it matches or ranks pages.

The first question I wondered about is this. Like most search engines I assume when you search you are matching an index of content their crawlers have seen earlier.

But does it then extract the information from the indexed version or does it scrape the result on the fly? I believe it scrapes the page on the fly,

![Image 112](https://miro.medium.com/v2/resize:fit:700/1*S4xRZds4ma--qqx-bw3LoA.png)

[https://www.perplexity.ai/?s=u&uuid=fa02755a-5d6c-4096-9e44-8c273ac69cee](https://www.perplexity.ai/?s=u&uuid=fa02755a-5d6c-4096-9e44-8c273ac69cee)

This is because when I search for the current date it is able to give me the right date and time, so it is definitely looking at the current contents of the pages found and not the indexed cached version.

One other feature I did not mention is, you can actually edit sources, by adding or removing them.

For example, when I do a search restricted to core.ac.uk, it is unable to find the right answer because the paper isn’t on core.ac.uk. You can actually edit sources to improve the results.

![Image 113](https://miro.medium.com/v2/resize:fit:700/1*lVBxUyXvDUZz_HLGU3Qbug.png)

[https://www.perplexity.ai/?s=u&uuid=93257103-9929-4db7-98c2-af1573aef5f1](https://www.perplexity.ai/?s=u&uuid=93257103-9929-4db7-98c2-af1573aef5f1)

The feature to edit sources is quite hidden. Click on the three dots button and then “Edit sources”.

![Image 114](https://miro.medium.com/v2/resize:fit:700/1*ebBgWCXSxgig8s9vvjgqWw.png)

![Image 115](https://miro.medium.com/v2/resize:fit:700/1*5xGmKanBy0BOd4uGDcNhog.png)

Removing sources is nice particularly if you use a full internet search and you want to remove results from less trust-worthy sources.

Still in this particular case, Perplexity is unable to find the right answer as the paper with the right answer simply isn’t on core.ac.uk as it isnt open access. However, by simply adding a URL to a page with the right paper’s title & abstract the problem should be fixed. (See earliest example’s using Perplexity restricted to Google scholar domain)

However while there is a “add more sources” feature button, but disappointingly, it does not allow you to add URLs directly, but just gives you the next highest ranked urls.

In fact, I would love for perplexity to allow me to define list of domains as a whitelist (only show results from these domains. I would add say all preprint, publisher etc. domains for research papers) or alternatively a blacklist (exclude trash domains)

Conclusion
----------

Perplexity restricted to domains with papers seems unreasonably effective! And this is despite not being designed for this use case.

I have long talked [about the power of Machine learning and deep learning coupled with open access to change the game](https://musingsaboutlibrarianship.blogspot.com/2022/06/diversity-of-scholarly-record-push-to.html). This appears to be one aspect of it.

> Related: [Are we undervaluing Open Access by not correctly factoring in the potentially huge impacts of Machine learning? — An academic librarian’s view](https://medium.com/a-academic-librarians-thoughts-on-open-access/are-we-undervaluing-open-access-by-not-correctly-evaluating-the-potentially-huge-impacts-of-e93af1de9414)

More specifically back in 2020 during the height of the pandemic, [I mused about how the CORD-19 (COVID open research dataset) which was a huge project, partnered by Publishers, discovery vendors etc to aggregate all papers on COVID (including full-text) , harmonize the data to allow researchers to do text mining was a interesting “grand experiment”](https://musingsaboutlibrarianship.blogspot.com/2020/05/covid-19-and-text-data-mining-tdm.html) on the power of such techniques.

It seems two years on, the combination of search technology + even more powerful LLMs in general will kick off yet another larger wave of experimentation.

From my point of view, I am nearly sold, it seems inevitable to me that the future of search belongs to this class of systems that combine search results with LLMs extraction!

Post edit note: I just got access to the new Bing+chat feature. And the results are out of this world. Most of the time, I don’t even need to do site restriction. Some examples below

![Image 116](https://miro.medium.com/v2/resize:fit:700/1*7WRKSCz0BoEqu48QUD-YIg.png)

![Image 117](https://miro.medium.com/v2/resize:fit:700/1*FXmluflgn7GQ1yggqJSZmQ.png)

![Image 118](https://miro.medium.com/v2/resize:fit:700/1*xV-njfJQcbeFQU59tF36CA.png)

![Image 119](https://miro.medium.com/v2/resize:fit:700/1*wxQH6nOc8Qvl20A-LlRAQw.png)

![Image 120](https://miro.medium.com/v2/resize:fit:700/1*v6o8-GBHEJDRxIEQxxnR-A.png)

## Metadata

```json
{
  "title": "Using Large language models like GPT to do Q&A over papers (II) — using Perplexity.ai (free) over CORE, Scite.ai, Semantic Scholar etc domains",
  "description": "Summary : In this blog post, I delve into the use of Perplexity.ai, a startup that combines search engine results with GPT-3 results like Bing’s new chatbot. But instead of letting it get results…",
  "url": "https://aarontay.medium.com/using-large-language-models-like-gpt-to-do-q-a-over-papers-ii-using-perplexity-ai-15684629f02b",
  "content": "[![Image 83: Aaron Tay](https://miro.medium.com/v2/resize:fill:44:44/0*nvlIFawVEcFLbCxY.jpg)](https://medium.com/@aarontay?source=post_page---byline--15684629f02b--------------------------------)\n\n[![Image 84: Academic librarians and open access](https://miro.medium.com/v2/resize:fill:24:24/1*LLTh-8I_JetOtI1WUzClKA.jpeg)](https://medium.com/a-academic-librarians-thoughts-on-open-access?source=post_page---byline--15684629f02b--------------------------------)\n\n_Summary : In this blog post, I delve into the use of Perplexity.ai,_ [_a startup that combines search engine results with GPT-3 results_](https://gpt3demo.com/apps/perplexity-ai) _like Bing’s new chatbot. But instead of letting it get results from all over the net, I test with a few examples what happens if you restrict the results, so it gets results only from domains that include only academic content such as Google Scholar (scholar.google.com), CORE (core.ac.uk), Semantic Scholar (semanticscholar.org/), Scite (scite.ai) and Google books(books.google.com/)._\n\n_Effectively, you are now querying papers directly for answers using the power of state of art — large language models (LLMs). The results are amazing! Among other things, this technique is able to find seminal papers, answer direct questions on the paper that first coined a certain term etc._\n\n_Interestingly, two of these domains scite.ai and semanticscholar.org have specialized tools that already apply LLMs on their content. In the case of_ [_scite.ai there is a beta “Ask a question feature”_](https://twitter.com/scite/status/1626706467272130567?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1626706467272130567%7Ctwgr%5Ed0bfe8fdf636e7df3c960eb10071d5229c5d3b5b%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext2Fhtmlkey%3Da19fcc184b9711e1b4764040d3dc5c07schema%3Dtwitterurl%3Dhttp3A%2F%2Ftwitter.com%2Fscite%2Fstatus%2F1626706467272130567image%3D) _, while_ [_elicit.org does the same over Semantic Scholar data._](https://elicit.org/)\n\n_When the results from these specialized tools are compared against the simplistic idea of restricting results to specific domain in Perplexity, Perplexity shockingly does a lot better in these few examples! I speculate in the blog post why this is so._\n\n_All in all, I am nearly sold, it isn’t perfect but Perplexity does amazingly well for a task that it wasn’t designed for. And this isn’t just about Perplexity, I expect with a bit more fine tuning and tweaks this way of using LLMs will become the standard in the next few years for search._\n\nIntroduction\n------------\n\nIn [part I, I shared about how the latest Large Language Models are being combined with search engine technology to create real Q&A systems](https://medium.com/@aarontay/using-the-latest-large-language-models-like-gpt-to-do-q-a-over-webpages-or-papers-i-dd22b7671d7e).\n\nUnlike past promises of semantic search, _this seems like the real deal_. The latest generation of language models particularly the transformer based models like BERT and GPT which use tricks like self-attention and masked self-attention really seem to be able to “understand” text.\n\nThey combine the state of art capabilities of LLMs to do Natural Language processing with the information retrieval capabilities of traditional search engines.\n\nRoughly speaking, when you do a query it looks up the top N promising documents, then tries to see which parts of the top N document might best match the query (embeddings are used!). The top passages which are deemed to likely answer the query are then passed over to the LLM (e.g. ChatGPT, GPT3.5-davinci model, OPT, BLOOM) which then use these passages to answer the question.\n\nIf you are interested in knowing [more how LLM technology is combined with traditional search technology please refer to my last post](https://medium.com/@aarontay/using-the-latest-large-language-models-like-gpt-to-do-q-a-over-webpages-or-papers-i-dd22b7671d7e)\n\nExamples of search engines that work in such a way **currently at time of writing** includes general search systems like Microsoft’s Bing+Chatbot — so called Sydney (limited release at time of writing), Google’s Bard (not released at time of writing) and other commercial systems like [you.com](http://you.com/) and [Perplexity.ai](http://perplexity.ai/)\n\n> I’m going to stick my head out to make a prediction that in 3–5 years times, such search engines will be the norm!\n\nThese systems will find results from the general web but you might prefer one that works closer to Google Scholar and extracts results only from academic papers when doing academic research.\n\nAcademic search + Large Language models\n---------------------------------------\n\nTake the example below.\n\nWhile the example above looks good, you notice the sources are domains like [womenshealthmag.com](https://www.womenshealthmag.com/) and [naturalnews.com](https://naturalnews.com/) which aren’t the best sites you want your evidence to come from. ([Clinicaltrials.gov](https://clinicaltrials.gov/) is much better).\n\nWhile [OpenAI’s WebGPT](https://openai.com/blog/webgpt/) (unreleased) was trained to try to learn which websites are reputable and search accordingly(the model has full access to a BING api which it can use to send queries and extract from webpages), this might not be something in the current Bing model.\n\nOne obvious idea in the case of doing academic queries is to do this search only over academic websites/papers.\n\n> In practice, if you looking for health type evidence, it might even be better to just do the query over Systematic reviews and meta-analysis!\n\nIf so your choices include tools like [elicit.org](https://clinicaltrials.gov/) , [scite.ai](http://scite.ai/), [scispace](https://typeset.io/) do.\n\nBelow shows an example of Elicit.org query which extracts answers from papers available in the Semantic Scholar Corpus.\n\n![Image 85](https://miro.medium.com/v2/resize:fit:700/0*Z2FcZYwWeQb2o6c6.png)\n\n[Elicit query can you use google scholar alone for systematic reviews?](https://elicit.org/search?q=can+you+use+google+scholar+standalone+for+systematic+reviews%3F&token=01GT8Z09AYSFDJQG4SB24MA3Q1)\n\nSee my post on [Q&A academic systems — Elicit.org, Scispace, Consensus.app, Scite.ai and Galactica](https://musingsaboutlibrarianship.blogspot.com/2022/11/q-academic-systems-elicitorg-scispace.html).\n\nRolling your own search + large language model\n----------------------------------------------\n\nOr you can consider building your own! See [here](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb), [here](https://github.com/openai/openai-cookbook/blob/main/apps/web-crawl-q-and-a/web-qa.ipynb), [here](https://simonwillison.net/2023/Jan/13/semantic-search-answers/) ,[here](https://github.com/shauryr/S2QA) but all this require a bit of know how and either cost some money if you use OpenAI and other paid APIs for state of art embeddings or need a fairly powerful computer to run opensource LLMs like T5.\n\nIn this blog post, I will show you how using [Perplexity.ai](http://perplexity.ai/) or [You.com](http://you.com/) you can have a feel of how such a system will work for your use case without paying a cent or knowing a line of code.\n\n> Obviously, Bing+Chatbot might work as well, but as of time of writing I don’t have access to it.\n\nAs noted in the last blog, the trick is simply restricting the queries to a specific domain. In my example, I wanted to do a Q&A over my library website so I simply did\\*\n\n**site:smu.edu.sg <query\\>**\n\n\\*I assume it honors the site operator….\n\n![Image 86](https://miro.medium.com/v2/resize:fit:700/0*rl5lJLdEgN1DsxuY.png)\n\n[Perplexity search — restricted to my University site.](https://www.perplexity.ai/?s=c&uuid=5a84b6da-000b-4ba9-b2de-bb6d662e2770)\n\nYou get similar results using the [Perplexity Chrome extension](https://chrome.google.com/webstore/detail/perplexity/hlgbcneanomplepojfcnclggenpcoldo) by going to a specific domain (e.g. your website) and selecting “This domain”\n\n![Image 87](https://miro.medium.com/v2/resize:fit:433/0*HR-Vb3d2U5bQKbu0.png)\n\nUsing “this domain” option with Perplexity Chrome extension\n\nYou get similar results with You.com\n\n![Image 88](https://miro.medium.com/v2/resize:fit:700/0*wonkcm__8wFBemV4.png)\n\n[Using you.com on smu.edu.sg domain](https://you.com/search?q=site%3Asmu.edu.sg+how+many+books+can+you+borrow+as+an+undergraduate%3F&fromSearchBar=true&tbm=youchat) (it got the answer wrong!)\n\nThe results aren’t always perfect, for example it can get confused by tables, but this is something that can be worked around by parsing the table etc.\n\nWhat happens if you do it over only academic content?\n-----------------------------------------------------\n\nI was toying with the idea of it answering research questions as a library chatbot and I shot it the question\n\n**site:smu.edu.sg what are good datasets for ceo renumeration**\n\nAnd I was amazed it gave an excellent answer.\n\n![Image 89](https://miro.medium.com/v2/resize:fit:700/1*xANeGnB-E4drctYWi7LYNg.png)\n\n[Askng Perplexity a research question restricted to smu.edu.sg](https://www.perplexity.ai/?s=c&uuid=4814b3a4-7295-4c04-876a-53b06c29b094)\n\nHow did it do that? A lot of it was simply the fact that our institutional repository was hosting a lot of papers in finance and accounting on the same domain and Perplexity was extracting the answer from there! (Our ResearchGuides on the same domain helps too sometimes)\n\nThis led me to think, could I do the same trick over domains with a ton of papers? Sure I could do it on domains for preprint servers like [Arxiv.org](https://arxiv.org/) but that would be domain specific. Publisher sites like [wiley.com](https://www.wiley.com/) might work but that would be too publisher specific.\n\nIn the end I thought of the following\n\n1.  Google Scholar ([scholar.google.com](http://scholar.google.com/))\n2.  CORE ([core.ac.uk](https://core.ac.uk/))\n3.  Semantic Scholar ([semanticscholar.org/](https://www.semanticscholar.org/me/research))\n4.  Scite —([scite.ai](http://scite.ai/))\n5.  Google books — ([books.google.com/](https://books.google.com/))\n\nAfter some testing, Perplexity.ai seems to have a large index than You.com so I will show results only from perplexity.\n\n1\\. Restricting to Google Scholar ([scholar.google.com](http://scholar.google.com/))\n------------------------------------------------------------------------------------\n\nA natural idea was to try this on the largest single source of academic content — Google Scholar.\n\nIn my first query I asked about the result from [one of my old published papers](https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.20755)\n\n**site:scholar.google.com is accuracy of Wikipedia articles correlated with edit age?**\n\n![Image 90](https://miro.medium.com/v2/resize:fit:700/1*1Od7aC7_-F6TGw01GRpQdA.png)\n\n[https://www.perplexity.ai/?s=c&uuid=08c1d2a9-9fc9-4788-be70-cd3ba088868b](https://www.perplexity.ai/?s=c&uuid=08c1d2a9-9fc9-4788-be70-cd3ba088868b)\n\nPerplexity did very well and correctly found the paper — Improving Wikipedia’s accuracy: Is edit age a solution? that had the result. The last sentence might not be correct though.\n\nWhat is interesting is that the sources given when linked on goes to the [Google Scholar profile of the two authors including mine.](https://scholar.google.com/citations?hl=en&user=F9_kHm0AAAAJ&inst=14102473421921925766) I have a suspicion it is drawing own from [the brief record with title , abstract like this page](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=F9_kHm0AAAAJ&citation_for_view=F9_kHm0AAAAJ%3Au-x6o8ySG0sC&inst=14102473421921925766) as Google Scholar does not itself host full text.\n\nYou certainly can ask questions about metadata\n\n![Image 91](https://miro.medium.com/v2/resize:fit:700/1*v8MeTuCzvfAzU1lNDmjZhA.png)\n\n[https://www.perplexity.ai/?s=u&uuid=37662a7c-dd81-4550-b9d5-ce2499362a86](https://www.perplexity.ai/?s=u&uuid=37662a7c-dd81-4550-b9d5-ce2499362a86)\n\nHere’s some evidence it is only using title/abstract and not full-text when asked\n\n**site:scholar.google.com what are seminal papers on deep learning.**\n\n> You might be interested in [my recent blog post on methods for finding seminal papers](https://musingsaboutlibrarianship.blogspot.com/2023/02/identifying-seminal-papers-some-methods.html)\n\nThe response was as follows\n\n![Image 92](https://miro.medium.com/v2/resize:fit:700/1*YvAfaXSxybeZe-kJ1Y6jrw.png)\n\n[https://www.perplexity.ai/?s=c&uuid=2d9ac2b0-c3a5-46e8-9416-93b2b6bd7910](https://www.perplexity.ai/?s=c&uuid=2d9ac2b0-c3a5-46e8-9416-93b2b6bd7910)\n\nThe papers suggested seemed odd to me even though I’m not a deep learning specialist. But when I looked at [one of the papers suggested](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=80MfVJ8AAAAJ&citation_for_view=80MfVJ8AAAAJ%3AqjMakFHDy7sC&inst=14102473421921925766), you can see it is picking it up from the abstract where it mentions “seminal segmentation”.\n\nSimilarly asking which paper coined the term bronze OA gets zero answers.\n\n![Image 93](https://miro.medium.com/v2/resize:fit:700/1*hIXbYkKKn3wXCZ--vWxM3g.png)\n\n[https://www.perplexity.ai/?s=u&uuid=8c5ae915-d405-4d30-9fbc-2e98e1048a18](https://www.perplexity.ai/?s=u&uuid=8c5ae915-d405-4d30-9fbc-2e98e1048a18)\n\n**Preliminary Conclusion — In general, this technique works only if the content you are looking for is in the title, abstract or other metadata. Can we do better with domains with full-text?**\n\n2\\. Restricting to CORE (core.ac.uk) Domain\n-------------------------------------------\n\nBut what if I wanted to search full-text of papers for answers? Unfortunately, we don’t quite live in a world of full open-access.\n\nThat said one of the largest aggregator of Open academic content I know of is the CORE service at [core.ac.uk](https://core.ac.uk/).\n\n![Image 94](https://miro.medium.com/v2/resize:fit:700/1*MxutSfIvav8VicZXs2kJ0w.png)\n\n[Core Service](https://core.ac.uk/)\n\nMore importantly, unlike other aggregators like [BASE (Bielefeld Academic Search Engine)](https://www.base-search.net/) Core _actually harvests and hosts full text of papers on their domain_, so hopefully the full-text can be used by Perplexity to answer queries.\n\nFirst let’s try asking the question on seminal papers on deep learning\n\n![Image 95](https://miro.medium.com/v2/resize:fit:700/1*ivrBWaHxioc1iygHENIIoA.png)\n\n[https://www.perplexity.ai/?s=u&uuid=4710eaa8-6f35-4625-9afc-cf83c02853ef](https://www.perplexity.ai/?s=u&uuid=4710eaa8-6f35-4625-9afc-cf83c02853ef)\n\nI’m not expert enough to judge if this answer is good, but checking the sources you can see it is picking up some answers from not just the abstract but also the full text ([e.g. source 5](https://core.ac.uk/download/pdf/158246434.pdf))\n\n![Image 96](https://miro.medium.com/v2/resize:fit:700/1*i9C1oIS74ZN_i2XAvtqsdw.png)\n\n[Perplexity picks up seminal papers using full-text of paper indexed by CORE — source 5](https://core.ac.uk/download/pdf/158246434.pdf)\n\nAfter some testing, it seems [asking for “Seminal works”](https://www.perplexity.ai/?s=c&uuid=7906a3d5-463f-4678-be42-6511f1f7fc80) instead of papers might give better results.\n\n![Image 97](https://miro.medium.com/v2/resize:fit:700/1*y7qFWrvxVj5JzIdwi0YhJw.png)\n\n[https://www.perplexity.ai/?s=c&uuid=7906a3d5-463f-4678-be42-6511f1f7fc80](https://www.perplexity.ai/?s=c&uuid=7906a3d5-463f-4678-be42-6511f1f7fc80)\n\nHere are other attempts to find seminal papers. The results look fairly decent (though not perfect particularly as it goes on) to my untrained eyes.\n\n![Image 98](https://miro.medium.com/v2/resize:fit:700/1*j50ecDrfetRT0M37dXfNbw.png)\n\n[https://www.perplexity.ai/?s=u&uuid=7b0e6e23-4c69-44cd-b83b-0b8b2d8a7cf2](https://www.perplexity.ai/?s=u&uuid=7b0e6e23-4c69-44cd-b83b-0b8b2d8a7cf2)\n\nAgain, changing the query to ask about seminal works instead of seminal papers make a difference. This shows how sensitive these searches are to different queries , which is characteristic of LLMs.\n\n![Image 99](https://miro.medium.com/v2/resize:fit:700/1*Vn8K139xDyI2O0UaZ4Y6ew.png)\n\n[https://www.perplexity.ai/?s=u&uuid=991f2edd-db8f-4082-9fa1-ed14224d4d1b](https://www.perplexity.ai/?s=u&uuid=991f2edd-db8f-4082-9fa1-ed14224d4d1b)\n\nLet’s try asking the question that Perplexity failed when restricting to Google Scholar — which paper first coined the term Bronze OA?\n\n![Image 100](https://miro.medium.com/v2/resize:fit:700/1*fMxyDrdqiHsoZamZoOJ_RQ.png)\n\n[https://www.perplexity.ai/?s=c&uuid=af8b3f88-fec3-4936-8588-73912af5a349](https://www.perplexity.ai/?s=c&uuid=af8b3f88-fec3-4936-8588-73912af5a349)\n\nAs far as I know this answer is correct. At the very least it was extracted from [source 1](https://core.ac.uk/download/pdf/345178270.pdf) — that believes this is so and is citing the Piwowar et al. (2018)\n\n**Preliminary Conclusion — In general, this technique looks to be really powerful, and it seems to be really looking into full-text of papers! But like any LLM prompts it can be sensitive to the phrasing you use.**\n\n3\\. Restricting to Semantic Scholar ([semanticscholar.org/](https://www.semanticscholar.org/me/research))\n---------------------------------------------------------------------------------------------------------\n\nThe other major source of open access data (both metadata and full-text) is Semantic Scholar. In fact, it is the source used by Elicit.org and [many other tools that need a source of scholarly paper data](https://musingsaboutlibrarianship.blogspot.com/p/list-of-innovative-literature-mapping.html).\n\nYou might bebetter off using [Elicit.org](http://elicit.org/) here, since they use the same source but use LLMs in a far more refined manner, but I was curious to see the difference.\n\nlet’s try to find seminal works.\n\nThe results don’t look as good if I ask for “[seminal paper](https://www.perplexity.ai/?s=u&uuid=8b81bb66-1e88-48ec-b830-9381f322c4e4)s” rather than “[Seminal works](https://www.perplexity.ai/?s=u&uuid=5c0d18ec-46e1-4ca4-8d1c-d636547fc679)” for unknown reasons.\n\n![Image 101](https://miro.medium.com/v2/resize:fit:700/1*irNe8yYMNZ8yiq1AMjf8Qg.png)\n\n[https://www.perplexity.ai/?s=u&uuid=5c0d18ec-46e1-4ca4-8d1c-d636547fc679](https://www.perplexity.ai/?s=u&uuid=5c0d18ec-46e1-4ca4-8d1c-d636547fc679)\n\nFor comparison, you might want to try the same queries on Elicit.org, which uses also Semantic Scholar as data with large language models to extract answers.\n\nHere’s a comparison when I use elicit.org to ask for seminal works.\n\n![Image 102](https://miro.medium.com/v2/resize:fit:700/1*LccijvZeb4xoUMr-LbR_Ew.png)\n\n[Using elicit to ask for seminal papers](https://elicit.org/search?q=what+are+seminal+works+on+theory+of+the+firm%3F&token=01GTA50Z37PPA55KB46MGAMHXG)\n\nInterestingly, the answers look worse in Elicit.org. I speculate that because Elicit is trying to rank papers to find seminal works, its top 4 papers which it uses to generate answers are quite old and do not tend to mention other seminal works?\n\nPerplexity restricted to Semantic Scholar also passes the test when I ask which paper first coined the term bronze OA as it is able to look into full-text of papers.\n\n![Image 103](https://miro.medium.com/v2/resize:fit:700/1*yGHWBPwOqbQ81vaVa0m63A.png)\n\n[https://www.perplexity.ai/?s=u&uuid=1c9fb150-8670-44f1-bf91-03dbcecbfead](https://www.perplexity.ai/?s=u&uuid=1c9fb150-8670-44f1-bf91-03dbcecbfead)\n\nWhen we try the same query in Elicit.org , it totally fails.\n\n![Image 104](https://miro.medium.com/v2/resize:fit:700/1*oGXBnZ5R4wF_pqoNTv7lhA.png)\n\n[Elicit query on which paper first coined the term bronze OA](https://elicit.org/search?q=which+paper+first+coined+the+term+%22bronze+oa%22%3F&token=01GTA58HG2XKCSVMKM7VHAGG2T)\n\nHere you can see the obvious problem. Elicit.org’s sematic search has totally failed to find the right papers at all. My guess is it’s ignoring the quotes for “bronze OA” and gets into trouble.\n\n[Changing the query to say “bronze open access” gets slightly better results but is still nowhere as good.](https://elicit.org/search?q=which+paper+first+coined+the+term+%22bronze+open+access%22%3F&token=01GTA5FAET6PAD82BS5JA1M4NG)\n\n**Preliminary Conclusion — In general restricting perplexity to answers from** [semanticscholar.org/](https://www.semanticscholar.org/me/research) is gives similar results to restricting answers to [core.ac.uk](http://core.ac.uk/) domain and both seem to be able to extract answers from full text.\n\nGiven [Elicit.org](http://elicit.org/) is using Semantic Scholar data with LLM technology, it is natural to compare the results there with this technique.\n\nInterestingly, for the few queries I tested, Perplexity restricted to Semantic Scholar domain trounces elicit.\n\nMy theory is as such. Elicit.org generates results from the top 4 results while Perplexity from the top 10. But more importantly, Perplexity probably is using a “dumber” keyword search, while Elicit is doing a smarter semantic type search to find documents.\n\nIronically this hurts certain type of searches. For example, when I use Perplexity it probably just does a keyword search (which matches full-text) and looks for documents that mention paper XYZ is seminal and surfaces those. Elicit.org is probably smarter, and tries to actually find seminal papers….\n\nFor whatever reason for the few use cases I tried, elicit.org’s more semantic searches are surfacing far worse results than Perplexity’s, and given the worse results, the LLM is unable to extract good answers.\n\n4\\. Restricting to scite ([scite.ai](http://scholar.google.com/))\n-----------------------------------------------------------------\n\nThe next domain I tried with Perplexity is using scite.ai. This is a interesting search index that doesn't have full-text. What they have besides the usual metadata is [citation citance or statements.](https://help.scite.ai/en-us/article/how-does-citation-statement-search-work-13tnvx7/)\n\nThey have recently launched in beta a [“Ask a question” feature that essentially uses LLMs to extract answers](https://www.linkedin.com/feed/update/urn:li:activity:7020861658109501440/)… but not from full-text, instead they use [citation citance or statements.](https://help.scite.ai/en-us/article/how-does-citation-statement-search-work-13tnvx7/) If you think about it is just a special part of the full-text aka the sentences around citations.\n\nAre the results better? Let’s try again with perplexity limited to scite.ai\n\n![Image 105](https://miro.medium.com/v2/resize:fit:700/1*VE0OuXgvnh_4iejd2MWJVQ.png)\n\n[https://www.perplexity.ai/?s=c&uuid=a76ee219-f4c3-48df-b0ed-238ea99a4de3](https://www.perplexity.ai/?s=c&uuid=a76ee219-f4c3-48df-b0ed-238ea99a4de3)\n\nHere’s a s[imilar search asking for seminal works on deep learning using scite’s beta feature](https://www.perplexity.ai/?s=c&uuid=e1b58dc8-980f-4022-97e7-5f4ac8fd214b)\n\nAs mentioned above, scite.ai has it’s own beta “Ask a question” feature that is using GPT-3 to extract answers. How does it match up for the same query?\n\nNot very well in my opinion.\n\n![Image 106](https://miro.medium.com/v2/resize:fit:700/1*u4RfMuBgLMFO_vqRAcmeSA.png)\n\n[https://scite.ai/search?mode=question-answering&q=what%20are%20some%20seminal%20works%20on%20theory%20of%20the%20firm%3F](https://scite.ai/search?mode=question-answering&q=what+are+some+seminal+works+on+theory+of+the+firm%3F)\n\nNow let’s try Perplexity on the question — which paper first coined the term bronze OA. As before this is restricted to the scite.ai domain.\n\n![Image 107](https://miro.medium.com/v2/resize:fit:700/1*uwnYuAafG9ZsYDyazYikbw.png)\n\n[https://www.perplexity.ai/?s=u&uuid=0a2e339e-89f2-4a62-8f7c-6442ac3c052b](https://www.perplexity.ai/?s=u&uuid=0a2e339e-89f2-4a62-8f7c-6442ac3c052b)\n\nSo it failed for the specific question on which paper first coined the term bronze OA. It’s unclear why since the same type of query worked when restricting on the domain core.ac.uk. Maybe the papers available was different?\n\nFor what’s it worth using the scite.ai’s beta ask a question feature, [also did not do well.](https://scite.ai/search?mode=question-answering&q=which+paper+first+coined+the+term+%22bronze+oa%22%3F)\n\n![Image 108](https://miro.medium.com/v2/resize:fit:700/1*TdgLQVIJJITizl9CMNnVwQ.png)\n\n[https://scite.ai/search?mode=question-answering&q=which%20paper%20first%20coined%20the%20phrase%20%22bronze%20oa%22%3F](https://scite.ai/search?mode=question-answering&q=which+paper+first+coined+the+phrase+%22bronze+oa%22%3F)\n\n**Preliminary Conclusion —It's hard to say what’s going on. It seems to be able to identify seminal works to some extent, but in my few examples, restricting to scite.ai domain doesn’t seem to do as well as to say core.ac.uk**\n\nI’m guessing because each article paper comes with citation statements, it can see how other papers are describing the paper itself. For example, a seminal paper like [Coase(1937) will have a scite.ai page](https://scite.ai/reports/the-nature-of-the-firm-6p6W9E) listing not just the metadata of the paper but also include citation statements from other papers saying it is a seminal work and this is picked up by perplexity.\n\nWhy it can’t find Piwowar (2018) as the paper that coined Bronze OA is unclear to me, [as there is a scite page for it.](https://scite.ai/reports/the-state-of-oa-a-b2AZ2gN) Is it simply the lack of a citation statement in scite saying so?\n\nSimilar to the Semantic Scholar case, for some reason the results I get using perplexity restricted to scite domain seem superior to using specialized search systems that use these sources. In this case, Perplexity restricted to scite.ai gives better results than scite.ai’s build-in ask a question feature!\n\nThis feels surprising because you would expect a specialized tool like elicit.org or scite.ai to work better than a tool like perplexity that was never designed for this use case.\n\nThen again Scite.ai’s feature is still in beta and while elicit has been working with OpenAI for almost as long as Perplexity (1 year+), it focused more on extraction of article properties (e.g. population sample, sample size, region of study etc) and the generative answer part was added fairly recently.\n\n5\\. Restricting to Google books (books.google.com)\n--------------------------------------------------\n\nLet’s now switch to books, in particular let’s restrict results to books.google.com\n\n![Image 109](https://miro.medium.com/v2/resize:fit:700/1*jr8BKeF5zzu8MukSJN43sw.png)\n\n[https://www.perplexity.ai/?s=u&uuid=fda982fc-3217-4872-9a55-63796d05d3e8](https://www.perplexity.ai/?s=u&uuid=fda982fc-3217-4872-9a55-63796d05d3e8)\n\nIn first test query, I see the sources it points to are pages like\n\nSome of these books have preview versions available, is Perplexity able to “See” them?\n\nProbably. Take the query below.\n\n![Image 110](https://miro.medium.com/v2/resize:fit:700/1*Jgb9lPPn1h5MVIVNZF5wJA.png)\n\n[https://www.perplexity.ai/?s=u&uuid=5d9c66bd-1f08-4ef4-9289-87957a5f11f8](https://www.perplexity.ai/?s=u&uuid=5d9c66bd-1f08-4ef4-9289-87957a5f11f8)\n\nYou can see in the sources, sentences found by Perplexity, and when you check google books , you will notice there are from within Preview versions of books.\n\nIn the example below, I looked at the first source and searched within the book “It is clear that Darwin did not sail directly from Christian orthodoxy to atheistic materialism.” and you can see the hit.\n\n![Image 111](https://miro.medium.com/v2/resize:fit:700/1*CXJJzxV3zhWmKgumTUlVAw.png)\n\n[https://books.google.com.sg/books?redir\\_esc=y&id=0TA81BTW3dIC&q=It+is+clear+that+Darwin+did+not+sail+directly+from+Christian+orthodoxy+to+atheistic+materialism.#v=snippet&q=It%20is%20clear%20that%20Darwin%20did%20not%20sail%20directly%20from%20Christian%20orthodoxy%20to%20atheistic%20materialism.&f=false](https://books.google.com.sg/books?redir_esc=y&id=0TA81BTW3dIC&q=It+is+clear+that+Darwin+did+not+sail+directly+from+Christian+orthodoxy+to+atheistic+materialism.#v=snippet&q=It%20is%20clear%20that%20Darwin%20did%20not%20sail%20directly%20from%20Christian%20orthodoxy%20to%20atheistic%20materialism.&f=false)\n\nAll this seems very good, but when I try to work the other way, where I search for something that is available in Google book preview , Perplexity can’t seem to find the answer.\n\nI suspect this has to do with the way Perplexity works . My guess is for googlebooks it doesnt have all the google book previews indexed…but if you hit the right pages, it can extract the results?\n\nPerplexity — how it works\n-------------------------\n\nPerplexity [has precious little information on how it works.](https://www.perplexity.ai/about) we do know it [uses or used OpenAI’s GPT-3 (similar to Elicit)](https://gpt3demo.com/apps/perplexity-ai) , but we don’t how it matches or ranks pages.\n\nThe first question I wondered about is this. Like most search engines I assume when you search you are matching an index of content their crawlers have seen earlier.\n\nBut does it then extract the information from the indexed version or does it scrape the result on the fly? I believe it scrapes the page on the fly,\n\n![Image 112](https://miro.medium.com/v2/resize:fit:700/1*S4xRZds4ma--qqx-bw3LoA.png)\n\n[https://www.perplexity.ai/?s=u&uuid=fa02755a-5d6c-4096-9e44-8c273ac69cee](https://www.perplexity.ai/?s=u&uuid=fa02755a-5d6c-4096-9e44-8c273ac69cee)\n\nThis is because when I search for the current date it is able to give me the right date and time, so it is definitely looking at the current contents of the pages found and not the indexed cached version.\n\nOne other feature I did not mention is, you can actually edit sources, by adding or removing them.\n\nFor example, when I do a search restricted to core.ac.uk, it is unable to find the right answer because the paper isn’t on core.ac.uk. You can actually edit sources to improve the results.\n\n![Image 113](https://miro.medium.com/v2/resize:fit:700/1*lVBxUyXvDUZz_HLGU3Qbug.png)\n\n[https://www.perplexity.ai/?s=u&uuid=93257103-9929-4db7-98c2-af1573aef5f1](https://www.perplexity.ai/?s=u&uuid=93257103-9929-4db7-98c2-af1573aef5f1)\n\nThe feature to edit sources is quite hidden. Click on the three dots button and then “Edit sources”.\n\n![Image 114](https://miro.medium.com/v2/resize:fit:700/1*ebBgWCXSxgig8s9vvjgqWw.png)\n\n![Image 115](https://miro.medium.com/v2/resize:fit:700/1*5xGmKanBy0BOd4uGDcNhog.png)\n\nRemoving sources is nice particularly if you use a full internet search and you want to remove results from less trust-worthy sources.\n\nStill in this particular case, Perplexity is unable to find the right answer as the paper with the right answer simply isn’t on core.ac.uk as it isnt open access. However, by simply adding a URL to a page with the right paper’s title & abstract the problem should be fixed. (See earliest example’s using Perplexity restricted to Google scholar domain)\n\nHowever while there is a “add more sources” feature button, but disappointingly, it does not allow you to add URLs directly, but just gives you the next highest ranked urls.\n\nIn fact, I would love for perplexity to allow me to define list of domains as a whitelist (only show results from these domains. I would add say all preprint, publisher etc. domains for research papers) or alternatively a blacklist (exclude trash domains)\n\nConclusion\n----------\n\nPerplexity restricted to domains with papers seems unreasonably effective! And this is despite not being designed for this use case.\n\nI have long talked [about the power of Machine learning and deep learning coupled with open access to change the game](https://musingsaboutlibrarianship.blogspot.com/2022/06/diversity-of-scholarly-record-push-to.html). This appears to be one aspect of it.\n\n> Related: [Are we undervaluing Open Access by not correctly factoring in the potentially huge impacts of Machine learning? — An academic librarian’s view](https://medium.com/a-academic-librarians-thoughts-on-open-access/are-we-undervaluing-open-access-by-not-correctly-evaluating-the-potentially-huge-impacts-of-e93af1de9414)\n\nMore specifically back in 2020 during the height of the pandemic, [I mused about how the CORD-19 (COVID open research dataset) which was a huge project, partnered by Publishers, discovery vendors etc to aggregate all papers on COVID (including full-text) , harmonize the data to allow researchers to do text mining was a interesting “grand experiment”](https://musingsaboutlibrarianship.blogspot.com/2020/05/covid-19-and-text-data-mining-tdm.html) on the power of such techniques.\n\nIt seems two years on, the combination of search technology + even more powerful LLMs in general will kick off yet another larger wave of experimentation.\n\nFrom my point of view, I am nearly sold, it seems inevitable to me that the future of search belongs to this class of systems that combine search results with LLMs extraction!\n\nPost edit note: I just got access to the new Bing+chat feature. And the results are out of this world. Most of the time, I don’t even need to do site restriction. Some examples below\n\n![Image 116](https://miro.medium.com/v2/resize:fit:700/1*7WRKSCz0BoEqu48QUD-YIg.png)\n\n![Image 117](https://miro.medium.com/v2/resize:fit:700/1*FXmluflgn7GQ1yggqJSZmQ.png)\n\n![Image 118](https://miro.medium.com/v2/resize:fit:700/1*xV-njfJQcbeFQU59tF36CA.png)\n\n![Image 119](https://miro.medium.com/v2/resize:fit:700/1*wxQH6nOc8Qvl20A-LlRAQw.png)\n\n![Image 120](https://miro.medium.com/v2/resize:fit:700/1*v6o8-GBHEJDRxIEQxxnR-A.png)",
  "publishedTime": "2023-02-28T02:55:02.849Z",
  "usage": {
    "tokens": 9565
  }
}
```
