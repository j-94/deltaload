---
title: Carrot2 search results clustering engine
description: Carrot2 organizes your search results into topics. With an instant overview of what's available, you will quickly find what you're looking for.
url: https://search.carrot2.org/#/workbench
timestamp: 2025-01-20T16:19:35.467Z
domain: search.carrot2.org
path: root
---

# Carrot2 search results clustering engine


Carrot2 organizes your search results into topics. With an instant overview of what's available, you will quickly find what you're looking for.


## Content

Carrot2 search results clustering engine
===============

[](https://search.carrot2.org/#/)[](https://search.carrot2.org/#/search)[](https://search.carrot2.org/#/workbench)

[](https://search.carrot2.org/#/about)[](https://github.com/carrot2/carrot2)

clusteringWorkbench

Cluster

Data source

Clustering algorithm

Filters

#### Web

Query

Language

Country

Safe search

Data sources

AllFastest

Partner

Customer ID

#### PubMed

Query

Max results

0

500

100

API key

#### Local file

Loads documents from a local file. Carrot2 XML, JSON, CSV and Excel formats are supported.

File

Browse or drag 'n' drop your file here.

Fields to cluster

No natural text content detected

Only natural text fields shown, show all fields.

#### Solr

Queries Apache Solr.

Solr service URL

Connect

Solr collection to search

Collection list is empty, no content to search.

Fields to cluster

No natural text content detected

Only natural text fields shown, show all fields.

Query

Max results

0

1000

100

Use highlights for clustering

Additional search request parameters

#### Elasticsearch

Queries Elasticsearch.

Elasticsearch service URL

Connect

Elasticsearch collection to search

Collection list is empty, no content to search.

Fields to cluster

No natural text content detected

Only natural text fields shown, show all fields.

Query

Max results

0

1000

100

#### Clusters

Parameters affecting the number, structure and content of clusters.

Desired cluster count

2

100

30

Minimum cluster size

1

100

2

Cluster label assignment method

SimpleLabelAssigner

UniqueLabelAssigner

Exact phrase assignment

Cluster merging threshold

0

1

0.70

Size-score sorting ratio

0

1

0

#### Cluster labels

Customization of cluster labels.

Phrase label boost

0

10

1.5

Phrase length penalty start

2

8

8

Phrase length penalty stop

2

8

8

Truncated label filter enabled

Truncated label threshold

0

1

0.65

Genitive label filter enabled

Minimum label length filter enabled

Minimum label length

Numeric label filter enabled

Query label filter enabled

Stop label filter enabled

Stop word label filter enabled

#### Dictionaries

Label and word exclusion dictionaries.

Excluded label patterns

glob

exact

regexp

Copy JSONCopy JSONCopy JSON

One pattern per line, separate words with spaces, `*` is zero or more words, syntax help

Stop words

glob

exact

regexp

Copy JSONCopy JSONCopy JSON

One pattern per line, separate words with spaces, `*` is zero or more words, syntax help

#### Language model

Parameters of the document representation used by the clustering algorithm.

Language

Term weighting for term-document matrix

Boosted fields

Boosted fields weight

0

10

2.0

Phrase document frequency threshold

1

100

1

Word document frequency threshold

1

100

1

Maximum word document frequency

0

1

0.90

Term-document matrix factorization method

Factorization quality

Factorization quality

Factorization quality

Factorization quality

Maximum term-document matrix size

#### Clusters

Parameters affecting the number, structure and content of clusters.

Maximum number of final clusters

Maximum base clusters

Minimum base cluster score

0

10

2.0

Minimum base cluster documents

2

20

2

Document count boost

Merge all stem-equivalent phrases when discovering base clusters

Base cluster merge threshold

0

1

0.60

Size-score sorting ratio

0

1

0

#### Cluster labels

Customization of cluster labels.

Boost single-term clusters

Optimal cluster label length

Phrase length tolerance

Maximum words per label

Maximum phrases per label

Maximum cluster phrase overlap

0

1

0.60

Minimum general phrase coverage

0

1

0.50

#### Language model

Parameters of the document representation used by the clustering algorithm.

Language

Max relative word DF

0

1

0.90

Word document frequency threshold

1

100

1

#### Clusters

Parameters affecting the number, structure and content of clusters.

Cluster count

Maximum iterations

Partition count

2

10

2

#### Cluster labels

Customization of cluster labels.

Label count

1

10

3

#### Language model

Parameters of the document representation used by the clustering algorithm.

Language

Term weighting for term-document matrix

Boosted fields

Boosted fields weight

0

10

2.0

Maximum word document frequency

0

1

0.90

Word document frequency threshold

1

100

1

Use dimensionality reduction

Term-document matrix factorization method

Factorization quality

Factorization quality

Factorization quality

Factorization quality

Maximum term-document matrix size

Welcome to Clustering Workbench
-------------------------------

### the expert-level Carrot2 application

1.  ### Choose data source:
    
    *   Web search results
    *   PubMed abstracts
    *   Excel, CSV, OpenOffice, JSON or XML files
    *   Apache Solr search results
    *   Elasticsearch results
2.  ### Configure **Web** data source
    
    Type your query in the **Query** box. Use the common web search engine syntax such as double quotes for `"phrase search"`,`-` to exclude words or phrases etc.
3.  ### Press the **Cluster** button

## Metadata

```json
{
  "title": "Carrot2 search results clustering engine",
  "description": "Carrot2 organizes your search results into topics. With an instant overview of what's available, you will quickly find what you're looking for.",
  "url": "https://search.carrot2.org/#/workbench",
  "content": "Carrot2 search results clustering engine\n===============\n\n[](https://search.carrot2.org/#/)[](https://search.carrot2.org/#/search)[](https://search.carrot2.org/#/workbench)\n\n[](https://search.carrot2.org/#/about)[](https://github.com/carrot2/carrot2)\n\nclusteringWorkbench\n\nCluster\n\nData source\n\nClustering algorithm\n\nFilters\n\n#### Web\n\nQuery\n\nLanguage\n\nCountry\n\nSafe search\n\nData sources\n\nAllFastest\n\nPartner\n\nCustomer ID\n\n#### PubMed\n\nQuery\n\nMax results\n\n0\n\n500\n\n100\n\nAPI key\n\n#### Local file\n\nLoads documents from a local file. Carrot2 XML, JSON, CSV and Excel formats are supported.\n\nFile\n\nBrowse or drag 'n' drop your file here.\n\nFields to cluster\n\nNo natural text content detected\n\nOnly natural text fields shown, show all fields.\n\n#### Solr\n\nQueries Apache Solr.\n\nSolr service URL\n\nConnect\n\nSolr collection to search\n\nCollection list is empty, no content to search.\n\nFields to cluster\n\nNo natural text content detected\n\nOnly natural text fields shown, show all fields.\n\nQuery\n\nMax results\n\n0\n\n1000\n\n100\n\nUse highlights for clustering\n\nAdditional search request parameters\n\n#### Elasticsearch\n\nQueries Elasticsearch.\n\nElasticsearch service URL\n\nConnect\n\nElasticsearch collection to search\n\nCollection list is empty, no content to search.\n\nFields to cluster\n\nNo natural text content detected\n\nOnly natural text fields shown, show all fields.\n\nQuery\n\nMax results\n\n0\n\n1000\n\n100\n\n#### Clusters\n\nParameters affecting the number, structure and content of clusters.\n\nDesired cluster count\n\n2\n\n100\n\n30\n\nMinimum cluster size\n\n1\n\n100\n\n2\n\nCluster label assignment method\n\nSimpleLabelAssigner\n\nUniqueLabelAssigner\n\nExact phrase assignment\n\nCluster merging threshold\n\n0\n\n1\n\n0.70\n\nSize-score sorting ratio\n\n0\n\n1\n\n0\n\n#### Cluster labels\n\nCustomization of cluster labels.\n\nPhrase label boost\n\n0\n\n10\n\n1.5\n\nPhrase length penalty start\n\n2\n\n8\n\n8\n\nPhrase length penalty stop\n\n2\n\n8\n\n8\n\nTruncated label filter enabled\n\nTruncated label threshold\n\n0\n\n1\n\n0.65\n\nGenitive label filter enabled\n\nMinimum label length filter enabled\n\nMinimum label length\n\nNumeric label filter enabled\n\nQuery label filter enabled\n\nStop label filter enabled\n\nStop word label filter enabled\n\n#### Dictionaries\n\nLabel and word exclusion dictionaries.\n\nExcluded label patterns\n\nglob\n\nexact\n\nregexp\n\nCopy JSONCopy JSONCopy JSON\n\nOne pattern per line, separate words with spaces, `*` is zero or more words, syntax help\n\nStop words\n\nglob\n\nexact\n\nregexp\n\nCopy JSONCopy JSONCopy JSON\n\nOne pattern per line, separate words with spaces, `*` is zero or more words, syntax help\n\n#### Language model\n\nParameters of the document representation used by the clustering algorithm.\n\nLanguage\n\nTerm weighting for term-document matrix\n\nBoosted fields\n\nBoosted fields weight\n\n0\n\n10\n\n2.0\n\nPhrase document frequency threshold\n\n1\n\n100\n\n1\n\nWord document frequency threshold\n\n1\n\n100\n\n1\n\nMaximum word document frequency\n\n0\n\n1\n\n0.90\n\nTerm-document matrix factorization method\n\nFactorization quality\n\nFactorization quality\n\nFactorization quality\n\nFactorization quality\n\nMaximum term-document matrix size\n\n#### Clusters\n\nParameters affecting the number, structure and content of clusters.\n\nMaximum number of final clusters\n\nMaximum base clusters\n\nMinimum base cluster score\n\n0\n\n10\n\n2.0\n\nMinimum base cluster documents\n\n2\n\n20\n\n2\n\nDocument count boost\n\nMerge all stem-equivalent phrases when discovering base clusters\n\nBase cluster merge threshold\n\n0\n\n1\n\n0.60\n\nSize-score sorting ratio\n\n0\n\n1\n\n0\n\n#### Cluster labels\n\nCustomization of cluster labels.\n\nBoost single-term clusters\n\nOptimal cluster label length\n\nPhrase length tolerance\n\nMaximum words per label\n\nMaximum phrases per label\n\nMaximum cluster phrase overlap\n\n0\n\n1\n\n0.60\n\nMinimum general phrase coverage\n\n0\n\n1\n\n0.50\n\n#### Language model\n\nParameters of the document representation used by the clustering algorithm.\n\nLanguage\n\nMax relative word DF\n\n0\n\n1\n\n0.90\n\nWord document frequency threshold\n\n1\n\n100\n\n1\n\n#### Clusters\n\nParameters affecting the number, structure and content of clusters.\n\nCluster count\n\nMaximum iterations\n\nPartition count\n\n2\n\n10\n\n2\n\n#### Cluster labels\n\nCustomization of cluster labels.\n\nLabel count\n\n1\n\n10\n\n3\n\n#### Language model\n\nParameters of the document representation used by the clustering algorithm.\n\nLanguage\n\nTerm weighting for term-document matrix\n\nBoosted fields\n\nBoosted fields weight\n\n0\n\n10\n\n2.0\n\nMaximum word document frequency\n\n0\n\n1\n\n0.90\n\nWord document frequency threshold\n\n1\n\n100\n\n1\n\nUse dimensionality reduction\n\nTerm-document matrix factorization method\n\nFactorization quality\n\nFactorization quality\n\nFactorization quality\n\nFactorization quality\n\nMaximum term-document matrix size\n\nWelcome to Clustering Workbench\n-------------------------------\n\n### the expert-level Carrot2 application\n\n1.  ### Choose data source:\n    \n    *   Web search results\n    *   PubMed abstracts\n    *   Excel, CSV, OpenOffice, JSON or XML files\n    *   Apache Solr search results\n    *   Elasticsearch results\n2.  ### Configure **Web** data source\n    \n    Type your query in the **Query** box. Use the common web search engine syntax such as double quotes for `\"phrase search\"`,`-` to exclude words or phrases etc.\n3.  ### Press the **Cluster** button",
  "usage": {
    "tokens": 1159
  }
}
```
