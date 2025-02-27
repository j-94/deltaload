---
title: Mixtral 8x7B Instruct - API, Providers, Stats
description: Mixtral 8x7B Instruct is a pretrained generative Sparse Mixture of Experts, by Mistral AI, for chat and instruction use. Incorporates 8 experts (feed-forward networks) for a total of 47 billion parameters. Run Mixtral 8x7B Instruct with API
url: https://openrouter.ai/models/mistralai/mixtral-8x7b-instruct
timestamp: 2025-01-20T15:50:31.950Z
domain: openrouter.ai
path: models_mistralai_mixtral-8x7b-instruct
---

# Mixtral 8x7B Instruct - API, Providers, Stats


Mixtral 8x7B Instruct is a pretrained generative Sparse Mixture of Experts, by Mistral AI, for chat and instruction use. Incorporates 8 experts (feed-forward networks) for a total of 47 billion parameters. Run Mixtral 8x7B Instruct with API


## Content

Created Dec 10, 202332,768 context

$0.24/M input tokens$0.24/M output tokens

Mixtral 8x7B Instruct is a pretrained generative Sparse Mixture of Experts, by Mistral AI, for chat and instruction use. Incorporates 8 experts (feed-forward networks) for a total of 47 billion parameters.

Instruct model fine-tuned by Mistral. #moe

