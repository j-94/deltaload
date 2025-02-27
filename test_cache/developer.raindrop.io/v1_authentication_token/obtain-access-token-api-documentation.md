---
title: Obtain access token | API Documentation
description: 
url: https://developer.raindrop.io/v1/authentication/token
timestamp: 2025-01-20T15:55:38.417Z
domain: developer.raindrop.io
path: v1_authentication_token
---

# Obtain access token | API Documentation



## Content

1.  [Rest API v1](https://developer.raindrop.io/v1)
3.  [Authentication](https://developer.raindrop.io/v1/authentication)

Obtain access token
-------------------

External applications could obtain a user authorized API token via the OAuth2 protocol. Before getting started, developers need to create their applications in [App Management Console](https://app.raindrop.io/settings/integrations) and configure a valid OAuth redirect URL. A registered Raindrop.io application is assigned a unique `Client ID` and `Client Secret` which are needed for the OAuth2 flow.

This procedure is comprised of several steps, which will be described below.

If you just want to test your application, or do not plan to access any data except yours account you don't need to make all of those steps.

Just go to [App Management Console](https://app.raindrop.io/settings/integrations) and open your application settings. Copy **Test token** and use it as described in [**Make authorized calls**](https://developer.raindrop.io/v1/authentication/calls)**.**

Step 1: The authorization request


-------------------------------------

`GET` `https://raindrop.io/oauth/authorize`

Direct the user to our authorization URL with specified request parameters. — If the user is not logged in, they will be asked to log in — The user will be asked if he would like to grant your application access to his Raindrop.io data

Redirect URL configured in your application setting

The unique Client ID of the Raindrop.io app that you registered

![Image 7](https://developer.raindrop.io/~gitbook/image?url=https%3A%2F%2F3611960587-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M-GPP1TyNN8gNuijaj7%252F-M-of5es4601IU9HtzYf%252F-M-og97-rwxYlVDTb5mi%252Fauthorize.png%3Falt%3Dmedia%26token%3Dd81cc512-68bb-49a4-9342-f436f1b85c74&width=768&dpr=4&quality=100&sign=cbc9d6&sv=2)

User will be asked if he would like to grant your application access to his Raindrop.io data

Here example CURL request:

```
curl "https://api.raindrop.io/v1/oauth/authorize?client_id=5e1c382cf6f48c0211359083&redirect_uri=https:%2F%2Foauthdebugger.com%2Fdebug"
```

Step 2: The redirection to your application site


----------------------------------------------------

When the user grants your authorization request, the user will be redirected to the redirect URL configured in your application setting. The redirect request will come with query parameter attached: `code` .

The `code` parameter contains the authorization code that you will use to exchange for an access token.

In case of error redirect request will come with `error` query parameter:

When the user denies your authorization request

invalid\_application\_status

When your application exceeds the maximum token limit or when your application is being suspended due to abuse

Step 3: The token exchange


------------------------------

`POST` `https://raindrop.io/oauth/access_token`

Once you have the authorization `code`, you can exchange it for the `access_token` by doing a `POST` request with all required body parameters as JSON:

Code that you received in step 2

The unique Client ID of the Raindrop.io app that you registered

Same `redirect_uri` from step 1

```
{
  "access_token": "ae261404-11r4-47c0-bce3-e18a423da828",
  "refresh_token": "c8080368-fad2-4a3f-b2c9-71d3z85011vb",
  "expires": 1209599768, //in miliseconds, deprecated
  "expires_in": 1209599, //in seconds, use this instead!!!
  "token_type": "Bearer"
}
```

```
{"error": "bad_authorization_code"}
```

Here an example CURL request:

```
curl -X "POST" "https://raindrop.io/oauth/access_token" \
     -H 'Content-Type: application/json' \
     -d $'{
  "code": "c8983220-1cca-4626-a19d-801a6aae003c",
  "client_id": "5e1c589cf6f48c0211311383",
  "redirect_uri": "https://oauthdebugger.com/debug",
  "client_secret": "c3363988-9d27-4bc6-a0ae-d126ce78dc09",
  "grant_type": "authorization_code"
}'
```

♻️ The access token refresh


-------------------------------

`POST` `https://raindrop.io/oauth/access_token`

For security reasons access tokens (except "test tokens") will **expire after two weeks**. In this case you should request the new one, by calling `POST` request with body parameters (JSON):

The unique Client ID of your app that you registered

Client secret of your app

Refresh token that you get in step 3

```
{
  "access_token": "ae261404-18r4-47c0-bce3-e18a423da898",
  "refresh_token": "c8080368-fad2-4a9f-b2c9-73d3z850111b",
  "expires": 1209599768, //in miliseconds, deprecated
  "expires_in": 1209599, //in seconds, use this instead!!!
  "token_type": "Bearer"
}
```

## Metadata

```json
{
  "title": "Obtain access token | API Documentation",
  "description": "",
  "url": "https://developer.raindrop.io/v1/authentication/token",
  "content": "1.  [Rest API v1](https://developer.raindrop.io/v1)\n3.  [Authentication](https://developer.raindrop.io/v1/authentication)\n\nObtain access token\n-------------------\n\nExternal applications could obtain a user authorized API token via the OAuth2 protocol. Before getting started, developers need to create their applications in [App Management Console](https://app.raindrop.io/settings/integrations) and configure a valid OAuth redirect URL. A registered Raindrop.io application is assigned a unique `Client ID` and `Client Secret` which are needed for the OAuth2 flow.\n\nThis procedure is comprised of several steps, which will be described below.\n\nIf you just want to test your application, or do not plan to access any data except yours account you don't need to make all of those steps.\n\nJust go to [App Management Console](https://app.raindrop.io/settings/integrations) and open your application settings. Copy **Test token** and use it as described in [**Make authorized calls**](https://developer.raindrop.io/v1/authentication/calls)**.**\n\nStep 1: The authorization request\n\n\n-------------------------------------\n\n`GET` `https://raindrop.io/oauth/authorize`\n\nDirect the user to our authorization URL with specified request parameters. — If the user is not logged in, they will be asked to log in — The user will be asked if he would like to grant your application access to his Raindrop.io data\n\nRedirect URL configured in your application setting\n\nThe unique Client ID of the Raindrop.io app that you registered\n\n![Image 7](https://developer.raindrop.io/~gitbook/image?url=https%3A%2F%2F3611960587-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M-GPP1TyNN8gNuijaj7%252F-M-of5es4601IU9HtzYf%252F-M-og97-rwxYlVDTb5mi%252Fauthorize.png%3Falt%3Dmedia%26token%3Dd81cc512-68bb-49a4-9342-f436f1b85c74&width=768&dpr=4&quality=100&sign=cbc9d6&sv=2)\n\nUser will be asked if he would like to grant your application access to his Raindrop.io data\n\nHere example CURL request:\n\n```\ncurl \"https://api.raindrop.io/v1/oauth/authorize?client_id=5e1c382cf6f48c0211359083&redirect_uri=https:%2F%2Foauthdebugger.com%2Fdebug\"\n```\n\nStep 2: The redirection to your application site\n\n\n----------------------------------------------------\n\nWhen the user grants your authorization request, the user will be redirected to the redirect URL configured in your application setting. The redirect request will come with query parameter attached: `code` .\n\nThe `code` parameter contains the authorization code that you will use to exchange for an access token.\n\nIn case of error redirect request will come with `error` query parameter:\n\nWhen the user denies your authorization request\n\ninvalid\\_application\\_status\n\nWhen your application exceeds the maximum token limit or when your application is being suspended due to abuse\n\nStep 3: The token exchange\n\n\n------------------------------\n\n`POST` `https://raindrop.io/oauth/access_token`\n\nOnce you have the authorization `code`, you can exchange it for the `access_token` by doing a `POST` request with all required body parameters as JSON:\n\nCode that you received in step 2\n\nThe unique Client ID of the Raindrop.io app that you registered\n\nSame `redirect_uri` from step 1\n\n```\n{\n  \"access_token\": \"ae261404-11r4-47c0-bce3-e18a423da828\",\n  \"refresh_token\": \"c8080368-fad2-4a3f-b2c9-71d3z85011vb\",\n  \"expires\": 1209599768, //in miliseconds, deprecated\n  \"expires_in\": 1209599, //in seconds, use this instead!!!\n  \"token_type\": \"Bearer\"\n}\n```\n\n```\n{\"error\": \"bad_authorization_code\"}\n```\n\nHere an example CURL request:\n\n```\ncurl -X \"POST\" \"https://raindrop.io/oauth/access_token\" \\\n     -H 'Content-Type: application/json' \\\n     -d $'{\n  \"code\": \"c8983220-1cca-4626-a19d-801a6aae003c\",\n  \"client_id\": \"5e1c589cf6f48c0211311383\",\n  \"redirect_uri\": \"https://oauthdebugger.com/debug\",\n  \"client_secret\": \"c3363988-9d27-4bc6-a0ae-d126ce78dc09\",\n  \"grant_type\": \"authorization_code\"\n}'\n```\n\n♻️ The access token refresh\n\n\n-------------------------------\n\n`POST` `https://raindrop.io/oauth/access_token`\n\nFor security reasons access tokens (except \"test tokens\") will **expire after two weeks**. In this case you should request the new one, by calling `POST` request with body parameters (JSON):\n\nThe unique Client ID of your app that you registered\n\nClient secret of your app\n\nRefresh token that you get in step 3\n\n```\n{\n  \"access_token\": \"ae261404-18r4-47c0-bce3-e18a423da898\",\n  \"refresh_token\": \"c8080368-fad2-4a9f-b2c9-73d3z850111b\",\n  \"expires\": 1209599768, //in miliseconds, deprecated\n  \"expires_in\": 1209599, //in seconds, use this instead!!!\n  \"token_type\": \"Bearer\"\n}\n```",
  "usage": {
    "tokens": 1251
  }
}
```
