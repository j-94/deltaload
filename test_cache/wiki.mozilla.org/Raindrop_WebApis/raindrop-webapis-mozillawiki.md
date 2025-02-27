---
title: Raindrop/WebApis - MozillaWiki
description: 
url: https://wiki.mozilla.org/Raindrop/WebApis
timestamp: 2025-01-20T15:56:11.450Z
domain: wiki.mozilla.org
path: Raindrop_WebApis
---

# Raindrop/WebApis - MozillaWiki



## Content

[Raindrop](https://wiki.mozilla.org/Raindrop "Raindrop")

This outlines the current state of the Raindrop Web APIs. We welcome all contributions and input into what we have described here.

High level goals
----------------

There are lots of reasons to have web based APIs to a messaging system like Raindrop. Here are some of them. Note that some are platform requirements, some are more product/application specific. We may need multiple APIs to support the different goals:

### Modularity

Having well defined APIs allows modularity between the various tiers of the system, from the message aggregation and back-end extension engine (currently CouchDB-based), to the conversation-aggregation layer, to the front-end UI code (in the client). Having APIs allow us to be resilient to changes in CouchDB, to considering alternatives in any of the tiers, etc. It's just good software engineering.

### Lighter weight clients

The current APIs allow for alot of work, both in terms of processing power, and in terms of HTTP connections to the database, to be off-loaded from the client. This means we are better able to support clients on less capable platforms (e.g. phones), and in some installations we should be able to deploy web server technologies like caching layers to improve performance further.

### Support and develop open standards

We want to help define open standards around messaging. We want to use current best practices in our domain - of which the only real contender is a REST based API accessed over HTTP. The API must allow for high-bandwidth low-latency applications.

### Simplicity

The API should deal in the same concepts as the application rather than the details of the implementation; for example, messaging applications want to work with message related objects, not with database documents. The API should be simple enough to allow designers to easily experiment with concepts without needing them to understand all the technical details of the platform.

On simplicity...
----------------

While many of the above goals are self-explanatory, there are a number of aspects relating to the simplicity of the API that deserve further discussion.

#### Up in the sky, is it an application, is it a platform? No, it's a raindrop!

What exactly is a 'raindrop application'? The inflow application we ship with raindrop is intended to be just one of many possible raindrop applications. We expect people will innovate with their own applications, and while these are likely to be vaguely 'message based', they may deal with concepts and metaphors which are foreign to our inflow application.

This implies that we need a sense of layering in the API itself, so each application can provide an application specific API built around some lower-level constructs provided by the platform. In other words, this API itself needs to be hugely extensible and is based around a similar 'extension' model that raindrop itself uses. This means third parties can easily and simply add extensions to raindrop which add further attributes to contacts or messages.

The API is be implemented by way of couchdb [externals processes](http://wiki.apache.org/couchdb/ExternalProcesses). Raindrop provides an "api-runner" which knows how to load API implementations from the database and expose them.

One consequence of the above discussions is that each application is likely to require its own application specific API. As a result, each application defines and documents its own API.

Implemented APIs
----------------

*   The [inflow](https://wiki.mozilla.org/Raindrop/WebApis/inflow "Raindrop/WebApis/inflow") api
*   The [document model](https://wiki.mozilla.org/Raindrop/WebApis/model "Raindrop/WebApis/model") api

Missing APIs
------------

A list of the [apis](https://wiki.mozilla.org/Raindrop/WebApis/missing "Raindrop/WebApis/missing") we probably need to clarify/document/write

## Metadata

```json
{
  "title": "Raindrop/WebApis - MozillaWiki",
  "description": "",
  "url": "https://wiki.mozilla.org/Raindrop/WebApis",
  "content": "[Raindrop](https://wiki.mozilla.org/Raindrop \"Raindrop\")\n\nThis outlines the current state of the Raindrop Web APIs. We welcome all contributions and input into what we have described here.\n\nHigh level goals\n----------------\n\nThere are lots of reasons to have web based APIs to a messaging system like Raindrop. Here are some of them. Note that some are platform requirements, some are more product/application specific. We may need multiple APIs to support the different goals:\n\n### Modularity\n\nHaving well defined APIs allows modularity between the various tiers of the system, from the message aggregation and back-end extension engine (currently CouchDB-based), to the conversation-aggregation layer, to the front-end UI code (in the client). Having APIs allow us to be resilient to changes in CouchDB, to considering alternatives in any of the tiers, etc. It's just good software engineering.\n\n### Lighter weight clients\n\nThe current APIs allow for alot of work, both in terms of processing power, and in terms of HTTP connections to the database, to be off-loaded from the client. This means we are better able to support clients on less capable platforms (e.g. phones), and in some installations we should be able to deploy web server technologies like caching layers to improve performance further.\n\n### Support and develop open standards\n\nWe want to help define open standards around messaging. We want to use current best practices in our domain - of which the only real contender is a REST based API accessed over HTTP. The API must allow for high-bandwidth low-latency applications.\n\n### Simplicity\n\nThe API should deal in the same concepts as the application rather than the details of the implementation; for example, messaging applications want to work with message related objects, not with database documents. The API should be simple enough to allow designers to easily experiment with concepts without needing them to understand all the technical details of the platform.\n\nOn simplicity...\n----------------\n\nWhile many of the above goals are self-explanatory, there are a number of aspects relating to the simplicity of the API that deserve further discussion.\n\n#### Up in the sky, is it an application, is it a platform? No, it's a raindrop!\n\nWhat exactly is a 'raindrop application'? The inflow application we ship with raindrop is intended to be just one of many possible raindrop applications. We expect people will innovate with their own applications, and while these are likely to be vaguely 'message based', they may deal with concepts and metaphors which are foreign to our inflow application.\n\nThis implies that we need a sense of layering in the API itself, so each application can provide an application specific API built around some lower-level constructs provided by the platform. In other words, this API itself needs to be hugely extensible and is based around a similar 'extension' model that raindrop itself uses. This means third parties can easily and simply add extensions to raindrop which add further attributes to contacts or messages.\n\nThe API is be implemented by way of couchdb [externals processes](http://wiki.apache.org/couchdb/ExternalProcesses). Raindrop provides an \"api-runner\" which knows how to load API implementations from the database and expose them.\n\nOne consequence of the above discussions is that each application is likely to require its own application specific API. As a result, each application defines and documents its own API.\n\nImplemented APIs\n----------------\n\n*   The [inflow](https://wiki.mozilla.org/Raindrop/WebApis/inflow \"Raindrop/WebApis/inflow\") api\n*   The [document model](https://wiki.mozilla.org/Raindrop/WebApis/model \"Raindrop/WebApis/model\") api\n\nMissing APIs\n------------\n\nA list of the [apis](https://wiki.mozilla.org/Raindrop/WebApis/missing \"Raindrop/WebApis/missing\") we probably need to clarify/document/write",
  "usage": {
    "tokens": 781
  }
}
```