Providers for Mixtral 8x7B Instruct[](https://openrouter.ai/mistralai/mixtral-8x7b-instruct/providers)
------------------------------------------------------------------------------------------------------

### OpenRouter [routes requests](https://openrouter.ai/docs/provider-routing) to the top-ranked providers able to handle your prompts.

Apps using Mixtral 8x7B Instruct[](https://openrouter.ai/mistralai/mixtral-8x7b-instruct/apps)
----------------------------------------------------------------------------------------------

### Top public apps this week using this model

Recent activity on Mixtral 8x7B Instruct[](https://openrouter.ai/mistralai/mixtral-8x7b-instruct/activity)
----------------------------------------------------------------------------------------------------------

### Tokens processed per day

Uptime stats for Mixtral 8x7B Instruct[](https://openrouter.ai/mistralai/mixtral-8x7b-instruct/uptime)
------------------------------------------------------------------------------------------------------

### Uptime stats for Mixtral 8x7B Instruct across all providers

Sample code and API for Mixtral 8x7B Instruct[](https://openrouter.ai/mistralai/mixtral-8x7b-instruct/api)
----------------------------------------------------------------------------------------------------------

### OpenRouter normalizes requests and responses across providers for you.

OpenRouter provides an OpenAI-compatible completion API to 0 models & providers that you can call directly, or using the OpenAI SDK. Additionally, some third-party SDKs are available.

In the examples below, the [OpenRouter-specific headers](https://openrouter.ai/docs/requests#request-headers) are optional. Setting them allows your app to appear on the OpenRouter leaderboards.

Using the OpenAI SDK
--------------------

```
import OpenAI from "openai"

const openai = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: "<OPENROUTER_API_KEY>",
  defaultHeaders: {
    "HTTP-Referer": "<YOUR_SITE_URL>", // Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", // Optional. Site title for rankings on openrouter.ai.
  }
})

async function main() {
  const completion = await openai.chat.completions.create({
    model: "mistralai/mixtral-8x7b-instruct",
    messages: [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })

  console.log(completion.choices[0].message)
}
main()
```

Using the OpenRouter API directly
---------------------------------

```
fetch("https://openrouter.ai/api/v1/chat/completions", {
  method: "POST",
  headers: {
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "HTTP-Referer": "<YOUR_SITE_URL>", // Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", // Optional. Site title for rankings on openrouter.ai.
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    "model": "mistralai/mixtral-8x7b-instruct",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })
});
```

Using third-party SDKs
----------------------

For information about using third-party SDKs and frameworks with OpenRouter, please see our [frameworks documentation](https://openrouter.ai/docs/frameworks).

See the [Request docs](https://openrouter.ai/docs/requests) for all possible parameters, and [Parameters](https://openrouter.ai/mistralai/mixtral-8x7b-instruct?tab=parameters) for recommended values.

## Metadata

```json
{
  "title": "Mixtral 8x7B Instruct - API, Providers, Stats",
  "description": "Mixtral 8x7B Instruct is a pretrained generative Sparse Mixture of Experts, by Mistral AI, for chat and instruction use. Incorporates 8 experts (feed-forward networks) for a total of 47 billion parameters. Run Mixtral 8x7B Instruct with API",
  "url": "https://openrouter.ai/models/mistralai/mixtral-8x7b-instruct",
  "content": "Created Dec 10, 202332,768 context\n\n$0.24/M input tokens$0.24/M output tokens\n\nMixtral 8x7B Instruct is a pretrained generative Sparse Mixture of Experts, by Mistral AI, for chat and instruction use. Incorporates 8 experts (feed-forward networks) for a total of 47 billion parameters.\n\nInstruct model fine-tuned by Mistral. #moe\n\nProviders for Mixtral 8x7B Instruct[](https://openrouter.ai/mistralai/mixtral-8x7b-instruct/providers)\n------------------------------------------------------------------------------------------------------\n\n### OpenRouter [routes requests](https://openrouter.ai/docs/provider-routing) to the top-ranked providers able to handle your prompts.\n\nApps using Mixtral 8x7B Instruct[](https://openrouter.ai/mistralai/mixtral-8x7b-instruct/apps)\n----------------------------------------------------------------------------------------------\n\n### Top public apps this week using this model\n\nRecent activity on Mixtral 8x7B Instruct[](https://openrouter.ai/mistralai/mixtral-8x7b-instruct/activity)\n----------------------------------------------------------------------------------------------------------\n\n### Tokens processed per day\n\nUptime stats for Mixtral 8x7B Instruct[](https://openrouter.ai/mistralai/mixtral-8x7b-instruct/uptime)\n------------------------------------------------------------------------------------------------------\n\n### Uptime stats for Mixtral 8x7B Instruct across all providers\n\nSample code and API for Mixtral 8x7B Instruct[](https://openrouter.ai/mistralai/mixtral-8x7b-instruct/api)\n----------------------------------------------------------------------------------------------------------\n\n### OpenRouter normalizes requests and responses across providers for you.\n\nOpenRouter provides an OpenAI-compatible completion API to 0 models & providers that you can call directly, or using the OpenAI SDK. Additionally, some third-party SDKs are available.\n\nIn the examples below, the [OpenRouter-specific headers](https://openrouter.ai/docs/requests#request-headers) are optional. Setting them allows your app to appear on the OpenRouter leaderboards.\n\nUsing the OpenAI SDK\n--------------------\n\n```\nimport OpenAI from \"openai\"\n\nconst openai = new OpenAI({\n  baseURL: \"https://openrouter.ai/api/v1\",\n  apiKey: \"<OPENROUTER_API_KEY>\",\n  defaultHeaders: {\n    \"HTTP-Referer\": \"<YOUR_SITE_URL>\", // Optional. Site URL for rankings on openrouter.ai.\n    \"X-Title\": \"<YOUR_SITE_NAME>\", // Optional. Site title for rankings on openrouter.ai.\n  }\n})\n\nasync function main() {\n  const completion = await openai.chat.completions.create({\n    model: \"mistralai/mixtral-8x7b-instruct\",\n    messages: [\n      {\n        \"role\": \"user\",\n        \"content\": \"What is the meaning of life?\"\n      }\n    ]\n  })\n\n  console.log(completion.choices[0].message)\n}\nmain()\n```\n\nUsing the OpenRouter API directly\n---------------------------------\n\n```\nfetch(\"https://openrouter.ai/api/v1/chat/completions\", {\n  method: \"POST\",\n  headers: {\n    \"Authorization\": \"Bearer <OPENROUTER_API_KEY>\",\n    \"HTTP-Referer\": \"<YOUR_SITE_URL>\", // Optional. Site URL for rankings on openrouter.ai.\n    \"X-Title\": \"<YOUR_SITE_NAME>\", // Optional. Site title for rankings on openrouter.ai.\n    \"Content-Type\": \"application/json\"\n  },\n  body: JSON.stringify({\n    \"model\": \"mistralai/mixtral-8x7b-instruct\",\n    \"messages\": [\n      {\n        \"role\": \"user\",\n        \"content\": \"What is the meaning of life?\"\n      }\n    ]\n  })\n});\n```\n\nUsing third-party SDKs\n----------------------\n\nFor information about using third-party SDKs and frameworks with OpenRouter, please see our [frameworks documentation](https://openrouter.ai/docs/frameworks).\n\nSee the [Request docs](https://openrouter.ai/docs/requests) for all possible parameters, and [Parameters](https://openrouter.ai/mistralai/mixtral-8x7b-instruct?tab=parameters) for recommended values.",
  "usage": {
    "tokens": 888
  }
}
```
