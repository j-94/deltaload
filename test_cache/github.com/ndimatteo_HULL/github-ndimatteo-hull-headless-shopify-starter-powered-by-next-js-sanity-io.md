---
title: GitHub - ndimatteo/HULL: 💀 Headless Shopify Starter – powered by Next.js + Sanity.io
description: 💀 Headless Shopify Starter – powered by Next.js + Sanity.io - ndimatteo/HULL
url: https://github.com/ndimatteo/HULL
timestamp: 2025-01-20T15:32:08.036Z
domain: github.com
path: ndimatteo_HULL
---

# GitHub - ndimatteo/HULL: 💀 Headless Shopify Starter – powered by Next.js + Sanity.io


💀 Headless Shopify Starter – powered by Next.js + Sanity.io - ndimatteo/HULL


## Content

[![Image 8](https://github.com/ndimatteo/HULL/raw/main/public/HULL-Logo.svg)](https://github.com/ndimatteo/HULL/blob/main/public/HULL-Logo.svg)

**Headless Shopify starter built on [Next.js](https://nextjs.org/)** 🤘  
**Headless CMS powered by [Sanity.io](https://sanity.io/)** ⚡

[![Image 9](https://camo.githubusercontent.com/dce88759e61cfbee5302a692f3cbb14475cacf563fc32e9d0be0e5fb9ee8596d/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d266d6573736167653d5669657725323044656d6f267374796c653d666f722d7468652d626164676526636f6c6f723d626c61636b266c6f676f3d76657263656c)](https://hull.dev/)  
[![Image 10](https://camo.githubusercontent.com/49cd300d64232508ef8b92f4f5d529570a359db066b0e0e9582482f1622ad94e/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d53616e697479266d6573736167653d43726561746525323050726f6a656374267374796c653d666f722d7468652d626164676526636f6c6f723d313536646666266c6162656c436f6c6f723d626c61636b)](https://www.sanity.io/create?template=ndimatteo/HULL)

[Features](https://github.com/ndimatteo/HULL?screenshot=true#-features) • [Tours](https://github.com/ndimatteo/HULL?screenshot=true#-tours) • [Set Up](https://github.com/ndimatteo/HULL?screenshot=true#-automatic-set-up) • [Spin Up](https://github.com/ndimatteo/HULL?screenshot=true#-spin-up) • [Deployment](https://github.com/ndimatteo/HULL?screenshot=true#-deployment) • [Extras](https://github.com/ndimatteo/HULL?screenshot=true#-extrastips)

✨ Features
----------

[](https://github.com/ndimatteo/HULL?screenshot=true#-features)

*   Utility-first CSS with [Tailwind CSS](https://tailwindcss.com/)
*   Animations powered by [Framer Motion](https://www.framer.com/motion/)
*   Cart powered by [Shopify Buy SDK](https://www.npmjs.com/package/shopify-buy)
*   Real-time inventory check for products using [SWR](https://swr.vercel.app/)
*   Customizable Filtering & Sorting for product collections
*   Klaviyo waitlist form for out-of-stock products
*   Klaviyo newsletter form with opt-in field
*   Dynamic Page Routes for custom page creation
*   Automatic `Sitemap.xml` generation
*   Automatic `robots.txt` generation
*   Automatic 301 Redirects from Sanity
*   Live Preview content directly from Sanity
*   Modern Image component using Sanity's Hotspot, Crop, and automatic WEBP format
*   Modular page content for all pages, including dynamic grid layouts
*   Customizable Promotion Banner
*   Customizable Cookie Notice
*   Accessibility features:
    *   ARIA Landmark Roles
    *   Default focus states preserved for keyboard navigation
    *   Correctly trap focus for drawers with [focus-trap-react](https://www.npmjs.com/package/focus-trap-react)
    *   Roving tabindex for radio buttons
    *   Input-based quantity counters
    *   Required `alt` text for all images
    *   "Skip to Content" link
*   SEO features:
    *   Page-level SEO/Share settings with previews
    *   Fallback Global SEO/Share settings
    *   Automatic JSON-LD Schema markup for products

### Shopify Integration Features

[](https://github.com/ndimatteo/HULL?screenshot=true#shopify-integration-features)

*   Automatically syncs products from Shopify into Sanity
*   Custom action to sync product cart thumbnails back to Shopify from Sanity
*   Tracks product status _(draft/published)_ from Shopify to help control visibility while editing
*   Deleted products and variants are preserved and flagged in Sanity
*   Updates the URL on variant changes while keeping a clean history stack
*   Vanity shop URL masking
*   Global Cart with access to all variant data for line items
*   Supports Single Variant products out of the box
*   Product photo galleries with variant granularity
*   Dynamic `/shop` collection page
*   Custom collection pages
*   Ability to surface a variant option on product cards

🎧 Tours
--------

[](https://github.com/ndimatteo/HULL?screenshot=true#-tours)

Still not sold? Here's some videos to get you psyched:

**Famous 5-Minute Setup™ - `Coming Soon`**  
_From sync to sale, watch me spin up a fresh storefront in under 5 minutes!_

**Explore the file Structure - `Coming Soon`**  
_In-depth look at the file structure, naming conventions, and logic under the hood_

**Setting up your first Product - `Coming Soon`**  
_Explore the Product settings within Sanity and how to properly setup PDP pages and PLP cards_

**Connecting to Klaviyo and testing your Forms - `Coming Soon`**  
_Learn how to quickly connect Klaviyo to utilize product waitlist and newsletter forms_

**Setup your first Vercel deployment - `Coming Soon`**  
_Using the Sanity Vercel Deploy plugin, see how easy it is to empower your clients to trigger deploys_

🔥 Automatic Set Up
-------------------

[](https://github.com/ndimatteo/HULL?screenshot=true#-automatic-set-up)

Quickly [deploy as a Sanity Starter](https://www.sanity.io/create?template=ndimatteo/HULL) on [Vercel](https://vercel.com/) with a pre-populated store! Once deployed, simply follow step 2 and 3 below to connect your Shopify store.

> **Warning**  
> You should delete the demo products once you connect your own Shopify account. Demo products will not function properly as they are not part of _your Shopify store_. Additionally, any existing products in your Shopify store will not automatically sync into Sanity. To trigger a sync, you must make a change to your existing product(s) in Shopify first.

💀 Manual Set Up
----------------

[](https://github.com/ndimatteo/HULL?screenshot=true#-manual-set-up)

Clone this repository from your GitHub account with the [Use this template](https://github.com/ndimatteo/HULL/generate) button

### 1) Sanity

[](https://github.com/ndimatteo/HULL?screenshot=true#1-sanity)

1.  **Initialize and build the Sanity Studio**
    *   Make sure you have the [Sanity CLI](https://www.sanity.io/docs/getting-started-with-sanity-cli) installed globally first
    *   `yarn && sanity init` in the `/studio` folder
    *   During Sanity's initalization it will warn you that the Sanity Studio is already configured. Type `Y` and hit `enter` to reconfigure it to your own project
    *   When it asks you what dataset configuration to use, go with the `default`
2.  **Add CORS Origins to Sanity project**
    *   Visit [manage.sanity.io](https://manage.sanity.io/) and go to \[your-project\] \> API \> "CORS origins"
    *   Add your Studio URLs **_with_** credentials: `http://localhost:3333` and `[subdomain].sanity.studio`
    *   Add your front-end URLs **_without_** credentials: `http://localhost:3000` and `https://[subdomain].vercel.app`

### 2) Shopify Storefront Access

[](https://github.com/ndimatteo/HULL?screenshot=true#2-shopify-storefront-access)

1.  **Allow custom app development in Shopify**
    *   Go to "Settings" _(bottom left)_ \> "Apps and sales channels" \> "Develop apps" _(top right)_
    *   click "Allow custom app development"
2.  **Create a custom app in Shopify**
    *   Go to "Settings" _(bottom left)_ \> "Apps and sales channels" \> "Develop apps" _(top right)_
    *   click "Create an app"
    *   Give this a relevant App name, I prefer: "Headless Storefront", so it's clear what it's being used for
    *   Use your dev account as the App developer to know when there are issues
3.  **Configure Admin API scopes**
    *   Configuration \> Admin API integration \> "Configure"
    *   Check the following boxes for the "Products" scope: `write_products` and `read_products`
4.  **Configure Storefront API scopes**
    *   Configuration \> Storefront API integration \> "Configure"
    *   Check the following boxes for the "Products" scope: `unauthenticated_read_product_listings` and `unauthenticated_read_product_inventory`
    *   Check the following boxes for the "Checkout" scope: `unauthenticated_write_checkouts` and `unauthenticated_read_checkouts`
5.  **Install the App**

### 3) Shopify Webhooks

[](https://github.com/ndimatteo/HULL?screenshot=true#3-shopify-webhooks)

1.  Go to "Settings" _(bottom left)_ -\> "Notifications" -\> "Webhooks" _(very bottom)_
2.  add the following webhooks with the (Latest) stable API version:
    *   Product creation - `[live-domain]/api/shopify/product-update`
    *   Product update - `[live-domain]/api/shopify/product-update`
    *   Product deletion - `[live-domain]/api/shopify/product-delete`
        
        > **Warning**  
        > You have to use a real, live domain name (not localhost!). Be sure to use your Vercel project URL during development, and then switch to the production domain once live. You may not know your Vercel project URL until you deploy, feel free to enter something temporary, but make sure to update this once deployed!
        

### 4) NextJS

[](https://github.com/ndimatteo/HULL?screenshot=true#4-nextjs)

1.  `yarn` in the project root folder on local
2.  Create an `.env.local` file in the project folder, and add the following variables:

```
NEXT_PUBLIC_SANITY_PROJECT_DATASET=production
NEXT_PUBLIC_SANITY_PROJECT_ID=XXXXXX
SANITY_API_TOKEN=XXXXXX
SANITY_STUDIO_PREVIEW_SECRET=XXXXXX

NEXT_PUBLIC_SHOPIFY_STORE_ID=XXXXXX
NEXT_PUBLIC_SHOPIFY_STOREFRONT_API_TOKEN=XXXXXX
SHOPIFY_ADMIN_API_TOKEN=XXXXXX
SHOPIFY_WEBHOOK_INTEGRITY=XXXXXX

// Needed for Klaviyo forms:
KLAVIYO_API_KEY=XXXXXX

// Needed for Mailchimp forms:
MAILCHIMP_API_KEY=XXXXXX-usX
MAILCHIMP_SERVER=usX

// Needed for SendGrid forms:
SENDGRID_API_KEY=XXXXXX
```

3.  Update all the `XXXXXX` values, here's where to find each:

*   `NEXT_PUBLIC_SANITY_PROJECT_ID` - You can grab this after you've initalized Sanity, either from the `studio/sanity.json` file, or from your Sanity Manage dashboard
*   `SANITY_API_TOKEN` - Generate an API token for your Sanity project. Access your project from the Sanity Manage dashboard, and navigate to: "Settings" -\> "API" -\> "Add New Token" button. Make sure you give `read + write` access!
*   `SANITY_STUDIO_PREVIEW_SECRET` - A unique string of your choice. This is used to confirm the authenticity of "preview mode" requests from the Sanity Studio
*   `NEXT_PUBLIC_SHOPIFY_STORE_ID` - This is your Shopify store ID, it's the subdomain behind `.myshopify.com`
*   `NEXT_PUBLIC_SHOPIFY_STOREFRONT_API_TOKEN` - Copy the Storefront API access token from "Apps" -\> "Develop apps" -\> \[your\_custom\_app\] -\> "API credentials".
*   `SHOPIFY_ADMIN_API_TOKEN` - Copy the Admin API access token from "Apps" -\> "Develop apps" -\> \[your\_custom\_app\] -\> "API credentials". (**Note: you’ll only be able to reveal your Admin API token once.**)
*   `SHOPIFY_WEBHOOK_INTEGRITY` - Copy the Integrity hash from "Settings" -\> "Notifications" -\> "Webhooks" _(very bottom of page)_
*   `KLAVIYO_API_KEY` - Create a Private API Key from your Klaviyo Account "Settings" -\> "API Keys"
*   `MAILCHIMP_API_KEY` - Create an API key from "Account -\> "Extras" -\> API Keys
*   `MAILCHIMP_SERVER` - This is the server your account is from. It's in the URL when logged in and at the end of your API Key
*   `SENDGRID_API_KEY` - Create an API key from "Settings" -\> "API Keys" with "Restricted Access" to only "Mail Send"

4.  Create an `.env.production` and `.env.development` file in the `/studio` folder, and add the following (using the same value as above):

```
SANITY_STUDIO_PREVIEW_SECRET=XXXXXX
```

### 5) Shopify Store Theme

[](https://github.com/ndimatteo/HULL?screenshot=true#5-shopify-store-theme)

Since we're serving our store through a headless environment, we don't want visitors accessing our unused shopify theme. The domain for this is visible during checkout, and is publicly accessible. To silence it, replace your current theme's `theme.liquid` file with the one from this repo, and replace `YOUR_STOREFRONT_DOMAIN_NO_PROTOCOL` with your actual frontsite domain URL **(do not include protocol or trailing slash)**

This will essentially "pass-through" URLs accessed at your Shopify Store to your true headless storefront _(ie. `shop.hull.dev/products` -\> `hull.dev/products`)_

⚡ Spin Up
---------

[](https://github.com/ndimatteo/HULL?screenshot=true#-spin-up)

### Next (Front End)

[](https://github.com/ndimatteo/HULL?screenshot=true#next-front-end)

`yarn dev` in the project folder to start the front end locally

*   Your front end should be running on [http://localhost:3000](http://localhost:3000/)

### Sanity (Back End)

[](https://github.com/ndimatteo/HULL?screenshot=true#sanity-back-end)

`yarn dev` in the `/studio` folder to start the studio locally

*   Your Sanity Studio should be running on [http://localhost:3333](http://localhost:3333/)
    
    > **Warning**  
    > If you did not manually set up your project, the `projectId` in `/studio/sanity.json` will still be set to the HULL demo project. Make sure to update this before starting the studio, otherwise you will be denied access when trying to access your studio.
    

🚀 Deployment
-------------

[](https://github.com/ndimatteo/HULL?screenshot=true#-deployment)

### Vercel

[](https://github.com/ndimatteo/HULL?screenshot=true#vercel)

This is setup to work seamlessly with Vercel, which I highly recommend as your hosting provider of choice. Simply follow the on-screen instructions to setup your new project, and be sure to **add the same `.env.local` variables to your Vercel Project**

### Sanity

[](https://github.com/ndimatteo/HULL?screenshot=true#sanity)

This is an easy one, you can simply run `sanity deploy` from the `/studio` folder in your project. Select a subdomain you want; your Studio is now accessible from the web. This is where I'll invite the client to manage the project so they can both add billing info and begin editing content.

### Client Updates

[](https://github.com/ndimatteo/HULL?screenshot=true#client-updates)

Once you hand off to the client you'll want to give them the ability to generate builds when they make updates within the Sanity Studio. The easiest way to do this is through my [Vercel Deploy plugin](https://github.com/ndimatteo/sanity-plugin-vercel-deploy).

🤘 Extras/Tips
--------------

[](https://github.com/ndimatteo/HULL?screenshot=true#-extrastips)

**This looks like a theme... How can I use this like a starter?**While this starter is relatively opinionated, the goal was three-fold:

1.  Use high-quality packages that don't get in the way
2.  Solve common UX problems and complex logic so you can focus on the fun stuff
3.  Create a more approachable starter for anyone looking to build production-ready headless Shopify experiences

That being said, I understand this means a lot of what's included is **very opinionated**. However, you'll find that at it's core the structure and naming conventions lend itself to really making it your own.

I've purposefully used extracted component classes, not only for cleaner file structure, but also so you can easily work in your own styles exclusively within the styles folder. Feel free to extend or outright remove the applied styles for all of the components!

**What's up with the CSS? Why are you using @apply?**Previously, `@apply` was used to extract component classes away from your javascript files. However, since then Tailwind has been opposed to this approach. In the coming releases HULL will move away from this approach in favor of applying styles directly to the components so functionality and styling is done in one place.

You can read more about Tailwind's stance on `@apply` here: [https://tailwindcss.com/docs/reusing-styles#avoiding-premature-abstraction](https://tailwindcss.com/docs/reusing-styles#avoiding-premature-abstraction)

**Can I use this for non-Shopify projects?**Absolutely! This starter was actually born out of a non-shopify starter I had been using for my own client projects.

I made a `marketing-starter` branch that is **HULL without all the Shopify logic**! The fastest way to get started is simply cloning that branch locally into an empty project folder:

```
git clone -b marketing-starter --single-branch git@github.com:ndimatteo/HULL.git .
```

You can read the [setup instructions](https://github.com/ndimatteo/HULL/tree/marketing-starter#-set-up) for this version from the branch's README.

**Error: Failed to communicate with the Sanity API**If you get this error in your CLI, you need to logout and log back in again. Simply do `sanity logout` and then `sanity login` to fix.

**Access your "product\_sync" metafields in Shopify without using a plugin**Simply navigate directly to: `https://[store_id].myshopify.com/admin/bulk?resource_name=Product&edit=metafields.sanity.product_sync`

_(making sure to replace `[store_id]` with your Shopify Store ID)_

**How do I properly hand-off a Vercel project to the client?**While not as easy as Netlify, what I prefer to do is:

1.  Have the client create their own [Vercel account](https://vercel.com/signup)
2.  At the time of writing, Github connections can only be connected to one Vercel account at a time, so have the client [create a Github account](https://github.com/join) if they don't already have one, and transfer the project repo to them
3.  Delete the dev project from your own Vercel account (this is so the client can utilize the project name and domain you were using during dev)
4.  You or the client can now connect their newly transferred Github repo to their own Vercel account!

**How can I see the bundle size of my website?**Simply run `yarn analyze` from the project folder. This will run a build of your site and automatically open the [Webpack Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer) visuals for your site's build files.

💯 Shoutouts
------------

[](https://github.com/ndimatteo/HULL?screenshot=true#-shoutouts)

Huge ups to the following talented and rad folks who helped in countless ways. Thank you for all the support, code contributions, and discussions.

### Developers

[](https://github.com/ndimatteo/HULL?screenshot=true#developers)

*   🔥 [@tuckercs](https://github.com/tuckercs)
*   🍝 [@iamkevingreen](https://github.com/iamkevingreen)
*   🧈 [@mikehwagz](https://github.com/mikehwagz)
*   😎 [@dictions](https://github.com/dictions)

### Designers

[](https://github.com/ndimatteo/HULL?screenshot=true#designers)

*   [@thecollectedworks](https://www.instagram.com/thecollectedworks/)
*   [@joyntnotjoint](https://www.instagram.com/joyntnotjoint/)

🤝 License
----------

[](https://github.com/ndimatteo/HULL?screenshot=true#-license)

### [MIT](https://github.com/ndimatteo/HULL/blob/main/LICENSE)

[](https://github.com/ndimatteo/HULL?screenshot=true#mit)

> [nickdimatteo.com](https://nickdimatteo.com/)  ·  Github [@ndimatteo](https://github.com/ndimatteo)  ·  Instagram [@ndimatteo](https://instagram.com/ndimatteo)

## Metadata

```json
{
  "title": "GitHub - ndimatteo/HULL: 💀 Headless Shopify Starter – powered by Next.js + Sanity.io",
  "description": "💀 Headless Shopify Starter – powered by Next.js + Sanity.io - ndimatteo/HULL",
  "url": "https://github.com/ndimatteo/HULL?screenshot=true",
  "content": "[![Image 8](https://github.com/ndimatteo/HULL/raw/main/public/HULL-Logo.svg)](https://github.com/ndimatteo/HULL/blob/main/public/HULL-Logo.svg)\n\n**Headless Shopify starter built on [Next.js](https://nextjs.org/)** 🤘  \n**Headless CMS powered by [Sanity.io](https://sanity.io/)** ⚡\n\n[![Image 9](https://camo.githubusercontent.com/dce88759e61cfbee5302a692f3cbb14475cacf563fc32e9d0be0e5fb9ee8596d/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d266d6573736167653d5669657725323044656d6f267374796c653d666f722d7468652d626164676526636f6c6f723d626c61636b266c6f676f3d76657263656c)](https://hull.dev/)  \n[![Image 10](https://camo.githubusercontent.com/49cd300d64232508ef8b92f4f5d529570a359db066b0e0e9582482f1622ad94e/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6c6162656c3d53616e697479266d6573736167653d43726561746525323050726f6a656374267374796c653d666f722d7468652d626164676526636f6c6f723d313536646666266c6162656c436f6c6f723d626c61636b)](https://www.sanity.io/create?template=ndimatteo/HULL)\n\n[Features](https://github.com/ndimatteo/HULL?screenshot=true#-features) • [Tours](https://github.com/ndimatteo/HULL?screenshot=true#-tours) • [Set Up](https://github.com/ndimatteo/HULL?screenshot=true#-automatic-set-up) • [Spin Up](https://github.com/ndimatteo/HULL?screenshot=true#-spin-up) • [Deployment](https://github.com/ndimatteo/HULL?screenshot=true#-deployment) • [Extras](https://github.com/ndimatteo/HULL?screenshot=true#-extrastips)\n\n✨ Features\n----------\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#-features)\n\n*   Utility-first CSS with [Tailwind CSS](https://tailwindcss.com/)\n*   Animations powered by [Framer Motion](https://www.framer.com/motion/)\n*   Cart powered by [Shopify Buy SDK](https://www.npmjs.com/package/shopify-buy)\n*   Real-time inventory check for products using [SWR](https://swr.vercel.app/)\n*   Customizable Filtering & Sorting for product collections\n*   Klaviyo waitlist form for out-of-stock products\n*   Klaviyo newsletter form with opt-in field\n*   Dynamic Page Routes for custom page creation\n*   Automatic `Sitemap.xml` generation\n*   Automatic `robots.txt` generation\n*   Automatic 301 Redirects from Sanity\n*   Live Preview content directly from Sanity\n*   Modern Image component using Sanity's Hotspot, Crop, and automatic WEBP format\n*   Modular page content for all pages, including dynamic grid layouts\n*   Customizable Promotion Banner\n*   Customizable Cookie Notice\n*   Accessibility features:\n    *   ARIA Landmark Roles\n    *   Default focus states preserved for keyboard navigation\n    *   Correctly trap focus for drawers with [focus-trap-react](https://www.npmjs.com/package/focus-trap-react)\n    *   Roving tabindex for radio buttons\n    *   Input-based quantity counters\n    *   Required `alt` text for all images\n    *   \"Skip to Content\" link\n*   SEO features:\n    *   Page-level SEO/Share settings with previews\n    *   Fallback Global SEO/Share settings\n    *   Automatic JSON-LD Schema markup for products\n\n### Shopify Integration Features\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#shopify-integration-features)\n\n*   Automatically syncs products from Shopify into Sanity\n*   Custom action to sync product cart thumbnails back to Shopify from Sanity\n*   Tracks product status _(draft/published)_ from Shopify to help control visibility while editing\n*   Deleted products and variants are preserved and flagged in Sanity\n*   Updates the URL on variant changes while keeping a clean history stack\n*   Vanity shop URL masking\n*   Global Cart with access to all variant data for line items\n*   Supports Single Variant products out of the box\n*   Product photo galleries with variant granularity\n*   Dynamic `/shop` collection page\n*   Custom collection pages\n*   Ability to surface a variant option on product cards\n\n🎧 Tours\n--------\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#-tours)\n\nStill not sold? Here's some videos to get you psyched:\n\n**Famous 5-Minute Setup™ - `Coming Soon`**  \n_From sync to sale, watch me spin up a fresh storefront in under 5 minutes!_\n\n**Explore the file Structure - `Coming Soon`**  \n_In-depth look at the file structure, naming conventions, and logic under the hood_\n\n**Setting up your first Product - `Coming Soon`**  \n_Explore the Product settings within Sanity and how to properly setup PDP pages and PLP cards_\n\n**Connecting to Klaviyo and testing your Forms - `Coming Soon`**  \n_Learn how to quickly connect Klaviyo to utilize product waitlist and newsletter forms_\n\n**Setup your first Vercel deployment - `Coming Soon`**  \n_Using the Sanity Vercel Deploy plugin, see how easy it is to empower your clients to trigger deploys_\n\n🔥 Automatic Set Up\n-------------------\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#-automatic-set-up)\n\nQuickly [deploy as a Sanity Starter](https://www.sanity.io/create?template=ndimatteo/HULL) on [Vercel](https://vercel.com/) with a pre-populated store! Once deployed, simply follow step 2 and 3 below to connect your Shopify store.\n\n> **Warning**  \n> You should delete the demo products once you connect your own Shopify account. Demo products will not function properly as they are not part of _your Shopify store_. Additionally, any existing products in your Shopify store will not automatically sync into Sanity. To trigger a sync, you must make a change to your existing product(s) in Shopify first.\n\n💀 Manual Set Up\n----------------\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#-manual-set-up)\n\nClone this repository from your GitHub account with the [Use this template](https://github.com/ndimatteo/HULL/generate) button\n\n### 1) Sanity\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#1-sanity)\n\n1.  **Initialize and build the Sanity Studio**\n    *   Make sure you have the [Sanity CLI](https://www.sanity.io/docs/getting-started-with-sanity-cli) installed globally first\n    *   `yarn && sanity init` in the `/studio` folder\n    *   During Sanity's initalization it will warn you that the Sanity Studio is already configured. Type `Y` and hit `enter` to reconfigure it to your own project\n    *   When it asks you what dataset configuration to use, go with the `default`\n2.  **Add CORS Origins to Sanity project**\n    *   Visit [manage.sanity.io](https://manage.sanity.io/) and go to \\[your-project\\] \\> API \\> \"CORS origins\"\n    *   Add your Studio URLs **_with_** credentials: `http://localhost:3333` and `[subdomain].sanity.studio`\n    *   Add your front-end URLs **_without_** credentials: `http://localhost:3000` and `https://[subdomain].vercel.app`\n\n### 2) Shopify Storefront Access\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#2-shopify-storefront-access)\n\n1.  **Allow custom app development in Shopify**\n    *   Go to \"Settings\" _(bottom left)_ \\> \"Apps and sales channels\" \\> \"Develop apps\" _(top right)_\n    *   click \"Allow custom app development\"\n2.  **Create a custom app in Shopify**\n    *   Go to \"Settings\" _(bottom left)_ \\> \"Apps and sales channels\" \\> \"Develop apps\" _(top right)_\n    *   click \"Create an app\"\n    *   Give this a relevant App name, I prefer: \"Headless Storefront\", so it's clear what it's being used for\n    *   Use your dev account as the App developer to know when there are issues\n3.  **Configure Admin API scopes**\n    *   Configuration \\> Admin API integration \\> \"Configure\"\n    *   Check the following boxes for the \"Products\" scope: `write_products` and `read_products`\n4.  **Configure Storefront API scopes**\n    *   Configuration \\> Storefront API integration \\> \"Configure\"\n    *   Check the following boxes for the \"Products\" scope: `unauthenticated_read_product_listings` and `unauthenticated_read_product_inventory`\n    *   Check the following boxes for the \"Checkout\" scope: `unauthenticated_write_checkouts` and `unauthenticated_read_checkouts`\n5.  **Install the App**\n\n### 3) Shopify Webhooks\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#3-shopify-webhooks)\n\n1.  Go to \"Settings\" _(bottom left)_ -\\> \"Notifications\" -\\> \"Webhooks\" _(very bottom)_\n2.  add the following webhooks with the (Latest) stable API version:\n    *   Product creation - `[live-domain]/api/shopify/product-update`\n    *   Product update - `[live-domain]/api/shopify/product-update`\n    *   Product deletion - `[live-domain]/api/shopify/product-delete`\n        \n        > **Warning**  \n        > You have to use a real, live domain name (not localhost!). Be sure to use your Vercel project URL during development, and then switch to the production domain once live. You may not know your Vercel project URL until you deploy, feel free to enter something temporary, but make sure to update this once deployed!\n        \n\n### 4) NextJS\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#4-nextjs)\n\n1.  `yarn` in the project root folder on local\n2.  Create an `.env.local` file in the project folder, and add the following variables:\n\n```\nNEXT_PUBLIC_SANITY_PROJECT_DATASET=production\nNEXT_PUBLIC_SANITY_PROJECT_ID=XXXXXX\nSANITY_API_TOKEN=XXXXXX\nSANITY_STUDIO_PREVIEW_SECRET=XXXXXX\n\nNEXT_PUBLIC_SHOPIFY_STORE_ID=XXXXXX\nNEXT_PUBLIC_SHOPIFY_STOREFRONT_API_TOKEN=XXXXXX\nSHOPIFY_ADMIN_API_TOKEN=XXXXXX\nSHOPIFY_WEBHOOK_INTEGRITY=XXXXXX\n\n// Needed for Klaviyo forms:\nKLAVIYO_API_KEY=XXXXXX\n\n// Needed for Mailchimp forms:\nMAILCHIMP_API_KEY=XXXXXX-usX\nMAILCHIMP_SERVER=usX\n\n// Needed for SendGrid forms:\nSENDGRID_API_KEY=XXXXXX\n```\n\n3.  Update all the `XXXXXX` values, here's where to find each:\n\n*   `NEXT_PUBLIC_SANITY_PROJECT_ID` - You can grab this after you've initalized Sanity, either from the `studio/sanity.json` file, or from your Sanity Manage dashboard\n*   `SANITY_API_TOKEN` - Generate an API token for your Sanity project. Access your project from the Sanity Manage dashboard, and navigate to: \"Settings\" -\\> \"API\" -\\> \"Add New Token\" button. Make sure you give `read + write` access!\n*   `SANITY_STUDIO_PREVIEW_SECRET` - A unique string of your choice. This is used to confirm the authenticity of \"preview mode\" requests from the Sanity Studio\n*   `NEXT_PUBLIC_SHOPIFY_STORE_ID` - This is your Shopify store ID, it's the subdomain behind `.myshopify.com`\n*   `NEXT_PUBLIC_SHOPIFY_STOREFRONT_API_TOKEN` - Copy the Storefront API access token from \"Apps\" -\\> \"Develop apps\" -\\> \\[your\\_custom\\_app\\] -\\> \"API credentials\".\n*   `SHOPIFY_ADMIN_API_TOKEN` - Copy the Admin API access token from \"Apps\" -\\> \"Develop apps\" -\\> \\[your\\_custom\\_app\\] -\\> \"API credentials\". (**Note: you’ll only be able to reveal your Admin API token once.**)\n*   `SHOPIFY_WEBHOOK_INTEGRITY` - Copy the Integrity hash from \"Settings\" -\\> \"Notifications\" -\\> \"Webhooks\" _(very bottom of page)_\n*   `KLAVIYO_API_KEY` - Create a Private API Key from your Klaviyo Account \"Settings\" -\\> \"API Keys\"\n*   `MAILCHIMP_API_KEY` - Create an API key from \"Account -\\> \"Extras\" -\\> API Keys\n*   `MAILCHIMP_SERVER` - This is the server your account is from. It's in the URL when logged in and at the end of your API Key\n*   `SENDGRID_API_KEY` - Create an API key from \"Settings\" -\\> \"API Keys\" with \"Restricted Access\" to only \"Mail Send\"\n\n4.  Create an `.env.production` and `.env.development` file in the `/studio` folder, and add the following (using the same value as above):\n\n```\nSANITY_STUDIO_PREVIEW_SECRET=XXXXXX\n```\n\n### 5) Shopify Store Theme\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#5-shopify-store-theme)\n\nSince we're serving our store through a headless environment, we don't want visitors accessing our unused shopify theme. The domain for this is visible during checkout, and is publicly accessible. To silence it, replace your current theme's `theme.liquid` file with the one from this repo, and replace `YOUR_STOREFRONT_DOMAIN_NO_PROTOCOL` with your actual frontsite domain URL **(do not include protocol or trailing slash)**\n\nThis will essentially \"pass-through\" URLs accessed at your Shopify Store to your true headless storefront _(ie. `shop.hull.dev/products` -\\> `hull.dev/products`)_\n\n⚡ Spin Up\n---------\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#-spin-up)\n\n### Next (Front End)\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#next-front-end)\n\n`yarn dev` in the project folder to start the front end locally\n\n*   Your front end should be running on [http://localhost:3000](http://localhost:3000/)\n\n### Sanity (Back End)\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#sanity-back-end)\n\n`yarn dev` in the `/studio` folder to start the studio locally\n\n*   Your Sanity Studio should be running on [http://localhost:3333](http://localhost:3333/)\n    \n    > **Warning**  \n    > If you did not manually set up your project, the `projectId` in `/studio/sanity.json` will still be set to the HULL demo project. Make sure to update this before starting the studio, otherwise you will be denied access when trying to access your studio.\n    \n\n🚀 Deployment\n-------------\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#-deployment)\n\n### Vercel\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#vercel)\n\nThis is setup to work seamlessly with Vercel, which I highly recommend as your hosting provider of choice. Simply follow the on-screen instructions to setup your new project, and be sure to **add the same `.env.local` variables to your Vercel Project**\n\n### Sanity\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#sanity)\n\nThis is an easy one, you can simply run `sanity deploy` from the `/studio` folder in your project. Select a subdomain you want; your Studio is now accessible from the web. This is where I'll invite the client to manage the project so they can both add billing info and begin editing content.\n\n### Client Updates\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#client-updates)\n\nOnce you hand off to the client you'll want to give them the ability to generate builds when they make updates within the Sanity Studio. The easiest way to do this is through my [Vercel Deploy plugin](https://github.com/ndimatteo/sanity-plugin-vercel-deploy).\n\n🤘 Extras/Tips\n--------------\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#-extrastips)\n\n**This looks like a theme... How can I use this like a starter?**While this starter is relatively opinionated, the goal was three-fold:\n\n1.  Use high-quality packages that don't get in the way\n2.  Solve common UX problems and complex logic so you can focus on the fun stuff\n3.  Create a more approachable starter for anyone looking to build production-ready headless Shopify experiences\n\nThat being said, I understand this means a lot of what's included is **very opinionated**. However, you'll find that at it's core the structure and naming conventions lend itself to really making it your own.\n\nI've purposefully used extracted component classes, not only for cleaner file structure, but also so you can easily work in your own styles exclusively within the styles folder. Feel free to extend or outright remove the applied styles for all of the components!\n\n**What's up with the CSS? Why are you using @apply?**Previously, `@apply` was used to extract component classes away from your javascript files. However, since then Tailwind has been opposed to this approach. In the coming releases HULL will move away from this approach in favor of applying styles directly to the components so functionality and styling is done in one place.\n\nYou can read more about Tailwind's stance on `@apply` here: [https://tailwindcss.com/docs/reusing-styles#avoiding-premature-abstraction](https://tailwindcss.com/docs/reusing-styles#avoiding-premature-abstraction)\n\n**Can I use this for non-Shopify projects?**Absolutely! This starter was actually born out of a non-shopify starter I had been using for my own client projects.\n\nI made a `marketing-starter` branch that is **HULL without all the Shopify logic**! The fastest way to get started is simply cloning that branch locally into an empty project folder:\n\n```\ngit clone -b marketing-starter --single-branch git@github.com:ndimatteo/HULL.git .\n```\n\nYou can read the [setup instructions](https://github.com/ndimatteo/HULL/tree/marketing-starter#-set-up) for this version from the branch's README.\n\n**Error: Failed to communicate with the Sanity API**If you get this error in your CLI, you need to logout and log back in again. Simply do `sanity logout` and then `sanity login` to fix.\n\n**Access your \"product\\_sync\" metafields in Shopify without using a plugin**Simply navigate directly to: `https://[store_id].myshopify.com/admin/bulk?resource_name=Product&edit=metafields.sanity.product_sync`\n\n_(making sure to replace `[store_id]` with your Shopify Store ID)_\n\n**How do I properly hand-off a Vercel project to the client?**While not as easy as Netlify, what I prefer to do is:\n\n1.  Have the client create their own [Vercel account](https://vercel.com/signup)\n2.  At the time of writing, Github connections can only be connected to one Vercel account at a time, so have the client [create a Github account](https://github.com/join) if they don't already have one, and transfer the project repo to them\n3.  Delete the dev project from your own Vercel account (this is so the client can utilize the project name and domain you were using during dev)\n4.  You or the client can now connect their newly transferred Github repo to their own Vercel account!\n\n**How can I see the bundle size of my website?**Simply run `yarn analyze` from the project folder. This will run a build of your site and automatically open the [Webpack Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer) visuals for your site's build files.\n\n💯 Shoutouts\n------------\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#-shoutouts)\n\nHuge ups to the following talented and rad folks who helped in countless ways. Thank you for all the support, code contributions, and discussions.\n\n### Developers\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#developers)\n\n*   🔥 [@tuckercs](https://github.com/tuckercs)\n*   🍝 [@iamkevingreen](https://github.com/iamkevingreen)\n*   🧈 [@mikehwagz](https://github.com/mikehwagz)\n*   😎 [@dictions](https://github.com/dictions)\n\n### Designers\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#designers)\n\n*   [@thecollectedworks](https://www.instagram.com/thecollectedworks/)\n*   [@joyntnotjoint](https://www.instagram.com/joyntnotjoint/)\n\n🤝 License\n----------\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#-license)\n\n### [MIT](https://github.com/ndimatteo/HULL/blob/main/LICENSE)\n\n[](https://github.com/ndimatteo/HULL?screenshot=true#mit)\n\n> [nickdimatteo.com](https://nickdimatteo.com/)  ·  Github [@ndimatteo](https://github.com/ndimatteo)  ·  Instagram [@ndimatteo](https://instagram.com/ndimatteo)",
  "usage": {
    "tokens": 4915
  }
}
```
