---
title: Untitled
description: 
url: https://api.apis.guru/v2/openapi.yaml
timestamp: 2025-01-20T16:18:46.868Z
domain: api.apis.guru
path: v2_openapi.yaml
---

# Untitled



## Content

openapi: 3.0.0
x-optic-url: "https://app.useoptic.com/organizations/febf8ac6-ee67-4565-b45a-5c85a469dca7/apis/\_0fKWqUvhs9ssYNkq1k-c"
"x-optic-standard": "@febf8ac6-ee67-4565-b45a-5c85a469dca7/Fz6KU3\_wMIO5iJ6\_VUZ30"
info:
  version: 2.2.0
  title: APIs.guru
  description: \>
    Wikipedia for Web APIs. Repository of API definitions in OpenAPI format.

    \*\*Warning\*\*: If you want to be notified about changes in advance please join our \[Slack channel\](https://join.slack.com/t/mermade/shared\_invite/zt-g78g7xir-MLE\_CTCcXCdfJfG3CJe9qA).

    Client sample: \[\[Demo\]\](https://apis.guru/simple-ui) \[\[Repo\]\](https://github.com/APIs-guru/simple-ui)
  contact:
    name: APIs.guru
    url: https://APIs.guru
    email: mike.ralphson@gmail.com
  license:
    name: CC0 1.0
    url: https://github.com/APIs-guru/openapi-directory#licenses
  x-logo:
    url: https://apis.guru/branding/logo\_vertical.svg
externalDocs:
  url: https://github.com/APIs-guru/openapi-directory/blob/master/API.md
servers:
  - url: https://api.apis.guru/v2
security: \[\]
tags:
  - name: APIs
    description: Actions relating to APIs in the collection
paths:
  /providers.json:
    get:
      operationId: getProviders
      tags:
        - APIs
      summary: List all providers
      description: \>
        List all the providers in the directory
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: string
                      minLength: 1
                    minItems: 1
  /{provider}.json:
    get:
      operationId: getProvider
      tags:
        - APIs
      summary: List all APIs for a particular provider
      description: \>
        List all APIs in the directory for a particular providerName

        Returns links to the individual API entry for each API.
      parameters:
        - $ref: "#/components/parameters/provider"
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/APIs"
  /{provider}/services.json:
    get:
      operationId: getServices
      tags:
        - APIs
      summary: List all serviceNames for a particular provider
      description: \>
        List all serviceNames in the directory for a particular providerName
      parameters:
        - $ref: "#/components/parameters/provider"
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: string
                      minLength: 0
                    minItems: 1
  /specs/{provider}/{api}.json:
    get:
      operationId: getAPI
      tags: 
        - APIs
      summary: Retrieve one version of a particular API
      description: Returns the API entry for one specific version of an API where there is no serviceName.
      parameters:
        - $ref: "#/components/parameters/provider"
        - $ref: "#/components/parameters/api"
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/API"
  /specs/{provider}/{service}/{api}.json:
    get:
      operationId: getServiceAPI
      tags: 
        - APIs
      summary: Retrieve one version of a particular API with a serviceName.
      description: Returns the API entry for one specific version of an API where there is a serviceName.
      parameters:
        - $ref: "#/components/parameters/provider"
        - name: service
          in: path
          required: true
          schema:
            type: string
            minLength: 1
            maxLength: 255
            example: graph
        - $ref: "#/components/parameters/api"
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/API"
  /list.json:
    get:
      operationId: listAPIs
      tags:
        - APIs
      summary: List all APIs
      description: \>
        List all APIs in the directory.

        Returns links to the OpenAPI definitions for each API in the directory.

        If API exist in multiple versions \`preferred\` one is explicitly marked.

        Some basic info from the OpenAPI definition is cached inside each object.

        This allows you to generate some simple views without needing to fetch the OpenAPI definition for each API.
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/APIs"
  /metrics.json:
    get:
      operationId: getMetrics
      summary: Get basic metrics
      description: \>
        Some basic metrics for the entire directory.

        Just stunning numbers to put on a front page and are intended purely for WoW effect :)
      tags:
        - APIs
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Metrics"
components:
  schemas:
    APIs:
      description: |
        List of API details.
        It is a JSON object with API IDs(\`<provider\>\[:<service\>\]\`) as keys.
      type: object
      additionalProperties:
        $ref: "#/components/schemas/API"
      minProperties: 1
      example:
        googleapis.com:drive:
          added: 2015-02-22T20:00:45.000Z
          preferred: v3
          versions:
            v2:
              added: 2015-02-22T20:00:45.000Z
              info:
                title: Drive
                version: v2
                x-apiClientRegistration:
                  url: https://console.developers.google.com
                x-logo:
                  url: https://api.apis.guru/v2/cache/logo/https\_www.gstatic.com\_images\_icons\_material\_product\_2x\_drive\_32dp.png
                x-origin:
                  format: google
                  url: https://www.googleapis.com/discovery/v1/apis/drive/v2/rest
                  version: v1
                x-preferred: false
                x-providerName: googleapis.com
                x-serviceName: drive
              swaggerUrl: https://api.apis.guru/v2/specs/googleapis.com/drive/v2/swagger.json
              swaggerYamlUrl: https://api.apis.guru/v2/specs/googleapis.com/drive/v2/swagger.yaml
              updated: 2016-06-17T00:21:44.000Z
            v3:
              added: 2015-12-12T00:25:13.000Z
              info:
                title: Drive
                version: v3
                x-apiClientRegistration:
                  url: https://console.developers.google.com
                x-logo:
                  url: https://api.apis.guru/v2/cache/logo/https\_www.gstatic.com\_images\_icons\_material\_product\_2x\_drive\_32dp.png
                x-origin:
                  format: google
                  url: https://www.googleapis.com/discovery/v1/apis/drive/v3/rest
                  version: v1
                x-preferred: true
                x-providerName: googleapis.com
                x-serviceName: drive
              swaggerUrl: https://api.apis.guru/v2/specs/googleapis.com/drive/v3/swagger.json
              swaggerYamlUrl: https://api.apis.guru/v2/specs/googleapis.com/drive/v3/swagger.yaml
              updated: 2016-06-17T00:21:44.000Z
    API:
      description: Meta information about API
      type: object
      required:
        - added
        - preferred
        - versions
      properties:
        added:
          description: Timestamp when the API was first added to the directory
          type: string
          format: date-time
        preferred:
          description: Recommended version
          type: string
        versions:
          description: List of supported versions of the API
          type: object
          additionalProperties:
            $ref: "#/components/schemas/ApiVersion"
          minProperties: 1
      additionalProperties: false
    ApiVersion:
      type: object
      required:
        - added
        - updated
        - swaggerUrl
        - swaggerYamlUrl
        - info
        - openapiVer
      properties:
        added:
          description: Timestamp when the version was added
          type: string
          format: date-time
        updated:
          description: Timestamp when the version was updated
          type: string
          format: date-time
        swaggerUrl:
          description: URL to OpenAPI definition in JSON format
          type: string
          format: url
        swaggerYamlUrl:
          description: URL to OpenAPI definition in YAML format
          type: string
          format: url
        link:
          description: Link to the individual API entry for this API
          type: string
          format: url
        info:
          description: Copy of \`info\` section from OpenAPI definition
          type: object
          minProperties: 1
        externalDocs:
          description: Copy of \`externalDocs\` section from OpenAPI definition
          type: object
          minProperties: 1
        openapiVer:
          description: The value of the \`openapi\` or \`swagger\` property of the source definition
          type: string
      additionalProperties: false
    Metrics:
      description: List of basic metrics
      type: object
      required:
        - numSpecs
        - numAPIs
        - numEndpoints
      properties:
        numSpecs:
          description: Number of API definitions including different versions of the same API
          type: integer
          minimum: 1
        numAPIs:
          description: Number of unique APIs
          type: integer
          minimum: 1
        numEndpoints:
          description: Total number of endpoints inside all definitions
          type: integer
          minimum: 1
        unreachable:
          description: Number of unreachable (4XX,5XX status) APIs
          type: integer
        invalid:
          description: Number of newly invalid APIs  
          type: integer
        unofficial:
          description: Number of unofficial APIs
          type: integer
        fixes:
          description: Total number of fixes applied across all APIs
          type: integer
        fixedPct:
          description: Percentage of all APIs where auto fixes have been applied
          type: integer
        datasets:
          description: Data used for charting etc
          type: array
          items: {}
        stars:
          description: GitHub stars for our main repo
          type: integer
        issues:
          description: Open GitHub issues on our main repo
          type: integer
        thisWeek:
          description: Summary totals for the last 7 days
          type: object
          properties:
            added:
              description: APIs added in the last week
              type: integer
            updated:
              description: APIs updated in the last week
              type: integer
        numDrivers:
          description: Number of methods of API retrieval
          type: integer
        numProviders:
          description: Number of API providers in directory
          type: integer
      additionalProperties: false
      example:
        numAPIs: 2501
        numEndpoints: 106448
        numSpecs: 3329
        unreachable: 123
        invalid: 598
        unofficial: 25
        fixes: 81119
        fixedPct: 22
        datasets: \[\]
        stars: 2429
        issues: 28
        thisWeek:
          added: 45
          updated: 171
        numDrivers: 10
        numProviders: 659
  parameters:
    provider:
      name: provider
      in: path
      required: true
      schema:
        type: string
        minLength: 1
        maxLength: 255
        example: apis.guru
    api:
      name: api
      in: path
      required: true
      schema:
        type: string
        minLength: 1
        maxLength: 255
        example: 2.1.0

## Metadata

```json
{
  "title": "",
  "description": "",
  "url": "https://api.apis.guru/v2/openapi.yaml",
  "content": "openapi: 3.0.0\nx-optic-url: \"https://app.useoptic.com/organizations/febf8ac6-ee67-4565-b45a-5c85a469dca7/apis/\\_0fKWqUvhs9ssYNkq1k-c\"\n\"x-optic-standard\": \"@febf8ac6-ee67-4565-b45a-5c85a469dca7/Fz6KU3\\_wMIO5iJ6\\_VUZ30\"\ninfo:\n  version: 2.2.0\n  title: APIs.guru\n  description: \\>\n    Wikipedia for Web APIs. Repository of API definitions in OpenAPI format.\n\n    \\*\\*Warning\\*\\*: If you want to be notified about changes in advance please join our \\[Slack channel\\](https://join.slack.com/t/mermade/shared\\_invite/zt-g78g7xir-MLE\\_CTCcXCdfJfG3CJe9qA).\n\n    Client sample: \\[\\[Demo\\]\\](https://apis.guru/simple-ui) \\[\\[Repo\\]\\](https://github.com/APIs-guru/simple-ui)\n  contact:\n    name: APIs.guru\n    url: https://APIs.guru\n    email: mike.ralphson@gmail.com\n  license:\n    name: CC0 1.0\n    url: https://github.com/APIs-guru/openapi-directory#licenses\n  x-logo:\n    url: https://apis.guru/branding/logo\\_vertical.svg\nexternalDocs:\n  url: https://github.com/APIs-guru/openapi-directory/blob/master/API.md\nservers:\n  - url: https://api.apis.guru/v2\nsecurity: \\[\\]\ntags:\n  - name: APIs\n    description: Actions relating to APIs in the collection\npaths:\n  /providers.json:\n    get:\n      operationId: getProviders\n      tags:\n        - APIs\n      summary: List all providers\n      description: \\>\n        List all the providers in the directory\n      responses:\n        \"200\":\n          description: OK\n          content:\n            application/json:\n              schema:\n                type: object\n                properties:\n                  data:\n                    type: array\n                    items:\n                      type: string\n                      minLength: 1\n                    minItems: 1\n  /{provider}.json:\n    get:\n      operationId: getProvider\n      tags:\n        - APIs\n      summary: List all APIs for a particular provider\n      description: \\>\n        List all APIs in the directory for a particular providerName\n\n        Returns links to the individual API entry for each API.\n      parameters:\n        - $ref: \"#/components/parameters/provider\"\n      responses:\n        \"200\":\n          description: OK\n          content:\n            application/json:\n              schema:\n                $ref: \"#/components/schemas/APIs\"\n  /{provider}/services.json:\n    get:\n      operationId: getServices\n      tags:\n        - APIs\n      summary: List all serviceNames for a particular provider\n      description: \\>\n        List all serviceNames in the directory for a particular providerName\n      parameters:\n        - $ref: \"#/components/parameters/provider\"\n      responses:\n        \"200\":\n          description: OK\n          content:\n            application/json:\n              schema:\n                type: object\n                properties:\n                  data:\n                    type: array\n                    items:\n                      type: string\n                      minLength: 0\n                    minItems: 1\n  /specs/{provider}/{api}.json:\n    get:\n      operationId: getAPI\n      tags: \n        - APIs\n      summary: Retrieve one version of a particular API\n      description: Returns the API entry for one specific version of an API where there is no serviceName.\n      parameters:\n        - $ref: \"#/components/parameters/provider\"\n        - $ref: \"#/components/parameters/api\"\n      responses:\n        \"200\":\n          description: OK\n          content:\n            application/json:\n              schema:\n                $ref: \"#/components/schemas/API\"\n  /specs/{provider}/{service}/{api}.json:\n    get:\n      operationId: getServiceAPI\n      tags: \n        - APIs\n      summary: Retrieve one version of a particular API with a serviceName.\n      description: Returns the API entry for one specific version of an API where there is a serviceName.\n      parameters:\n        - $ref: \"#/components/parameters/provider\"\n        - name: service\n          in: path\n          required: true\n          schema:\n            type: string\n            minLength: 1\n            maxLength: 255\n            example: graph\n        - $ref: \"#/components/parameters/api\"\n      responses:\n        \"200\":\n          description: OK\n          content:\n            application/json:\n              schema:\n                $ref: \"#/components/schemas/API\"\n  /list.json:\n    get:\n      operationId: listAPIs\n      tags:\n        - APIs\n      summary: List all APIs\n      description: \\>\n        List all APIs in the directory.\n\n        Returns links to the OpenAPI definitions for each API in the directory.\n\n        If API exist in multiple versions \\`preferred\\` one is explicitly marked.\n\n        Some basic info from the OpenAPI definition is cached inside each object.\n\n        This allows you to generate some simple views without needing to fetch the OpenAPI definition for each API.\n      responses:\n        \"200\":\n          description: OK\n          content:\n            application/json:\n              schema:\n                $ref: \"#/components/schemas/APIs\"\n  /metrics.json:\n    get:\n      operationId: getMetrics\n      summary: Get basic metrics\n      description: \\>\n        Some basic metrics for the entire directory.\n\n        Just stunning numbers to put on a front page and are intended purely for WoW effect :)\n      tags:\n        - APIs\n      responses:\n        \"200\":\n          description: OK\n          content:\n            application/json:\n              schema:\n                $ref: \"#/components/schemas/Metrics\"\ncomponents:\n  schemas:\n    APIs:\n      description: |\n        List of API details.\n        It is a JSON object with API IDs(\\`<provider\\>\\[:<service\\>\\]\\`) as keys.\n      type: object\n      additionalProperties:\n        $ref: \"#/components/schemas/API\"\n      minProperties: 1\n      example:\n        googleapis.com:drive:\n          added: 2015-02-22T20:00:45.000Z\n          preferred: v3\n          versions:\n            v2:\n              added: 2015-02-22T20:00:45.000Z\n              info:\n                title: Drive\n                version: v2\n                x-apiClientRegistration:\n                  url: https://console.developers.google.com\n                x-logo:\n                  url: https://api.apis.guru/v2/cache/logo/https\\_www.gstatic.com\\_images\\_icons\\_material\\_product\\_2x\\_drive\\_32dp.png\n                x-origin:\n                  format: google\n                  url: https://www.googleapis.com/discovery/v1/apis/drive/v2/rest\n                  version: v1\n                x-preferred: false\n                x-providerName: googleapis.com\n                x-serviceName: drive\n              swaggerUrl: https://api.apis.guru/v2/specs/googleapis.com/drive/v2/swagger.json\n              swaggerYamlUrl: https://api.apis.guru/v2/specs/googleapis.com/drive/v2/swagger.yaml\n              updated: 2016-06-17T00:21:44.000Z\n            v3:\n              added: 2015-12-12T00:25:13.000Z\n              info:\n                title: Drive\n                version: v3\n                x-apiClientRegistration:\n                  url: https://console.developers.google.com\n                x-logo:\n                  url: https://api.apis.guru/v2/cache/logo/https\\_www.gstatic.com\\_images\\_icons\\_material\\_product\\_2x\\_drive\\_32dp.png\n                x-origin:\n                  format: google\n                  url: https://www.googleapis.com/discovery/v1/apis/drive/v3/rest\n                  version: v1\n                x-preferred: true\n                x-providerName: googleapis.com\n                x-serviceName: drive\n              swaggerUrl: https://api.apis.guru/v2/specs/googleapis.com/drive/v3/swagger.json\n              swaggerYamlUrl: https://api.apis.guru/v2/specs/googleapis.com/drive/v3/swagger.yaml\n              updated: 2016-06-17T00:21:44.000Z\n    API:\n      description: Meta information about API\n      type: object\n      required:\n        - added\n        - preferred\n        - versions\n      properties:\n        added:\n          description: Timestamp when the API was first added to the directory\n          type: string\n          format: date-time\n        preferred:\n          description: Recommended version\n          type: string\n        versions:\n          description: List of supported versions of the API\n          type: object\n          additionalProperties:\n            $ref: \"#/components/schemas/ApiVersion\"\n          minProperties: 1\n      additionalProperties: false\n    ApiVersion:\n      type: object\n      required:\n        - added\n        - updated\n        - swaggerUrl\n        - swaggerYamlUrl\n        - info\n        - openapiVer\n      properties:\n        added:\n          description: Timestamp when the version was added\n          type: string\n          format: date-time\n        updated:\n          description: Timestamp when the version was updated\n          type: string\n          format: date-time\n        swaggerUrl:\n          description: URL to OpenAPI definition in JSON format\n          type: string\n          format: url\n        swaggerYamlUrl:\n          description: URL to OpenAPI definition in YAML format\n          type: string\n          format: url\n        link:\n          description: Link to the individual API entry for this API\n          type: string\n          format: url\n        info:\n          description: Copy of \\`info\\` section from OpenAPI definition\n          type: object\n          minProperties: 1\n        externalDocs:\n          description: Copy of \\`externalDocs\\` section from OpenAPI definition\n          type: object\n          minProperties: 1\n        openapiVer:\n          description: The value of the \\`openapi\\` or \\`swagger\\` property of the source definition\n          type: string\n      additionalProperties: false\n    Metrics:\n      description: List of basic metrics\n      type: object\n      required:\n        - numSpecs\n        - numAPIs\n        - numEndpoints\n      properties:\n        numSpecs:\n          description: Number of API definitions including different versions of the same API\n          type: integer\n          minimum: 1\n        numAPIs:\n          description: Number of unique APIs\n          type: integer\n          minimum: 1\n        numEndpoints:\n          description: Total number of endpoints inside all definitions\n          type: integer\n          minimum: 1\n        unreachable:\n          description: Number of unreachable (4XX,5XX status) APIs\n          type: integer\n        invalid:\n          description: Number of newly invalid APIs  \n          type: integer\n        unofficial:\n          description: Number of unofficial APIs\n          type: integer\n        fixes:\n          description: Total number of fixes applied across all APIs\n          type: integer\n        fixedPct:\n          description: Percentage of all APIs where auto fixes have been applied\n          type: integer\n        datasets:\n          description: Data used for charting etc\n          type: array\n          items: {}\n        stars:\n          description: GitHub stars for our main repo\n          type: integer\n        issues:\n          description: Open GitHub issues on our main repo\n          type: integer\n        thisWeek:\n          description: Summary totals for the last 7 days\n          type: object\n          properties:\n            added:\n              description: APIs added in the last week\n              type: integer\n            updated:\n              description: APIs updated in the last week\n              type: integer\n        numDrivers:\n          description: Number of methods of API retrieval\n          type: integer\n        numProviders:\n          description: Number of API providers in directory\n          type: integer\n      additionalProperties: false\n      example:\n        numAPIs: 2501\n        numEndpoints: 106448\n        numSpecs: 3329\n        unreachable: 123\n        invalid: 598\n        unofficial: 25\n        fixes: 81119\n        fixedPct: 22\n        datasets: \\[\\]\n        stars: 2429\n        issues: 28\n        thisWeek:\n          added: 45\n          updated: 171\n        numDrivers: 10\n        numProviders: 659\n  parameters:\n    provider:\n      name: provider\n      in: path\n      required: true\n      schema:\n        type: string\n        minLength: 1\n        maxLength: 255\n        example: apis.guru\n    api:\n      name: api\n      in: path\n      required: true\n      schema:\n        type: string\n        minLength: 1\n        maxLength: 255\n        example: 2.1.0",
  "usage": {
    "tokens": 2823
  }
}
```
