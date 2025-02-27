---
title: BERT Automatic Interlinking Streamlit App V2 | Lee Foot
description: The first version of this app was recently highlighted in this excellent article, 'Mastering Topic Clusters in SEO.' (If you haven't yet, it's a must-read!) This got me thinking it’s high time for an overhaul of the original app. Checking in, I’m amazed it had over 17,000 unique visitors since its release in May 2022! I’ve done absolutely nothing to market it other than the initial tweet and being featured as Streamlit’s app of the month in May 2022. This success led me to realise that it's high time the app received an overhaul.
url: https://leefoot.co.uk/portfolio/bert-automatic-interlinking-streamlit-app-v2/
timestamp: 2025-01-20T16:05:36.566Z
domain: leefoot.co.uk
path: portfolio_bert-automatic-interlinking-streamlit-app-v2
---

# BERT Automatic Interlinking Streamlit App V2 | Lee Foot


The first version of this app was recently highlighted in this excellent article, 'Mastering Topic Clusters in SEO.' (If you haven't yet, it's a must-read!) This got me thinking it’s high time for an overhaul of the original app. Checking in, I’m amazed it had over 17,000 unique visitors since its release in May 2022! I’ve done absolutely nothing to market it other than the initial tweet and being featured as Streamlit’s app of the month in May 2022. This success led me to realise that it's high time the app received an overhaul.


## Content

What’s it all about?
--------------------

