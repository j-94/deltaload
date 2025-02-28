---
title: Quickstart | Overview
description: Full documentation for Steel - the open-source headless browser API for AI agents. Here you'll find all the guides, concepts, and API reference for developing with Steel.
url: https://docs.steel.dev/overview/sessions-api/quickstart
timestamp: 2025-01-20T16:18:07.656Z
domain: docs.steel.dev
path: overview_sessions-api_quickstart
---

# Quickstart | Overview


Full documentation for Steel - the open-source headless browser API for AI agents. Here you'll find all the guides, concepts, and API reference for developing with Steel.


## Content

Get up a running with your first Steel Session in a few minutes

This guide will walk you through setting up your Steel account, running your first browser session in the cloud, and driving it using TypeScript/Puppeteer. In just a few minutes, you'll be ready to start automating with Steel.

### Initial SetupCopied!

#### 1\. Create a Steel Account

1.  Sign up for a free account at [steel.dev](http://app.steel.dev/)
    
2.  The free plan includes 100 browser hours to get you started
    
3.  No credit card required
    

#### 2\. Get Your API Key

1.  After signing up, navigate to [Settings \> API Keys](https://app.steel.dev/settings/api-keys)
    
2.  Create an API key and save it somewhere safe. You will not be able to generate the same key again.
    

#### 3\. Set Up Environment Variables

1.  Create a `.env` file in your project root (if you don't have one)
    
2.  Add your Steel API key:
    

Make sure to add `.env` to your `.gitignore` file to keep your key secure

### Install the SDKCopied!

Now install the Steel Node SDK:

```
// For node.js
npm install steel-sdk
```

### Create Your First SessionCopied!

Let's create a simple script that launches a session and visits a webpage. Choose your preferred language:

Node.js

```
import Steel from 'steel-sdk';
import dotenv from 'dotenv';

dotenv.config();

const client = new Steel({
  steelAPIKey: process.env.STEEL_API_KEY,
});

async function main() {
  // Create a session
  const session = await client.sessions.create();
  console.log('Session created:', session.id);
  
  // Your session is now ready to use!
  // Keep this ID handy - you'll need it to connect with automation tools

  // When done, release the session
  await client.sessions.release(session.id);
  console.log('Session released');
}

main().catch(console.error);
```

### Connecting to Your SessionCopied!

Now that you have a session, you can connect to it using your preferred automation tool.

Here are some quick ways for each supported tool:

Node.js / Puppeteer

```
import puppeteer from 'puppeteer';

const browser = await puppeteer.connect({
    browserWSEndpoint: `wss://connect.steel.dev?apiKey=${process.env.STEEL_API_KEY}&sessionId=${session.id}`,
});

const page = await browser.newPage();
await page.goto('https://example.com');
```

### Session FeaturesCopied!

Want to do more with your session? Here are some common options you can add when creating:

```
const session = await client.sessions.create({
    useProxy: true,           // Use Steel's residential proxy network
    solveCaptcha: true,       // Enable automatic CAPTCHA solving
    sessionTimeout: 1800000,  // Set 30-minute timeout (default is 15 minutes)
    userAgent: 'custom-ua'    // Set a custom user agent
});
```

You've now created your first Steel session and learned the basics of session management. With these fundamentals, you can start building more complex automations using Steel's cloud browser infrastructure.

Need help? Join our [Discord community](https://discord.gg/gPpvhNvc5R) or check out our full [API Reference](https://docs.steel.dev/api-reference).

## Metadata

```json
{
  "title": "Quickstart | Overview",
  "description": "Full documentation for Steel - the open-source headless browser API for AI agents. Here you'll find all the guides, concepts, and API reference for developing with Steel.",
  "url": "https://docs.steel.dev/overview/sessions-api/quickstart",
  "content": "Get up a running with your first Steel Session in a few minutes\n\nThis guide will walk you through setting up your Steel account, running your first browser session in the cloud, and driving it using TypeScript/Puppeteer. In just a few minutes, you'll be ready to start automating with Steel.\n\n### Initial SetupCopied!\n\n#### 1\\. Create a Steel Account\n\n1.  Sign up for a free account at [steel.dev](http://app.steel.dev/)\n    \n2.  The free plan includes 100 browser hours to get you started\n    \n3.  No credit card required\n    \n\n#### 2\\. Get Your API Key\n\n1.  After signing up, navigate to [Settings \\> API Keys](https://app.steel.dev/settings/api-keys)\n    \n2.  Create an API key and save it somewhere safe. You will not be able to generate the same key again.\n    \n\n#### 3\\. Set Up Environment Variables\n\n1.  Create a `.env` file in your project root (if you don't have one)\n    \n2.  Add your Steel API key:\n    \n\nMake sure to add `.env` to your `.gitignore` file to keep your key secure\n\n### Install the SDKCopied!\n\nNow install the Steel Node SDK:\n\n```\n// For node.js\nnpm install steel-sdk\n```\n\n### Create Your First SessionCopied!\n\nLet's create a simple script that launches a session and visits a webpage. Choose your preferred language:\n\nNode.js\n\n```\nimport Steel from 'steel-sdk';\nimport dotenv from 'dotenv';\n\ndotenv.config();\n\nconst client = new Steel({\n  steelAPIKey: process.env.STEEL_API_KEY,\n});\n\nasync function main() {\n  // Create a session\n  const session = await client.sessions.create();\n  console.log('Session created:', session.id);\n  \n  // Your session is now ready to use!\n  // Keep this ID handy - you'll need it to connect with automation tools\n\n  // When done, release the session\n  await client.sessions.release(session.id);\n  console.log('Session released');\n}\n\nmain().catch(console.error);\n```\n\n### Connecting to Your SessionCopied!\n\nNow that you have a session, you can connect to it using your preferred automation tool.\n\nHere are some quick ways for each supported tool:\n\nNode.js / Puppeteer\n\n```\nimport puppeteer from 'puppeteer';\n\nconst browser = await puppeteer.connect({\n    browserWSEndpoint: `wss://connect.steel.dev?apiKey=${process.env.STEEL_API_KEY}&sessionId=${session.id}`,\n});\n\nconst page = await browser.newPage();\nawait page.goto('https://example.com');\n```\n\n### Session FeaturesCopied!\n\nWant to do more with your session? Here are some common options you can add when creating:\n\n```\nconst session = await client.sessions.create({\n    useProxy: true,           // Use Steel's residential proxy network\n    solveCaptcha: true,       // Enable automatic CAPTCHA solving\n    sessionTimeout: 1800000,  // Set 30-minute timeout (default is 15 minutes)\n    userAgent: 'custom-ua'    // Set a custom user agent\n});\n```\n\nYou've now created your first Steel session and learned the basics of session management. With these fundamentals, you can start building more complex automations using Steel's cloud browser infrastructure.\n\nNeed help? Join our [Discord community](https://discord.gg/gPpvhNvc5R) or check out our full [API Reference](https://docs.steel.dev/api-reference).",
  "usage": {
    "tokens": 728
  }
}
```
