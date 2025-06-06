---
title: GitHub - appbaseio/dejavu: A Web UI for Elasticsearch and OpenSearch: Import, browse and edit data with rich filters and query views, create reference search UIs.
description: A Web UI for Elasticsearch and OpenSearch: Import, browse and edit data with rich filters and query views, create reference search UIs. - appbaseio/dejavu
url: https://github.com/appbaseio/dejavu
timestamp: 2025-01-20T15:30:17.701Z
domain: github.com
path: appbaseio_dejavu
---

# GitHub - appbaseio/dejavu: A Web UI for Elasticsearch and OpenSearch: Import, browse and edit data with rich filters and query views, create reference search UIs.


A Web UI for Elasticsearch and OpenSearch: Import, browse and edit data with rich filters and query views, create reference search UIs. - appbaseio/dejavu


## Content

dejavu: The Web UI for OpenSearch and Elasticsearch
---------------------------------------------------

[](https://github.com/appbaseio/dejavu?screenshot=true#dejavu-the-web-ui-for-opensearch-and-elasticsearch)

[![Image 37: GitHub License](https://camo.githubusercontent.com/6581c31c16c1b13ddc2efb92e2ad69a93ddc4a92fd871ff15d401c4c6c9155a4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/LICENSE.md) [![Image 38: React Version](https://camo.githubusercontent.com/368893121734bd9a58113d7cc6e03712844a9f8a74ac917b611265856af1293f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656163742d7631362e362d627269676874677265656e2e737667)](https://camo.githubusercontent.com/368893121734bd9a58113d7cc6e03712844a9f8a74ac917b611265856af1293f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656163742d7631362e362d627269676874677265656e2e737667) [![Image 39: Docker Pulls](https://camo.githubusercontent.com/08b21611a9836683bfce90fe9b0d9dc550098f0d9bf52315b9127b951e23a9b1/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f61707062617365696f2f64656a6176752e737667)](https://hub.docker.com/r/appbaseio/dejavu/)

1.  **[Dejavu: Intro](https://github.com/appbaseio/dejavu?screenshot=true#1-dejavu-intro)**
2.  **[Features](https://github.com/appbaseio/dejavu?screenshot=true#2-features)**  
    a. [Easily Connect to Indices](https://github.com/appbaseio/dejavu?screenshot=true#easily-connect-and-remember-indices)  
    b. [Visual Filters](https://github.com/appbaseio/dejavu?screenshot=true#visual-filters)  
    c. [Modern UI Elements](https://github.com/appbaseio/dejavu?screenshot=true#modern-ui-elements)  
    d. [Import JSON or CSV Data](https://github.com/appbaseio/dejavu?screenshot=true#import-json-or-csv-data)  
    e. [Build search UIs](https://github.com/appbaseio/dejavu?screenshot=true#build-search-uis)
3.  **[Comparison](https://github.com/appbaseio/dejavu?screenshot=true#3-comparison-with-other-data-browsers)**
4.  **[Roadmap](https://github.com/appbaseio/dejavu?screenshot=true#4-roadmap)**
5.  **[Build Locally / Contributing](https://github.com/appbaseio/dejavu?screenshot=true#5-build-locally)**
6.  **[Get Dejavu](https://github.com/appbaseio/dejavu?screenshot=true#6-get-dejavu)**  
    a. [Docker Installation](https://github.com/appbaseio/dejavu?screenshot=true#docker-installation)  
    b. [Hosted Alternatives](https://github.com/appbaseio/dejavu?screenshot=true#hosted-alternatives)

* * *

### 1\. Dejavu Intro

[](https://github.com/appbaseio/dejavu?screenshot=true#1-dejavu-intro)

**Dejavu** is a modern web UI for OpenSearch and Elasticsearch.

It was designed with the goal of providing a seamless user experience, featuring no page reloads, infinite scroll, filtered views, real-time updates, and a search UI builder. With 100% client-side rendering, Dejavu can easily be run as a [hosted app on github pages](https://dejavu.reactivesearch.io/) or [as a docker image](https://hub.docker.com/r/appbaseio/dejavu/).

Starting `v1.0`, dejavu is the only Elasticsearch web UI that supports importing data via JSON and CSV files, as well as defining field mappings from the GUI.

Starting with `v1.5`, we support the ability of creating custom headers so you can easily pass different authentication headers, provide enhanced filtering and bulk updating of data via Elasticsearch's Query DSL.

Starting with `v2.0`, we support the ability to build faceted search UIs to test relevancy. You can also export the generated code to a codesandbox.

Starting with `v3.0`, we support the ability to connect to multiple indexes. You can also globally search across your indexes using global search bar.

### 2\. Features

[](https://github.com/appbaseio/dejavu?screenshot=true#2-features)

#### Easily Connect and Remember Indices

[](https://github.com/appbaseio/dejavu?screenshot=true#easily-connect-and-remember-indices)

[![Image 40: Connect to an Index](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f1.gif)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f1.gif)

Dejavu allows you to connect to any index present in your cluster and caches each connected index locally, making them easily accessible when browsing again.

#### Visual Filters

[](https://github.com/appbaseio/dejavu?screenshot=true#visual-filters)

[![Image 41: Filter Views](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f2.gif)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f2.gif)

Sort through data, find information visually, hide irrelevant data, and make sense of everything using the native data types. The global search bar allows you to perform text searches across your dataset.

Additionally, any filtered view can be exported as a JSON or CSV file.

#### Modern UI Elements

[](https://github.com/appbaseio/dejavu?screenshot=true#modern-ui-elements)

[![Image 42: Pagination](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f3.gif)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f3.gif)

It's not uncommon to have thousands of documents in your index. Dejavu supports a paginated view that also allows you to change the page size.

Dejavu also supports browsing data from multiple indexes and types, updating data either individually or via queries in bulk. Deletions are also supported.

#### Import JSON or CSV Data

[](https://github.com/appbaseio/dejavu?screenshot=true#import-json-or-csv-data)

[![Image 43: Import JSON or CSV files](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f4.gif)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f4.gif)

The importer view allows you to import CSV or JSON data directly into Elasticsearch through a guided data mapping configuration.

#### Build Search UIs

[](https://github.com/appbaseio/dejavu?screenshot=true#build-search-uis)

[![Image 44: Build search UIs](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f5.gif)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f5.gif)

With Search Preview, you can now build visual search UIs, test search relevancy, and export code to CodeSandbox.

* * *

### 3\. Comparison with other data browsers

[](https://github.com/appbaseio/dejavu?screenshot=true#3-comparison-with-other-data-browsers)

| Features | dejavu | [ES-head](https://github.com/mobz/elasticsearch-head) | [ES-kopf](https://github.com/lmenezes/elasticsearch-kopf) | [ES-browser](https://github.com/OlegKunitsyn/elasticsearch-browser) | [Kibana](https://github.com/elastic/kibana) |
| --- | --- | --- | --- | --- | --- |
| Installation | Docker image, Hosted app | Elasticsearch plugin, static page | Elasticsearch plugin, static page | Elasticsearch plugin (doesn't work with 2.0+) | Elasticsearch plugin |
| Modern UI | React 16.6. | jQuery 1.6.1, slightly stodgy | Angular 1.x | ExtJs, a bit stodgy | Node.JS, Hapi, Jade |
| Browser features | [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete), data filters | Read data, full-text search | ❌ | Data view for a single type | Read view, visualizations, charting |
| Data import/export | ✔️ JSON, CSV | ❌ | ❌ | ❌ | Only export, no CSV |
| Search preview | Visually build and test search UI | ❌ | ❌ | ❌ | ❌ |
| License | [MIT](https://github.com/appbaseio/dejavu/blob/dev/LICENSE.md) | [Apache 2.0](https://github.com/mobz/elasticsearch-head/blob/master/LICENCE) | [MIT](https://github.com/lmenezes/elasticsearch-kopf/blob/master/LICENSE) | [Apache 2.0](https://github.com/OlegKunitsyn/elasticsearch-browser/blob/master/LICENSE) | [Apache 2.0](https://github.com/elastic/kibana/blob/master/LICENSE.txt) |

* * *

### 4\. Roadmap

[](https://github.com/appbaseio/dejavu?screenshot=true#4-roadmap)

~Here's a rough roadmap of things to come in the version `1.0.0` release.~

🎆 We just hit the 1.0.0 roadmap:

*   Battle-testing with different datasets
*   Feature support for advanced filtering ~Offline detection and reconnection for realtime updates~
*   Performance improvements while scrolling
*   Support for importing and exporting data
*   Support for a continuous query view
*   Available as a docker image

🍾 We just hit the 2.0.0 release:

*   An intuitive data editing experience in tabular mode (v/s JSON edit mode)
*   View data types from within the data browser view
*   A more streamlined import process
*   Refactor codebase to improve hackability (Migrate to React 16+, ES6 syntax)
*   Ability to build (and test) search visually

✨ We just hit the 3.0.0 release:

*   Rewrite dejavu browser for high performance when browsing large datasets
*   Add support for browsing multiple indexes
*   Powerful filtering of data with field level facet based filters and a global search
*   Built on React 16.6 and future compatible with React 17
*   A more intuitive data editing experience (in addition to the raw JSON, we now show a relevant UI field with validations)

* * *

### 5\. Build Locally

[](https://github.com/appbaseio/dejavu?screenshot=true#5-build-locally)

See the **[contributing guidelines](https://github.com/appbaseio/dejavu/blob/dev/CONTRIBUTING.md)**.

* * *

### 6\. Get Dejavu

[](https://github.com/appbaseio/dejavu?screenshot=true#6-get-dejavu)

#### Docker Installation

[](https://github.com/appbaseio/dejavu?screenshot=true#docker-installation)

docker run -p 1358:1358 -d appbaseio/dejavu
open http://localhost:1358/

You can also run a specific version of **dejavu** by specifying a tag. For example, version `3.6.0` can be used by specifying the `docker run -p 1358:1358 appbaseio/dejavu:3.6.0` command.

##### Cross-origin resource sharing (CORS)

[](https://github.com/appbaseio/dejavu?screenshot=true#cross-origin-resource-sharing-cors)

To make sure you enable CORS settings for your Elasticsearch instance, add the following lines in the `elasticsearch.yml` configuration file.

http.port: 9200
http.cors.allow-origin: 'http://localhost:1358'
http.cors.enabled: true
http.cors.allow-headers: X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization
http.cors.allow-credentials: true

If you are running your Elasticsearch with docker-compose, you can refer to the example [reference here](https://github.com/appbaseio/dejavu/blob/dev/docker-compose.yml).

If you are running your Elasticsearch with docker, you can use the following flags to pass the custom CORS configuration:

###### OpenSearch 1.x

[](https://github.com/appbaseio/dejavu?screenshot=true#opensearch-1x)

docker run --name opensearch --rm -d -p 9200:9200 -e http.port=9200 -e discovery.type=single-node -e http.max\_content\_length=10MB -e http.cors.enabled=true -e http.cors.allow-origin=\\\* -e http.cors.allow-headers=X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization -e http.cors.allow-credentials=true -e plugins.security.disabled=true opensearchproject/opensearch:2.17.0

You can run both Opensearch and Dejavu together with:

`docker-compose up -d`

###### Elasticsearch 8.x

[](https://github.com/appbaseio/dejavu?screenshot=true#elasticsearch-8x)

docker run -d --rm --name elasticsearch -p 127.0.0.1:9200:9200 -e http.port=9200 -e discovery.type=single-node -e http.max\_content\_length=10MB -e http.cors.enabled=true -e http.cors.allow-origin=\\\* -e http.cors.allow-headers=X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization -e http.cors.allow-credentials=true -e network.publish\_host=localhost -e xpack.security.enabled=false docker.elastic.co/elasticsearch/elasticsearch:8.15.1

You can run both Elasticsearch 8.15.1 and Dejavu together with:

`docker-compose -f docker-compose-v8.yml up -d`

###### Elasticsearch 7.x

[](https://github.com/appbaseio/dejavu?screenshot=true#elasticsearch-7x)

docker run -d --rm --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "http.cors.enabled=true" -e "http.cors.allow-origin=\*" -e "http.cors.allow-headers=X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization" -e "http.cors.allow-credentials=true" docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2

You can run both Elasticsearch 7.10.2 and Dejavu together with:

`docker-compose -f docker-compose-v7.yml up -d`

#### Hosted Alternatives

[](https://github.com/appbaseio/dejavu?screenshot=true#hosted-alternatives)

**dejavu** can also be run as a hosted app at [https://dejavu.appbase.io](https://dejavu.appbase.io/).

* * *

## Metadata

```json
{
  "title": "GitHub - appbaseio/dejavu: A Web UI for Elasticsearch and OpenSearch: Import, browse and edit data with rich filters and query views, create reference search UIs.",
  "description": "A Web UI for Elasticsearch and OpenSearch: Import, browse and edit data with rich filters and query views, create reference search UIs. - appbaseio/dejavu",
  "url": "https://github.com/appbaseio/dejavu?screenshot=true",
  "content": "dejavu: The Web UI for OpenSearch and Elasticsearch\n---------------------------------------------------\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#dejavu-the-web-ui-for-opensearch-and-elasticsearch)\n\n[![Image 37: GitHub License](https://camo.githubusercontent.com/6581c31c16c1b13ddc2efb92e2ad69a93ddc4a92fd871ff15d401c4c6c9155a4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e737667)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/LICENSE.md) [![Image 38: React Version](https://camo.githubusercontent.com/368893121734bd9a58113d7cc6e03712844a9f8a74ac917b611265856af1293f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656163742d7631362e362d627269676874677265656e2e737667)](https://camo.githubusercontent.com/368893121734bd9a58113d7cc6e03712844a9f8a74ac917b611265856af1293f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656163742d7631362e362d627269676874677265656e2e737667) [![Image 39: Docker Pulls](https://camo.githubusercontent.com/08b21611a9836683bfce90fe9b0d9dc550098f0d9bf52315b9127b951e23a9b1/68747470733a2f2f696d672e736869656c64732e696f2f646f636b65722f70756c6c732f61707062617365696f2f64656a6176752e737667)](https://hub.docker.com/r/appbaseio/dejavu/)\n\n1.  **[Dejavu: Intro](https://github.com/appbaseio/dejavu?screenshot=true#1-dejavu-intro)**\n2.  **[Features](https://github.com/appbaseio/dejavu?screenshot=true#2-features)**  \n    a. [Easily Connect to Indices](https://github.com/appbaseio/dejavu?screenshot=true#easily-connect-and-remember-indices)  \n    b. [Visual Filters](https://github.com/appbaseio/dejavu?screenshot=true#visual-filters)  \n    c. [Modern UI Elements](https://github.com/appbaseio/dejavu?screenshot=true#modern-ui-elements)  \n    d. [Import JSON or CSV Data](https://github.com/appbaseio/dejavu?screenshot=true#import-json-or-csv-data)  \n    e. [Build search UIs](https://github.com/appbaseio/dejavu?screenshot=true#build-search-uis)\n3.  **[Comparison](https://github.com/appbaseio/dejavu?screenshot=true#3-comparison-with-other-data-browsers)**\n4.  **[Roadmap](https://github.com/appbaseio/dejavu?screenshot=true#4-roadmap)**\n5.  **[Build Locally / Contributing](https://github.com/appbaseio/dejavu?screenshot=true#5-build-locally)**\n6.  **[Get Dejavu](https://github.com/appbaseio/dejavu?screenshot=true#6-get-dejavu)**  \n    a. [Docker Installation](https://github.com/appbaseio/dejavu?screenshot=true#docker-installation)  \n    b. [Hosted Alternatives](https://github.com/appbaseio/dejavu?screenshot=true#hosted-alternatives)\n\n* * *\n\n### 1\\. Dejavu Intro\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#1-dejavu-intro)\n\n**Dejavu** is a modern web UI for OpenSearch and Elasticsearch.\n\nIt was designed with the goal of providing a seamless user experience, featuring no page reloads, infinite scroll, filtered views, real-time updates, and a search UI builder. With 100% client-side rendering, Dejavu can easily be run as a [hosted app on github pages](https://dejavu.reactivesearch.io/) or [as a docker image](https://hub.docker.com/r/appbaseio/dejavu/).\n\nStarting `v1.0`, dejavu is the only Elasticsearch web UI that supports importing data via JSON and CSV files, as well as defining field mappings from the GUI.\n\nStarting with `v1.5`, we support the ability of creating custom headers so you can easily pass different authentication headers, provide enhanced filtering and bulk updating of data via Elasticsearch's Query DSL.\n\nStarting with `v2.0`, we support the ability to build faceted search UIs to test relevancy. You can also export the generated code to a codesandbox.\n\nStarting with `v3.0`, we support the ability to connect to multiple indexes. You can also globally search across your indexes using global search bar.\n\n### 2\\. Features\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#2-features)\n\n#### Easily Connect and Remember Indices\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#easily-connect-and-remember-indices)\n\n[![Image 40: Connect to an Index](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f1.gif)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f1.gif)\n\nDejavu allows you to connect to any index present in your cluster and caches each connected index locally, making them easily accessible when browsing again.\n\n#### Visual Filters\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#visual-filters)\n\n[![Image 41: Filter Views](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f2.gif)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f2.gif)\n\nSort through data, find information visually, hide irrelevant data, and make sense of everything using the native data types. The global search bar allows you to perform text searches across your dataset.\n\nAdditionally, any filtered view can be exported as a JSON or CSV file.\n\n#### Modern UI Elements\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#modern-ui-elements)\n\n[![Image 42: Pagination](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f3.gif)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f3.gif)\n\nIt's not uncommon to have thousands of documents in your index. Dejavu supports a paginated view that also allows you to change the page size.\n\nDejavu also supports browsing data from multiple indexes and types, updating data either individually or via queries in bulk. Deletions are also supported.\n\n#### Import JSON or CSV Data\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#import-json-or-csv-data)\n\n[![Image 43: Import JSON or CSV files](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f4.gif)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f4.gif)\n\nThe importer view allows you to import CSV or JSON data directly into Elasticsearch through a guided data mapping configuration.\n\n#### Build Search UIs\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#build-search-uis)\n\n[![Image 44: Build search UIs](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f5.gif)](https://raw.githubusercontent.com/appbaseio/dejavu/dev/media/f5.gif)\n\nWith Search Preview, you can now build visual search UIs, test search relevancy, and export code to CodeSandbox.\n\n* * *\n\n### 3\\. Comparison with other data browsers\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#3-comparison-with-other-data-browsers)\n\n| Features | dejavu | [ES-head](https://github.com/mobz/elasticsearch-head) | [ES-kopf](https://github.com/lmenezes/elasticsearch-kopf) | [ES-browser](https://github.com/OlegKunitsyn/elasticsearch-browser) | [Kibana](https://github.com/elastic/kibana) |\n| --- | --- | --- | --- | --- | --- |\n| Installation | Docker image, Hosted app | Elasticsearch plugin, static page | Elasticsearch plugin, static page | Elasticsearch plugin (doesn't work with 2.0+) | Elasticsearch plugin |\n| Modern UI | React 16.6. | jQuery 1.6.1, slightly stodgy | Angular 1.x | ExtJs, a bit stodgy | Node.JS, Hapi, Jade |\n| Browser features | [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete), data filters | Read data, full-text search | ❌ | Data view for a single type | Read view, visualizations, charting |\n| Data import/export | ✔️ JSON, CSV | ❌ | ❌ | ❌ | Only export, no CSV |\n| Search preview | Visually build and test search UI | ❌ | ❌ | ❌ | ❌ |\n| License | [MIT](https://github.com/appbaseio/dejavu/blob/dev/LICENSE.md) | [Apache 2.0](https://github.com/mobz/elasticsearch-head/blob/master/LICENCE) | [MIT](https://github.com/lmenezes/elasticsearch-kopf/blob/master/LICENSE) | [Apache 2.0](https://github.com/OlegKunitsyn/elasticsearch-browser/blob/master/LICENSE) | [Apache 2.0](https://github.com/elastic/kibana/blob/master/LICENSE.txt) |\n\n* * *\n\n### 4\\. Roadmap\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#4-roadmap)\n\n~Here's a rough roadmap of things to come in the version `1.0.0` release.~\n\n🎆 We just hit the 1.0.0 roadmap:\n\n*   Battle-testing with different datasets\n*   Feature support for advanced filtering ~Offline detection and reconnection for realtime updates~\n*   Performance improvements while scrolling\n*   Support for importing and exporting data\n*   Support for a continuous query view\n*   Available as a docker image\n\n🍾 We just hit the 2.0.0 release:\n\n*   An intuitive data editing experience in tabular mode (v/s JSON edit mode)\n*   View data types from within the data browser view\n*   A more streamlined import process\n*   Refactor codebase to improve hackability (Migrate to React 16+, ES6 syntax)\n*   Ability to build (and test) search visually\n\n✨ We just hit the 3.0.0 release:\n\n*   Rewrite dejavu browser for high performance when browsing large datasets\n*   Add support for browsing multiple indexes\n*   Powerful filtering of data with field level facet based filters and a global search\n*   Built on React 16.6 and future compatible with React 17\n*   A more intuitive data editing experience (in addition to the raw JSON, we now show a relevant UI field with validations)\n\n* * *\n\n### 5\\. Build Locally\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#5-build-locally)\n\nSee the **[contributing guidelines](https://github.com/appbaseio/dejavu/blob/dev/CONTRIBUTING.md)**.\n\n* * *\n\n### 6\\. Get Dejavu\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#6-get-dejavu)\n\n#### Docker Installation\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#docker-installation)\n\ndocker run -p 1358:1358 -d appbaseio/dejavu\nopen http://localhost:1358/\n\nYou can also run a specific version of **dejavu** by specifying a tag. For example, version `3.6.0` can be used by specifying the `docker run -p 1358:1358 appbaseio/dejavu:3.6.0` command.\n\n##### Cross-origin resource sharing (CORS)\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#cross-origin-resource-sharing-cors)\n\nTo make sure you enable CORS settings for your Elasticsearch instance, add the following lines in the `elasticsearch.yml` configuration file.\n\nhttp.port: 9200\nhttp.cors.allow-origin: 'http://localhost:1358'\nhttp.cors.enabled: true\nhttp.cors.allow-headers: X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization\nhttp.cors.allow-credentials: true\n\nIf you are running your Elasticsearch with docker-compose, you can refer to the example [reference here](https://github.com/appbaseio/dejavu/blob/dev/docker-compose.yml).\n\nIf you are running your Elasticsearch with docker, you can use the following flags to pass the custom CORS configuration:\n\n###### OpenSearch 1.x\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#opensearch-1x)\n\ndocker run --name opensearch --rm -d -p 9200:9200 -e http.port=9200 -e discovery.type=single-node -e http.max\\_content\\_length=10MB -e http.cors.enabled=true -e http.cors.allow-origin=\\\\\\* -e http.cors.allow-headers=X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization -e http.cors.allow-credentials=true -e plugins.security.disabled=true opensearchproject/opensearch:2.17.0\n\nYou can run both Opensearch and Dejavu together with:\n\n`docker-compose up -d`\n\n###### Elasticsearch 8.x\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#elasticsearch-8x)\n\ndocker run -d --rm --name elasticsearch -p 127.0.0.1:9200:9200 -e http.port=9200 -e discovery.type=single-node -e http.max\\_content\\_length=10MB -e http.cors.enabled=true -e http.cors.allow-origin=\\\\\\* -e http.cors.allow-headers=X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization -e http.cors.allow-credentials=true -e network.publish\\_host=localhost -e xpack.security.enabled=false docker.elastic.co/elasticsearch/elasticsearch:8.15.1\n\nYou can run both Elasticsearch 8.15.1 and Dejavu together with:\n\n`docker-compose -f docker-compose-v8.yml up -d`\n\n###### Elasticsearch 7.x\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#elasticsearch-7x)\n\ndocker run -d --rm --name elasticsearch -p 9200:9200 -p 9300:9300 -e \"discovery.type=single-node\" -e \"http.cors.enabled=true\" -e \"http.cors.allow-origin=\\*\" -e \"http.cors.allow-headers=X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization\" -e \"http.cors.allow-credentials=true\" docker.elastic.co/elasticsearch/elasticsearch-oss:7.10.2\n\nYou can run both Elasticsearch 7.10.2 and Dejavu together with:\n\n`docker-compose -f docker-compose-v7.yml up -d`\n\n#### Hosted Alternatives\n\n[](https://github.com/appbaseio/dejavu?screenshot=true#hosted-alternatives)\n\n**dejavu** can also be run as a hosted app at [https://dejavu.appbase.io](https://dejavu.appbase.io/).\n\n* * *",
  "usage": {
    "tokens": 3432
  }
}
```
