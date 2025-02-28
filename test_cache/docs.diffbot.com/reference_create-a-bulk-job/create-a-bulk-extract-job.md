---
title: Create a Bulk Extract Job
description: Extract a list of URLs asynchronously
url: https://docs.diffbot.com/reference/create-a-bulk-job
timestamp: 2025-01-20T15:49:37.674Z
domain: docs.diffbot.com
path: reference_create-a-bulk-job
---

# Create a Bulk Extract Job


Extract a list of URLs asynchronously


## Content

Create a Bulk Extract Job
===============
                                                                                                              

[Jump to Content](https://docs.diffbot.com/reference/create-a-bulk-job#content)

[![Image 3: Diffbot Docs](https://files.readme.io/d48004d-Docs_Logo_-_Light_BG.svg)](https://docs.diffbot.com/)

[Guides](https://docs.diffbot.com/docs)[API Reference](https://docs.diffbot.com/reference)[Changelog](https://docs.diffbot.com/changelog)

* * *

[Log In](https://docs.diffbot.com/login?redirect_uri=/reference/create-a-bulk-job)[![Image 4: Diffbot Docs](https://files.readme.io/d48004d-Docs_Logo_-_Light_BG.svg)](https://docs.diffbot.com/)

API Reference

[Log In](https://docs.diffbot.com/login?redirect_uri=/reference/create-a-bulk-job)

[Guides](https://docs.diffbot.com/docs)[API Reference](https://docs.diffbot.com/reference)[Changelog](https://docs.diffbot.com/changelog)

Create a Bulk Extract Job

Search

JUMP TO

Getting Started
---------------

*   [Introduction to Diffbot APIs](https://docs.diffbot.com/reference/introduction-to-diffbot-apis)
*   [Authentication](https://docs.diffbot.com/reference/authentication)
    *   [Get Account Detailsget](https://docs.diffbot.com/reference/account)
*   [Rate Limits](https://docs.diffbot.com/reference/rate-limits)

DQL API
-------

*   [Introduction to Search (DQL API)](https://docs.diffbot.com/reference/introduction-to-search-dql)
*   [DQL Search](https://docs.diffbot.com/reference/dqlget)
    *   [Search with DQLget](https://docs.diffbot.com/reference/dqlget)
    *   [Search with DQLpost](https://docs.diffbot.com/reference/dqlpost)
    *   [Coverage report by Queryget](https://docs.diffbot.com/reference/reportfind)
    *   [Coverage report by IDget](https://docs.diffbot.com/reference/reportget)
*   [Filtering Fields](https://docs.diffbot.com/reference/filtering-fields)
*   [Exporting CSV](https://docs.diffbot.com/reference/exporting-csv)
*   [Coverage Reports](https://docs.diffbot.com/reference/dql-coverage-reports)
*   [Migrating from Legacy API](https://docs.diffbot.com/reference/migrating-from-legacy-api)
*   [/kg/dql/resolve-lost-id](https://docs.diffbot.com/reference/resolvelostid)
    *   [getget](https://docs.diffbot.com/reference/resolvelostid)

ENHANCE API
-----------

*   [Introduction to Enhance API](https://docs.diffbot.com/reference/introduction-to-enhance-api)
*   [Combine](https://docs.diffbot.com/reference/combine-1)
    *   [Combineget](https://docs.diffbot.com/reference/combine-1)
*   [Enhance](https://docs.diffbot.com/reference/enhanceget)
    *   [Enhanceget](https://docs.diffbot.com/reference/enhanceget)
    *   [Enhancepost](https://docs.diffbot.com/reference/enhancepost)
*   [Bulk Enhance](https://docs.diffbot.com/reference/bulk-enhance)
    *   [Create a Bulkjobpost](https://docs.diffbot.com/reference/submitbulkjob)
    *   [List Bulkjobs for Tokenget](https://docs.diffbot.com/reference/bulkjobstatusfortoken)
    *   [Poll bulkjob statusget](https://docs.diffbot.com/reference/bulkjobstatus)
    *   [Download Results of Bulkjobget](https://docs.diffbot.com/reference/bulkjobresultget)
    *   [Download Results of Bulkjobpost](https://docs.diffbot.com/reference/bulkjobresultpost)
    *   [Download Bulkjob Coverage Reportget](https://docs.diffbot.com/reference/coveragereportget-1)
    *   [Download Single Result of Bulkjobget](https://docs.diffbot.com/reference/singleresult)
    *   [Stop Bulkjobget](https://docs.diffbot.com/reference/stopbulkjob)

Natural Language API
--------------------

*   [Introduction to Natural Language API](https://docs.diffbot.com/reference/introduction-to-natural-language-api)
*   [Natural Language](https://docs.diffbot.com/reference/nl-post)
    *   [Process Textpost](https://docs.diffbot.com/reference/nl-post)
*   [List of Supported Languages (Sentiment, only)](https://docs.diffbot.com/reference/list-of-supported-languages-sentiment-only)

Extract APIs
------------

*   [Introduction to Extract API](https://docs.diffbot.com/reference/extract-introduction)
*   [Analyze](https://docs.diffbot.com/reference/extract-analyze)
    *   [Analyzeget](https://docs.diffbot.com/reference/extract-analyze)
*   [Article](https://docs.diffbot.com/reference/article)
    *   [Articleget](https://docs.diffbot.com/reference/article)
*   [Product](https://docs.diffbot.com/reference/product)
    *   [Productget](https://docs.diffbot.com/reference/product)
*   [Discussion](https://docs.diffbot.com/reference/discussion)
    *   [Discussionget](https://docs.diffbot.com/reference/discussion)
*   [Job](https://docs.diffbot.com/reference/job)
    *   [Jobget](https://docs.diffbot.com/reference/job)
*   [Image](https://docs.diffbot.com/reference/image)
    *   [Imageget](https://docs.diffbot.com/reference/image)
*   [Video](https://docs.diffbot.com/reference/video)
    *   [Videoget](https://docs.diffbot.com/reference/video)
*   [List](https://docs.diffbot.com/reference/list)
    *   [Listget](https://docs.diffbot.com/reference/list)
*   [Event](https://docs.diffbot.com/reference/event)
    *   [Eventget](https://docs.diffbot.com/reference/event)
*   [Optional Fields](https://docs.diffbot.com/reference/extract-optional-fields)
*   [Custom Javascript](https://docs.diffbot.com/reference/extract-custom-javascript)
*   [Custom Headers](https://docs.diffbot.com/reference/extract-custom-headers)
*   [Using Proxies](https://docs.diffbot.com/reference/using-proxies)
*   [Extract Content Not Available Online](https://docs.diffbot.com/reference/extract-content-not-available-online)
*   [Troubleshooting Extract API](https://docs.diffbot.com/reference/error-could-not-download-page)
    *   [Error 404: Could Not Download Page](https://docs.diffbot.com/reference/error-could-not-download-page)
    *   [Error 429: Site has received too many requests. Please try again later.](https://docs.diffbot.com/reference/error-429-too-many-requests)
    *   [Error 500: Unable to Apply Rules](https://docs.diffbot.com/reference/error-500-unable-to-apply-rules)
    *   [Error 500: Site has received too many requests.](https://docs.diffbot.com/reference/error-500-too-many-requests)
    *   [Automatic Page Concatenation Exceeded Timeout Error](https://docs.diffbot.com/reference/automatic-page-concatenation-exceeded-timeout-error)
    *   [Normalized HTML Fields for Article API](https://docs.diffbot.com/reference/normalized-html-fields)
    *   [Normalized Specifications for Product API](https://docs.diffbot.com/reference/normalized-product-specifications)
*   [Custom](https://docs.diffbot.com/reference/custom)
    *   [Extract with Custom APIget](https://docs.diffbot.com/reference/custom)
    *   [Retrieve Custom APIsget](https://docs.diffbot.com/reference/retrieve-a-custom-api)
    *   [Create or Update a Custom APIpost](https://docs.diffbot.com/reference/create-a-custom-api)
    *   [Custom API Rulesets](https://docs.diffbot.com/reference/custom-api-rulesets)
    *   [Custom API Selectors and Filters](https://docs.diffbot.com/reference/custom-api-selectors)
    *   [Custom API Collections](https://docs.diffbot.com/reference/custom-api-collections)
    *   [Delete a Custom APIdelete](https://docs.diffbot.com/reference/delete-a-custom-api)

Bulk API
--------

*   [Introduction to Bulk Extract API](https://docs.diffbot.com/reference/bulk-job-introduction)
*   [Create a Bulk Extract Jobpost](https://docs.diffbot.com/reference/create-a-bulk-job)
*   [Manage a Bulk Extract Jobget](https://docs.diffbot.com/reference/pause-delete-or-restart-a-bulk-job)
*   [Retrieve Bulk Extract Job Dataget](https://docs.diffbot.com/reference/retrieve-bulk-job-data)

Crawl
-----

*   [Introduction to Crawl API](https://docs.diffbot.com/reference/crawl-introduction)
*   [Create a Crawlpost](https://docs.diffbot.com/reference/create-a-crawl)
*   [Manage a Crawl Jobget](https://docs.diffbot.com/reference/manage-a-crawl-job)
*   [List All Crawl Jobs](https://docs.diffbot.com/reference/manage-a-crawl-job#view-the-status-of-crawl-jobs)
*   [Retrieve Crawl Job Dataget](https://docs.diffbot.com/reference/retrieve-crawl-job-data)

Search API
----------

*   [Search a Crawl/Bulk Jobget](https://docs.diffbot.com/reference/search)

Powered by [](https://readme.com/?ref_src=hub&project=diffbot-2)

JUMP TO

Getting Started
---------------

*   [Introduction to Diffbot APIs](https://docs.diffbot.com/reference/introduction-to-diffbot-apis)
*   [Authentication](https://docs.diffbot.com/reference/authentication)
    *   [Get Account Detailsget](https://docs.diffbot.com/reference/account)
*   [Rate Limits](https://docs.diffbot.com/reference/rate-limits)

DQL API
-------

*   [Introduction to Search (DQL API)](https://docs.diffbot.com/reference/introduction-to-search-dql)
*   [DQL Search](https://docs.diffbot.com/reference/dqlget)
    *   [Search with DQLget](https://docs.diffbot.com/reference/dqlget)
    *   [Search with DQLpost](https://docs.diffbot.com/reference/dqlpost)
    *   [Coverage report by Queryget](https://docs.diffbot.com/reference/reportfind)
    *   [Coverage report by IDget](https://docs.diffbot.com/reference/reportget)
*   [Filtering Fields](https://docs.diffbot.com/reference/filtering-fields)
*   [Exporting CSV](https://docs.diffbot.com/reference/exporting-csv)
*   [Coverage Reports](https://docs.diffbot.com/reference/dql-coverage-reports)
*   [Migrating from Legacy API](https://docs.diffbot.com/reference/migrating-from-legacy-api)
*   [/kg/dql/resolve-lost-id](https://docs.diffbot.com/reference/resolvelostid)
    *   [getget](https://docs.diffbot.com/reference/resolvelostid)

ENHANCE API
-----------

*   [Introduction to Enhance API](https://docs.diffbot.com/reference/introduction-to-enhance-api)
*   [Combine](https://docs.diffbot.com/reference/combine-1)
    *   [Combineget](https://docs.diffbot.com/reference/combine-1)
*   [Enhance](https://docs.diffbot.com/reference/enhanceget)
    *   [Enhanceget](https://docs.diffbot.com/reference/enhanceget)
    *   [Enhancepost](https://docs.diffbot.com/reference/enhancepost)
*   [Bulk Enhance](https://docs.diffbot.com/reference/bulk-enhance)
    *   [Create a Bulkjobpost](https://docs.diffbot.com/reference/submitbulkjob)
    *   [List Bulkjobs for Tokenget](https://docs.diffbot.com/reference/bulkjobstatusfortoken)
    *   [Poll bulkjob statusget](https://docs.diffbot.com/reference/bulkjobstatus)
    *   [Download Results of Bulkjobget](https://docs.diffbot.com/reference/bulkjobresultget)
    *   [Download Results of Bulkjobpost](https://docs.diffbot.com/reference/bulkjobresultpost)
    *   [Download Bulkjob Coverage Reportget](https://docs.diffbot.com/reference/coveragereportget-1)
    *   [Download Single Result of Bulkjobget](https://docs.diffbot.com/reference/singleresult)
    *   [Stop Bulkjobget](https://docs.diffbot.com/reference/stopbulkjob)

Natural Language API
--------------------

*   [Introduction to Natural Language API](https://docs.diffbot.com/reference/introduction-to-natural-language-api)
*   [Natural Language](https://docs.diffbot.com/reference/nl-post)
    *   [Process Textpost](https://docs.diffbot.com/reference/nl-post)
*   [List of Supported Languages (Sentiment, only)](https://docs.diffbot.com/reference/list-of-supported-languages-sentiment-only)

Extract APIs
------------

*   [Introduction to Extract API](https://docs.diffbot.com/reference/extract-introduction)
*   [Analyze](https://docs.diffbot.com/reference/extract-analyze)
    *   [Analyzeget](https://docs.diffbot.com/reference/extract-analyze)
*   [Article](https://docs.diffbot.com/reference/article)
    *   [Articleget](https://docs.diffbot.com/reference/article)
*   [Product](https://docs.diffbot.com/reference/product)
    *   [Productget](https://docs.diffbot.com/reference/product)
*   [Discussion](https://docs.diffbot.com/reference/discussion)
    *   [Discussionget](https://docs.diffbot.com/reference/discussion)
*   [Job](https://docs.diffbot.com/reference/job)
    *   [Jobget](https://docs.diffbot.com/reference/job)
*   [Image](https://docs.diffbot.com/reference/image)
    *   [Imageget](https://docs.diffbot.com/reference/image)
*   [Video](https://docs.diffbot.com/reference/video)
    *   [Videoget](https://docs.diffbot.com/reference/video)
*   [List](https://docs.diffbot.com/reference/list)
    *   [Listget](https://docs.diffbot.com/reference/list)
*   [Event](https://docs.diffbot.com/reference/event)
    *   [Eventget](https://docs.diffbot.com/reference/event)
*   [Optional Fields](https://docs.diffbot.com/reference/extract-optional-fields)
*   [Custom Javascript](https://docs.diffbot.com/reference/extract-custom-javascript)
*   [Custom Headers](https://docs.diffbot.com/reference/extract-custom-headers)
*   [Using Proxies](https://docs.diffbot.com/reference/using-proxies)
*   [Extract Content Not Available Online](https://docs.diffbot.com/reference/extract-content-not-available-online)
*   [Troubleshooting Extract API](https://docs.diffbot.com/reference/error-could-not-download-page)
    *   [Error 404: Could Not Download Page](https://docs.diffbot.com/reference/error-could-not-download-page)
    *   [Error 429: Site has received too many requests. Please try again later.](https://docs.diffbot.com/reference/error-429-too-many-requests)
    *   [Error 500: Unable to Apply Rules](https://docs.diffbot.com/reference/error-500-unable-to-apply-rules)
    *   [Error 500: Site has received too many requests.](https://docs.diffbot.com/reference/error-500-too-many-requests)
    *   [Automatic Page Concatenation Exceeded Timeout Error](https://docs.diffbot.com/reference/automatic-page-concatenation-exceeded-timeout-error)
    *   [Normalized HTML Fields for Article API](https://docs.diffbot.com/reference/normalized-html-fields)
    *   [Normalized Specifications for Product API](https://docs.diffbot.com/reference/normalized-product-specifications)
*   [Custom](https://docs.diffbot.com/reference/custom)
    *   [Extract with Custom APIget](https://docs.diffbot.com/reference/custom)
    *   [Retrieve Custom APIsget](https://docs.diffbot.com/reference/retrieve-a-custom-api)
    *   [Create or Update a Custom APIpost](https://docs.diffbot.com/reference/create-a-custom-api)
    *   [Custom API Rulesets](https://docs.diffbot.com/reference/custom-api-rulesets)
    *   [Custom API Selectors and Filters](https://docs.diffbot.com/reference/custom-api-selectors)
    *   [Custom API Collections](https://docs.diffbot.com/reference/custom-api-collections)
    *   [Delete a Custom APIdelete](https://docs.diffbot.com/reference/delete-a-custom-api)

Bulk API
--------

*   [Introduction to Bulk Extract API](https://docs.diffbot.com/reference/bulk-job-introduction)
*   [Create a Bulk Extract Jobpost](https://docs.diffbot.com/reference/create-a-bulk-job)
*   [Manage a Bulk Extract Jobget](https://docs.diffbot.com/reference/pause-delete-or-restart-a-bulk-job)
*   [Retrieve Bulk Extract Job Dataget](https://docs.diffbot.com/reference/retrieve-bulk-job-data)

Crawl
-----

*   [Introduction to Crawl API](https://docs.diffbot.com/reference/crawl-introduction)
*   [Create a Crawlpost](https://docs.diffbot.com/reference/create-a-crawl)
*   [Manage a Crawl Jobget](https://docs.diffbot.com/reference/manage-a-crawl-job)
*   [List All Crawl Jobs](https://docs.diffbot.com/reference/manage-a-crawl-job#view-the-status-of-crawl-jobs)
*   [Retrieve Crawl Job Dataget](https://docs.diffbot.com/reference/retrieve-crawl-job-data)

Search API
----------

*   [Search a Crawl/Bulk Jobget](https://docs.diffbot.com/reference/search)

Powered by [](https://readme.com/?ref_src=hub&project=diffbot-2)

Create a Bulk Extract Job
=========================

post https://api.diffbot.com/v3/bulk

Extract a list of URLs asynchronously

To create a bulk job, make a POST request to this endpoint.

Payload Setup

[](https://docs.diffbot.com/reference/create-a-bulk-job#payload-setup)
---------------------------------------------------------------------------------------

Set your `Content-Type` header to `application/x-www-form-urlencoded` (not multipart/form-data). Your POST body content should be in querystring format (key/value pairs), for example:

```
name=bulkTest&token=YOURDIFFBOTTOKEN&urls=https://www.diffbot.com https://blog.diffbot.com&apiUrl=https://api.diffbot.com/v3/analyze
```

Response

[](https://docs.diffbot.com/reference/create-a-bulk-job#response)
-----------------------------------------------------------------------------

Upon adding a new bulk job, you will receive a success message in the JSON response, in addition to full job details:

JSON

```
{
    "response": "Successfully added urls for spidering.",
    "jobs": [
        {
            "jobStatus": {
                "message": "Job is initializing.",
                "status": 0
            },
            "maxHops": -1,
            "downloadJson": "...json",
            "urlProcessPattern": "",
            "jobCompletionTimeUTC": 0,
            "maxRounds": -1,
            "type": "bulk",
            "pageCrawlSuccessesThisRound": 0,
            "urlCrawlRegEx": "",
            "pageProcessPattern": "",
            "apiUrl": "https://api.diffbot.com/v3/analyze",
            "useCanonical": 1,
            "jobCreationTimeUTC": 1649950325,
            "repeat": 0,
            "downloadUrls": "...csv",
            "obeyRobots": 1,
            "roundsCompleted": 0,
            "pageCrawlAttempts": 0,
            "notifyWebhook": "",
            "pageProcessSuccessesThisRound": 0,
            "customHeaders": {},
            "objectsFound": 0,
            "roundStartTime": 0,
            "urlCrawlPattern": "",
            "seedRecrawlFrequency": -1,
            "urlProcessRegEx": "",
            "pageProcessSuccesses": 0,
            "urlsHarvested": 0,
            "crawlDelay": -1,
            "currentTime": 1649950325,
            "useProxies": 0,
            "sentJobDoneNotification": 0,
            "currentTimeUTC": 1649950325,
            "name": "bulkTest",
            "notifyEmail": "",
            "pageCrawlSuccesses": 0,
            "pageProcessAttempts": 0
        }
    ]
}
```

Language

ShellNodeRubyPHPPython

RESPONSE

Click `Try It!` to start a request and see the response here!

## Metadata

```json
{
  "title": "Create a Bulk Extract Job",
  "description": "Extract a list of URLs asynchronously",
  "url": "https://docs.diffbot.com/reference/create-a-bulk-job",
  "content": "Create a Bulk Extract Job\n===============\n                                                                                                              \n\n[Jump to Content](https://docs.diffbot.com/reference/create-a-bulk-job#content)\n\n[![Image 3: Diffbot Docs](https://files.readme.io/d48004d-Docs_Logo_-_Light_BG.svg)](https://docs.diffbot.com/)\n\n[Guides](https://docs.diffbot.com/docs)[API Reference](https://docs.diffbot.com/reference)[Changelog](https://docs.diffbot.com/changelog)\n\n* * *\n\n[Log In](https://docs.diffbot.com/login?redirect_uri=/reference/create-a-bulk-job)[![Image 4: Diffbot Docs](https://files.readme.io/d48004d-Docs_Logo_-_Light_BG.svg)](https://docs.diffbot.com/)\n\nAPI Reference\n\n[Log In](https://docs.diffbot.com/login?redirect_uri=/reference/create-a-bulk-job)\n\n[Guides](https://docs.diffbot.com/docs)[API Reference](https://docs.diffbot.com/reference)[Changelog](https://docs.diffbot.com/changelog)\n\nCreate a Bulk Extract Job\n\nSearch\n\nJUMP TO\n\nGetting Started\n---------------\n\n*   [Introduction to Diffbot APIs](https://docs.diffbot.com/reference/introduction-to-diffbot-apis)\n*   [Authentication](https://docs.diffbot.com/reference/authentication)\n    *   [Get Account Detailsget](https://docs.diffbot.com/reference/account)\n*   [Rate Limits](https://docs.diffbot.com/reference/rate-limits)\n\nDQL API\n-------\n\n*   [Introduction to Search (DQL API)](https://docs.diffbot.com/reference/introduction-to-search-dql)\n*   [DQL Search](https://docs.diffbot.com/reference/dqlget)\n    *   [Search with DQLget](https://docs.diffbot.com/reference/dqlget)\n    *   [Search with DQLpost](https://docs.diffbot.com/reference/dqlpost)\n    *   [Coverage report by Queryget](https://docs.diffbot.com/reference/reportfind)\n    *   [Coverage report by IDget](https://docs.diffbot.com/reference/reportget)\n*   [Filtering Fields](https://docs.diffbot.com/reference/filtering-fields)\n*   [Exporting CSV](https://docs.diffbot.com/reference/exporting-csv)\n*   [Coverage Reports](https://docs.diffbot.com/reference/dql-coverage-reports)\n*   [Migrating from Legacy API](https://docs.diffbot.com/reference/migrating-from-legacy-api)\n*   [/kg/dql/resolve-lost-id](https://docs.diffbot.com/reference/resolvelostid)\n    *   [getget](https://docs.diffbot.com/reference/resolvelostid)\n\nENHANCE API\n-----------\n\n*   [Introduction to Enhance API](https://docs.diffbot.com/reference/introduction-to-enhance-api)\n*   [Combine](https://docs.diffbot.com/reference/combine-1)\n    *   [Combineget](https://docs.diffbot.com/reference/combine-1)\n*   [Enhance](https://docs.diffbot.com/reference/enhanceget)\n    *   [Enhanceget](https://docs.diffbot.com/reference/enhanceget)\n    *   [Enhancepost](https://docs.diffbot.com/reference/enhancepost)\n*   [Bulk Enhance](https://docs.diffbot.com/reference/bulk-enhance)\n    *   [Create a Bulkjobpost](https://docs.diffbot.com/reference/submitbulkjob)\n    *   [List Bulkjobs for Tokenget](https://docs.diffbot.com/reference/bulkjobstatusfortoken)\n    *   [Poll bulkjob statusget](https://docs.diffbot.com/reference/bulkjobstatus)\n    *   [Download Results of Bulkjobget](https://docs.diffbot.com/reference/bulkjobresultget)\n    *   [Download Results of Bulkjobpost](https://docs.diffbot.com/reference/bulkjobresultpost)\n    *   [Download Bulkjob Coverage Reportget](https://docs.diffbot.com/reference/coveragereportget-1)\n    *   [Download Single Result of Bulkjobget](https://docs.diffbot.com/reference/singleresult)\n    *   [Stop Bulkjobget](https://docs.diffbot.com/reference/stopbulkjob)\n\nNatural Language API\n--------------------\n\n*   [Introduction to Natural Language API](https://docs.diffbot.com/reference/introduction-to-natural-language-api)\n*   [Natural Language](https://docs.diffbot.com/reference/nl-post)\n    *   [Process Textpost](https://docs.diffbot.com/reference/nl-post)\n*   [List of Supported Languages (Sentiment, only)](https://docs.diffbot.com/reference/list-of-supported-languages-sentiment-only)\n\nExtract APIs\n------------\n\n*   [Introduction to Extract API](https://docs.diffbot.com/reference/extract-introduction)\n*   [Analyze](https://docs.diffbot.com/reference/extract-analyze)\n    *   [Analyzeget](https://docs.diffbot.com/reference/extract-analyze)\n*   [Article](https://docs.diffbot.com/reference/article)\n    *   [Articleget](https://docs.diffbot.com/reference/article)\n*   [Product](https://docs.diffbot.com/reference/product)\n    *   [Productget](https://docs.diffbot.com/reference/product)\n*   [Discussion](https://docs.diffbot.com/reference/discussion)\n    *   [Discussionget](https://docs.diffbot.com/reference/discussion)\n*   [Job](https://docs.diffbot.com/reference/job)\n    *   [Jobget](https://docs.diffbot.com/reference/job)\n*   [Image](https://docs.diffbot.com/reference/image)\n    *   [Imageget](https://docs.diffbot.com/reference/image)\n*   [Video](https://docs.diffbot.com/reference/video)\n    *   [Videoget](https://docs.diffbot.com/reference/video)\n*   [List](https://docs.diffbot.com/reference/list)\n    *   [Listget](https://docs.diffbot.com/reference/list)\n*   [Event](https://docs.diffbot.com/reference/event)\n    *   [Eventget](https://docs.diffbot.com/reference/event)\n*   [Optional Fields](https://docs.diffbot.com/reference/extract-optional-fields)\n*   [Custom Javascript](https://docs.diffbot.com/reference/extract-custom-javascript)\n*   [Custom Headers](https://docs.diffbot.com/reference/extract-custom-headers)\n*   [Using Proxies](https://docs.diffbot.com/reference/using-proxies)\n*   [Extract Content Not Available Online](https://docs.diffbot.com/reference/extract-content-not-available-online)\n*   [Troubleshooting Extract API](https://docs.diffbot.com/reference/error-could-not-download-page)\n    *   [Error 404: Could Not Download Page](https://docs.diffbot.com/reference/error-could-not-download-page)\n    *   [Error 429: Site has received too many requests. Please try again later.](https://docs.diffbot.com/reference/error-429-too-many-requests)\n    *   [Error 500: Unable to Apply Rules](https://docs.diffbot.com/reference/error-500-unable-to-apply-rules)\n    *   [Error 500: Site has received too many requests.](https://docs.diffbot.com/reference/error-500-too-many-requests)\n    *   [Automatic Page Concatenation Exceeded Timeout Error](https://docs.diffbot.com/reference/automatic-page-concatenation-exceeded-timeout-error)\n    *   [Normalized HTML Fields for Article API](https://docs.diffbot.com/reference/normalized-html-fields)\n    *   [Normalized Specifications for Product API](https://docs.diffbot.com/reference/normalized-product-specifications)\n*   [Custom](https://docs.diffbot.com/reference/custom)\n    *   [Extract with Custom APIget](https://docs.diffbot.com/reference/custom)\n    *   [Retrieve Custom APIsget](https://docs.diffbot.com/reference/retrieve-a-custom-api)\n    *   [Create or Update a Custom APIpost](https://docs.diffbot.com/reference/create-a-custom-api)\n    *   [Custom API Rulesets](https://docs.diffbot.com/reference/custom-api-rulesets)\n    *   [Custom API Selectors and Filters](https://docs.diffbot.com/reference/custom-api-selectors)\n    *   [Custom API Collections](https://docs.diffbot.com/reference/custom-api-collections)\n    *   [Delete a Custom APIdelete](https://docs.diffbot.com/reference/delete-a-custom-api)\n\nBulk API\n--------\n\n*   [Introduction to Bulk Extract API](https://docs.diffbot.com/reference/bulk-job-introduction)\n*   [Create a Bulk Extract Jobpost](https://docs.diffbot.com/reference/create-a-bulk-job)\n*   [Manage a Bulk Extract Jobget](https://docs.diffbot.com/reference/pause-delete-or-restart-a-bulk-job)\n*   [Retrieve Bulk Extract Job Dataget](https://docs.diffbot.com/reference/retrieve-bulk-job-data)\n\nCrawl\n-----\n\n*   [Introduction to Crawl API](https://docs.diffbot.com/reference/crawl-introduction)\n*   [Create a Crawlpost](https://docs.diffbot.com/reference/create-a-crawl)\n*   [Manage a Crawl Jobget](https://docs.diffbot.com/reference/manage-a-crawl-job)\n*   [List All Crawl Jobs](https://docs.diffbot.com/reference/manage-a-crawl-job#view-the-status-of-crawl-jobs)\n*   [Retrieve Crawl Job Dataget](https://docs.diffbot.com/reference/retrieve-crawl-job-data)\n\nSearch API\n----------\n\n*   [Search a Crawl/Bulk Jobget](https://docs.diffbot.com/reference/search)\n\nPowered by [](https://readme.com/?ref_src=hub&project=diffbot-2)\n\nJUMP TO\n\nGetting Started\n---------------\n\n*   [Introduction to Diffbot APIs](https://docs.diffbot.com/reference/introduction-to-diffbot-apis)\n*   [Authentication](https://docs.diffbot.com/reference/authentication)\n    *   [Get Account Detailsget](https://docs.diffbot.com/reference/account)\n*   [Rate Limits](https://docs.diffbot.com/reference/rate-limits)\n\nDQL API\n-------\n\n*   [Introduction to Search (DQL API)](https://docs.diffbot.com/reference/introduction-to-search-dql)\n*   [DQL Search](https://docs.diffbot.com/reference/dqlget)\n    *   [Search with DQLget](https://docs.diffbot.com/reference/dqlget)\n    *   [Search with DQLpost](https://docs.diffbot.com/reference/dqlpost)\n    *   [Coverage report by Queryget](https://docs.diffbot.com/reference/reportfind)\n    *   [Coverage report by IDget](https://docs.diffbot.com/reference/reportget)\n*   [Filtering Fields](https://docs.diffbot.com/reference/filtering-fields)\n*   [Exporting CSV](https://docs.diffbot.com/reference/exporting-csv)\n*   [Coverage Reports](https://docs.diffbot.com/reference/dql-coverage-reports)\n*   [Migrating from Legacy API](https://docs.diffbot.com/reference/migrating-from-legacy-api)\n*   [/kg/dql/resolve-lost-id](https://docs.diffbot.com/reference/resolvelostid)\n    *   [getget](https://docs.diffbot.com/reference/resolvelostid)\n\nENHANCE API\n-----------\n\n*   [Introduction to Enhance API](https://docs.diffbot.com/reference/introduction-to-enhance-api)\n*   [Combine](https://docs.diffbot.com/reference/combine-1)\n    *   [Combineget](https://docs.diffbot.com/reference/combine-1)\n*   [Enhance](https://docs.diffbot.com/reference/enhanceget)\n    *   [Enhanceget](https://docs.diffbot.com/reference/enhanceget)\n    *   [Enhancepost](https://docs.diffbot.com/reference/enhancepost)\n*   [Bulk Enhance](https://docs.diffbot.com/reference/bulk-enhance)\n    *   [Create a Bulkjobpost](https://docs.diffbot.com/reference/submitbulkjob)\n    *   [List Bulkjobs for Tokenget](https://docs.diffbot.com/reference/bulkjobstatusfortoken)\n    *   [Poll bulkjob statusget](https://docs.diffbot.com/reference/bulkjobstatus)\n    *   [Download Results of Bulkjobget](https://docs.diffbot.com/reference/bulkjobresultget)\n    *   [Download Results of Bulkjobpost](https://docs.diffbot.com/reference/bulkjobresultpost)\n    *   [Download Bulkjob Coverage Reportget](https://docs.diffbot.com/reference/coveragereportget-1)\n    *   [Download Single Result of Bulkjobget](https://docs.diffbot.com/reference/singleresult)\n    *   [Stop Bulkjobget](https://docs.diffbot.com/reference/stopbulkjob)\n\nNatural Language API\n--------------------\n\n*   [Introduction to Natural Language API](https://docs.diffbot.com/reference/introduction-to-natural-language-api)\n*   [Natural Language](https://docs.diffbot.com/reference/nl-post)\n    *   [Process Textpost](https://docs.diffbot.com/reference/nl-post)\n*   [List of Supported Languages (Sentiment, only)](https://docs.diffbot.com/reference/list-of-supported-languages-sentiment-only)\n\nExtract APIs\n------------\n\n*   [Introduction to Extract API](https://docs.diffbot.com/reference/extract-introduction)\n*   [Analyze](https://docs.diffbot.com/reference/extract-analyze)\n    *   [Analyzeget](https://docs.diffbot.com/reference/extract-analyze)\n*   [Article](https://docs.diffbot.com/reference/article)\n    *   [Articleget](https://docs.diffbot.com/reference/article)\n*   [Product](https://docs.diffbot.com/reference/product)\n    *   [Productget](https://docs.diffbot.com/reference/product)\n*   [Discussion](https://docs.diffbot.com/reference/discussion)\n    *   [Discussionget](https://docs.diffbot.com/reference/discussion)\n*   [Job](https://docs.diffbot.com/reference/job)\n    *   [Jobget](https://docs.diffbot.com/reference/job)\n*   [Image](https://docs.diffbot.com/reference/image)\n    *   [Imageget](https://docs.diffbot.com/reference/image)\n*   [Video](https://docs.diffbot.com/reference/video)\n    *   [Videoget](https://docs.diffbot.com/reference/video)\n*   [List](https://docs.diffbot.com/reference/list)\n    *   [Listget](https://docs.diffbot.com/reference/list)\n*   [Event](https://docs.diffbot.com/reference/event)\n    *   [Eventget](https://docs.diffbot.com/reference/event)\n*   [Optional Fields](https://docs.diffbot.com/reference/extract-optional-fields)\n*   [Custom Javascript](https://docs.diffbot.com/reference/extract-custom-javascript)\n*   [Custom Headers](https://docs.diffbot.com/reference/extract-custom-headers)\n*   [Using Proxies](https://docs.diffbot.com/reference/using-proxies)\n*   [Extract Content Not Available Online](https://docs.diffbot.com/reference/extract-content-not-available-online)\n*   [Troubleshooting Extract API](https://docs.diffbot.com/reference/error-could-not-download-page)\n    *   [Error 404: Could Not Download Page](https://docs.diffbot.com/reference/error-could-not-download-page)\n    *   [Error 429: Site has received too many requests. Please try again later.](https://docs.diffbot.com/reference/error-429-too-many-requests)\n    *   [Error 500: Unable to Apply Rules](https://docs.diffbot.com/reference/error-500-unable-to-apply-rules)\n    *   [Error 500: Site has received too many requests.](https://docs.diffbot.com/reference/error-500-too-many-requests)\n    *   [Automatic Page Concatenation Exceeded Timeout Error](https://docs.diffbot.com/reference/automatic-page-concatenation-exceeded-timeout-error)\n    *   [Normalized HTML Fields for Article API](https://docs.diffbot.com/reference/normalized-html-fields)\n    *   [Normalized Specifications for Product API](https://docs.diffbot.com/reference/normalized-product-specifications)\n*   [Custom](https://docs.diffbot.com/reference/custom)\n    *   [Extract with Custom APIget](https://docs.diffbot.com/reference/custom)\n    *   [Retrieve Custom APIsget](https://docs.diffbot.com/reference/retrieve-a-custom-api)\n    *   [Create or Update a Custom APIpost](https://docs.diffbot.com/reference/create-a-custom-api)\n    *   [Custom API Rulesets](https://docs.diffbot.com/reference/custom-api-rulesets)\n    *   [Custom API Selectors and Filters](https://docs.diffbot.com/reference/custom-api-selectors)\n    *   [Custom API Collections](https://docs.diffbot.com/reference/custom-api-collections)\n    *   [Delete a Custom APIdelete](https://docs.diffbot.com/reference/delete-a-custom-api)\n\nBulk API\n--------\n\n*   [Introduction to Bulk Extract API](https://docs.diffbot.com/reference/bulk-job-introduction)\n*   [Create a Bulk Extract Jobpost](https://docs.diffbot.com/reference/create-a-bulk-job)\n*   [Manage a Bulk Extract Jobget](https://docs.diffbot.com/reference/pause-delete-or-restart-a-bulk-job)\n*   [Retrieve Bulk Extract Job Dataget](https://docs.diffbot.com/reference/retrieve-bulk-job-data)\n\nCrawl\n-----\n\n*   [Introduction to Crawl API](https://docs.diffbot.com/reference/crawl-introduction)\n*   [Create a Crawlpost](https://docs.diffbot.com/reference/create-a-crawl)\n*   [Manage a Crawl Jobget](https://docs.diffbot.com/reference/manage-a-crawl-job)\n*   [List All Crawl Jobs](https://docs.diffbot.com/reference/manage-a-crawl-job#view-the-status-of-crawl-jobs)\n*   [Retrieve Crawl Job Dataget](https://docs.diffbot.com/reference/retrieve-crawl-job-data)\n\nSearch API\n----------\n\n*   [Search a Crawl/Bulk Jobget](https://docs.diffbot.com/reference/search)\n\nPowered by [](https://readme.com/?ref_src=hub&project=diffbot-2)\n\nCreate a Bulk Extract Job\n=========================\n\npost https://api.diffbot.com/v3/bulk\n\nExtract a list of URLs asynchronously\n\nTo create a bulk job, make a POST request to this endpoint.\n\nPayload Setup\n\n[](https://docs.diffbot.com/reference/create-a-bulk-job#payload-setup)\n---------------------------------------------------------------------------------------\n\nSet your `Content-Type` header to `application/x-www-form-urlencoded` (not multipart/form-data). Your POST body content should be in querystring format (key/value pairs), for example:\n\n```\nname=bulkTest&token=YOURDIFFBOTTOKEN&urls=https://www.diffbot.com https://blog.diffbot.com&apiUrl=https://api.diffbot.com/v3/analyze\n```\n\nResponse\n\n[](https://docs.diffbot.com/reference/create-a-bulk-job#response)\n-----------------------------------------------------------------------------\n\nUpon adding a new bulk job, you will receive a success message in the JSON response, in addition to full job details:\n\nJSON\n\n```\n{\n    \"response\": \"Successfully added urls for spidering.\",\n    \"jobs\": [\n        {\n            \"jobStatus\": {\n                \"message\": \"Job is initializing.\",\n                \"status\": 0\n            },\n            \"maxHops\": -1,\n            \"downloadJson\": \"...json\",\n            \"urlProcessPattern\": \"\",\n            \"jobCompletionTimeUTC\": 0,\n            \"maxRounds\": -1,\n            \"type\": \"bulk\",\n            \"pageCrawlSuccessesThisRound\": 0,\n            \"urlCrawlRegEx\": \"\",\n            \"pageProcessPattern\": \"\",\n            \"apiUrl\": \"https://api.diffbot.com/v3/analyze\",\n            \"useCanonical\": 1,\n            \"jobCreationTimeUTC\": 1649950325,\n            \"repeat\": 0,\n            \"downloadUrls\": \"...csv\",\n            \"obeyRobots\": 1,\n            \"roundsCompleted\": 0,\n            \"pageCrawlAttempts\": 0,\n            \"notifyWebhook\": \"\",\n            \"pageProcessSuccessesThisRound\": 0,\n            \"customHeaders\": {},\n            \"objectsFound\": 0,\n            \"roundStartTime\": 0,\n            \"urlCrawlPattern\": \"\",\n            \"seedRecrawlFrequency\": -1,\n            \"urlProcessRegEx\": \"\",\n            \"pageProcessSuccesses\": 0,\n            \"urlsHarvested\": 0,\n            \"crawlDelay\": -1,\n            \"currentTime\": 1649950325,\n            \"useProxies\": 0,\n            \"sentJobDoneNotification\": 0,\n            \"currentTimeUTC\": 1649950325,\n            \"name\": \"bulkTest\",\n            \"notifyEmail\": \"\",\n            \"pageCrawlSuccesses\": 0,\n            \"pageProcessAttempts\": 0\n        }\n    ]\n}\n```\n\nLanguage\n\nShellNodeRubyPHPPython\n\nRESPONSE\n\nClick `Try It!` to start a request and see the response here!",
  "usage": {
    "tokens": 4520
  }
}
```
