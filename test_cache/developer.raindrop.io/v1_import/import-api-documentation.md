---
title: Import | API Documentation
description: Handy methods to implement import functionality
url: https://developer.raindrop.io/v1/import
timestamp: 2025-01-20T16:02:59.417Z
domain: developer.raindrop.io
path: v1_import
---

# Import | API Documentation


Handy methods to implement import functionality


## Content

1.  [Rest API v1](https://developer.raindrop.io/v1)

Import
------

Handy methods to implement import functionality

`GET` `https://api.raindrop.io/rest/v1/import/url/parse`

Parse and extract useful info from any URL

```
//Success
{
  "item": {
    "title": "Яндекс",
    "excerpt": "Найдётся всё",
    "media": [
      {
        "type": "image",
        "link": "http://yastatic.net/s3/home/logos/share/share-logo_ru.png"
      }
    ],
    "type": "link",
    "meta": {
      "possibleArticle": false,
      "canonical": "https://ya.ru",
      "site": "Яндекс",
      "tags": []
    }
  },
  "result": true
}

//Invalid URL
{
  "error": "not_found",
  "errorMessage": "invalid_url",
  "item": {
    "title": "Fdfdfdf",
    "excerpt": "",
    "media": [
      {
        "link": "<screenshot>"
      }
    ],
    "type": "link",
    "parser": "local",
    "meta": {
      "possibleArticle": false,
      "tags": []
    }
  },
  "result": true
}

//Not found
{
  "error": "not_found",
  "errorMessage": "url_status_404",
  "item": {
    "title": "Some",
    "excerpt": "",
    "media": [
      {
        "link": "<screenshot>"
      }
    ],
    "type": "link",
    "parser": "local",
    "meta": {
      "possibleArticle": false,
      "tags": []
    }
  },
  "result": true
}
```

`POST` `https://api.raindrop.io/rest/v1/import/url/exists`

Does specified URL's are already saved?

```
//Found
{
    "result": true,
    "ids": [
        3322,
        12323
    ]
}

//Not found
{
    "result": false,
    "ids": []
}
```

`POST` `https://api.raindrop.io/rest/v1/import/file`

Convert HTML bookmark file to JSON. Support Nestcape, Pocket and Instapaper file formats

```
{
  "result": true,
  "items": [
    {
      "title": "Web",
      "folders": [
        {
          "title": "Default",
          "folders": [],
          "bookmarks": [
            {
              "link": "https://aaa.com/a",
              "title": "Name 1",
              "lastUpdate": "2016-09-13T11:17:09.000Z",
              "tags": ["tag"],
              "excerpt": ""
            }
          ]
        }
      ],
      "bookmarks": [
        {
          "link": "https://bbb.com/b",
          "title": "Name 2",
          "lastUpdate": "2016-09-13T11:17:09.000Z",
          "tags": ["tag"],
          "excerpt": ""
        }
      ]
    },
    {
      "title": "Home",
      "folders": [
        {
          "title": "Inspiration",
          "folders": [],
          "bookmarks": [
            {
              "link": "https://ccc.com/c",
              "title": "Name 3",
              "lastUpdate": "2016-09-13T11:17:09.000Z",
              "tags": ["tag"],
              "excerpt": ""
            }
          ]
        }
      ],
      "bookmarks": []
    }
  ]
}
```

## Metadata

```json
{
  "title": "Import | API Documentation",
  "description": "Handy methods to implement import functionality",
  "url": "https://developer.raindrop.io/v1/import",
  "content": "1.  [Rest API v1](https://developer.raindrop.io/v1)\n\nImport\n------\n\nHandy methods to implement import functionality\n\n`GET` `https://api.raindrop.io/rest/v1/import/url/parse`\n\nParse and extract useful info from any URL\n\n```\n//Success\n{\n  \"item\": {\n    \"title\": \"Яндекс\",\n    \"excerpt\": \"Найдётся всё\",\n    \"media\": [\n      {\n        \"type\": \"image\",\n        \"link\": \"http://yastatic.net/s3/home/logos/share/share-logo_ru.png\"\n      }\n    ],\n    \"type\": \"link\",\n    \"meta\": {\n      \"possibleArticle\": false,\n      \"canonical\": \"https://ya.ru\",\n      \"site\": \"Яндекс\",\n      \"tags\": []\n    }\n  },\n  \"result\": true\n}\n\n//Invalid URL\n{\n  \"error\": \"not_found\",\n  \"errorMessage\": \"invalid_url\",\n  \"item\": {\n    \"title\": \"Fdfdfdf\",\n    \"excerpt\": \"\",\n    \"media\": [\n      {\n        \"link\": \"<screenshot>\"\n      }\n    ],\n    \"type\": \"link\",\n    \"parser\": \"local\",\n    \"meta\": {\n      \"possibleArticle\": false,\n      \"tags\": []\n    }\n  },\n  \"result\": true\n}\n\n//Not found\n{\n  \"error\": \"not_found\",\n  \"errorMessage\": \"url_status_404\",\n  \"item\": {\n    \"title\": \"Some\",\n    \"excerpt\": \"\",\n    \"media\": [\n      {\n        \"link\": \"<screenshot>\"\n      }\n    ],\n    \"type\": \"link\",\n    \"parser\": \"local\",\n    \"meta\": {\n      \"possibleArticle\": false,\n      \"tags\": []\n    }\n  },\n  \"result\": true\n}\n```\n\n`POST` `https://api.raindrop.io/rest/v1/import/url/exists`\n\nDoes specified URL's are already saved?\n\n```\n//Found\n{\n    \"result\": true,\n    \"ids\": [\n        3322,\n        12323\n    ]\n}\n\n//Not found\n{\n    \"result\": false,\n    \"ids\": []\n}\n```\n\n`POST` `https://api.raindrop.io/rest/v1/import/file`\n\nConvert HTML bookmark file to JSON. Support Nestcape, Pocket and Instapaper file formats\n\n```\n{\n  \"result\": true,\n  \"items\": [\n    {\n      \"title\": \"Web\",\n      \"folders\": [\n        {\n          \"title\": \"Default\",\n          \"folders\": [],\n          \"bookmarks\": [\n            {\n              \"link\": \"https://aaa.com/a\",\n              \"title\": \"Name 1\",\n              \"lastUpdate\": \"2016-09-13T11:17:09.000Z\",\n              \"tags\": [\"tag\"],\n              \"excerpt\": \"\"\n            }\n          ]\n        }\n      ],\n      \"bookmarks\": [\n        {\n          \"link\": \"https://bbb.com/b\",\n          \"title\": \"Name 2\",\n          \"lastUpdate\": \"2016-09-13T11:17:09.000Z\",\n          \"tags\": [\"tag\"],\n          \"excerpt\": \"\"\n        }\n      ]\n    },\n    {\n      \"title\": \"Home\",\n      \"folders\": [\n        {\n          \"title\": \"Inspiration\",\n          \"folders\": [],\n          \"bookmarks\": [\n            {\n              \"link\": \"https://ccc.com/c\",\n              \"title\": \"Name 3\",\n              \"lastUpdate\": \"2016-09-13T11:17:09.000Z\",\n              \"tags\": [\"tag\"],\n              \"excerpt\": \"\"\n            }\n          ]\n        }\n      ],\n      \"bookmarks\": []\n    }\n  ]\n}\n```",
  "usage": {
    "tokens": 795
  }
}
```
