---
title: rest_create_corpus.py | Vectara Docs
description: This is an example of using the platform via REST.  For more sample code, including any dependencies this file has, please have a look at our GitHub examples repository.  This file can be found in that repo at python/vectara-rest/restcreatecorpus.py
url: https://docs.vectara.com/docs/getting-started-samples/rest_create_corpus.py
timestamp: 2025-01-20T16:02:21.286Z
domain: docs.vectara.com
path: docs_getting-started-samples_rest_create_corpus.py
---

# rest_create_corpus.py | Vectara Docs


This is an example of using the platform via REST.  For more sample code, including any dependencies this file has, please have a look at our GitHub examples repository.  This file can be found in that repo at python/vectara-rest/restcreatecorpus.py


## Content

```
"""Simple example of using the Vectara REST API for creating a corpus."""import jsonimport loggingimport requestsdef _get_create_corpus_json():    """ Returns a create corpus json. """    corpus = {}    corpus["name"] = "Vectara Test Corpus(Python)"    corpus["description"] = "An example corpus generated via REST API from Python code."    return json.dumps({"corpus":corpus})def create_corpus(customer_id: int, admin_address: str, jwt_token: str):    """Create a corpus.    Args:        customer_id: Unique customer ID in vectara platform.        admin_address: Address of the admin server. e.g., api.vectara.io        jwt_token: A valid Auth token.    Returns:        (response, True) in case of success and returns (error, False) in case of failure.    """    post_headers = {        "customer-id": f"{customer_id}",        "Authorization": f"Bearer {jwt_token}"    }    response = requests.post(        f"https://{admin_address}/v1/create-corpus",        data=_get_create_corpus_json(),        verify=True,        headers=post_headers)    if response.status_code != 200:        logging.error("Create Corpus failed with code %d, reason %s, text %s",                       response.status_code,                       response.reason,                       response.text)        return response, False    message = response.json()    if message["status"] and message["status"]["code"] != "OK":        logging.error("Create Corpus failed with status: %s", message["status"])        return message["status"], False    return message, True
```

## Metadata

```json
{
  "title": "rest_create_corpus.py | Vectara Docs",
  "description": "This is an example of using the platform via REST.  For more sample code, including any dependencies this file has, please have a look at our GitHub examples repository.  This file can be found in that repo at python/vectara-rest/restcreatecorpus.py",
  "url": "https://docs.vectara.com/docs/getting-started-samples/rest_create_corpus.py",
  "content": "```\n\"\"\"Simple example of using the Vectara REST API for creating a corpus.\"\"\"import jsonimport loggingimport requestsdef _get_create_corpus_json():    \"\"\" Returns a create corpus json. \"\"\"    corpus = {}    corpus[\"name\"] = \"Vectara Test Corpus(Python)\"    corpus[\"description\"] = \"An example corpus generated via REST API from Python code.\"    return json.dumps({\"corpus\":corpus})def create_corpus(customer_id: int, admin_address: str, jwt_token: str):    \"\"\"Create a corpus.    Args:        customer_id: Unique customer ID in vectara platform.        admin_address: Address of the admin server. e.g., api.vectara.io        jwt_token: A valid Auth token.    Returns:        (response, True) in case of success and returns (error, False) in case of failure.    \"\"\"    post_headers = {        \"customer-id\": f\"{customer_id}\",        \"Authorization\": f\"Bearer {jwt_token}\"    }    response = requests.post(        f\"https://{admin_address}/v1/create-corpus\",        data=_get_create_corpus_json(),        verify=True,        headers=post_headers)    if response.status_code != 200:        logging.error(\"Create Corpus failed with code %d, reason %s, text %s\",                       response.status_code,                       response.reason,                       response.text)        return response, False    message = response.json()    if message[\"status\"] and message[\"status\"][\"code\"] != \"OK\":        logging.error(\"Create Corpus failed with status: %s\", message[\"status\"])        return message[\"status\"], False    return message, True\n```",
  "usage": {
    "tokens": 344
  }
}
```
