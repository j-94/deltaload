---
title: GitHub - service-relief/gatsby-starter-service-relief: The starter for your service relief site
description: The starter for your service relief site. Contribute to service-relief/gatsby-starter-service-relief development by creating an account on GitHub.
url: https://github.com/service-relief/gatsby-starter-service-relief
timestamp: 2025-01-20T15:31:45.821Z
domain: github.com
path: service-relief_gatsby-starter-service-relief
---

# GitHub - service-relief/gatsby-starter-service-relief: The starter for your service relief site


The starter for your service relief site. Contribute to service-relief/gatsby-starter-service-relief development by creating an account on GitHub.


## Content

[![Image 38: Gatsby](https://camo.githubusercontent.com/1ecc542de363ab8c15cb03351da0793e1e20701d23e48a2f8f7bc67641ab8c0d/68747470733a2f2f7777772e6761747362796a732e6f72672f6d6f6e6f6772616d2e737667)](https://www.gatsbyjs.org/)

Service Relief Starter
----------------------

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#--service-relief-starter)

Kick off your city's relief efforts as we all learn to cope with COVID-19 with this starter powered by Gatsby, Airtable, and community efforts.

Overview
--------

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#overview)

This project is aims to make it as easy as possible to launch and manage an index of resources in your city during the COVID-19 pandemic.

Using this template you can set up a service relief site without touching any code.

**1\. Get Ready**

*   Secure a domain name
*   Create your accounts
    *   Create Github Account
    *   Create Netlify Account or Zeit Account
    *   Create Airtable Account
*   Add Github build webhook (optional)

**2\. Set up data source**

*   Set up Airtable
*   Get ready to deploy
    *   Get keys for env variables

**3\. Deploy your site**

*   Click Deploy button
*   Connect to Airtable, set City/State
*   Configure domain name

**4\. Go Live**

*   Add your site to the [directory](https://servicerelief.us/submit)
*   Spread the word

1️⃣ Get Ready
-------------

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#1%EF%B8%8F%E2%83%A3-get-ready)

### Secure a domain name

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#secure-a-domain-name)

Generally we're using the pattern `citynameservicerelief.com` -- for example:

*   `austinservicerelief.com`
*   `seattleservicerelief.com`

### Create your accounts

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#create-your-accounts)

First, you'll need to create a few accounts with free tiers from different software services.

#### 👉🏼 Create a GitHub Account

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#-create-a-github-account)

If you have a GitHub account, go ahead and [log in](https://github.com/join). If not, [sign up for an account](https://github.com/join).

#### 👉🏼 Create a Netlify Account

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#-create-a-netlify-account)

If you have a Netlify account, go ahead and [log in](https://app.netlify.com/signup). If not, [sign up for an account](https://github.com/join). (_Recommend logging in with GitHub._)

#### 👉🏼 Create an Airtable Account

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#-create-an-airtable-account)

If you have an Airtable account, go ahead and [log in](https://airtable.com/login). If not, [sign up for an account](https://airtable.com/signup).

2️⃣ Set up your data source
---------------------------

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#2%EF%B8%8F%E2%83%A3-set-up-your-data-source)

### Set up Airtable base

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#set-up-airtable-base)

To set up Airtable, you can use a base template configured specifically for a service relief site.

👉🏼 [Open the template](https://airtable.com/addBaseFromShare/shroKwQGVsips8KI2?utm_source=airtable_shared_application) and click "Add base".

[![Image 39: Workspace showing bases in Airtable](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/airtable-base-copy.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/airtable-base-copy.png)

Then you should see several tiles that correspond to individual "Bases" that Airtable has set up for you. Look for "Service Relief Template".

👉🏼 Hover over the "Service Relief Template" tile, and click the "down" caret that appears. Replace the text **"Service Relief Template"** with something like **"Service Relief Austin"**. (_Use your city name_).

[![Image 40: Rename airtable base](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/rename-airtable-base.gif)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/rename-airtable-base.gif)

### Collect keys from Airtable

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#collect-keys-from-airtable)

In order for your site to grab the data from your Airtable document, you'll need to collect **4 key values**.

Copy the following snippet into a text file.

```
AIRTABLE_API_KEY=key00000000000000
AIRTABLE_BASE_ID=app00000000000000
AIRTABLE_TABLE_NAME=tbl00000000000
AIRTABLE_EMBED_ID=shr0000000000000
```

#### Collect Airtable API key

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#collect-airtable-api-key)

> Your **API key** is secret, sort of like a key for a safe deposit box. Don't share it.

👉🏼 Visit your [Airtable account](https://airtable.com/account), and find the "API" section.

👉🏼 Click the "Generate API key" button.

[![Image 41: Button to generate API key](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/generate.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/generate.png)

👉🏼 Click on the dots to show your key, and copy it.

[![Image 42: API key to copy](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/copy-key.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/copy-key.png)

👉🏼 Paste the key in your text file as the value for `AIRTABLE_API_KEY`.

For example, if my key were `key123`, it would look like this:

```
AIRTABLE_API_KEY=key123
AIRTABLE_BASE_ID=app00000000000000
AIRTABLE_TABLE_NAME=tbl00000000000
AIRTABLE_EMBED_ID=shr0000000000000
```

#### Collect Airtable Base Id

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#collect-airtable-base-id)

👉🏼 Visit [the Airtable API page](https://airtable.com/api).

👉🏼 Click on the base you just created and renamed for your city.

[![Image 43: An Airtable base ID in the API section](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/airtable-base-id.gif)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/airtable-base-id.gif)

👉🏼 Copy the base id found halfway down the page (highlighted in the gif above).

👉🏼 Paste the id in your text file as the value for `AIRTABLE_BASE_ID`.

For example, if my key were `app123`, it would look like this:

```
AIRTABLE_API_KEY=key123
AIRTABLE_BASE_ID=app123
AIRTABLE_TABLE_NAME=tbl00000000000
AIRTABLE_EMBED_ID=shr0000000000000
```

#### Collect Airtable Table Id

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#collect-airtable-table-id)

👉🏼 Visit the Airtable base you've created for your city by visiting the [Airtable homepage](https://airtable.com/) and then clicking the tile for your base.

You can find your table id in part of the url. After `https://airtable.com/`, copy everything before the next `/`. For example, in the following URL:

`https://airtable.com/tbl6QXLCylcd2ukYr/viw0PQQWbtAfxZ8qa`

The part you need would be `tbl6QXLCylcd2ukYr`.

[![Image 44: An Airtable table ID from the url of your base](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/airtable-table-id.gif)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/airtable-table-id.gif)

👉🏼 Paste the table id in your text file as the value for `AIRTABLE_TABLE_NAME`.

For example, if my table id were `tbl123`, it would look like this:

```
AIRTABLE_API_KEY=key123
AIRTABLE_BASE_ID=app123
AIRTABLE_TABLE_NAME=tbl123
AIRTABLE_EMBED_ID=shr0000000000000
```

#### Collect Airtable Embed Id

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#collect-airtable-embed-id)

👉🏼 Click the "Grid View" at the top left of your base.

👉🏼 Select "Submit a Fundraiser". This will take you to the form view, a submission form created automatically, which corresponds to your Airtable base.

👉🏼 Click "Share Form". You should see a link. Copy everything after `https://airtable.com/`.

[![Image 45: Flow to find and copy the embed id](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/airtable-embed-id.gif)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/airtable-embed-id.gif)

👉🏼 Paste the embed id in your text file as the value for `AIRTABLE_EMBED_ID`.

For example, if my table id were `shr123`, it would look like this:

```
AIRTABLE_API_KEY=key123
AIRTABLE_BASE_ID=app123
AIRTABLE_TABLE_NAME=tbl123
AIRTABLE_EMBED_ID=shr123
```

With all four values collected, you're ready to set up the site.

3️⃣ Deploy Your Site
--------------------

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#3%EF%B8%8F%E2%83%A3-deploy-your-site)

### Deploy to Netlify

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#deploy-to-netlify)

> _Note: We plan to set up instructions for other providers eventually, as well._

👉🏼 Click the button below to begin the process of deploying to Netlify.

[![Image 46: Deploy to Netlify](https://camo.githubusercontent.com/8ef0cc1d083b2d67eb72500031401d9b52c3ecb9fb4c4405f46afd0d0aba02d6/68747470733a2f2f7777772e6e65746c6966792e636f6d2f696d672f6465706c6f792f627574746f6e2e737667)](https://app.netlify.com/start/deploy?repository=https://github.com/service-relief/gatsby-starter-service-relief)

👉🏼 Click "Connect to GitHub". (_You should already be logged in, but if you're not, log in_).

[![Image 47: Netlify deploy flow](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netlify-connect-github.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netlify-connect-github.png)

👉🏼 For the repository name, use something like `service-relief-austin` (_using your city, of course_).

👉🏼 Use the text file with your four Airtable values to populate the prompts for API key, base id, table name, and embed id.

👉🏼 In the final two prompts, specify your city and state. (_We'll use this to personalize your site a bit_).

[![Image 48: Netlify create site](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netlify-create-site.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netlify-create-site.png)

👉🏼 Click "Save and Deploy".

It will take a little while for your new site to build. You'll see the message "Site deploy in progress".

When the build is published, you'll see a live green link under the site title:

[![Image 49: Netlify open site](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netlify-open-site.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netlify-open-site.png)

### Customize the site domain

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#customize-the-site-domain)

You can set a custom domain in your Netlify site settings. From your site's main admin page on Netlify:

👉🏼 Click "Domain Settings".

[![Image 50: Netlify domain settings](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netlify-domain-settings.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netlify-domain-settings.png)

👉🏼 Under "Custom Domains", click "Add Custom Domain".

[![Image 51: Netlify domain settings](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netlify-add-domain.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netlify-add-domain.png)

From there, follow the steps to add your domain.

4️⃣ Go Live
-----------

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#4%EF%B8%8F%E2%83%A3-go-live)

### Last Steps

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#last-steps)

👉🏼 Be sure to clear out the data pre-loaded into the table you created in Airtable. Add in some organizations you know of in your city.

👉🏼 In that Airtable table, there's a column called `Approved`. In order to have any given entry show up on the deployed site, that column needs to be set to `Yes`.

👉🏼 For now, after events are added to Airtable, you need to trigger a manual deploy on Netlify.

*   From the Netlify Overview page of your site, head to the `Deploys` page.
*   Under the `Trigger deploy` dropdown on the right side of that page, select `Deploy sites`.
*   After a couple of minutes, Netlify should deploy the latest changes. Refresh your site to double check.

### Build webhook

[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#build-webhook)

If you'd like to build out the site on some cadence instead of manually publishing, you can use the Github action and a build webhook to build on an automated schedule (set to two hours, by default).

First -- get a build webhook from Netlify.

1.  Navigate to your site
2.  Settings -\> Build & Deploy
3.  Continuous Deployment -\> Add Build Hook (configure like below)

[![Image 52: Build hook with Netlify](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netilfy-build-hook.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netilfy-build-hook.png)

Next -- add this build webhook as a secret to your Github repository.

1.  First, go to your repo and go to Settings
2.  Next, go to "Secrets"
3.  Add `BUILD_WEBHOOK` with the value we grabbed from Netlify

That's it! Now every two hours your site will deploy with any new approved submissions that have been submitted and vetted. Easy peasy lemon squeezy.

[![Image 53: Github env var](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/actions-webhook.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/actions-webhook.png)

Note: If you're not interested in doing this, delete the `.github` folder in your cloned starter.

## Metadata

```json
{
  "title": "GitHub - service-relief/gatsby-starter-service-relief: The starter for your service relief site",
  "description": "The starter for your service relief site. Contribute to service-relief/gatsby-starter-service-relief development by creating an account on GitHub.",
  "url": "https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true",
  "content": "[![Image 38: Gatsby](https://camo.githubusercontent.com/1ecc542de363ab8c15cb03351da0793e1e20701d23e48a2f8f7bc67641ab8c0d/68747470733a2f2f7777772e6761747362796a732e6f72672f6d6f6e6f6772616d2e737667)](https://www.gatsbyjs.org/)\n\nService Relief Starter\n----------------------\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#--service-relief-starter)\n\nKick off your city's relief efforts as we all learn to cope with COVID-19 with this starter powered by Gatsby, Airtable, and community efforts.\n\nOverview\n--------\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#overview)\n\nThis project is aims to make it as easy as possible to launch and manage an index of resources in your city during the COVID-19 pandemic.\n\nUsing this template you can set up a service relief site without touching any code.\n\n**1\\. Get Ready**\n\n*   Secure a domain name\n*   Create your accounts\n    *   Create Github Account\n    *   Create Netlify Account or Zeit Account\n    *   Create Airtable Account\n*   Add Github build webhook (optional)\n\n**2\\. Set up data source**\n\n*   Set up Airtable\n*   Get ready to deploy\n    *   Get keys for env variables\n\n**3\\. Deploy your site**\n\n*   Click Deploy button\n*   Connect to Airtable, set City/State\n*   Configure domain name\n\n**4\\. Go Live**\n\n*   Add your site to the [directory](https://servicerelief.us/submit)\n*   Spread the word\n\n1️⃣ Get Ready\n-------------\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#1%EF%B8%8F%E2%83%A3-get-ready)\n\n### Secure a domain name\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#secure-a-domain-name)\n\nGenerally we're using the pattern `citynameservicerelief.com` -- for example:\n\n*   `austinservicerelief.com`\n*   `seattleservicerelief.com`\n\n### Create your accounts\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#create-your-accounts)\n\nFirst, you'll need to create a few accounts with free tiers from different software services.\n\n#### 👉🏼 Create a GitHub Account\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#-create-a-github-account)\n\nIf you have a GitHub account, go ahead and [log in](https://github.com/join). If not, [sign up for an account](https://github.com/join).\n\n#### 👉🏼 Create a Netlify Account\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#-create-a-netlify-account)\n\nIf you have a Netlify account, go ahead and [log in](https://app.netlify.com/signup). If not, [sign up for an account](https://github.com/join). (_Recommend logging in with GitHub._)\n\n#### 👉🏼 Create an Airtable Account\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#-create-an-airtable-account)\n\nIf you have an Airtable account, go ahead and [log in](https://airtable.com/login). If not, [sign up for an account](https://airtable.com/signup).\n\n2️⃣ Set up your data source\n---------------------------\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#2%EF%B8%8F%E2%83%A3-set-up-your-data-source)\n\n### Set up Airtable base\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#set-up-airtable-base)\n\nTo set up Airtable, you can use a base template configured specifically for a service relief site.\n\n👉🏼 [Open the template](https://airtable.com/addBaseFromShare/shroKwQGVsips8KI2?utm_source=airtable_shared_application) and click \"Add base\".\n\n[![Image 39: Workspace showing bases in Airtable](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/airtable-base-copy.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/airtable-base-copy.png)\n\nThen you should see several tiles that correspond to individual \"Bases\" that Airtable has set up for you. Look for \"Service Relief Template\".\n\n👉🏼 Hover over the \"Service Relief Template\" tile, and click the \"down\" caret that appears. Replace the text **\"Service Relief Template\"** with something like **\"Service Relief Austin\"**. (_Use your city name_).\n\n[![Image 40: Rename airtable base](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/rename-airtable-base.gif)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/rename-airtable-base.gif)\n\n### Collect keys from Airtable\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#collect-keys-from-airtable)\n\nIn order for your site to grab the data from your Airtable document, you'll need to collect **4 key values**.\n\nCopy the following snippet into a text file.\n\n```\nAIRTABLE_API_KEY=key00000000000000\nAIRTABLE_BASE_ID=app00000000000000\nAIRTABLE_TABLE_NAME=tbl00000000000\nAIRTABLE_EMBED_ID=shr0000000000000\n```\n\n#### Collect Airtable API key\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#collect-airtable-api-key)\n\n> Your **API key** is secret, sort of like a key for a safe deposit box. Don't share it.\n\n👉🏼 Visit your [Airtable account](https://airtable.com/account), and find the \"API\" section.\n\n👉🏼 Click the \"Generate API key\" button.\n\n[![Image 41: Button to generate API key](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/generate.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/generate.png)\n\n👉🏼 Click on the dots to show your key, and copy it.\n\n[![Image 42: API key to copy](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/copy-key.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/copy-key.png)\n\n👉🏼 Paste the key in your text file as the value for `AIRTABLE_API_KEY`.\n\nFor example, if my key were `key123`, it would look like this:\n\n```\nAIRTABLE_API_KEY=key123\nAIRTABLE_BASE_ID=app00000000000000\nAIRTABLE_TABLE_NAME=tbl00000000000\nAIRTABLE_EMBED_ID=shr0000000000000\n```\n\n#### Collect Airtable Base Id\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#collect-airtable-base-id)\n\n👉🏼 Visit [the Airtable API page](https://airtable.com/api).\n\n👉🏼 Click on the base you just created and renamed for your city.\n\n[![Image 43: An Airtable base ID in the API section](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/airtable-base-id.gif)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/airtable-base-id.gif)\n\n👉🏼 Copy the base id found halfway down the page (highlighted in the gif above).\n\n👉🏼 Paste the id in your text file as the value for `AIRTABLE_BASE_ID`.\n\nFor example, if my key were `app123`, it would look like this:\n\n```\nAIRTABLE_API_KEY=key123\nAIRTABLE_BASE_ID=app123\nAIRTABLE_TABLE_NAME=tbl00000000000\nAIRTABLE_EMBED_ID=shr0000000000000\n```\n\n#### Collect Airtable Table Id\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#collect-airtable-table-id)\n\n👉🏼 Visit the Airtable base you've created for your city by visiting the [Airtable homepage](https://airtable.com/) and then clicking the tile for your base.\n\nYou can find your table id in part of the url. After `https://airtable.com/`, copy everything before the next `/`. For example, in the following URL:\n\n`https://airtable.com/tbl6QXLCylcd2ukYr/viw0PQQWbtAfxZ8qa`\n\nThe part you need would be `tbl6QXLCylcd2ukYr`.\n\n[![Image 44: An Airtable table ID from the url of your base](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/airtable-table-id.gif)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/airtable-table-id.gif)\n\n👉🏼 Paste the table id in your text file as the value for `AIRTABLE_TABLE_NAME`.\n\nFor example, if my table id were `tbl123`, it would look like this:\n\n```\nAIRTABLE_API_KEY=key123\nAIRTABLE_BASE_ID=app123\nAIRTABLE_TABLE_NAME=tbl123\nAIRTABLE_EMBED_ID=shr0000000000000\n```\n\n#### Collect Airtable Embed Id\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#collect-airtable-embed-id)\n\n👉🏼 Click the \"Grid View\" at the top left of your base.\n\n👉🏼 Select \"Submit a Fundraiser\". This will take you to the form view, a submission form created automatically, which corresponds to your Airtable base.\n\n👉🏼 Click \"Share Form\". You should see a link. Copy everything after `https://airtable.com/`.\n\n[![Image 45: Flow to find and copy the embed id](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/airtable-embed-id.gif)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/airtable-embed-id.gif)\n\n👉🏼 Paste the embed id in your text file as the value for `AIRTABLE_EMBED_ID`.\n\nFor example, if my table id were `shr123`, it would look like this:\n\n```\nAIRTABLE_API_KEY=key123\nAIRTABLE_BASE_ID=app123\nAIRTABLE_TABLE_NAME=tbl123\nAIRTABLE_EMBED_ID=shr123\n```\n\nWith all four values collected, you're ready to set up the site.\n\n3️⃣ Deploy Your Site\n--------------------\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#3%EF%B8%8F%E2%83%A3-deploy-your-site)\n\n### Deploy to Netlify\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#deploy-to-netlify)\n\n> _Note: We plan to set up instructions for other providers eventually, as well._\n\n👉🏼 Click the button below to begin the process of deploying to Netlify.\n\n[![Image 46: Deploy to Netlify](https://camo.githubusercontent.com/8ef0cc1d083b2d67eb72500031401d9b52c3ecb9fb4c4405f46afd0d0aba02d6/68747470733a2f2f7777772e6e65746c6966792e636f6d2f696d672f6465706c6f792f627574746f6e2e737667)](https://app.netlify.com/start/deploy?repository=https://github.com/service-relief/gatsby-starter-service-relief)\n\n👉🏼 Click \"Connect to GitHub\". (_You should already be logged in, but if you're not, log in_).\n\n[![Image 47: Netlify deploy flow](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netlify-connect-github.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netlify-connect-github.png)\n\n👉🏼 For the repository name, use something like `service-relief-austin` (_using your city, of course_).\n\n👉🏼 Use the text file with your four Airtable values to populate the prompts for API key, base id, table name, and embed id.\n\n👉🏼 In the final two prompts, specify your city and state. (_We'll use this to personalize your site a bit_).\n\n[![Image 48: Netlify create site](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netlify-create-site.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netlify-create-site.png)\n\n👉🏼 Click \"Save and Deploy\".\n\nIt will take a little while for your new site to build. You'll see the message \"Site deploy in progress\".\n\nWhen the build is published, you'll see a live green link under the site title:\n\n[![Image 49: Netlify open site](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netlify-open-site.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netlify-open-site.png)\n\n### Customize the site domain\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#customize-the-site-domain)\n\nYou can set a custom domain in your Netlify site settings. From your site's main admin page on Netlify:\n\n👉🏼 Click \"Domain Settings\".\n\n[![Image 50: Netlify domain settings](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netlify-domain-settings.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netlify-domain-settings.png)\n\n👉🏼 Under \"Custom Domains\", click \"Add Custom Domain\".\n\n[![Image 51: Netlify domain settings](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netlify-add-domain.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netlify-add-domain.png)\n\nFrom there, follow the steps to add your domain.\n\n4️⃣ Go Live\n-----------\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#4%EF%B8%8F%E2%83%A3-go-live)\n\n### Last Steps\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#last-steps)\n\n👉🏼 Be sure to clear out the data pre-loaded into the table you created in Airtable. Add in some organizations you know of in your city.\n\n👉🏼 In that Airtable table, there's a column called `Approved`. In order to have any given entry show up on the deployed site, that column needs to be set to `Yes`.\n\n👉🏼 For now, after events are added to Airtable, you need to trigger a manual deploy on Netlify.\n\n*   From the Netlify Overview page of your site, head to the `Deploys` page.\n*   Under the `Trigger deploy` dropdown on the right side of that page, select `Deploy sites`.\n*   After a couple of minutes, Netlify should deploy the latest changes. Refresh your site to double check.\n\n### Build webhook\n\n[](https://github.com/service-relief/gatsby-starter-service-relief?screenshot=true#build-webhook)\n\nIf you'd like to build out the site on some cadence instead of manually publishing, you can use the Github action and a build webhook to build on an automated schedule (set to two hours, by default).\n\nFirst -- get a build webhook from Netlify.\n\n1.  Navigate to your site\n2.  Settings -\\> Build & Deploy\n3.  Continuous Deployment -\\> Add Build Hook (configure like below)\n\n[![Image 52: Build hook with Netlify](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/netilfy-build-hook.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/netilfy-build-hook.png)\n\nNext -- add this build webhook as a secret to your Github repository.\n\n1.  First, go to your repo and go to Settings\n2.  Next, go to \"Secrets\"\n3.  Add `BUILD_WEBHOOK` with the value we grabbed from Netlify\n\nThat's it! Now every two hours your site will deploy with any new approved submissions that have been submitted and vetted. Easy peasy lemon squeezy.\n\n[![Image 53: Github env var](https://github.com/service-relief/gatsby-starter-service-relief/raw/master/assets/images/actions-webhook.png)](https://github.com/service-relief/gatsby-starter-service-relief/blob/master/assets/images/actions-webhook.png)\n\nNote: If you're not interested in doing this, delete the `.github` folder in your cloned starter.",
  "usage": {
    "tokens": 3845
  }
}
```
