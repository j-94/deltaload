---
title: Next.js - Resend
description: Learn how to send your first email using Next.js and the Resend Node.js SDK.
url: https://resend.com/docs/send-with-nextjs
timestamp: 2025-01-20T15:43:48.526Z
domain: resend.com
path: docs_send-with-nextjs
---

# Next.js - Resend


Learn how to send your first email using Next.js and the Resend Node.js SDK.


## Content

Next.js - Resend
===============
 

[Resend home page![Image 3: light logo](https://mintlify.s3.us-west-1.amazonaws.com/resend/logo-black.svg)![Image 4: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/resend/logo-white.svg)](https://resend.com/)

Search or ask...

*   [Sign In](https://resend.com/login)
*   [Get Started](https://resend.com/signup)
*   [Get Started](https://resend.com/signup)

Search...

Navigation

Node.js

Next.js

*   [Documentation](https://resend.com/docs/introduction)
*   [API Reference](https://resend.com/docs/api-reference/introduction)
*   [Knowledge Base](https://resend.com/docs/knowledge-base/introduction)

##### Documentation

*   [Introduction](https://resend.com/docs/introduction)

##### Quickstart

*   Node.js
    
    *   [Introduction](https://resend.com/docs/send-with-nodejs)
    *   [Next.js](https://resend.com/docs/send-with-nextjs)
    *   [Remix](https://resend.com/docs/send-with-remix)
    *   [Nuxt](https://resend.com/docs/send-with-nuxt)
    *   [Express](https://resend.com/docs/send-with-express)
    *   [RedwoodJS](https://resend.com/docs/send-with-redwoodjs)
    *   [Hono](https://resend.com/docs/send-with-hono)
    *   [Bun](https://resend.com/docs/send-with-bun)
    *   [Astro](https://resend.com/docs/send-with-astro)
*   Serverless
    
*   PHP
    
*   Ruby
    
*   Python
    
*   Go
    
*   Rust
    
*   Elixir
    
*   Java
    
*   SMTP
    

##### Learn

*   Emails
    
*   Domains
    
*   API Keys
    
*   Webhooks
    
*   Audiences
    
*   Broadcasts
    

##### Resources

*   [Examples](https://resend.com/docs/examples)
*   [SDKs](https://resend.com/docs/sdks)
*   [Security](https://resend.com/docs/security)
*   [Integrations](https://resend.com/docs/integrations)

Node.js

Next.js
=======

Learn how to send your first email using Next.js and the Resend Node.js SDK.

[​](https://resend.com/docs/send-with-nextjs#prerequisites)

Prerequisites
----------------------------------------------------------------------------

To get the most out of this guide, you’ll need to:

*   [Create an API key](https://resend.com/api-keys)
*   [Verify your domain](https://resend.com/domains)

[​](https://resend.com/docs/send-with-nextjs#1-install)

1\. Install
----------------------------------------------------------------------

Get the Resend Node.js SDK.

[​](https://resend.com/docs/send-with-nextjs#2-create-an-email-template)

2\. Create an email template
--------------------------------------------------------------------------------------------------------

Start by creating your email template on `components/email-template.tsx`.

components/email-template.tsx

```tsx
import * as React from 'react';

interface EmailTemplateProps {
  firstName: string;
}

export const EmailTemplate: React.FC<Readonly<EmailTemplateProps>> = ({
  firstName,
}) => (
  <div>
    <h1>Welcome, {firstName}!</h1>
  </div>
);
```

[​](https://resend.com/docs/send-with-nextjs#3-send-email-using-react)

3\. Send email using React
----------------------------------------------------------------------------------------------------

Create an API file under `pages/api/send.ts` if you’re using the [Pages Router](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) or create a route file under `app/api/send/route.ts` if you’re using the [App Router](https://nextjs.org/docs/app/building-your-application/routing/router-handlers).

Import the React email template and send an email using the `react` parameter.

[​](https://resend.com/docs/send-with-nextjs#4-try-it-yourself)

4\. Try it yourself
--------------------------------------------------------------------------------------

[Next.js Example (Pages Router) ------------------------------ See the full source code.](https://github.com/resend/resend-nextjs-pages-router-example)[Next.js Example (App Router) ---------------------------- See the full source code.](https://github.com/resend/resend-nextjs-app-router-example)

Was this page helpful?

YesNo

[Introduction](https://resend.com/docs/send-with-nodejs)[Remix](https://resend.com/docs/send-with-remix)

[twitter](https://twitter.com/resend)[github](https://github.com/resend)[discord](https://resend.com/discord)[website](https://resend.com/)

On this page

*   [Prerequisites](https://resend.com/docs/send-with-nextjs#prerequisites)
*   [1\. Install](https://resend.com/docs/send-with-nextjs#1-install)
*   [2\. Create an email template](https://resend.com/docs/send-with-nextjs#2-create-an-email-template)
*   [3\. Send email using React](https://resend.com/docs/send-with-nextjs#3-send-email-using-react)
*   [4\. Try it yourself](https://resend.com/docs/send-with-nextjs#4-try-it-yourself)

## Metadata

```json
{
  "title": "Next.js - Resend",
  "description": "Learn how to send your first email using Next.js and the Resend Node.js SDK.",
  "url": "https://resend.com/docs/send-with-nextjs",
  "content": "Next.js - Resend\n===============\n \n\n[Resend home page![Image 3: light logo](https://mintlify.s3.us-west-1.amazonaws.com/resend/logo-black.svg)![Image 4: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/resend/logo-white.svg)](https://resend.com/)\n\nSearch or ask...\n\n*   [Sign In](https://resend.com/login)\n*   [Get Started](https://resend.com/signup)\n*   [Get Started](https://resend.com/signup)\n\nSearch...\n\nNavigation\n\nNode.js\n\nNext.js\n\n*   [Documentation](https://resend.com/docs/introduction)\n*   [API Reference](https://resend.com/docs/api-reference/introduction)\n*   [Knowledge Base](https://resend.com/docs/knowledge-base/introduction)\n\n##### Documentation\n\n*   [Introduction](https://resend.com/docs/introduction)\n\n##### Quickstart\n\n*   Node.js\n    \n    *   [Introduction](https://resend.com/docs/send-with-nodejs)\n    *   [Next.js](https://resend.com/docs/send-with-nextjs)\n    *   [Remix](https://resend.com/docs/send-with-remix)\n    *   [Nuxt](https://resend.com/docs/send-with-nuxt)\n    *   [Express](https://resend.com/docs/send-with-express)\n    *   [RedwoodJS](https://resend.com/docs/send-with-redwoodjs)\n    *   [Hono](https://resend.com/docs/send-with-hono)\n    *   [Bun](https://resend.com/docs/send-with-bun)\n    *   [Astro](https://resend.com/docs/send-with-astro)\n*   Serverless\n    \n*   PHP\n    \n*   Ruby\n    \n*   Python\n    \n*   Go\n    \n*   Rust\n    \n*   Elixir\n    \n*   Java\n    \n*   SMTP\n    \n\n##### Learn\n\n*   Emails\n    \n*   Domains\n    \n*   API Keys\n    \n*   Webhooks\n    \n*   Audiences\n    \n*   Broadcasts\n    \n\n##### Resources\n\n*   [Examples](https://resend.com/docs/examples)\n*   [SDKs](https://resend.com/docs/sdks)\n*   [Security](https://resend.com/docs/security)\n*   [Integrations](https://resend.com/docs/integrations)\n\nNode.js\n\nNext.js\n=======\n\nLearn how to send your first email using Next.js and the Resend Node.js SDK.\n\n[​](https://resend.com/docs/send-with-nextjs#prerequisites)\n\nPrerequisites\n----------------------------------------------------------------------------\n\nTo get the most out of this guide, you’ll need to:\n\n*   [Create an API key](https://resend.com/api-keys)\n*   [Verify your domain](https://resend.com/domains)\n\n[​](https://resend.com/docs/send-with-nextjs#1-install)\n\n1\\. Install\n----------------------------------------------------------------------\n\nGet the Resend Node.js SDK.\n\n[​](https://resend.com/docs/send-with-nextjs#2-create-an-email-template)\n\n2\\. Create an email template\n--------------------------------------------------------------------------------------------------------\n\nStart by creating your email template on `components/email-template.tsx`.\n\ncomponents/email-template.tsx\n\n```tsx\nimport * as React from 'react';\n\ninterface EmailTemplateProps {\n  firstName: string;\n}\n\nexport const EmailTemplate: React.FC<Readonly<EmailTemplateProps>> = ({\n  firstName,\n}) => (\n  <div>\n    <h1>Welcome, {firstName}!</h1>\n  </div>\n);\n```\n\n[​](https://resend.com/docs/send-with-nextjs#3-send-email-using-react)\n\n3\\. Send email using React\n----------------------------------------------------------------------------------------------------\n\nCreate an API file under `pages/api/send.ts` if you’re using the [Pages Router](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) or create a route file under `app/api/send/route.ts` if you’re using the [App Router](https://nextjs.org/docs/app/building-your-application/routing/router-handlers).\n\nImport the React email template and send an email using the `react` parameter.\n\n[​](https://resend.com/docs/send-with-nextjs#4-try-it-yourself)\n\n4\\. Try it yourself\n--------------------------------------------------------------------------------------\n\n[Next.js Example (Pages Router) ------------------------------ See the full source code.](https://github.com/resend/resend-nextjs-pages-router-example)[Next.js Example (App Router) ---------------------------- See the full source code.](https://github.com/resend/resend-nextjs-app-router-example)\n\nWas this page helpful?\n\nYesNo\n\n[Introduction](https://resend.com/docs/send-with-nodejs)[Remix](https://resend.com/docs/send-with-remix)\n\n[twitter](https://twitter.com/resend)[github](https://github.com/resend)[discord](https://resend.com/discord)[website](https://resend.com/)\n\nOn this page\n\n*   [Prerequisites](https://resend.com/docs/send-with-nextjs#prerequisites)\n*   [1\\. Install](https://resend.com/docs/send-with-nextjs#1-install)\n*   [2\\. Create an email template](https://resend.com/docs/send-with-nextjs#2-create-an-email-template)\n*   [3\\. Send email using React](https://resend.com/docs/send-with-nextjs#3-send-email-using-react)\n*   [4\\. Try it yourself](https://resend.com/docs/send-with-nextjs#4-try-it-yourself)",
  "usage": {
    "tokens": 1151
  }
}
```
