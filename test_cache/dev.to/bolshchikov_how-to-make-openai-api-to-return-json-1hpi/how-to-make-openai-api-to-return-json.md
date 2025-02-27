---
title: How to Make OpenAI API to Return JSON
description: During OpenAI's dev day, one of the major announcements was the ability to receive a JSON from the... Tagged with openai, ai, javascript, howto.
url: https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi
timestamp: 2025-01-20T15:52:25.737Z
domain: dev.to
path: bolshchikov_how-to-make-openai-api-to-return-json-1hpi
---

# How to Make OpenAI API to Return JSON


During OpenAI's dev day, one of the major announcements was the ability to receive a JSON from the... Tagged with openai, ai, javascript, howto.


## Content

How to Make OpenAI API to Return JSON - DEV Community
===============                                         

  

[Skip to content](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#main-content)

 [![Image 26: DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)](https://dev.to/)

  [Powered by Algolia](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)

[](https://dev.to/search)

[Log in](https://dev.to/enter) [Create account](https://dev.to/enter?state=new-user)

DEV Community
-------------

 

 ![Image 27](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)Add reaction

 ![Image 28](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)Like ![Image 29](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)Unicorn  ![Image 30](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)Exploding Head  ![Image 31](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)Raised Hands  ![Image 32](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)Fire

Jump to Comments Save Boost

Copy link 

Copied to Clipboard

[Share to X](https://twitter.com/intent/tweet?text=%22How%20to%20Make%20OpenAI%20API%20to%20Return%20JSON%22%20by%20Sergey%20Bolshchikov%20%23DEVCommunity%20https%3A%2F%2Fdev.to%2Fbolshchikov%2Fhow-to-make-openai-api-to-return-json-1hpi) [Share to LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdev.to%2Fbolshchikov%2Fhow-to-make-openai-api-to-return-json-1hpi&title=How%20to%20Make%20OpenAI%20API%20to%20Return%20JSON&summary=During%20OpenAI%27s%20dev%20day%2C%20one%20of%20the%20major%20announcements%20was%20the%20ability%20to%20receive%20a%20JSON%20from%20the...&source=DEV%20Community) [Share to Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.to%2Fbolshchikov%2Fhow-to-make-openai-api-to-return-json-1hpi) [Share to Mastodon](https://toot.kytta.dev/?text=https%3A%2F%2Fdev.to%2Fbolshchikov%2Fhow-to-make-openai-api-to-return-json-1hpi)

[Share Post via...](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#) [Report Abuse](https://dev.to/report-abuse)

[![Image 33: Sergey Bolshchikov](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F886414%2F8ba89a43-ac80-4cb1-9e8a-ecbbe560b06f.jpeg)](https://dev.to/bolshchikov)

[Sergey Bolshchikov](https://dev.to/bolshchikov)Posted on Nov 15, 2023

   ![Image 34](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)  ![Image 35](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)  ![Image 36](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)  ![Image 37](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![Image 38](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

How to Make OpenAI API to Return JSON
=====================================

[#openai](https://dev.to/t/openai) [#ai](https://dev.to/t/ai) [#javascript](https://dev.to/t/javascript) [#howto](https://dev.to/t/howto)

During OpenAI's dev day, one of the [major announcements](https://openai.com/blog/function-calling-and-other-api-updates) was the ability to receive a JSON from the chat completion API. However, there aren't a few clear examples of how to do this as most examples focus on function calls.

Our objective is straightforward: given a query, we want to receive an answer in JSON format.

How can we achieve this?

There are three crucial steps.

### [](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#modify-your-prompt)Modify your prompt

Your prompt must explicitly specify that the response should be in JSON format and you need to define the structure of the JSON object.

```
Given this work history, what's the overall years of experience?
Work history includes start and end date (or present), title, and company name.
If the end date is "Present", use the current date. Today is November 2023.
Return the answer in JSON format with the field "experienceInMonths"
and value as a number.
```

 

Pay attention to the last sentence of the prompt.

### [](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#pass-responseformat)Pass response\_format

When calling the API, specify the response\_format.

```
const res = await this.openAI.chat.completions.create({
  model: 'gpt-3.5-turbo-1106',
  temperature: 0.0,
  top_p: 1,
  frequency_penalty: 0,
  presence_penalty: 0,
  response_format: {
    type: 'json_object', // specify the format
  },
  messages: [
    { role: 'system', content: systemPrompt },
    { role: 'user', content: workHistory },
  ],
});

```

 

It's crucial to modify the prompt as well. Just changing the response type to JSON might result in a JSON of an arbitrary structure.

See this comment from the OpenAI API:

```
**Important:** when using JSON mode, you **must** also instruct the model to
produce JSON yourself via a system or user message. Without this, the model may
generate an unending stream of whitespace until the generation reaches the token
limit, resulting in increased latency and the appearance of a "stuck" request.
Also note that the message content may be partially cut off if
`finish_reason="length"`, which indicates the generation exceeded `max_tokens`
or the conversation exceeded the max context length.

```

 

### [](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#parse-json-response)Parse JSON response

Once we receive the response, the content is still text (string type), but we can now parse it as JSON.

```
const content: string = get(res, 'choices[0].message.content');
try {
  return JSON.parse(content)['experienceInMonths'];
} catch (error) {
  this.logger.warn('Calculating total experience for a member did not work');
  return -1;
}

```

 

It's good practice to wrap JSON.parse in a try...catch statement in case we receive an invalid JSON structure.

You can find a [playground example here](https://platform.openai.com/playground/p/JP5k7UGrVtfbZAk8RyIkgEgi?mode=chat).

Top comments (0)
----------------

Subscribe

    ![Image 39: pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

Personal Trusted User

[Create template](https://dev.to/settings/response-templates)Templates let you quickly answer FAQs or store snippets for re-use.

Submit Preview [Dismiss](https://dev.to/404.html)

[Code of Conduct](https://dev.to/code-of-conduct) • [Report abuse](https://dev.to/report-abuse)

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's [permalink](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#).

Hide child comments as well

Confirm

For further actions, you may consider blocking this person and/or [reporting abuse](https://dev.to/report-abuse)

Read next
---------

[![Image 40: mikeyoung44 profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1054351%2F445fb057-59a3-41ac-81ec-9d0c93a5c618.jpg) ### AI System Combines Face Analysis and Body Signals to Better Detect Human Emotions Mike Young - Jan 8](https://dev.to/mikeyoung44/ai-system-combines-face-analysis-and-body-signals-to-better-detect-human-emotions-24a4)[![Image 41: arif-un profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F386259%2Fd7453040-87d1-42be-a5f2-2a9923755b52.jpeg) ### Timeline of key events in Nvidia's history Arif Uddin - Jan 3](https://dev.to/arif-un/timeline-of-key-events-in-nvidias-history-4f9e)[![Image 42: zeenox-stack profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2538557%2F3a28680a-d257-4d98-8d73-969d7073e30f.jpeg) ### AI-Integrated Web Development Projects to Level Up Your Skills: A Developer’s Guide dark gaming - Jan 3](https://dev.to/zeenox-stack/ai-integrated-web-development-projects-to-level-up-your-skills-a-developers-guide-5c2f)[![Image 43: fonteeboa profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1868513%2Fcbe4a3c0-28a6-433e-82e5-8adcf7a02944.png) ### 🚨 The Dangers of Developers Relying Exclusively on AI Without Understanding Fundamental Concepts João Victor - Jan 15](https://dev.to/fonteeboa/the-dangers-of-developers-relying-exclusively-on-ai-without-understanding-fundamental-concepts-6m7)

 [![Image 44](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F886414%2F8ba89a43-ac80-4cb1-9e8a-ecbbe560b06f.jpeg)Sergey Bolshchikov](https://dev.to/bolshchikov)

Follow

A path from Software Engineer to VP R&D and to VP HR

*   Education
    
    Technion
    
*   Work
    
    Finaloop
    
*   Joined
    
    Jul 3, 2022
    

### More from [Sergey Bolshchikov](https://dev.to/bolshchikov)

[🧹🧹 Sanitizing user input with OpenAI under $1 #ai #python #javascript #openai](https://dev.to/bolshchikov/sanitizing-any-user-input-with-openai-under-1-3ief)[😱 Sane front-end project architecture based on 12 years of experience #javascript #architecture #react #opensource](https://dev.to/bolshchikov/sane-front-end-project-architecture-based-on-12-years-of-experience-5051)[Why Software Engineers Aren't Going Anywhere, Even with AI #ai #career #discuss](https://dev.to/bolshchikov/why-software-engineers-arent-going-anywhere-even-with-ai-4i3d)

Thank you to our Diamond Sponsor [Neon](https://neon.tech/) for supporting our community.

[DEV Community](https://dev.to/) — A constructive and inclusive social network for software developers. With you every step of your journey.

*   [Home](https://dev.to/)
*   [DEV++](https://dev.to/++)
*   [Podcasts](https://dev.to/pod)
*   [Videos](https://dev.to/videos)
*   [Tags](https://dev.to/tags)
*   [DEV Help](https://dev.to/help)
*   [Forem Shop](https://shop.forem.com/)
*   [Advertise on DEV](https://dev.to/advertise)
*   [DEV Challenges](https://dev.to/challenges)
*   [DEV Showcase](https://dev.to/showcase)
*   [About](https://dev.to/about)
*   [Contact](https://dev.to/contact)
*   [Free Postgres Database](https://dev.to/free-postgres-database-tier)
*   [Software comparisons](https://dev.to/software-comparisons)

*   [Code of Conduct](https://dev.to/code-of-conduct)
*   [Privacy Policy](https://dev.to/privacy)
*   [Terms of use](https://dev.to/terms)

Built on [Forem](https://www.forem.com/) — the [open source](https://dev.to/t/opensource) software that powers [DEV](https://dev.to/) and other inclusive communities.

Made with love and [Ruby on Rails](https://dev.to/t/rails). DEV Community © 2016 - 2025.

![Image 45: DEV Community](https://media2.dev.to/dynamic/image/width=190,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

We're a place where coders share, stay up-to-date and grow their careers.

[Log in](https://dev.to/enter) [Create account](https://dev.to/enter?state=new-user)

![Image 46](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) ![Image 47](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![Image 48](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![Image 49](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![Image 50](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

## Metadata

```json
{
  "title": "How to Make OpenAI API to Return JSON",
  "description": "During OpenAI's dev day, one of the major announcements was the ability to receive a JSON from the... Tagged with openai, ai, javascript, howto.",
  "url": "https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi",
  "content": "How to Make OpenAI API to Return JSON - DEV Community\n===============                                         \n\n  \n\n[Skip to content](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#main-content)\n\n [![Image 26: DEV Community](https://media2.dev.to/dynamic/image/quality=100/https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png)](https://dev.to/)\n\n  [Powered by Algolia](https://www.algolia.com/developers/?utm_source=devto&utm_medium=referral)\n\n[](https://dev.to/search)\n\n[Log in](https://dev.to/enter) [Create account](https://dev.to/enter?state=new-user)\n\nDEV Community\n-------------\n\n \n\n ![Image 27](https://assets.dev.to/assets/heart-plus-active-9ea3b22f2bc311281db911d416166c5f430636e76b15cd5df6b3b841d830eefa.svg)Add reaction\n\n ![Image 28](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)Like ![Image 29](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)Unicorn  ![Image 30](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)Exploding Head  ![Image 31](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg)Raised Hands  ![Image 32](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)Fire\n\nJump to Comments Save Boost\n\nCopy link \n\nCopied to Clipboard\n\n[Share to X](https://twitter.com/intent/tweet?text=%22How%20to%20Make%20OpenAI%20API%20to%20Return%20JSON%22%20by%20Sergey%20Bolshchikov%20%23DEVCommunity%20https%3A%2F%2Fdev.to%2Fbolshchikov%2Fhow-to-make-openai-api-to-return-json-1hpi) [Share to LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fdev.to%2Fbolshchikov%2Fhow-to-make-openai-api-to-return-json-1hpi&title=How%20to%20Make%20OpenAI%20API%20to%20Return%20JSON&summary=During%20OpenAI%27s%20dev%20day%2C%20one%20of%20the%20major%20announcements%20was%20the%20ability%20to%20receive%20a%20JSON%20from%20the...&source=DEV%20Community) [Share to Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.to%2Fbolshchikov%2Fhow-to-make-openai-api-to-return-json-1hpi) [Share to Mastodon](https://toot.kytta.dev/?text=https%3A%2F%2Fdev.to%2Fbolshchikov%2Fhow-to-make-openai-api-to-return-json-1hpi)\n\n[Share Post via...](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#) [Report Abuse](https://dev.to/report-abuse)\n\n[![Image 33: Sergey Bolshchikov](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F886414%2F8ba89a43-ac80-4cb1-9e8a-ecbbe560b06f.jpeg)](https://dev.to/bolshchikov)\n\n[Sergey Bolshchikov](https://dev.to/bolshchikov)Posted on Nov 15, 2023\n\n   ![Image 34](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg)  ![Image 35](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg)  ![Image 36](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg)  ![Image 37](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![Image 38](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)\n\nHow to Make OpenAI API to Return JSON\n=====================================\n\n[#openai](https://dev.to/t/openai) [#ai](https://dev.to/t/ai) [#javascript](https://dev.to/t/javascript) [#howto](https://dev.to/t/howto)\n\nDuring OpenAI's dev day, one of the [major announcements](https://openai.com/blog/function-calling-and-other-api-updates) was the ability to receive a JSON from the chat completion API. However, there aren't a few clear examples of how to do this as most examples focus on function calls.\n\nOur objective is straightforward: given a query, we want to receive an answer in JSON format.\n\nHow can we achieve this?\n\nThere are three crucial steps.\n\n### [](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#modify-your-prompt)Modify your prompt\n\nYour prompt must explicitly specify that the response should be in JSON format and you need to define the structure of the JSON object.\n\n```\nGiven this work history, what's the overall years of experience?\nWork history includes start and end date (or present), title, and company name.\nIf the end date is \"Present\", use the current date. Today is November 2023.\nReturn the answer in JSON format with the field \"experienceInMonths\"\nand value as a number.\n```\n\n \n\nPay attention to the last sentence of the prompt.\n\n### [](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#pass-responseformat)Pass response\\_format\n\nWhen calling the API, specify the response\\_format.\n\n```\nconst res = await this.openAI.chat.completions.create({\n  model: 'gpt-3.5-turbo-1106',\n  temperature: 0.0,\n  top_p: 1,\n  frequency_penalty: 0,\n  presence_penalty: 0,\n  response_format: {\n    type: 'json_object', // specify the format\n  },\n  messages: [\n    { role: 'system', content: systemPrompt },\n    { role: 'user', content: workHistory },\n  ],\n});\n\n```\n\n \n\nIt's crucial to modify the prompt as well. Just changing the response type to JSON might result in a JSON of an arbitrary structure.\n\nSee this comment from the OpenAI API:\n\n```\n**Important:** when using JSON mode, you **must** also instruct the model to\nproduce JSON yourself via a system or user message. Without this, the model may\ngenerate an unending stream of whitespace until the generation reaches the token\nlimit, resulting in increased latency and the appearance of a \"stuck\" request.\nAlso note that the message content may be partially cut off if\n`finish_reason=\"length\"`, which indicates the generation exceeded `max_tokens`\nor the conversation exceeded the max context length.\n\n```\n\n \n\n### [](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#parse-json-response)Parse JSON response\n\nOnce we receive the response, the content is still text (string type), but we can now parse it as JSON.\n\n```\nconst content: string = get(res, 'choices[0].message.content');\ntry {\n  return JSON.parse(content)['experienceInMonths'];\n} catch (error) {\n  this.logger.warn('Calculating total experience for a member did not work');\n  return -1;\n}\n\n```\n\n \n\nIt's good practice to wrap JSON.parse in a try...catch statement in case we receive an invalid JSON structure.\n\nYou can find a [playground example here](https://platform.openai.com/playground/p/JP5k7UGrVtfbZAk8RyIkgEgi?mode=chat).\n\nTop comments (0)\n----------------\n\nSubscribe\n\n    ![Image 39: pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)\n\nPersonal Trusted User\n\n[Create template](https://dev.to/settings/response-templates)Templates let you quickly answer FAQs or store snippets for re-use.\n\nSubmit Preview [Dismiss](https://dev.to/404.html)\n\n[Code of Conduct](https://dev.to/code-of-conduct) • [Report abuse](https://dev.to/report-abuse)\n\nAre you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's [permalink](https://dev.to/bolshchikov/how-to-make-openai-api-to-return-json-1hpi#).\n\nHide child comments as well\n\nConfirm\n\nFor further actions, you may consider blocking this person and/or [reporting abuse](https://dev.to/report-abuse)\n\nRead next\n---------\n\n[![Image 40: mikeyoung44 profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1054351%2F445fb057-59a3-41ac-81ec-9d0c93a5c618.jpg) ### AI System Combines Face Analysis and Body Signals to Better Detect Human Emotions Mike Young - Jan 8](https://dev.to/mikeyoung44/ai-system-combines-face-analysis-and-body-signals-to-better-detect-human-emotions-24a4)[![Image 41: arif-un profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F386259%2Fd7453040-87d1-42be-a5f2-2a9923755b52.jpeg) ### Timeline of key events in Nvidia's history Arif Uddin - Jan 3](https://dev.to/arif-un/timeline-of-key-events-in-nvidias-history-4f9e)[![Image 42: zeenox-stack profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2538557%2F3a28680a-d257-4d98-8d73-969d7073e30f.jpeg) ### AI-Integrated Web Development Projects to Level Up Your Skills: A Developer’s Guide dark gaming - Jan 3](https://dev.to/zeenox-stack/ai-integrated-web-development-projects-to-level-up-your-skills-a-developers-guide-5c2f)[![Image 43: fonteeboa profile image](https://media2.dev.to/dynamic/image/width=100,height=100,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1868513%2Fcbe4a3c0-28a6-433e-82e5-8adcf7a02944.png) ### 🚨 The Dangers of Developers Relying Exclusively on AI Without Understanding Fundamental Concepts João Victor - Jan 15](https://dev.to/fonteeboa/the-dangers-of-developers-relying-exclusively-on-ai-without-understanding-fundamental-concepts-6m7)\n\n [![Image 44](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F886414%2F8ba89a43-ac80-4cb1-9e8a-ecbbe560b06f.jpeg)Sergey Bolshchikov](https://dev.to/bolshchikov)\n\nFollow\n\nA path from Software Engineer to VP R&D and to VP HR\n\n*   Education\n    \n    Technion\n    \n*   Work\n    \n    Finaloop\n    \n*   Joined\n    \n    Jul 3, 2022\n    \n\n### More from [Sergey Bolshchikov](https://dev.to/bolshchikov)\n\n[🧹🧹 Sanitizing user input with OpenAI under $1 #ai #python #javascript #openai](https://dev.to/bolshchikov/sanitizing-any-user-input-with-openai-under-1-3ief)[😱 Sane front-end project architecture based on 12 years of experience #javascript #architecture #react #opensource](https://dev.to/bolshchikov/sane-front-end-project-architecture-based-on-12-years-of-experience-5051)[Why Software Engineers Aren't Going Anywhere, Even with AI #ai #career #discuss](https://dev.to/bolshchikov/why-software-engineers-arent-going-anywhere-even-with-ai-4i3d)\n\nThank you to our Diamond Sponsor [Neon](https://neon.tech/) for supporting our community.\n\n[DEV Community](https://dev.to/) — A constructive and inclusive social network for software developers. With you every step of your journey.\n\n*   [Home](https://dev.to/)\n*   [DEV++](https://dev.to/++)\n*   [Podcasts](https://dev.to/pod)\n*   [Videos](https://dev.to/videos)\n*   [Tags](https://dev.to/tags)\n*   [DEV Help](https://dev.to/help)\n*   [Forem Shop](https://shop.forem.com/)\n*   [Advertise on DEV](https://dev.to/advertise)\n*   [DEV Challenges](https://dev.to/challenges)\n*   [DEV Showcase](https://dev.to/showcase)\n*   [About](https://dev.to/about)\n*   [Contact](https://dev.to/contact)\n*   [Free Postgres Database](https://dev.to/free-postgres-database-tier)\n*   [Software comparisons](https://dev.to/software-comparisons)\n\n*   [Code of Conduct](https://dev.to/code-of-conduct)\n*   [Privacy Policy](https://dev.to/privacy)\n*   [Terms of use](https://dev.to/terms)\n\nBuilt on [Forem](https://www.forem.com/) — the [open source](https://dev.to/t/opensource) software that powers [DEV](https://dev.to/) and other inclusive communities.\n\nMade with love and [Ruby on Rails](https://dev.to/t/rails). DEV Community © 2016 - 2025.\n\n![Image 45: DEV Community](https://media2.dev.to/dynamic/image/width=190,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)\n\nWe're a place where coders share, stay up-to-date and grow their careers.\n\n[Log in](https://dev.to/enter) [Create account](https://dev.to/enter?state=new-user)\n\n![Image 46](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) ![Image 47](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![Image 48](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![Image 49](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![Image 50](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)",
  "publishedTime": "2023-11-15T18:02:06Z",
  "usage": {
    "tokens": 4141
  }
}
```
