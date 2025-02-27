---
title: Endpoint Documentation | Arakoo.ai
description: Postman collection with various endpoints and their associated request and response details.
url: https://www.arakoo.com/doc/Endpoints
timestamp: 2025-01-20T15:44:43.101Z
domain: www.arakoo.com
path: doc_Endpoints
---

# Endpoint Documentation | Arakoo.ai


Postman collection with various endpoints and their associated request and response details.


## Content

Endpoint Documentation - Postman Collection
-------------------------------------------

> Postman collection with various endpoints and their associated request and response details.

Pinecone Controller[​](https://www.arakoo.com/doc/Endpoints#pinecone-controller "Direct link to Pinecone Controller")
---------------------------------------------------------------------------------------------------------------------

### 1\. Open AI - Upsert[​](https://www.arakoo.com/doc/Endpoints#1-open-ai---upsert "Direct link to 1. Open AI - Upsert")

*   **Description:** Upload a file to update Open AI data in the Pinecone namespace.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/pinecone/openai/upsert?namespace=machine-learning`
*   **Headers:**
    
    ```
    Content-Type: multipart/form-data
    ```
    
*   **Body:**
    *   Mode: formdata
    *   Key: file
    *   Type: file

**Request:**

```
POST /v1/examples/pinecone/openai/upsert?namespace=machine-learningContent-Type: multipart/form-datafile: <path_to_file>
```

### 2\. Open AI - Query[​](https://www.arakoo.com/doc/Endpoints#2-open-ai---query "Direct link to 2. Open AI - Query")

*   **Description:** Perform a query to retrieve results from Open AI in the Pinecone namespace.
    
*   **Method:** POST
    
*   **URL:** `localhost:8080/v1/examples/pinecone/openai/query?topK=6&namespace=machine-learning`
    
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    
*   **Body:**
    
*   Mode: raw
    
*   Data:
    

```
{    "query": "What is the collect stage for data maturity?"}
```

**Request:**

```
POST /v1/examples/pinecone/openai/query?topK=6&namespace=machine-learningContent-Type: application/json{    "query": "What is the collect stage for data maturity?"}
```

### 3\. Pinecone Chat[​](https://www.arakoo.com/doc/Endpoints#3-pinecone-chat "Direct link to 3. Pinecone Chat")

*   **Description:** Initiate a chat with Open AI in the Pinecone namespace.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/pinecone/openai/chat?namespace=machine-learning&id=historycontext:29557c60-715d-434c-acca-bf3a033783ad`
*   **Headers:** None
*   **Body:**
    *   Mode: raw
    *   data:

```
{    "query": "What is the collect stage for data maturity?"}
```

**Request:**

```
POST /v1/examples/pinecone/openai/chat?namespace=machine-learning&id=historycontext:29557c60-715d-434c-acca-bf3a033783ad{    "query": "What is the collect stage for data maturity?"}
```

### Delete All Pinecone Data[​](https://www.arakoo.com/doc/Endpoints#delete-all-pinecone-data "Direct link to delete-all-pinecone-data")

*   **Description:** Delete all data in the Pinecone namespace for machine learning.
*   **Method:** DELETE
*   **URL:** `localhost:8080/v1/pinecone/deleteAll?namespace=machine-learning`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    

**Request:**

```
DELETE /v1/pinecone/deleteAll?namespace=machine-learningContent-Type: application/json
```

* * *

Postgres Controller[​](https://www.arakoo.com/doc/Endpoints#postgres-controller "Direct link to Postgres Controller")
---------------------------------------------------------------------------------------------------------------------

### 1\. Open AI - Upsert[​](https://www.arakoo.com/doc/Endpoints#1-open-ai---upsert-1 "Direct link to 1. Open AI - Upsert")

*   **Description:** Upload a file to update Open AI data in the Postgres namespace.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/postgres/openai/upsert?table=spring_vectors&namespace=machine-learning`
*   **Headers:**
    
    ```
    Content-Type: multipart/form-data
    ```
    
*   **Body:**
    *   Mode: formdata
    *   Key: file
    *   Type: file

**Request:**

```
POST /v1/examples/postgres/openai/upsert?table=spring_vectors&namespace=machine-learningContent-Type: multipart/form-datafile: <path_to_file>
```

### 2\. Open AI - Query[​](https://www.arakoo.com/doc/Endpoints#2-open-ai---query-1 "Direct link to 2. Open AI - Query")

*   **Description:** Perform a query to retrieve results from Open AI in the Postgres namespace.
    
*   **Method:** POST
    
*   **URL:** `localhost:8080/v1/examples/postgres/openai/query?topK=5&table=spring_vectors&namespace=machine-learning`
    
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    
*   **Body:**
    
*   Mode: raw
    
*   Data:
    

```
{    "query": "What is the collect stage for data maturity?"}
```

**Request:**

```
POST /v1/examples/postgres/openai/query?topK=5&table=spring_vectors&namespace=machine-learningContent-Type: application/json{    "query": "What is the collect stage for data maturity?"}
```

### 3\. Open AI - Postgres Chat[​](https://www.arakoo.com/doc/Endpoints#3-open-ai---postgres-chat "Direct link to 3. Open AI - Postgres Chat")

*   **Description:** Initiate a chat with Open AI in the Postgres namespace.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/postgres/openai/chat?table=spring_vectors&id=historycontext:e350042b-d12b-4cb8-b072-51b854402ab3&namespace=machine-learning`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    
*   **Body:**
    *   Mode: raw
    *   data:

```
{    "query": "What is the collect stage for data maturity?"}
```

**Request:**

```
POST /v1/examples/postgres/openai/chat?table=spring_vectors&id=historycontext:e350042b-d12b-4cb8-b072-51b854402ab3&namespace=machine-learningContent-Type: application/json{    "query": "What is the collect stage for data maturity?"}
```

### Delete All Postgres Data[​](https://www.arakoo.com/doc/Endpoints#delete-all-postgres-data "Direct link to delete-all-postgres-data")

*   **Description:** Delete all data in the Postgres namespace for machine learning.
*   **Method:** DELETE
*   **URL:** `localhost:8080/v1/examples/postgres/deleteAll?table=spring_vectors&namespace=machine-learning`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    

**Request:**

```
DELETE /v1/examples/postgres/deleteAll?table=spring_vectors&namespace=machine-learningContent-Type: application/json
```

* * *

Redis Controller[​](https://www.arakoo.com/doc/Endpoints#redis-controller "Direct link to Redis Controller")
------------------------------------------------------------------------------------------------------------

### 1\. Open AI - Upsert[​](https://www.arakoo.com/doc/Endpoints#1-open-ai---upsert-2 "Direct link to 1. Open AI - Upsert")

*   **Description:** Upload a file to update Open AI data in the Redis namespace.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/redis/openai/upsert?namespace=machine-learning&indexName=vector_index`
*   **Headers:**
    
    ```
    Content-Type: multipart/form-data
    ```
    
*   **Body:**
    *   Mode: formdata
    *   Key: file
    *   Type: file

**Request:**

```
POST /v1/examples/redis/openai/upsert?namespace=machine-learning&indexName=vector_indexContent-Type: multipart/form-datafile: <path_to_file>
```

### 2\. Open AI - Query[​](https://www.arakoo.com/doc/Endpoints#2-open-ai---query-2 "Direct link to 2. Open AI - Query")

*   **Description:** Perform a query to retrieve results from Open AI in the Redis namespace.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/redis/openai/query?topK=7&namespace=machine-learning&indexName=vector_index`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    
*   **Body:**
*   Mode: raw
*   data:

```
{    "query":  "What is lexicography? Can you also explain social network analysis?"}
```

**Request:**

```
POST /v1/examples/redis/openai/query?topK=7&namespace=machine-learning&indexName=vector_indexContent-Type: application/json{    "query": "What is lexicography? Can you also explain social network analysis?"}
```

### 3\. Redis Chat[​](https://www.arakoo.com/doc/Endpoints#3-redis-chat "Direct link to 3. Redis Chat")

*   **Description:** Initiate a chat with Open AI in the Redis namespace.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/redis/openai/chat?namespace=machine-learning&id=historycontext:edd1e8d8-8734-4b8e-aa3d-de6a38f45ca9&indexName=vector_index`
*   **Headers:** None
*   **Body:**
*   Mode: raw
*   data:

```
{    "query":  "What is lexicography? Can you also explain social network analysis?"}
```

**Request:**

```
POST /v1/examples/redis/openai/chat?namespace=machine-learning&id=historycontext:edd1e8d8-8734-4b8e-aa3d-de6a38f45ca9&indexName=vector_index{    "query": "What is lexicography? Can you also explain social network analysis?"}
```

### 4\. Redis Similarity Search[​](https://www.arakoo.com/doc/Endpoints#4-redis-similarity-search "Direct link to 4. Redis Similarity Search")

*   **Description:** Perform a similarity search on Open AI data in the Redis namespace.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/redis/openai/similarity-search?topK=7&namespace=machine-learning&indexName=vector_index`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    
*   **Body:**
*   Mode: raw
*   data:

```
{    "query": "What is lexicography? Can you also explain social network analysis?"}
```

**Request:**

```
POST /v1/examples/redis/openai/similarity-search?topK=7&namespace=machine-learning&indexName=vector_indexContent-Type: application/json{    "query": "What is lexicography? Can you also explain social network analysis?"}
```

### Delete Redis Data[​](https://www.arakoo.com/doc/Endpoints#delete-redis-data "Direct link to delete-redis-data")

*   **Description:** Delete all data in the Redis namespace that matches the specified pattern.
*   **Method:** DELETE
*   **URL:** `localhost:8080/v1/examples/redis/delete?pattern=machine-learning*`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    

**Request:**

```
DELETE /v1/examples/redis/delete?pattern=machine-learning*Content-Type: application/json
```

* * *

Wiki Controller[​](https://www.arakoo.com/doc/Endpoints#wiki-controller "Direct link to Wiki Controller")
---------------------------------------------------------------------------------------------------------

### 1\. Wiki Summary[​](https://www.arakoo.com/doc/Endpoints#1-wiki-summary "Direct link to 1. Wiki Summary")

*   **Description:** Retrieve a summary of a given query from the Wiki.
*   **Method:** GET
*   **URL:** `localhost:8080/v1/examples/wiki-summary?query=Barack Obama`
*   **Headers:**
    
    ```
    Content-Type: application/jsonstream: false
    ```
    
*   **Body:**
*   Mode: raw
*   data: (empty)

**Request:**

```
GET /v1/examples/wiki-summary?query=Barack ObamaContent-Type: application/jsonstream: false
```

* * *

HistoryContext[​](https://www.arakoo.com/doc/Endpoints#historycontext "Direct link to HistoryContext")
------------------------------------------------------------------------------------------------------

### In Redis[​](https://www.arakoo.com/doc/Endpoints#-in-redis "Direct link to -in-redis")

### a. Create[​](https://www.arakoo.com/doc/Endpoints#a-create "Direct link to a. Create")

*   **Description:** Create a new HistoryContext in redis.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/redis/historycontext`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    
*   **Body:**
*   Mode: raw
*   data: (empty)

**Request:**

```
POST /v1/examples/redis/historycontextContent-Type: application/json
```

### b. Update[​](https://www.arakoo.com/doc/Endpoints#b-update "Direct link to b. Update")

*   **Description:** Update a HistoryContext in Redis.
*   **Method:** PUT
*   **URL:** `localhost:8080/v1/examples/redis/historycontext`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    
*   **Body:**
    *   Mode: raw
    *   Date:

```
{    "id": "historycontext:209fa722-1aa7-4495-ac5c-462beba721ae",    "response": ""}
```

**Request:**

```
PUT /v1/examples/redis/historycontextContent-Type: application/json{    "id": "historycontext:209fa722-1aa7-4495-ac5c-462beba721ae",    "response": ""}
```

### c. Get[​](https://www.arakoo.com/doc/Endpoints#c-get "Direct link to c. Get")

*   **Description:** Get a specific HistoryContext from Redis.
*   **Method:** GET
*   **URL:** `localhost:8080/v1/examples/redis/historycontext?id=historycontext:209fa722-1aa7-4495-ac5c-462beba721ae`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    

**Request:**

```
GET /v1/examples/redis/historycontext?id=historycontext:209fa722-1aa7-4495-ac5c-462beba721aeContent-Type: application/json
```

### Delete HistoryContext[​](https://www.arakoo.com/doc/Endpoints#-delete-historycontext "Direct link to -delete-historycontext")

*   **Description:** Delete a specific HistoryContext using it's ID from Redis.
*   **Method:** DELETE
*   **URL:** `localhost:8080/v1/examples/redis/historycontext?id=historycontext:af7c750f-f67e-4d9a-94e0-b10f6f434b07`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    

**Request:**

```
DELETE /v1/examples/redis/historycontext?id=historycontext:af7c750f-f67e-4d9a-94e0-b10f6f434b07Content-Type: application/json
```

* * *

### In PostgreSQL[​](https://www.arakoo.com/doc/Endpoints#-in-postgresql "Direct link to -in-postgresql")

### a. Create[​](https://www.arakoo.com/doc/Endpoints#a-create-1 "Direct link to a. Create")

*   **Description:** Create a new HistoryContext in PostgreSQL.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/postgresql/historycontext`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    
*   **Body:** (empty)

**Request:**

```
POST /v1/examples/postgresql/historycontextContent-Type: application/json
```

### b. Update[​](https://www.arakoo.com/doc/Endpoints#b-update-1 "Direct link to b. Update")

*   **Description:** Update a HistoryContext in PostgreSQL.
*   **Method:** PUT
*   **URL:** `localhost:8080/v1/examples/postgresql/historycontext`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    
*   **Body:**
    *   Mode: raw
    *   Data:

```
{    "id": "historycontext:0bbde9f8-88e6-413f-97d6-786033d59b7d",    "response": ""}
```

**Request:**

```
PUT /v1/examples/postgresql/historycontextContent-Type: application/json{    "id": "historycontext:0bbde9f8-88e6-413f-97d6-786033d59b7d",    "response": ""}
```

### c. Get[​](https://www.arakoo.com/doc/Endpoints#c-get-1 "Direct link to c. Get")

*   **Description:** Get a specific HistoryContext from PostgreSQL.
*   **Method:** GET
*   **URL:** `localhost:8080/v1/examples/postgresql/historycontext?id=historycontext:e350042b-d12b-4cb8-b072-51b854402ab3`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    

**Request:**

```
GET /v1/examples/postgresql/historycontext?id=historycontext:e350042b-d12b-4cb8-b072-51b854402ab3Content-Type: application/json
```

### Delete HistoryContext[​](https://www.arakoo.com/doc/Endpoints#-delete-historycontext-1 "Direct link to -delete-historycontext-1")

*   **Description:** Delete a specific HistoryContext from PostgreSQL.
*   **Method:** DELETE
*   **URL:** `localhost:8080/v1/examples/postgresql/historycontext?id=historycontext:437282ce-e31c-4ef7-b4bd-79a62ec98271`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    

**Request:**

```
DELETE /v1/examples/postgresql/historycontext?id=historycontext:437282ce-e31c-4ef7-b4bd-79a62ec98271Content-Type: application/json
```

* * *

Doc2Vec[​](https://www.arakoo.com/doc/Endpoints#doc2vec "Direct link to Doc2Vec")
---------------------------------------------------------------------------------

### 1\. Build[​](https://www.arakoo.com/doc/Endpoints#1-build "Direct link to 1. Build")

*   **Description:** Build a Doc2Vec model.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/doc2vec`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    

**Request:**

```
POST /v1/examples/doc2vecContent-Type: application/json
```

### 2\. Upsert[​](https://www.arakoo.com/doc/Endpoints#2-upsert "Direct link to 2. Upsert")

*   **Description:** Upload a file to update Doc2Vec data in the Redis namespace.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/examples/redis/doc2vec/upsert?namespace=doc2vec`
*   **Headers:**
    
    ```
    Content-Type: multipart/form-data
    ```
    
*   **Body:**
    *   Mode: formdata
    *   Date: `file: (file data)`

**Request:**

```
POST /v1/examples/redis/doc2vec/upsert?namespace=doc2vecContent-Type: multipart/form-datafile: (file data)
```

### 3\. Redis Similarity Search[​](https://www.arakoo.com/doc/Endpoints#3-redis-similarity-search "Direct link to 3. Redis Similarity Search")

*   **Description:** Perform a similarity search on Doc2Vec data in the Redis namespace.
*   **Method:** GET
*   **URL:** `localhost:8080/v1/examples/redis/doc2vec/similarity-search?topK=3&namespace=machine-learning&query=What is lexicography?`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    

**Request:**

```
GET /v1/examples/redis/doc2vec/similarity-search?topK=3&namespace=machine-learning&query=What is lexicography?Content-Type: application/json
```

* * *

Supabase[​](https://www.arakoo.com/doc/Endpoints#supabase "Direct link to Supabase")
------------------------------------------------------------------------------------

### 1\. Login[​](https://www.arakoo.com/doc/Endpoints#1-login "Direct link to 1. Login")

*   **Description:** Authenticate the user and get an access token.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/login`
*   **Headers:** (none)
*   **Body:**
    *   Mode: raw
    *   Data:

```
{    "email": "hiyafi2304@nmaller.com",    "password": "123456789"}
```

**Request:**

```
POST /v1/login{    "email": "hiyafi2304@nmaller.com",    "password": "123456789"}
```

### 2\. Signup[​](https://www.arakoo.com/doc/Endpoints#2-signup "Direct link to 2. Signup")

*   **Description:** Create a new user account.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/signup`
*   **Headers:**
    
    ```
    Content-Type: application/json
    ```
    
*   **Body:**
    *   Mode: raw
    *   Data:

```
{    "email": "hiyafi2304@nmaller.com",    "password": "123456789"}
```

**Request:**

```
POST /v1/signupContent-Type: application/json{    "email": "hiyafi2304@nmaller.com",    "password": "123456789"}
```

### 3\. Refresh Token[​](https://www.arakoo.com/doc/Endpoints#3-refresh-token "Direct link to 3. Refresh Token")

*   **Description:** Get a new access token using the refresh token.
*   **Method:** POST
*   **URL:** `localhost:8080/v1/refreshToken`
*   **Headers:** (none)
*   **Body:**
    *   Mode: raw
    *   Data:

```
{    "refreshToken": "sb7benGoy1fnPSR_CONpJg"}
```

**Request:**

```
POST /v1/refreshToken{    "refreshToken": "sb7benGoy1fnPSR_CONpJg"}
```

### 4\. Signout[​](https://www.arakoo.com/doc/Endpoints#4-signout "Direct link to 4. Signout")

*   **Description:** Sign out the user by invalidating the access token.
*   **Method:** POST
*   **URL:** `localhost:8080/signout`
*   **Headers:**
    
    ```
    Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IjZEME1JeERTQ0lpa3o2QjUiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjg5Njk4MTY0LCJpYXQiOjE2ODk2OTQ1NjQsImlzcyI6Imh0dHBzOi8vaHR0cHM6Ly9pdGxnZGRxaGx4aGRibmNkcW93YS5zdXBhYmFzZS5jby9hdXRoL3YxIiwic3ViIjoiZWYzNjU3NmMtY2FkOC00OGZmLWExNzktNzExMzQwNjAxZjgwIiwiZW1haWwiOiJoaXlhZmkyMzA0QG5tYWxsZXIuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJlbWFpbCIsInByb3ZpZGVycyI6WyJlbWFpbCJdfSwidXNlcl9tZXRhZGF0YSI6e30sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoicGFzc3dvcmQiLCJ0aW1lc3RhbXAiOjE2ODk2OTQ1NjR9XSwic2Vzc2lvbl9pZCI6ImYwOGJmNGJhLWFlOWEtNGRkMC04NTI3LWE0YWJjMjRmOGM5ZSJ9.0Cg9XmmgPYxu4ekZ0A_d65kzEtvjkJfA-REAsJ1JvLE
    ```
    

**Request:**

```
POST /signoutAuthorization: Bearer YOUR_ACCESS_TOKEN
```

* * *

## Metadata

```json
{
  "title": "Endpoint Documentation | Arakoo.ai",
  "description": "Postman collection with various endpoints and their associated request and response details.",
  "url": "https://www.arakoo.com/doc/Endpoints",
  "content": "Endpoint Documentation - Postman Collection\n-------------------------------------------\n\n> Postman collection with various endpoints and their associated request and response details.\n\nPinecone Controller[​](https://www.arakoo.com/doc/Endpoints#pinecone-controller \"Direct link to Pinecone Controller\")\n---------------------------------------------------------------------------------------------------------------------\n\n### 1\\. Open AI - Upsert[​](https://www.arakoo.com/doc/Endpoints#1-open-ai---upsert \"Direct link to 1. Open AI - Upsert\")\n\n*   **Description:** Upload a file to update Open AI data in the Pinecone namespace.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/pinecone/openai/upsert?namespace=machine-learning`\n*   **Headers:**\n    \n    ```\n    Content-Type: multipart/form-data\n    ```\n    \n*   **Body:**\n    *   Mode: formdata\n    *   Key: file\n    *   Type: file\n\n**Request:**\n\n```\nPOST /v1/examples/pinecone/openai/upsert?namespace=machine-learningContent-Type: multipart/form-datafile: <path_to_file>\n```\n\n### 2\\. Open AI - Query[​](https://www.arakoo.com/doc/Endpoints#2-open-ai---query \"Direct link to 2. Open AI - Query\")\n\n*   **Description:** Perform a query to retrieve results from Open AI in the Pinecone namespace.\n    \n*   **Method:** POST\n    \n*   **URL:** `localhost:8080/v1/examples/pinecone/openai/query?topK=6&namespace=machine-learning`\n    \n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n*   **Body:**\n    \n*   Mode: raw\n    \n*   Data:\n    \n\n```\n{    \"query\": \"What is the collect stage for data maturity?\"}\n```\n\n**Request:**\n\n```\nPOST /v1/examples/pinecone/openai/query?topK=6&namespace=machine-learningContent-Type: application/json{    \"query\": \"What is the collect stage for data maturity?\"}\n```\n\n### 3\\. Pinecone Chat[​](https://www.arakoo.com/doc/Endpoints#3-pinecone-chat \"Direct link to 3. Pinecone Chat\")\n\n*   **Description:** Initiate a chat with Open AI in the Pinecone namespace.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/pinecone/openai/chat?namespace=machine-learning&id=historycontext:29557c60-715d-434c-acca-bf3a033783ad`\n*   **Headers:** None\n*   **Body:**\n    *   Mode: raw\n    *   data:\n\n```\n{    \"query\": \"What is the collect stage for data maturity?\"}\n```\n\n**Request:**\n\n```\nPOST /v1/examples/pinecone/openai/chat?namespace=machine-learning&id=historycontext:29557c60-715d-434c-acca-bf3a033783ad{    \"query\": \"What is the collect stage for data maturity?\"}\n```\n\n### Delete All Pinecone Data[​](https://www.arakoo.com/doc/Endpoints#delete-all-pinecone-data \"Direct link to delete-all-pinecone-data\")\n\n*   **Description:** Delete all data in the Pinecone namespace for machine learning.\n*   **Method:** DELETE\n*   **URL:** `localhost:8080/v1/pinecone/deleteAll?namespace=machine-learning`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n\n**Request:**\n\n```\nDELETE /v1/pinecone/deleteAll?namespace=machine-learningContent-Type: application/json\n```\n\n* * *\n\nPostgres Controller[​](https://www.arakoo.com/doc/Endpoints#postgres-controller \"Direct link to Postgres Controller\")\n---------------------------------------------------------------------------------------------------------------------\n\n### 1\\. Open AI - Upsert[​](https://www.arakoo.com/doc/Endpoints#1-open-ai---upsert-1 \"Direct link to 1. Open AI - Upsert\")\n\n*   **Description:** Upload a file to update Open AI data in the Postgres namespace.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/postgres/openai/upsert?table=spring_vectors&namespace=machine-learning`\n*   **Headers:**\n    \n    ```\n    Content-Type: multipart/form-data\n    ```\n    \n*   **Body:**\n    *   Mode: formdata\n    *   Key: file\n    *   Type: file\n\n**Request:**\n\n```\nPOST /v1/examples/postgres/openai/upsert?table=spring_vectors&namespace=machine-learningContent-Type: multipart/form-datafile: <path_to_file>\n```\n\n### 2\\. Open AI - Query[​](https://www.arakoo.com/doc/Endpoints#2-open-ai---query-1 \"Direct link to 2. Open AI - Query\")\n\n*   **Description:** Perform a query to retrieve results from Open AI in the Postgres namespace.\n    \n*   **Method:** POST\n    \n*   **URL:** `localhost:8080/v1/examples/postgres/openai/query?topK=5&table=spring_vectors&namespace=machine-learning`\n    \n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n*   **Body:**\n    \n*   Mode: raw\n    \n*   Data:\n    \n\n```\n{    \"query\": \"What is the collect stage for data maturity?\"}\n```\n\n**Request:**\n\n```\nPOST /v1/examples/postgres/openai/query?topK=5&table=spring_vectors&namespace=machine-learningContent-Type: application/json{    \"query\": \"What is the collect stage for data maturity?\"}\n```\n\n### 3\\. Open AI - Postgres Chat[​](https://www.arakoo.com/doc/Endpoints#3-open-ai---postgres-chat \"Direct link to 3. Open AI - Postgres Chat\")\n\n*   **Description:** Initiate a chat with Open AI in the Postgres namespace.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/postgres/openai/chat?table=spring_vectors&id=historycontext:e350042b-d12b-4cb8-b072-51b854402ab3&namespace=machine-learning`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n*   **Body:**\n    *   Mode: raw\n    *   data:\n\n```\n{    \"query\": \"What is the collect stage for data maturity?\"}\n```\n\n**Request:**\n\n```\nPOST /v1/examples/postgres/openai/chat?table=spring_vectors&id=historycontext:e350042b-d12b-4cb8-b072-51b854402ab3&namespace=machine-learningContent-Type: application/json{    \"query\": \"What is the collect stage for data maturity?\"}\n```\n\n### Delete All Postgres Data[​](https://www.arakoo.com/doc/Endpoints#delete-all-postgres-data \"Direct link to delete-all-postgres-data\")\n\n*   **Description:** Delete all data in the Postgres namespace for machine learning.\n*   **Method:** DELETE\n*   **URL:** `localhost:8080/v1/examples/postgres/deleteAll?table=spring_vectors&namespace=machine-learning`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n\n**Request:**\n\n```\nDELETE /v1/examples/postgres/deleteAll?table=spring_vectors&namespace=machine-learningContent-Type: application/json\n```\n\n* * *\n\nRedis Controller[​](https://www.arakoo.com/doc/Endpoints#redis-controller \"Direct link to Redis Controller\")\n------------------------------------------------------------------------------------------------------------\n\n### 1\\. Open AI - Upsert[​](https://www.arakoo.com/doc/Endpoints#1-open-ai---upsert-2 \"Direct link to 1. Open AI - Upsert\")\n\n*   **Description:** Upload a file to update Open AI data in the Redis namespace.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/redis/openai/upsert?namespace=machine-learning&indexName=vector_index`\n*   **Headers:**\n    \n    ```\n    Content-Type: multipart/form-data\n    ```\n    \n*   **Body:**\n    *   Mode: formdata\n    *   Key: file\n    *   Type: file\n\n**Request:**\n\n```\nPOST /v1/examples/redis/openai/upsert?namespace=machine-learning&indexName=vector_indexContent-Type: multipart/form-datafile: <path_to_file>\n```\n\n### 2\\. Open AI - Query[​](https://www.arakoo.com/doc/Endpoints#2-open-ai---query-2 \"Direct link to 2. Open AI - Query\")\n\n*   **Description:** Perform a query to retrieve results from Open AI in the Redis namespace.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/redis/openai/query?topK=7&namespace=machine-learning&indexName=vector_index`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n*   **Body:**\n*   Mode: raw\n*   data:\n\n```\n{    \"query\":  \"What is lexicography? Can you also explain social network analysis?\"}\n```\n\n**Request:**\n\n```\nPOST /v1/examples/redis/openai/query?topK=7&namespace=machine-learning&indexName=vector_indexContent-Type: application/json{    \"query\": \"What is lexicography? Can you also explain social network analysis?\"}\n```\n\n### 3\\. Redis Chat[​](https://www.arakoo.com/doc/Endpoints#3-redis-chat \"Direct link to 3. Redis Chat\")\n\n*   **Description:** Initiate a chat with Open AI in the Redis namespace.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/redis/openai/chat?namespace=machine-learning&id=historycontext:edd1e8d8-8734-4b8e-aa3d-de6a38f45ca9&indexName=vector_index`\n*   **Headers:** None\n*   **Body:**\n*   Mode: raw\n*   data:\n\n```\n{    \"query\":  \"What is lexicography? Can you also explain social network analysis?\"}\n```\n\n**Request:**\n\n```\nPOST /v1/examples/redis/openai/chat?namespace=machine-learning&id=historycontext:edd1e8d8-8734-4b8e-aa3d-de6a38f45ca9&indexName=vector_index{    \"query\": \"What is lexicography? Can you also explain social network analysis?\"}\n```\n\n### 4\\. Redis Similarity Search[​](https://www.arakoo.com/doc/Endpoints#4-redis-similarity-search \"Direct link to 4. Redis Similarity Search\")\n\n*   **Description:** Perform a similarity search on Open AI data in the Redis namespace.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/redis/openai/similarity-search?topK=7&namespace=machine-learning&indexName=vector_index`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n*   **Body:**\n*   Mode: raw\n*   data:\n\n```\n{    \"query\": \"What is lexicography? Can you also explain social network analysis?\"}\n```\n\n**Request:**\n\n```\nPOST /v1/examples/redis/openai/similarity-search?topK=7&namespace=machine-learning&indexName=vector_indexContent-Type: application/json{    \"query\": \"What is lexicography? Can you also explain social network analysis?\"}\n```\n\n### Delete Redis Data[​](https://www.arakoo.com/doc/Endpoints#delete-redis-data \"Direct link to delete-redis-data\")\n\n*   **Description:** Delete all data in the Redis namespace that matches the specified pattern.\n*   **Method:** DELETE\n*   **URL:** `localhost:8080/v1/examples/redis/delete?pattern=machine-learning*`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n\n**Request:**\n\n```\nDELETE /v1/examples/redis/delete?pattern=machine-learning*Content-Type: application/json\n```\n\n* * *\n\nWiki Controller[​](https://www.arakoo.com/doc/Endpoints#wiki-controller \"Direct link to Wiki Controller\")\n---------------------------------------------------------------------------------------------------------\n\n### 1\\. Wiki Summary[​](https://www.arakoo.com/doc/Endpoints#1-wiki-summary \"Direct link to 1. Wiki Summary\")\n\n*   **Description:** Retrieve a summary of a given query from the Wiki.\n*   **Method:** GET\n*   **URL:** `localhost:8080/v1/examples/wiki-summary?query=Barack Obama`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/jsonstream: false\n    ```\n    \n*   **Body:**\n*   Mode: raw\n*   data: (empty)\n\n**Request:**\n\n```\nGET /v1/examples/wiki-summary?query=Barack ObamaContent-Type: application/jsonstream: false\n```\n\n* * *\n\nHistoryContext[​](https://www.arakoo.com/doc/Endpoints#historycontext \"Direct link to HistoryContext\")\n------------------------------------------------------------------------------------------------------\n\n### In Redis[​](https://www.arakoo.com/doc/Endpoints#-in-redis \"Direct link to -in-redis\")\n\n### a. Create[​](https://www.arakoo.com/doc/Endpoints#a-create \"Direct link to a. Create\")\n\n*   **Description:** Create a new HistoryContext in redis.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/redis/historycontext`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n*   **Body:**\n*   Mode: raw\n*   data: (empty)\n\n**Request:**\n\n```\nPOST /v1/examples/redis/historycontextContent-Type: application/json\n```\n\n### b. Update[​](https://www.arakoo.com/doc/Endpoints#b-update \"Direct link to b. Update\")\n\n*   **Description:** Update a HistoryContext in Redis.\n*   **Method:** PUT\n*   **URL:** `localhost:8080/v1/examples/redis/historycontext`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n*   **Body:**\n    *   Mode: raw\n    *   Date:\n\n```\n{    \"id\": \"historycontext:209fa722-1aa7-4495-ac5c-462beba721ae\",    \"response\": \"\"}\n```\n\n**Request:**\n\n```\nPUT /v1/examples/redis/historycontextContent-Type: application/json{    \"id\": \"historycontext:209fa722-1aa7-4495-ac5c-462beba721ae\",    \"response\": \"\"}\n```\n\n### c. Get[​](https://www.arakoo.com/doc/Endpoints#c-get \"Direct link to c. Get\")\n\n*   **Description:** Get a specific HistoryContext from Redis.\n*   **Method:** GET\n*   **URL:** `localhost:8080/v1/examples/redis/historycontext?id=historycontext:209fa722-1aa7-4495-ac5c-462beba721ae`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n\n**Request:**\n\n```\nGET /v1/examples/redis/historycontext?id=historycontext:209fa722-1aa7-4495-ac5c-462beba721aeContent-Type: application/json\n```\n\n### Delete HistoryContext[​](https://www.arakoo.com/doc/Endpoints#-delete-historycontext \"Direct link to -delete-historycontext\")\n\n*   **Description:** Delete a specific HistoryContext using it's ID from Redis.\n*   **Method:** DELETE\n*   **URL:** `localhost:8080/v1/examples/redis/historycontext?id=historycontext:af7c750f-f67e-4d9a-94e0-b10f6f434b07`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n\n**Request:**\n\n```\nDELETE /v1/examples/redis/historycontext?id=historycontext:af7c750f-f67e-4d9a-94e0-b10f6f434b07Content-Type: application/json\n```\n\n* * *\n\n### In PostgreSQL[​](https://www.arakoo.com/doc/Endpoints#-in-postgresql \"Direct link to -in-postgresql\")\n\n### a. Create[​](https://www.arakoo.com/doc/Endpoints#a-create-1 \"Direct link to a. Create\")\n\n*   **Description:** Create a new HistoryContext in PostgreSQL.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/postgresql/historycontext`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n*   **Body:** (empty)\n\n**Request:**\n\n```\nPOST /v1/examples/postgresql/historycontextContent-Type: application/json\n```\n\n### b. Update[​](https://www.arakoo.com/doc/Endpoints#b-update-1 \"Direct link to b. Update\")\n\n*   **Description:** Update a HistoryContext in PostgreSQL.\n*   **Method:** PUT\n*   **URL:** `localhost:8080/v1/examples/postgresql/historycontext`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n*   **Body:**\n    *   Mode: raw\n    *   Data:\n\n```\n{    \"id\": \"historycontext:0bbde9f8-88e6-413f-97d6-786033d59b7d\",    \"response\": \"\"}\n```\n\n**Request:**\n\n```\nPUT /v1/examples/postgresql/historycontextContent-Type: application/json{    \"id\": \"historycontext:0bbde9f8-88e6-413f-97d6-786033d59b7d\",    \"response\": \"\"}\n```\n\n### c. Get[​](https://www.arakoo.com/doc/Endpoints#c-get-1 \"Direct link to c. Get\")\n\n*   **Description:** Get a specific HistoryContext from PostgreSQL.\n*   **Method:** GET\n*   **URL:** `localhost:8080/v1/examples/postgresql/historycontext?id=historycontext:e350042b-d12b-4cb8-b072-51b854402ab3`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n\n**Request:**\n\n```\nGET /v1/examples/postgresql/historycontext?id=historycontext:e350042b-d12b-4cb8-b072-51b854402ab3Content-Type: application/json\n```\n\n### Delete HistoryContext[​](https://www.arakoo.com/doc/Endpoints#-delete-historycontext-1 \"Direct link to -delete-historycontext-1\")\n\n*   **Description:** Delete a specific HistoryContext from PostgreSQL.\n*   **Method:** DELETE\n*   **URL:** `localhost:8080/v1/examples/postgresql/historycontext?id=historycontext:437282ce-e31c-4ef7-b4bd-79a62ec98271`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n\n**Request:**\n\n```\nDELETE /v1/examples/postgresql/historycontext?id=historycontext:437282ce-e31c-4ef7-b4bd-79a62ec98271Content-Type: application/json\n```\n\n* * *\n\nDoc2Vec[​](https://www.arakoo.com/doc/Endpoints#doc2vec \"Direct link to Doc2Vec\")\n---------------------------------------------------------------------------------\n\n### 1\\. Build[​](https://www.arakoo.com/doc/Endpoints#1-build \"Direct link to 1. Build\")\n\n*   **Description:** Build a Doc2Vec model.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/doc2vec`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n\n**Request:**\n\n```\nPOST /v1/examples/doc2vecContent-Type: application/json\n```\n\n### 2\\. Upsert[​](https://www.arakoo.com/doc/Endpoints#2-upsert \"Direct link to 2. Upsert\")\n\n*   **Description:** Upload a file to update Doc2Vec data in the Redis namespace.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/examples/redis/doc2vec/upsert?namespace=doc2vec`\n*   **Headers:**\n    \n    ```\n    Content-Type: multipart/form-data\n    ```\n    \n*   **Body:**\n    *   Mode: formdata\n    *   Date: `file: (file data)`\n\n**Request:**\n\n```\nPOST /v1/examples/redis/doc2vec/upsert?namespace=doc2vecContent-Type: multipart/form-datafile: (file data)\n```\n\n### 3\\. Redis Similarity Search[​](https://www.arakoo.com/doc/Endpoints#3-redis-similarity-search \"Direct link to 3. Redis Similarity Search\")\n\n*   **Description:** Perform a similarity search on Doc2Vec data in the Redis namespace.\n*   **Method:** GET\n*   **URL:** `localhost:8080/v1/examples/redis/doc2vec/similarity-search?topK=3&namespace=machine-learning&query=What is lexicography?`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n\n**Request:**\n\n```\nGET /v1/examples/redis/doc2vec/similarity-search?topK=3&namespace=machine-learning&query=What is lexicography?Content-Type: application/json\n```\n\n* * *\n\nSupabase[​](https://www.arakoo.com/doc/Endpoints#supabase \"Direct link to Supabase\")\n------------------------------------------------------------------------------------\n\n### 1\\. Login[​](https://www.arakoo.com/doc/Endpoints#1-login \"Direct link to 1. Login\")\n\n*   **Description:** Authenticate the user and get an access token.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/login`\n*   **Headers:** (none)\n*   **Body:**\n    *   Mode: raw\n    *   Data:\n\n```\n{    \"email\": \"hiyafi2304@nmaller.com\",    \"password\": \"123456789\"}\n```\n\n**Request:**\n\n```\nPOST /v1/login{    \"email\": \"hiyafi2304@nmaller.com\",    \"password\": \"123456789\"}\n```\n\n### 2\\. Signup[​](https://www.arakoo.com/doc/Endpoints#2-signup \"Direct link to 2. Signup\")\n\n*   **Description:** Create a new user account.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/signup`\n*   **Headers:**\n    \n    ```\n    Content-Type: application/json\n    ```\n    \n*   **Body:**\n    *   Mode: raw\n    *   Data:\n\n```\n{    \"email\": \"hiyafi2304@nmaller.com\",    \"password\": \"123456789\"}\n```\n\n**Request:**\n\n```\nPOST /v1/signupContent-Type: application/json{    \"email\": \"hiyafi2304@nmaller.com\",    \"password\": \"123456789\"}\n```\n\n### 3\\. Refresh Token[​](https://www.arakoo.com/doc/Endpoints#3-refresh-token \"Direct link to 3. Refresh Token\")\n\n*   **Description:** Get a new access token using the refresh token.\n*   **Method:** POST\n*   **URL:** `localhost:8080/v1/refreshToken`\n*   **Headers:** (none)\n*   **Body:**\n    *   Mode: raw\n    *   Data:\n\n```\n{    \"refreshToken\": \"sb7benGoy1fnPSR_CONpJg\"}\n```\n\n**Request:**\n\n```\nPOST /v1/refreshToken{    \"refreshToken\": \"sb7benGoy1fnPSR_CONpJg\"}\n```\n\n### 4\\. Signout[​](https://www.arakoo.com/doc/Endpoints#4-signout \"Direct link to 4. Signout\")\n\n*   **Description:** Sign out the user by invalidating the access token.\n*   **Method:** POST\n*   **URL:** `localhost:8080/signout`\n*   **Headers:**\n    \n    ```\n    Authorization: Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IjZEME1JeERTQ0lpa3o2QjUiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjg5Njk4MTY0LCJpYXQiOjE2ODk2OTQ1NjQsImlzcyI6Imh0dHBzOi8vaHR0cHM6Ly9pdGxnZGRxaGx4aGRibmNkcW93YS5zdXBhYmFzZS5jby9hdXRoL3YxIiwic3ViIjoiZWYzNjU3NmMtY2FkOC00OGZmLWExNzktNzExMzQwNjAxZjgwIiwiZW1haWwiOiJoaXlhZmkyMzA0QG5tYWxsZXIuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJlbWFpbCIsInByb3ZpZGVycyI6WyJlbWFpbCJdfSwidXNlcl9tZXRhZGF0YSI6e30sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoicGFzc3dvcmQiLCJ0aW1lc3RhbXAiOjE2ODk2OTQ1NjR9XSwic2Vzc2lvbl9pZCI6ImYwOGJmNGJhLWFlOWEtNGRkMC04NTI3LWE0YWJjMjRmOGM5ZSJ9.0Cg9XmmgPYxu4ekZ0A_d65kzEtvjkJfA-REAsJ1JvLE\n    ```\n    \n\n**Request:**\n\n```\nPOST /signoutAuthorization: Bearer YOUR_ACCESS_TOKEN\n```\n\n* * *",
  "usage": {
    "tokens": 5857
  }
}
```