The premise is to use _[Sentence Transformers](https://www.sbert.net/index.html)_ to find deeper relationships between pages on a website.

Initially, it was designed to highlight related Buyer’s Guides on eCommerce category pages, as well as to suggest related products.

Here are some practical applications for this app:

*   Interlink Related Products Within Category Text
*   Show Related Categories on Existing Category Pages
*   Surface Related Content to Assist Conversion (Blogs, Buyers’ Guides, etc.)
*   Display Products Most Closely Related to Category Page for Increased Relevancy
*   Feature Related Blog Posts

Try it: [BERT interlinking app V2](https://bertlinker.streamlit.app/)

A Different Angle
-----------------

![Image 23](https://leefoot.co.uk/wp-content/uploads/2023/12/2023-12-19-11_35_37-BERT-Semantic-Interlinking-Tool-V2-%C2%B7-Streamlit.png)

BERT Semantic Page Interlinker V2

_“There are tons of page Interlinkers out there, why not just use those?”_

It’s a fair point, this script doesn’t even use anchor text or link metrics when making recommendations. Its unique approach lies in forming logical connections between pages, aimed at enhancing user satisfaction and potentially increasing revenue.

**Example #1:**

![Image 24](https://leefoot.co.uk/wp-content/uploads/2023/12/HP-Printer-Ink-Relationship.jpg)Here’s an example of the Interlinker correctly making the connection between a page about _HP Original Ink_ and _printer paper_.

If this was an eCommerce project, the recommendation would most likely be to show the printer and printer ink categories as related categories on the page or within the existing anchor text.

**Example #2:**

![Image 25](https://leefoot.co.uk/wp-content/uploads/2023/12/Hair-Care-Related-Products.jpg)How about linking _Hair Care_ to:

*   Hair Treatments
*   Hair Straighteners
*   Hair Curlers
*   Hair Brushes
*   Hair Clippers and
*   Hair Dryers?

Syntactically those words are far away from each other, but using the magic of _Sentence Transformers_ the app is able to understand that these pages are related.

Linking those related pages would be good for users, bots and ultimately the bottom line.

New Features
------------

Looking back, the initial version was quite basic, with a codebase that, although functional, left much to be desired.

In fact, I noticed a huge oversight that prevented around 90% of matches from being returned!

### Clustering

*   Minimum Similarity Cutoff
*   Choice of Sentence Transformers
*   Multi-Lingual Transformer Trained in 50 Languages

### Visualization Options

*   Choose between Tree Chart or Radial Chart Visualisations
*   Full Chart Customization Options: Nodes, Chart Size, Formatting
*   Real Time Chart Updates: See the Impact of Changing Values on Link Relationships
*   Automatic Source and Destination URL Mapping

### File Handling

*   Supports Uploads in Excel or CSV formats (UTF8 format only)
*   _Excel_ Download with Mapping Between Pages and Similarity Threshold Cutoff
*   Source File Filtering Options: Match Only Indexable Pages, Remove Parameters, etc.

### Code Base / Performance / UX

*   Completely Rewritten from the Ground Up
*   Cleaner, More Efficient Code Base
*   Fixed Bug Preventing Most Matches from Being Returned
*   Automatic Mapping of Screaming Frog’s Address and H1-1 Columns in Five Languages
*   Improved UX and Error Handling Including Tool Tips and Instructions

![Image 26](https://leefoot.co.uk/wp-content/uploads/2023/12/Clustering-Options.png)

BERT Interlinker V2 Clustering Options

Instructions and Getting Started
--------------------------------

![Image 27: screaming frog crawl file example](https://leefoot.co.uk/wp-content/uploads/2023/12/screaming-frog-crawl-file-example.png)

screaming frog crawl file example

You need a crawl file that at a minimum contains a URL column and a column to match.

Just crawl any site you need to run the interlinker on, export the html file as a _csv_ or _Excel_ file and upload it to the Streamlit app.

While I recommend matching on the H1 tag for best results, you’re free to match on any element you prefer, such as the page title, blog content, etc.

In testing I found the H1 works best because it’s a description of the content that can be found o the page, rather than the content itself – which gave mixed results.

The app is setup to automatically detect and populate the address column and keyword column using the default URL and H1 column names of Screaming Frog (in five languages) for convenience, but you’re free to change the mapping by changing the drop-down menu.

Please note: You are free to use any crawler you like as long as the output file contains a URL column and the column containing the content you would like to interlink. (You just may need to manually select the correct column, rather than have it automatically mapped for you).

Settings Deep Dive
------------------

### Clustering Options

I used sensible defaults for this app which should make it easy to just jump in and start using the app with little to no research.

If you want to get the best out of the app though, it’s worth your time drilling into the various options at your disposal.

#### Transformer Model

There are three transformer models available. They have been selected based on speed, a balance of speed and semantic performance and multi-linguistic capabilities.

*   _paraphrase-MiniLM-L3-v2_ (Fastest – default model)
*   _all-MiniLM-L6-v2_ (Good balance between speed and semantic performance)
*   _paraphrase-multilingual-MiniLM-L12-v2_ (Multilingual, trained in 50+ languages)

#### Minimum Similarity Score

This is the threshold in which results are considered to be similar. The higher the score, the stricter the matching. The chart will display the top results in real time, so you can get a good idea of which cut off works well for your website.

This option affects the _Excel_ file download. If you want to include all the results, set the similarity score to the lowest option (50%).

![Image 28: BERT Interlinker Clustering Options](https://leefoot.co.uk/wp-content/uploads/2023/12/clustering_options.jpg)

BERT Interlinker Clustering Options

![Image 29: BERT Semantic Interlinker File Operations](https://leefoot.co.uk/wp-content/uploads/2023/12/File-Operations.png)

BERT Semantic Interlinker File Operations

### File Operations

#### Upload File

Valid options are .csv or .xlsx.

#### Select Columns

Options to select both the Address and Content columns. Columns are automatically mapped to the default Screaming Frog column names for the URL and H1-1 by default. They can be mapped to any column you specify.

Includes automatic validation for the URL column.

#### Filtering Options

Filters are automated selected by default and filter out the following URL types.

*   Drop Duplicate Pages
*   Filter Out Paginated URLs
*   Filter Out URLs with Parameters
*   Keep Only Indexable Status URLs

Filtered URLs are removed from the total URL count when processing the file.

If a Indexability column is found, the option to keep only indexable URLs will drop any non-indexable URLs before processing.

### Chart Creation Options

#### Tree Layout Options

Choice of Tree layout or radial layout. This option can be changed on the fly after processing is completed, so you can see which you prefer. (The default is Tree).

Charts can be saved by right clicking and choosing the ‘Save image’ option in your browser.

### Number of Level 1 / Level 2 Nodes to Preview

This option restricts the number of nodes visible in the graph to the top X nodes at level 1 and 2 (It does not impact the final output).

#### Tree Chart Node Size

Increase or decrease the size of the Tree Chart node size. Useful for fine tuning visualisations.

#### Font Size of Labels

Increase or decrease the label font size, Useful for fine tuning visualisations.

#### Chart Height

Increase or decrease the height of the tree and radial chart. Useful to display more chart nodes on the screen / make charts easier to read. Useful if exporting to a presentation.

#### Source and Destination Path Filters

Note: Filters are applied to the saved Excel file.

![Image 30](https://leefoot.co.uk/wp-content/uploads/2023/12/bert_interlinker_chart.png)

Streamlit Web App Limitations – (Contact Me if You Need More)
-------------------------------------------------------------

### Input File Limited to a Maximum of 1,000 Rows

The Streamlit app currently limits imports to 1,000 rows. This may change in the future depending on how the Streamlit app copes. Sentence Transformers are _very_ resource intensive.

You can work around this to an extent by cleaning up the crawl file ahead of time. (Removing non-indexable pages or matching different templates individually).

Note: This value is calculated after the pre-filtering options are applied.

Should you require more rows, please don’t hesitate to [get in touch](https://leefoot.co.uk/hire-me/) – I’m available to customise this app further or provide it as a managed service, tailored to your needs.

### 15 Matches per URL

Limited to the first 15 matches per URL. In testing large eCommerce Websites this seemed to be more than enough related pages. The app needs to be constrained for situations when someone uploads 1000’s of boiler plate \[Keyword\] in \[Location\] type pages that would endlessly match to itself.

### Limited to Three Different Sentence Transformers

I tried to pick a good balance between speed and performance, whilst still ensuring that there is a multi-lingual option. For performance reasons the fastest transformer is selected, but there is an option to choose a slower model with a higher semantic score.

## Metadata

```json
{
  "title": "BERT Automatic Interlinking Streamlit App V2 | Lee Foot",
  "description": "The first version of this app was recently highlighted in this excellent article, 'Mastering Topic Clusters in SEO.' (If you haven't yet, it's a must-read!) This got me thinking it’s high time for an overhaul of the original app. Checking in, I’m amazed it had over 17,000 unique visitors since its release in May 2022! I’ve done absolutely nothing to market it other than the initial tweet and being featured as Streamlit’s app of the month in May 2022. This success led me to realise that it's high time the app received an overhaul.",
  "url": "https://leefoot.co.uk/portfolio/bert-automatic-interlinking-streamlit-app-v2/",
  "content": "What’s it all about?\n--------------------\n\nThe premise is to use _[Sentence Transformers](https://www.sbert.net/index.html)_ to find deeper relationships between pages on a website.\n\nInitially, it was designed to highlight related Buyer’s Guides on eCommerce category pages, as well as to suggest related products.\n\nHere are some practical applications for this app:\n\n*   Interlink Related Products Within Category Text\n*   Show Related Categories on Existing Category Pages\n*   Surface Related Content to Assist Conversion (Blogs, Buyers’ Guides, etc.)\n*   Display Products Most Closely Related to Category Page for Increased Relevancy\n*   Feature Related Blog Posts\n\nTry it: [BERT interlinking app V2](https://bertlinker.streamlit.app/)\n\nA Different Angle\n-----------------\n\n![Image 23](https://leefoot.co.uk/wp-content/uploads/2023/12/2023-12-19-11_35_37-BERT-Semantic-Interlinking-Tool-V2-%C2%B7-Streamlit.png)\n\nBERT Semantic Page Interlinker V2\n\n_“There are tons of page Interlinkers out there, why not just use those?”_\n\nIt’s a fair point, this script doesn’t even use anchor text or link metrics when making recommendations. Its unique approach lies in forming logical connections between pages, aimed at enhancing user satisfaction and potentially increasing revenue.\n\n**Example #1:**\n\n![Image 24](https://leefoot.co.uk/wp-content/uploads/2023/12/HP-Printer-Ink-Relationship.jpg)Here’s an example of the Interlinker correctly making the connection between a page about _HP Original Ink_ and _printer paper_.\n\nIf this was an eCommerce project, the recommendation would most likely be to show the printer and printer ink categories as related categories on the page or within the existing anchor text.\n\n**Example #2:**\n\n![Image 25](https://leefoot.co.uk/wp-content/uploads/2023/12/Hair-Care-Related-Products.jpg)How about linking _Hair Care_ to:\n\n*   Hair Treatments\n*   Hair Straighteners\n*   Hair Curlers\n*   Hair Brushes\n*   Hair Clippers and\n*   Hair Dryers?\n\nSyntactically those words are far away from each other, but using the magic of _Sentence Transformers_ the app is able to understand that these pages are related.\n\nLinking those related pages would be good for users, bots and ultimately the bottom line.\n\nNew Features\n------------\n\nLooking back, the initial version was quite basic, with a codebase that, although functional, left much to be desired.\n\nIn fact, I noticed a huge oversight that prevented around 90% of matches from being returned!\n\n### Clustering\n\n*   Minimum Similarity Cutoff\n*   Choice of Sentence Transformers\n*   Multi-Lingual Transformer Trained in 50 Languages\n\n### Visualization Options\n\n*   Choose between Tree Chart or Radial Chart Visualisations\n*   Full Chart Customization Options: Nodes, Chart Size, Formatting\n*   Real Time Chart Updates: See the Impact of Changing Values on Link Relationships\n*   Automatic Source and Destination URL Mapping\n\n### File Handling\n\n*   Supports Uploads in Excel or CSV formats (UTF8 format only)\n*   _Excel_ Download with Mapping Between Pages and Similarity Threshold Cutoff\n*   Source File Filtering Options: Match Only Indexable Pages, Remove Parameters, etc.\n\n### Code Base / Performance / UX\n\n*   Completely Rewritten from the Ground Up\n*   Cleaner, More Efficient Code Base\n*   Fixed Bug Preventing Most Matches from Being Returned\n*   Automatic Mapping of Screaming Frog’s Address and H1-1 Columns in Five Languages\n*   Improved UX and Error Handling Including Tool Tips and Instructions\n\n![Image 26](https://leefoot.co.uk/wp-content/uploads/2023/12/Clustering-Options.png)\n\nBERT Interlinker V2 Clustering Options\n\nInstructions and Getting Started\n--------------------------------\n\n![Image 27: screaming frog crawl file example](https://leefoot.co.uk/wp-content/uploads/2023/12/screaming-frog-crawl-file-example.png)\n\nscreaming frog crawl file example\n\nYou need a crawl file that at a minimum contains a URL column and a column to match.\n\nJust crawl any site you need to run the interlinker on, export the html file as a _csv_ or _Excel_ file and upload it to the Streamlit app.\n\nWhile I recommend matching on the H1 tag for best results, you’re free to match on any element you prefer, such as the page title, blog content, etc.\n\nIn testing I found the H1 works best because it’s a description of the content that can be found o the page, rather than the content itself – which gave mixed results.\n\nThe app is setup to automatically detect and populate the address column and keyword column using the default URL and H1 column names of Screaming Frog (in five languages) for convenience, but you’re free to change the mapping by changing the drop-down menu.\n\nPlease note: You are free to use any crawler you like as long as the output file contains a URL column and the column containing the content you would like to interlink. (You just may need to manually select the correct column, rather than have it automatically mapped for you).\n\nSettings Deep Dive\n------------------\n\n### Clustering Options\n\nI used sensible defaults for this app which should make it easy to just jump in and start using the app with little to no research.\n\nIf you want to get the best out of the app though, it’s worth your time drilling into the various options at your disposal.\n\n#### Transformer Model\n\nThere are three transformer models available. They have been selected based on speed, a balance of speed and semantic performance and multi-linguistic capabilities.\n\n*   _paraphrase-MiniLM-L3-v2_ (Fastest – default model)\n*   _all-MiniLM-L6-v2_ (Good balance between speed and semantic performance)\n*   _paraphrase-multilingual-MiniLM-L12-v2_ (Multilingual, trained in 50+ languages)\n\n#### Minimum Similarity Score\n\nThis is the threshold in which results are considered to be similar. The higher the score, the stricter the matching. The chart will display the top results in real time, so you can get a good idea of which cut off works well for your website.\n\nThis option affects the _Excel_ file download. If you want to include all the results, set the similarity score to the lowest option (50%).\n\n![Image 28: BERT Interlinker Clustering Options](https://leefoot.co.uk/wp-content/uploads/2023/12/clustering_options.jpg)\n\nBERT Interlinker Clustering Options\n\n![Image 29: BERT Semantic Interlinker File Operations](https://leefoot.co.uk/wp-content/uploads/2023/12/File-Operations.png)\n\nBERT Semantic Interlinker File Operations\n\n### File Operations\n\n#### Upload File\n\nValid options are .csv or .xlsx.\n\n#### Select Columns\n\nOptions to select both the Address and Content columns. Columns are automatically mapped to the default Screaming Frog column names for the URL and H1-1 by default. They can be mapped to any column you specify.\n\nIncludes automatic validation for the URL column.\n\n#### Filtering Options\n\nFilters are automated selected by default and filter out the following URL types.\n\n*   Drop Duplicate Pages\n*   Filter Out Paginated URLs\n*   Filter Out URLs with Parameters\n*   Keep Only Indexable Status URLs\n\nFiltered URLs are removed from the total URL count when processing the file.\n\nIf a Indexability column is found, the option to keep only indexable URLs will drop any non-indexable URLs before processing.\n\n### Chart Creation Options\n\n#### Tree Layout Options\n\nChoice of Tree layout or radial layout. This option can be changed on the fly after processing is completed, so you can see which you prefer. (The default is Tree).\n\nCharts can be saved by right clicking and choosing the ‘Save image’ option in your browser.\n\n### Number of Level 1 / Level 2 Nodes to Preview\n\nThis option restricts the number of nodes visible in the graph to the top X nodes at level 1 and 2 (It does not impact the final output).\n\n#### Tree Chart Node Size\n\nIncrease or decrease the size of the Tree Chart node size. Useful for fine tuning visualisations.\n\n#### Font Size of Labels\n\nIncrease or decrease the label font size, Useful for fine tuning visualisations.\n\n#### Chart Height\n\nIncrease or decrease the height of the tree and radial chart. Useful to display more chart nodes on the screen / make charts easier to read. Useful if exporting to a presentation.\n\n#### Source and Destination Path Filters\n\nNote: Filters are applied to the saved Excel file.\n\n![Image 30](https://leefoot.co.uk/wp-content/uploads/2023/12/bert_interlinker_chart.png)\n\nStreamlit Web App Limitations – (Contact Me if You Need More)\n-------------------------------------------------------------\n\n### Input File Limited to a Maximum of 1,000 Rows\n\nThe Streamlit app currently limits imports to 1,000 rows. This may change in the future depending on how the Streamlit app copes. Sentence Transformers are _very_ resource intensive.\n\nYou can work around this to an extent by cleaning up the crawl file ahead of time. (Removing non-indexable pages or matching different templates individually).\n\nNote: This value is calculated after the pre-filtering options are applied.\n\nShould you require more rows, please don’t hesitate to [get in touch](https://leefoot.co.uk/hire-me/) – I’m available to customise this app further or provide it as a managed service, tailored to your needs.\n\n### 15 Matches per URL\n\nLimited to the first 15 matches per URL. In testing large eCommerce Websites this seemed to be more than enough related pages. The app needs to be constrained for situations when someone uploads 1000’s of boiler plate \\[Keyword\\] in \\[Location\\] type pages that would endlessly match to itself.\n\n### Limited to Three Different Sentence Transformers\n\nI tried to pick a good balance between speed and performance, whilst still ensuring that there is a multi-lingual option. For performance reasons the fastest transformer is selected, but there is an option to choose a slower model with a higher semantic score.",
  "publishedTime": "2023-12-19T10:06:50+00:00",
  "usage": {
    "tokens": 2146
  }
}
```
