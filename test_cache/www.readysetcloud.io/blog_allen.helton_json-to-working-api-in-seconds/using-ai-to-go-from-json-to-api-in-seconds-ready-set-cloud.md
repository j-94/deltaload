---
title: Using AI To Go From JSON to API in Seconds | Ready, Set, Cloud!
description: You can go from thought to functional API in as little as 15 seconds.
url: https://www.readysetcloud.io/blog/allen.helton/json-to-working-api-in-seconds/
timestamp: 2025-01-20T16:01:47.400Z
domain: www.readysetcloud.io
path: blog_allen.helton_json-to-working-api-in-seconds
---

# Using AI To Go From JSON to API in Seconds | Ready, Set, Cloud!


You can go from thought to functional API in as little as 15 seconds.


## Content

I’ve seen a surge in the tech industry somewhere I wouldn’t expect. Every cool new startup or major service release from the big guns seems to have one thing in mind: **front-end enablement**.

That’s a pretty generic term, so let me explain.

We seem to be paying more attention to making it quicker and easier to build fullstack applications from the seat of a UI/UX developer. And while that certainly gives me a little pause (backend services still need to be thoughtfully designed and planned out), I am liking the idea more and more.

Coming from a career of primarily backend development, I can only wish services and APIs were the most important components of any application. While I do _actually_ think that, the reality is that backend services don’t get critiqued like your user interface does. It’s simply expected to be there and expected to work. User interfaces, on the other hand, are literally what everyone judges your application on. You could have the best services in the world but if your UI is bad, nobody is going to use it.

So front-end enablement is important. Get cycles on your UI as quickly as you can to make sure it satisfies your business problem and does it in a differentiating way.

A development paradigm we find ourselves in way too often reflects a backward approach to front-end development. We write our user stories in a way that prioritizes backend development before the UI. This makes sense, you need to have APIs to call via your front-end, but it ultimately slows down your time to first iteration.

I wanted to change that. I wanted something to kickstart the entire process. So I made it.

Start With An Object
--------------------

In almost any software design process, you will start with a JSON object. This object represents the data fields you will gather/generate and any child resources associated with it. Let’s take an example of a blog post entity for [Ready, Set, Cloud](https://readysetcloud.io/).

```
{
  "slug": "json-to-working-api-in-seconds",
  "title": "Using AI to Go From JSON To API In Seconds",
  "date": "2023-11-15",
  "categories": [ "ai"],
  "tags": [ "api", "dx" ],
  "socialPosts": [
    {
      "type": "Twitter",
      "message": "Did you know you can use AI to build your API spec AND create a mock for you in seconds? Find out how!",
      "scheduledDate": "2023-11-20T14:30:00"
    }
  ]
}
```

The above seems like a relatively basic object and a front-end dev could absolutely develop against it. But that’s not enough. If you’re building an application, you’ll likely need to build a service that communicates with an API to add, update, delete, read, and list resources. Beyond that, in a typical REST API, the child resources will need their own set of endpoints too. In our example above, we’d need a way to add, update, delete, and list `socialPosts` related to our article. _By the way, I just [automated social post creation and scheduling](https://www.readysetcloud.io/blog/allen.helton/automatic-social-posts) for my site, it’s now totally hands-free!_

It sounds like a lot of work just to get to a point where you can start building your user interface.

I’m a [strong believer in API-first development](https://www.readysetcloud.io/blog/allen.helton/seriously-write-your-spec-first) and feel like you should have your API spec written before any stories are created or code is written. But I also know that doesn’t happen as often as I wish it would.

With that in mind, I built an endpoint that will take our object from above, recursively check for child entities, identify potential endpoints, then pass it to Amazon Bedrock to generate an API spec.

![Image 15: Architecture diagram of OAS generation](https://readysetcloud.s3.amazonaws.com/json_to_api_1.png)

The concept itself is quite simple, but really only a possibility now that we have GenAI to do the hard work. With some simple logic to identify endpoints and an example model, you can get a solid representation of what an API might look like to maintain a given entity.

If you want to see it in action and run it yourself, you can [view the source in GitHub](https://github.com/allenheltondev/api-spec-quickstart).

Going A Step Further
--------------------

The endpoint I created will create an API spec and while that’s cool, I wouldn’t consider that front-end enablement. Generating the spec is a great first step for API-first development. You can use that as your foundation and work your way through the developer experience, modifying endpoints and models as necessary. But we want something that front-end devs can _use_. Something they can call `fetch` on and see “real” data come back.

Now, I’ve tried using AI to write code. It doesn’t work. At least not at the scale we’d want it to when building an API from a spec. There are lots of business requirements and specific implementation details missing from getting something meaningful. At the very least, [you would need unit tests for each endpoint](https://www.readysetcloud.io/blog/allen.helton/tdd-with-ai) to build your implementation successfully.

Really what we want is something that returns data in the shape of our model. Endpoints that accept inbound data and return the data we expect when called. _Sort of like a mock_. Come to think of it, exactly like a mock!

I’ve been an avid [Postman](https://postman.com/) user for years. I know they have mock server capabilities. These mocks are built from a collection and accept request data in a specific format and return responses that match a provided schema. Exactly like what we wanted!

So we have an API spec and we want to create a mock server from it. Using the Postman API, we can add, update, and get resources within Postman itself, which means we can automate the creation of everything!

Going through the Postman API documentation, I realized this wasn’t as simple as I thought it would be. There were a few roundabout steps I had to take, but still possible to do what I wanted. Below is the workflow to create a mock server.

![Image 16: Workflow of Postman collection to create mock server](https://readysetcloud.s3.amazonaws.com/json_to_api_2.png)

This collection starts off calling the API spec generator we built then uses the Postman API to create an API, collection, and mock server from it. It even updates the API spec to include the mock server url so you have it readily available.

### Using The Collection

This is a [public Postman collection in my workspace](https://www.postman.com/allenheltondev/workspace/allen-helton-s-public-workspace/collection/16041239-4164ca43-6e6b-4d0f-b046-a0a29cc91652). Anybody can freely fork it and run it on their own. Here are the steps to go from JSON object to functional mock server.

#### One-time Setup

1.  Deploy the [spec generation stack](https://github.com/allenheltondev/api-spec-quickstart) into your AWS account
2.  Copy the `GenerateSpecEndpoint` output value from your deployment
3.  [Fork the API quickstart](https://www.postman.com/allenheltondev/workspace/allen-helton-s-public-workspace/collection/16041239-4164ca43-6e6b-4d0f-b046-a0a29cc91652/fork?origin=tab) collection into your workspace
4.  Create a [Postman API key](https://web.postman.co/settings/me/api-keys)
5.  Create an environment in Postman and add a variable called `POSTMAN_API_KEY`, mark it as a secret, and paste the generated key in there
6.  Update the `GENERATOR_BASE_URL` variable _on the collection_ to use the value you copied in step 2
7.  Update the `workspaceId` variable _on the collection_ to use the identifier of the workspace to create your mock server

#### Generating A New API

After you do the initial setup, creating APIs is a snap! Every time you want to create a new API, perform the following actions.

1.  Create or copy your JSON object you want to make an API from
2.  Replace the value in the `example` property on the _Body_ tab of the [Generate Spec](https://www.postman.com/allenheltondev/workspace/allen-helton-s-public-workspace/request/16041239-d0ee18ba-e5e4-4503-b191-2449ab389900) request
3.  Replace the value in the `resourceName` property with the name you want your API to be called
4.  Click on the collection and hit the _Run_ button
5.  Don’t change any of the values on the run screen and hit the **Run API Quickstart** button

That’s it! The collection will run, generate an API spec based on the JSON object you provided in the `example` property and create a mock server from it. You will then be able to click on the _API tab_ in Postman to view the generated spec and get the mock server url. The server url will be in the `servers` section of the API spec.

### Example Run

Using the example of a blog post from before, let’s see what actually happens when we run this thing.

![Image 17: Updated request to include my example JSON object](https://readysetcloud.s3.amazonaws.com/json_to_api_3.png)

After running the collection, I can see the API spec that was created and the mock server endpoint to test it. Looking at the rendered version on [Swagger’s OAS editor](https://editor.swagger.io/) we can see pretty clearly this is a complete API that gets us exactly what we need.

![Image 18: Endpoints and schemas created by the collection](https://readysetcloud.s3.amazonaws.com/json_to_api_4.png)

From here, a front-end engineer can take the mock endpoint and start building! All that was needed was a JSON object!

Where To Go From Here
---------------------

This was a proof of concept I built to see the feasibility of using AI to get you off the ground in a hurry. Now that I know this is possible, there are a few things I’d change to make it more robust, faster, and more capable.

**Switch from _Claude instant_ to _GPT4-turbo_**

I wanted to prove you could do this using Amazon Bedrock. It is definitely possible but less than ideal. I initially used Claude-v2 as the AI model to generate the spec but would routinely exceed the 30-second timeout on API Gateway. So I went with the less capable but faster model, Claude-v1 instant. In an ideal scenario, I’d use the new GPT4-turbo model to build out the spec - but at the time of writing that model is not quite ready for production use.

**Generate SDKs**

Now that I have a solid way to make an Open API spec and get a functioning mock server, I’d like to take it a step further and generate an SDK to call it. Many developers use SDKs to communicate with their backend services, and tools like [OpenAPI Generator](https://openapi-generator.tech/) enable them to do so without having to manually build them. OpenAPI Generator will take an API spec and compile it down into an SDK in the language of your choice, including front-end compatible languages like [typescript-fetch](https://openapi-generator.tech/docs/generators/typescript-fetch).

**Web page and async workflow**

Not everybody likes bouncing around different tools (most don’t, as it turns out). If I were to turn this into a “real thing” I’d create a webpage and do the entire generation asynchronously. You’d have a page where you input your schema and you’d receive an email with your API spec and url to the mock server when it completes or just a simple in-app notification and screen re-render. This way you can control everything from a single location. The backend would also need to change a bit. I’d still probably use the same collection, but call it via [Newman](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/) in a Lambda function as part of a Step Function workflow.

Try It Out
----------

I hope you find this useful and give it a shot. Maybe you use this to start shifting to an API-first development cycle. Maybe you use it for front-end enablement. Any way you decide to use it is progress.

We’re all about time-saving and productivity boosts these days. The tidal wave of generative AI features, patterns, and paradigms has fundamentally changed the way we approach software. Things are going to move faster, that’s just the way it is. So use this as a way to get ahead of the curve and advance your API practices forward with AI.

Reminder - you can find the code for this in two places: the [generator in GitHub](https://github.com/allenheltondev/api-spec-quickstart) and the [Postman collection in my public workspace](https://www.postman.com/allenheltondev/workspace/allen-helton-s-public-workspace/request/16041239-d0ee18ba-e5e4-4503-b191-2449ab389900). If you need some help getting it working, let me know - I’m always here to help!

Happy coding!

## Metadata

```json
{
  "title": "Using AI To Go From JSON to API in Seconds | Ready, Set, Cloud!",
  "description": "You can go from thought to functional API in as little as 15 seconds.",
  "url": "https://www.readysetcloud.io/blog/allen.helton/json-to-working-api-in-seconds/",
  "content": "I’ve seen a surge in the tech industry somewhere I wouldn’t expect. Every cool new startup or major service release from the big guns seems to have one thing in mind: **front-end enablement**.\n\nThat’s a pretty generic term, so let me explain.\n\nWe seem to be paying more attention to making it quicker and easier to build fullstack applications from the seat of a UI/UX developer. And while that certainly gives me a little pause (backend services still need to be thoughtfully designed and planned out), I am liking the idea more and more.\n\nComing from a career of primarily backend development, I can only wish services and APIs were the most important components of any application. While I do _actually_ think that, the reality is that backend services don’t get critiqued like your user interface does. It’s simply expected to be there and expected to work. User interfaces, on the other hand, are literally what everyone judges your application on. You could have the best services in the world but if your UI is bad, nobody is going to use it.\n\nSo front-end enablement is important. Get cycles on your UI as quickly as you can to make sure it satisfies your business problem and does it in a differentiating way.\n\nA development paradigm we find ourselves in way too often reflects a backward approach to front-end development. We write our user stories in a way that prioritizes backend development before the UI. This makes sense, you need to have APIs to call via your front-end, but it ultimately slows down your time to first iteration.\n\nI wanted to change that. I wanted something to kickstart the entire process. So I made it.\n\nStart With An Object\n--------------------\n\nIn almost any software design process, you will start with a JSON object. This object represents the data fields you will gather/generate and any child resources associated with it. Let’s take an example of a blog post entity for [Ready, Set, Cloud](https://readysetcloud.io/).\n\n```\n{\n  \"slug\": \"json-to-working-api-in-seconds\",\n  \"title\": \"Using AI to Go From JSON To API In Seconds\",\n  \"date\": \"2023-11-15\",\n  \"categories\": [ \"ai\"],\n  \"tags\": [ \"api\", \"dx\" ],\n  \"socialPosts\": [\n    {\n      \"type\": \"Twitter\",\n      \"message\": \"Did you know you can use AI to build your API spec AND create a mock for you in seconds? Find out how!\",\n      \"scheduledDate\": \"2023-11-20T14:30:00\"\n    }\n  ]\n}\n```\n\nThe above seems like a relatively basic object and a front-end dev could absolutely develop against it. But that’s not enough. If you’re building an application, you’ll likely need to build a service that communicates with an API to add, update, delete, read, and list resources. Beyond that, in a typical REST API, the child resources will need their own set of endpoints too. In our example above, we’d need a way to add, update, delete, and list `socialPosts` related to our article. _By the way, I just [automated social post creation and scheduling](https://www.readysetcloud.io/blog/allen.helton/automatic-social-posts) for my site, it’s now totally hands-free!_\n\nIt sounds like a lot of work just to get to a point where you can start building your user interface.\n\nI’m a [strong believer in API-first development](https://www.readysetcloud.io/blog/allen.helton/seriously-write-your-spec-first) and feel like you should have your API spec written before any stories are created or code is written. But I also know that doesn’t happen as often as I wish it would.\n\nWith that in mind, I built an endpoint that will take our object from above, recursively check for child entities, identify potential endpoints, then pass it to Amazon Bedrock to generate an API spec.\n\n![Image 15: Architecture diagram of OAS generation](https://readysetcloud.s3.amazonaws.com/json_to_api_1.png)\n\nThe concept itself is quite simple, but really only a possibility now that we have GenAI to do the hard work. With some simple logic to identify endpoints and an example model, you can get a solid representation of what an API might look like to maintain a given entity.\n\nIf you want to see it in action and run it yourself, you can [view the source in GitHub](https://github.com/allenheltondev/api-spec-quickstart).\n\nGoing A Step Further\n--------------------\n\nThe endpoint I created will create an API spec and while that’s cool, I wouldn’t consider that front-end enablement. Generating the spec is a great first step for API-first development. You can use that as your foundation and work your way through the developer experience, modifying endpoints and models as necessary. But we want something that front-end devs can _use_. Something they can call `fetch` on and see “real” data come back.\n\nNow, I’ve tried using AI to write code. It doesn’t work. At least not at the scale we’d want it to when building an API from a spec. There are lots of business requirements and specific implementation details missing from getting something meaningful. At the very least, [you would need unit tests for each endpoint](https://www.readysetcloud.io/blog/allen.helton/tdd-with-ai) to build your implementation successfully.\n\nReally what we want is something that returns data in the shape of our model. Endpoints that accept inbound data and return the data we expect when called. _Sort of like a mock_. Come to think of it, exactly like a mock!\n\nI’ve been an avid [Postman](https://postman.com/) user for years. I know they have mock server capabilities. These mocks are built from a collection and accept request data in a specific format and return responses that match a provided schema. Exactly like what we wanted!\n\nSo we have an API spec and we want to create a mock server from it. Using the Postman API, we can add, update, and get resources within Postman itself, which means we can automate the creation of everything!\n\nGoing through the Postman API documentation, I realized this wasn’t as simple as I thought it would be. There were a few roundabout steps I had to take, but still possible to do what I wanted. Below is the workflow to create a mock server.\n\n![Image 16: Workflow of Postman collection to create mock server](https://readysetcloud.s3.amazonaws.com/json_to_api_2.png)\n\nThis collection starts off calling the API spec generator we built then uses the Postman API to create an API, collection, and mock server from it. It even updates the API spec to include the mock server url so you have it readily available.\n\n### Using The Collection\n\nThis is a [public Postman collection in my workspace](https://www.postman.com/allenheltondev/workspace/allen-helton-s-public-workspace/collection/16041239-4164ca43-6e6b-4d0f-b046-a0a29cc91652). Anybody can freely fork it and run it on their own. Here are the steps to go from JSON object to functional mock server.\n\n#### One-time Setup\n\n1.  Deploy the [spec generation stack](https://github.com/allenheltondev/api-spec-quickstart) into your AWS account\n2.  Copy the `GenerateSpecEndpoint` output value from your deployment\n3.  [Fork the API quickstart](https://www.postman.com/allenheltondev/workspace/allen-helton-s-public-workspace/collection/16041239-4164ca43-6e6b-4d0f-b046-a0a29cc91652/fork?origin=tab) collection into your workspace\n4.  Create a [Postman API key](https://web.postman.co/settings/me/api-keys)\n5.  Create an environment in Postman and add a variable called `POSTMAN_API_KEY`, mark it as a secret, and paste the generated key in there\n6.  Update the `GENERATOR_BASE_URL` variable _on the collection_ to use the value you copied in step 2\n7.  Update the `workspaceId` variable _on the collection_ to use the identifier of the workspace to create your mock server\n\n#### Generating A New API\n\nAfter you do the initial setup, creating APIs is a snap! Every time you want to create a new API, perform the following actions.\n\n1.  Create or copy your JSON object you want to make an API from\n2.  Replace the value in the `example` property on the _Body_ tab of the [Generate Spec](https://www.postman.com/allenheltondev/workspace/allen-helton-s-public-workspace/request/16041239-d0ee18ba-e5e4-4503-b191-2449ab389900) request\n3.  Replace the value in the `resourceName` property with the name you want your API to be called\n4.  Click on the collection and hit the _Run_ button\n5.  Don’t change any of the values on the run screen and hit the **Run API Quickstart** button\n\nThat’s it! The collection will run, generate an API spec based on the JSON object you provided in the `example` property and create a mock server from it. You will then be able to click on the _API tab_ in Postman to view the generated spec and get the mock server url. The server url will be in the `servers` section of the API spec.\n\n### Example Run\n\nUsing the example of a blog post from before, let’s see what actually happens when we run this thing.\n\n![Image 17: Updated request to include my example JSON object](https://readysetcloud.s3.amazonaws.com/json_to_api_3.png)\n\nAfter running the collection, I can see the API spec that was created and the mock server endpoint to test it. Looking at the rendered version on [Swagger’s OAS editor](https://editor.swagger.io/) we can see pretty clearly this is a complete API that gets us exactly what we need.\n\n![Image 18: Endpoints and schemas created by the collection](https://readysetcloud.s3.amazonaws.com/json_to_api_4.png)\n\nFrom here, a front-end engineer can take the mock endpoint and start building! All that was needed was a JSON object!\n\nWhere To Go From Here\n---------------------\n\nThis was a proof of concept I built to see the feasibility of using AI to get you off the ground in a hurry. Now that I know this is possible, there are a few things I’d change to make it more robust, faster, and more capable.\n\n**Switch from _Claude instant_ to _GPT4-turbo_**\n\nI wanted to prove you could do this using Amazon Bedrock. It is definitely possible but less than ideal. I initially used Claude-v2 as the AI model to generate the spec but would routinely exceed the 30-second timeout on API Gateway. So I went with the less capable but faster model, Claude-v1 instant. In an ideal scenario, I’d use the new GPT4-turbo model to build out the spec - but at the time of writing that model is not quite ready for production use.\n\n**Generate SDKs**\n\nNow that I have a solid way to make an Open API spec and get a functioning mock server, I’d like to take it a step further and generate an SDK to call it. Many developers use SDKs to communicate with their backend services, and tools like [OpenAPI Generator](https://openapi-generator.tech/) enable them to do so without having to manually build them. OpenAPI Generator will take an API spec and compile it down into an SDK in the language of your choice, including front-end compatible languages like [typescript-fetch](https://openapi-generator.tech/docs/generators/typescript-fetch).\n\n**Web page and async workflow**\n\nNot everybody likes bouncing around different tools (most don’t, as it turns out). If I were to turn this into a “real thing” I’d create a webpage and do the entire generation asynchronously. You’d have a page where you input your schema and you’d receive an email with your API spec and url to the mock server when it completes or just a simple in-app notification and screen re-render. This way you can control everything from a single location. The backend would also need to change a bit. I’d still probably use the same collection, but call it via [Newman](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/) in a Lambda function as part of a Step Function workflow.\n\nTry It Out\n----------\n\nI hope you find this useful and give it a shot. Maybe you use this to start shifting to an API-first development cycle. Maybe you use it for front-end enablement. Any way you decide to use it is progress.\n\nWe’re all about time-saving and productivity boosts these days. The tidal wave of generative AI features, patterns, and paradigms has fundamentally changed the way we approach software. Things are going to move faster, that’s just the way it is. So use this as a way to get ahead of the curve and advance your API practices forward with AI.\n\nReminder - you can find the code for this in two places: the [generator in GitHub](https://github.com/allenheltondev/api-spec-quickstart) and the [Postman collection in my public workspace](https://www.postman.com/allenheltondev/workspace/allen-helton-s-public-workspace/request/16041239-d0ee18ba-e5e4-4503-b191-2449ab389900). If you need some help getting it working, let me know - I’m always here to help!\n\nHappy coding!",
  "usage": {
    "tokens": 2895
  }
}
```
