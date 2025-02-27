---
title: Builder.io & Astro
description: Add content to your Astro project using Builder.io’s visual CMS
url: https://docs.astro.build/en/guides/cms/builderio/
timestamp: 2025-01-20T16:05:14.087Z
domain: docs.astro.build
path: en_guides_cms_builderio
---

# Builder.io & Astro


Add content to your Astro project using Builder.io’s visual CMS


## Content

[Builder.io](https://www.builder.io/) is a visual CMS that supports drag-and-drop content editing for building websites.

This recipe will show you how to connect your Builder space to Astro with zero client-side JavaScript.

To get started, you will need to have the following:

*   **A Builder account and space** - If you don’t have an account yet, [sign up for free](https://www.builder.io/) and create a new space. If you already have a space with Builder, feel free to use it, but you will need to modify the code to match the model name (`blogpost`) and custom data fields.
*   **A Builder API key** - This public key will be used to fetch your content from Builder. [Read Builder’s guide on how to find your key](https://www.builder.io/c/docs/using-your-api-key#finding-your-public-api-key).

Setting up credentials
----------------------

[Section titled Setting up credentials](https://docs.astro.build/en/guides/cms/builderio/#setting-up-credentials)

To add your Builder API key and your Builder model name to Astro, create a `.env` file in the root of your project (if one does not already exist) and add the following variables:

```
BUILDER_API_PUBLIC_KEY=YOUR_API_KEYBUILDER_BLOGPOST_MODEL='blogpost'
```

Now, you should be able to use this API key in your project.

If you would like to have IntelliSense for your environment variables, you can create a `env.d.ts` file in the `src/` directory and configure `ImportMetaEnv` like this:

```
interface ImportMetaEnv {  readonly BUILDER_API_PUBLIC_KEY: string;}
```

Your project should now include these files:

*   Directorysrc/
    
    *   **env.d.ts**
    
*   **.env**
*   astro.config.mjs
*   package.json

Making a blog with Astro and Builder
------------------------------------

[Section titled Making a blog with Astro and Builder](https://docs.astro.build/en/guides/cms/builderio/#making-a-blog-with-astro-and-builder)

### Creating a model for a blog post

[Section titled Creating a model for a blog post](https://docs.astro.build/en/guides/cms/builderio/#creating-a-model-for-a-blog-post)

The instructions below create an Astro blog using a Builder model (Type: “Section”) called `blogpost` that contains two required text fields: `title` and `slug`.

In the Builder app create the model that will represent a blog post: go to the **Models** tab and click the **\+ Create Model** button to create model with the following fields and values:

*   **Type:** Section
*   **Name:** “blogpost”
*   **Description:** “This model is for a blog post”

In your new model use the **\+ New Custom Field** button to create 2 new fields:

1.  Text field
    
    *   **Name:** “title”
    *   **Required:** Yes
    *   **Default value** “I forgot to give this a title”
    
    (leave the other parameters as their defaults)
    
2.  Text field
    
    *   **Name:** “slug”
    *   **Required:** Yes
    *   **Default value** “some-slugs-take-their-time”
    
    (leave the other parameters as their defaults)
    

Then click the **Save** button in the upper right.

### Setting up the preview

[Section titled Setting up the preview](https://docs.astro.build/en/guides/cms/builderio/#setting-up-the-preview)

To use Builder’s visual editor, create the page `src/pages/builder-preview.astro` that will render the special `<builder-component>`:

*   Directorysrc/
    
    *   Directorypages/
        
        *   **builder-preview.astro**
        
    *   env.d.ts
    
*   .env
*   astro.config.mjs
*   package.json

Then add the following content:

```
---const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;---<html lang="en">  <head>    <title>Preview for builder.io</title>  </head>  <body>    <header>This is your header</header>    <builder-component model={builderModel} api-key={builderAPIpublicKey}    ></builder-component>    <script async src="https://cdn.builder.io/js/webcomponents"></script>    <footer>This is your footer</footer>  </body></html>
```

In the above example, `<builder-component>` tells Builder where to insert the content from its CMS.

#### Setting the new route as the preview URL

[Section titled Setting the new route as the preview URL](https://docs.astro.build/en/guides/cms/builderio/#setting-the-new-route-as-the-preview-url)

1.  Copy the full URL of your preview, including the protocol, to your clipboard (e.g. `https://{your host}/builder-preview`).
    
2.  Go to the **Models** tab in your Builder space, pick the model you’ve created and paste the URL from step 1 into the **Preview URL** field. Make sure the URL is complete and includes the protocol, for example `https://`.
    
3.  Click the **Save** button in the upper right.
    

#### Testing the preview URL setup

[Section titled Testing the preview URL setup](https://docs.astro.build/en/guides/cms/builderio/#testing-the-preview-url-setup)

1.  Make sure your site is live (e.g. your dev server is running) and the `/builder-preview` route is working.
    
2.  In your Builder space under the **Content** tab, click on **New** to create a new content entry for your `blogpost` model.
    
3.  In the Builder editor that just opened, you should be able to see the `builder-preview.astro` page with a big **Add Block** in the middle.
    

### Creating a blog post

[Section titled Creating a blog post](https://docs.astro.build/en/guides/cms/builderio/#creating-a-blog-post)

1.  In Builder’s visual editor, create a new content entry with the following values:
    
    *   **title:** ‘First post, woohoo!‘
    *   **slug:** ‘first-post-woohoo’
2.  Complete your post using the **Add Block** button and add a text field with some post content.
    
3.  In the text field above the editor, give your entry a name. This is how it will be listed in the Builder app.
    
4.  When you’re ready click the **Publish** button in the upper right corner.
    
5.  Create as many posts as you like, ensuring that all content entries contain a `title` and a `slug` as well as some post content.
    

### Displaying a list of blog posts

[Section titled Displaying a list of blog posts](https://docs.astro.build/en/guides/cms/builderio/#displaying-a-list-of-blog-posts)

Add the following content to `src/pages/index.astro` in order to fetch and display a list of all post titles, each linking to its own page:

```
---const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;const { results: posts } = await fetch(  `https://cdn.builder.io/api/v3/content/${builderModel}?${new URLSearchParams({    apiKey: builderAPIpublicKey,    fields: ["data.slug", "data.title"].join(","),    cachebust: "true",  }).toString()}`)  .then((res) => res.json())  .catch();---<html lang="en">  <head>    <title>Blog Index</title>  </head>  <body>    <ul>      {        posts.flatMap(({ data: { slug, title } }) => (          <li>            <a href={`/posts/${slug}`}>{title}</a>          </li>        ))      }    </ul>  </body></html>
```

Fetching via the content API returns an array of objects containing data for each post. The `fields` query parameter tells Builder which data is included (see highlighted code). `slug` and `title` should match the names of the custom data fields you’ve added to your Builder model.

The `posts` array returned from the fetch displays a list of blog post titles on the home page. The individual page routes will be created in the next step.

Go to your index route and you should be able to see a list of links each with the title of a blog post!

### Displaying a single blog post

[Section titled Displaying a single blog post](https://docs.astro.build/en/guides/cms/builderio/#displaying-a-single-blog-post)

Create the page `src/pages/posts/[slug].astro` that will [dynamically generate a page](https://docs.astro.build/en/guides/routing/#dynamic-routes) for each post.

*   Directorysrc/
    
    *   Directorypages/
        
        *   index.astro
        *   Directoryposts/
            
            *   **\[slug\].astro**
            
        
    *   env.d.ts
    
*   .env
*   astro.config.mjs
*   package.json

This file must contain:

*   A [`getStaticPaths()`](https://docs.astro.build/en/reference/routing-reference/#getstaticpaths) function to fetch `slug` information from Builder and create a static route for each blog post.
*   A `fetch()` to the Builder API using the `slug` identifier to return post content and metadata (e.g. a `title`).
*   A `<Fragment />` in the template to render the post content as HTML.

Each of these is highlighted in the following code snippet.

```
---export async function getStaticPaths() {  const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;  const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;  const { results: posts } = await fetch(    `https://cdn.builder.io/api/v3/content/${builderModel}?${new URLSearchParams(      {        apiKey: builderAPIpublicKey,        fields: ["data.slug", "data.title"].join(","),        cachebust: "true",      }    ).toString()}`  )    .then((res) => res.json())    .catch    // ...catch some errors...);    ();  return posts.map(({ data: { slug, title } }) => ({    params: { slug },    props: { title },  }))}const { slug } = Astro.params;const { title } = Astro.props;const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;// Builder's API requires this field but for this use case the url doesn't seem to matter - the API returns the same HTMLconst encodedUrl = encodeURIComponent("moot");const { html: postHTML } = await fetch(  `https://cdn.builder.io/api/v1/qwik/${builderModel}?${new URLSearchParams({    apiKey: builderAPIpublicKey,    url: encodedUrl,    "query.data.slug": slug,    cachebust: "true",  }).toString()}`)  .then((res) => res.json())  .catch();---<html lang="en">  <head>    <title>{title}</title>  </head>  <body>    <header>This is your header</header>    <article>      <Fragment set:html={postHTML} />    </article>    <footer>This is your footer</footer>  </body></html>
```

Now when you click on a link on your index route, you will be taken to the individual blog post page.

### Publishing your site

[Section titled Publishing your site](https://docs.astro.build/en/guides/cms/builderio/#publishing-your-site)

To deploy your website, visit our [deployment guides](https://docs.astro.build/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

#### Rebuild on Builder changes

[Section titled Rebuild on Builder changes](https://docs.astro.build/en/guides/cms/builderio/#rebuild-on-builder-changes)

If your project is using Astro’s default static mode, you will need to set up a webhook to trigger a new build when your content changes. If you are using Netlify or Vercel as your hosting provider, you can use its webhook feature to trigger a new build whenever you click **Publish** in the Builder editor.

1.  Go to your site dashboard, then **Site Settings** and click on **Build & deploy**.
    
2.  Under the **Continuous Deployment** tab, find the **Build hooks** section and click on **Add build hook**.
    
3.  Provide a name for your webhook and select the branch you want to trigger the build on. Click on **Save** and copy the generated URL.
    

1.  Go to your project dashboard and click on **Settings**.
    
2.  Under the **Git** tab, find the **Deploy Hooks** section.
    
3.  Provide a name for your webhook and the branch you want to trigger the build on. Click **Add** and copy the generated URL.
    

##### Adding a webhook to Builder

[Section titled Adding a webhook to Builder](https://docs.astro.build/en/guides/cms/builderio/#adding-a-webhook-to-builder)

1.  In your Builder dashboard, go into your **`blogpost`** model. Under **Show More Options**, select **Edit Webhooks** at the bottom.
    
2.  Add a new webhook by clicking on **Webhook**. Paste the URL generated by your hosting provider into the **Url** field.
    
3.  Click on **Show Advanced** under the URL field and toggle the option to select **Disable Payload**. With the payload disabled, Builder sends a simpler POST request to your hosting provider, which can be helpful as your site grows. Click **Done** to save this selection.
    

With this webhook in place, whenever you click the **Publish** button in the Builder editor, your hosting provider rebuilds your site - and Astro fetches the newly published data for you. Nothing to do but lean back and pump out that sweet sweet content!

Official resources
------------------

[Section titled Official resources](https://docs.astro.build/en/guides/cms/builderio/#official-resources)

*   Check out [the official Builder.io starter project](https://github.com/BuilderIO/builder/tree/main/examples/astro-solidjs), which uses Astro and SolidJS.
*   The [official Builder quickstart guide](https://www.builder.io/c/docs/quickstart#step-1-add-builder-as-a-dependency) covers both the use of the REST API as well as data fetching through an integration with a JavaScript framework like Qwik, React or Vue.
*   [Builder’s API explorer](https://builder.io/api-explorer) can help if you need to troubleshoot your API calls.

*   Read [Connecting Builder.io’s Visual CMS to Astro](https://www.hamatoyogi.dev/blog/astro-log/connecting-builderio-to-astro) by Yoav Ganbar.

More CMS guides
---------------

*   ![Image 70](https://docs.astro.build/logos/apostrophecms.svg)
    
    ### [Apostrophe](https://docs.astro.build/en/guides/cms/apostrophecms/)
    
*   ![Image 71](https://docs.astro.build/logos/builderio.svg)
    
    ### [Builder.io](https://docs.astro.build/en/guides/cms/builderio/)
    
*   ![Image 72](https://docs.astro.build/logos/buttercms.svg)
    
    ### [ButterCMS](https://docs.astro.build/en/guides/cms/buttercms/)
    
*   ![Image 73](https://docs.astro.build/logos/caisy.svg)
    
    ### [Caisy](https://docs.astro.build/en/guides/cms/caisy/)
    
*   ![Image 74](https://docs.astro.build/logos/cloudcannon.svg)
    
    ### [CloudCannon](https://docs.astro.build/en/guides/cms/cloudcannon/)
    
*   ![Image 75](https://docs.astro.build/logos/contentful.svg)
    
    ### [Contentful](https://docs.astro.build/en/guides/cms/contentful/)
    
*   ![Image 76](https://docs.astro.build/logos/cosmic.svg)
    
    ### [Cosmic](https://docs.astro.build/en/guides/cms/cosmic/)
    
*   ![Image 77](https://docs.astro.build/logos/craft-cms.svg)
    
    ### [Craft CMS](https://docs.astro.build/en/guides/cms/craft-cms/)
    
*   ![Image 78](https://docs.astro.build/logos/crystallize.svg)
    
    ### [Crystallize](https://docs.astro.build/en/guides/cms/crystallize/)
    
*   ![Image 79](https://docs.astro.build/logos/datocms.svg)
    
    ### [DatoCMS](https://docs.astro.build/en/guides/cms/datocms/)
    
*   ![Image 80](https://docs.astro.build/logos/decap-cms.svg)
    
    ### [Decap CMS](https://docs.astro.build/en/guides/cms/decap-cms/)
    
*   ![Image 81](https://docs.astro.build/logos/directus.svg)
    
    ### [Directus](https://docs.astro.build/en/guides/cms/directus/)
    
*   ![Image 82](https://docs.astro.build/logos/drupal.svg)
    
    ### [Drupal](https://docs.astro.build/en/guides/cms/drupal/)
    
*   ![Image 83](https://docs.astro.build/logos/flotiq.svg)
    
    ### [Flotiq](https://docs.astro.build/en/guides/cms/flotiq/)
    
*   ![Image 84](https://docs.astro.build/logos/frontmatter-cms.svg)
    
    ### [Front Matter CMS](https://docs.astro.build/en/guides/cms/frontmatter-cms/)
    
*   ![Image 85](https://docs.astro.build/logos/ghost.png)
    
    ### [Ghost](https://docs.astro.build/en/guides/cms/ghost/)
    
*   ![Image 86](https://docs.astro.build/logos/hashnode.png)
    
    ### [Hashnode](https://docs.astro.build/en/guides/cms/hashnode/)
    
*   ![Image 87](https://docs.astro.build/logos/hygraph.svg)
    
    ### [Hygraph](https://docs.astro.build/en/guides/cms/hygraph/)
    
*   ![Image 88](https://docs.astro.build/logos/keystatic.svg)
    
    ### [Keystatic](https://docs.astro.build/en/guides/cms/keystatic/)
    
*   ![Image 89](https://docs.astro.build/logos/keystonejs.svg)
    
    ### [KeystoneJS](https://docs.astro.build/en/guides/cms/keystonejs/)
    
*   ![Image 90](https://docs.astro.build/logos/kontent-ai.svg)
    
    ### [Kontent.ai](https://docs.astro.build/en/guides/cms/kontent-ai/)
    
*   ![Image 91](https://docs.astro.build/logos/microcms.svg)
    
    ### [microCMS](https://docs.astro.build/en/guides/cms/microcms/)
    
*   ![Image 92](https://docs.astro.build/logos/payload.svg)
    
    ### [Payload CMS](https://docs.astro.build/en/guides/cms/payload/)
    
*   ![Image 93](https://docs.astro.build/logos/preprcms.svg)
    
    ### [Prepr CMS](https://docs.astro.build/en/guides/cms/preprcms/)
    
*   ![Image 94](https://docs.astro.build/logos/prismic.svg)
    
    ### [Prismic](https://docs.astro.build/en/guides/cms/prismic/)
    
*   ![Image 95](https://docs.astro.build/logos/sanity.svg)
    
    ### [Sanity](https://docs.astro.build/en/guides/cms/sanity/)
    
*   ![Image 96](https://docs.astro.build/logos/sitecore.svg)
    
    ### [Sitecore XM](https://docs.astro.build/en/guides/cms/sitecore/)
    
*   ![Image 97](https://docs.astro.build/logos/spinal.svg)
    
    ### [Spinal](https://docs.astro.build/en/guides/cms/spinal/)
    
*   ![Image 98](https://docs.astro.build/logos/statamic.svg)
    
    ### [Statamic](https://docs.astro.build/en/guides/cms/statamic/)
    
*   ![Image 99](https://docs.astro.build/logos/storyblok.svg)
    
    ### [Storyblok](https://docs.astro.build/en/guides/cms/storyblok/)
    
*   ![Image 100](https://docs.astro.build/logos/strapi.svg)
    
    ### [Strapi](https://docs.astro.build/en/guides/cms/strapi/)
    
*   ![Image 101](https://docs.astro.build/logos/tina-cms.svg)
    
    ### [Tina CMS](https://docs.astro.build/en/guides/cms/tina-cms/)
    
*   ![Image 102](https://docs.astro.build/logos/umbraco.svg)
    
    ### [Umbraco](https://docs.astro.build/en/guides/cms/umbraco/)
    
*   ![Image 103](https://docs.astro.build/logos/wordpress.svg)
    
    ### [WordPress](https://docs.astro.build/en/guides/cms/wordpress/)

## Metadata

```json
{
  "title": "Builder.io & Astro",
  "description": "Add content to your Astro project using Builder.io’s visual CMS",
  "url": "https://docs.astro.build/en/guides/cms/builderio/",
  "content": "[Builder.io](https://www.builder.io/) is a visual CMS that supports drag-and-drop content editing for building websites.\n\nThis recipe will show you how to connect your Builder space to Astro with zero client-side JavaScript.\n\nTo get started, you will need to have the following:\n\n*   **A Builder account and space** - If you don’t have an account yet, [sign up for free](https://www.builder.io/) and create a new space. If you already have a space with Builder, feel free to use it, but you will need to modify the code to match the model name (`blogpost`) and custom data fields.\n*   **A Builder API key** - This public key will be used to fetch your content from Builder. [Read Builder’s guide on how to find your key](https://www.builder.io/c/docs/using-your-api-key#finding-your-public-api-key).\n\nSetting up credentials\n----------------------\n\n[Section titled Setting up credentials](https://docs.astro.build/en/guides/cms/builderio/#setting-up-credentials)\n\nTo add your Builder API key and your Builder model name to Astro, create a `.env` file in the root of your project (if one does not already exist) and add the following variables:\n\n```\nBUILDER_API_PUBLIC_KEY=YOUR_API_KEYBUILDER_BLOGPOST_MODEL='blogpost'\n```\n\nNow, you should be able to use this API key in your project.\n\nIf you would like to have IntelliSense for your environment variables, you can create a `env.d.ts` file in the `src/` directory and configure `ImportMetaEnv` like this:\n\n```\ninterface ImportMetaEnv {  readonly BUILDER_API_PUBLIC_KEY: string;}\n```\n\nYour project should now include these files:\n\n*   Directorysrc/\n    \n    *   **env.d.ts**\n    \n*   **.env**\n*   astro.config.mjs\n*   package.json\n\nMaking a blog with Astro and Builder\n------------------------------------\n\n[Section titled Making a blog with Astro and Builder](https://docs.astro.build/en/guides/cms/builderio/#making-a-blog-with-astro-and-builder)\n\n### Creating a model for a blog post\n\n[Section titled Creating a model for a blog post](https://docs.astro.build/en/guides/cms/builderio/#creating-a-model-for-a-blog-post)\n\nThe instructions below create an Astro blog using a Builder model (Type: “Section”) called `blogpost` that contains two required text fields: `title` and `slug`.\n\nIn the Builder app create the model that will represent a blog post: go to the **Models** tab and click the **\\+ Create Model** button to create model with the following fields and values:\n\n*   **Type:** Section\n*   **Name:** “blogpost”\n*   **Description:** “This model is for a blog post”\n\nIn your new model use the **\\+ New Custom Field** button to create 2 new fields:\n\n1.  Text field\n    \n    *   **Name:** “title”\n    *   **Required:** Yes\n    *   **Default value** “I forgot to give this a title”\n    \n    (leave the other parameters as their defaults)\n    \n2.  Text field\n    \n    *   **Name:** “slug”\n    *   **Required:** Yes\n    *   **Default value** “some-slugs-take-their-time”\n    \n    (leave the other parameters as their defaults)\n    \n\nThen click the **Save** button in the upper right.\n\n### Setting up the preview\n\n[Section titled Setting up the preview](https://docs.astro.build/en/guides/cms/builderio/#setting-up-the-preview)\n\nTo use Builder’s visual editor, create the page `src/pages/builder-preview.astro` that will render the special `<builder-component>`:\n\n*   Directorysrc/\n    \n    *   Directorypages/\n        \n        *   **builder-preview.astro**\n        \n    *   env.d.ts\n    \n*   .env\n*   astro.config.mjs\n*   package.json\n\nThen add the following content:\n\n```\n---const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;---<html lang=\"en\">  <head>    <title>Preview for builder.io</title>  </head>  <body>    <header>This is your header</header>    <builder-component model={builderModel} api-key={builderAPIpublicKey}    ></builder-component>    <script async src=\"https://cdn.builder.io/js/webcomponents\"></script>    <footer>This is your footer</footer>  </body></html>\n```\n\nIn the above example, `<builder-component>` tells Builder where to insert the content from its CMS.\n\n#### Setting the new route as the preview URL\n\n[Section titled Setting the new route as the preview URL](https://docs.astro.build/en/guides/cms/builderio/#setting-the-new-route-as-the-preview-url)\n\n1.  Copy the full URL of your preview, including the protocol, to your clipboard (e.g. `https://{your host}/builder-preview`).\n    \n2.  Go to the **Models** tab in your Builder space, pick the model you’ve created and paste the URL from step 1 into the **Preview URL** field. Make sure the URL is complete and includes the protocol, for example `https://`.\n    \n3.  Click the **Save** button in the upper right.\n    \n\n#### Testing the preview URL setup\n\n[Section titled Testing the preview URL setup](https://docs.astro.build/en/guides/cms/builderio/#testing-the-preview-url-setup)\n\n1.  Make sure your site is live (e.g. your dev server is running) and the `/builder-preview` route is working.\n    \n2.  In your Builder space under the **Content** tab, click on **New** to create a new content entry for your `blogpost` model.\n    \n3.  In the Builder editor that just opened, you should be able to see the `builder-preview.astro` page with a big **Add Block** in the middle.\n    \n\n### Creating a blog post\n\n[Section titled Creating a blog post](https://docs.astro.build/en/guides/cms/builderio/#creating-a-blog-post)\n\n1.  In Builder’s visual editor, create a new content entry with the following values:\n    \n    *   **title:** ‘First post, woohoo!‘\n    *   **slug:** ‘first-post-woohoo’\n2.  Complete your post using the **Add Block** button and add a text field with some post content.\n    \n3.  In the text field above the editor, give your entry a name. This is how it will be listed in the Builder app.\n    \n4.  When you’re ready click the **Publish** button in the upper right corner.\n    \n5.  Create as many posts as you like, ensuring that all content entries contain a `title` and a `slug` as well as some post content.\n    \n\n### Displaying a list of blog posts\n\n[Section titled Displaying a list of blog posts](https://docs.astro.build/en/guides/cms/builderio/#displaying-a-list-of-blog-posts)\n\nAdd the following content to `src/pages/index.astro` in order to fetch and display a list of all post titles, each linking to its own page:\n\n```\n---const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;const { results: posts } = await fetch(  `https://cdn.builder.io/api/v3/content/${builderModel}?${new URLSearchParams({    apiKey: builderAPIpublicKey,    fields: [\"data.slug\", \"data.title\"].join(\",\"),    cachebust: \"true\",  }).toString()}`)  .then((res) => res.json())  .catch();---<html lang=\"en\">  <head>    <title>Blog Index</title>  </head>  <body>    <ul>      {        posts.flatMap(({ data: { slug, title } }) => (          <li>            <a href={`/posts/${slug}`}>{title}</a>          </li>        ))      }    </ul>  </body></html>\n```\n\nFetching via the content API returns an array of objects containing data for each post. The `fields` query parameter tells Builder which data is included (see highlighted code). `slug` and `title` should match the names of the custom data fields you’ve added to your Builder model.\n\nThe `posts` array returned from the fetch displays a list of blog post titles on the home page. The individual page routes will be created in the next step.\n\nGo to your index route and you should be able to see a list of links each with the title of a blog post!\n\n### Displaying a single blog post\n\n[Section titled Displaying a single blog post](https://docs.astro.build/en/guides/cms/builderio/#displaying-a-single-blog-post)\n\nCreate the page `src/pages/posts/[slug].astro` that will [dynamically generate a page](https://docs.astro.build/en/guides/routing/#dynamic-routes) for each post.\n\n*   Directorysrc/\n    \n    *   Directorypages/\n        \n        *   index.astro\n        *   Directoryposts/\n            \n            *   **\\[slug\\].astro**\n            \n        \n    *   env.d.ts\n    \n*   .env\n*   astro.config.mjs\n*   package.json\n\nThis file must contain:\n\n*   A [`getStaticPaths()`](https://docs.astro.build/en/reference/routing-reference/#getstaticpaths) function to fetch `slug` information from Builder and create a static route for each blog post.\n*   A `fetch()` to the Builder API using the `slug` identifier to return post content and metadata (e.g. a `title`).\n*   A `<Fragment />` in the template to render the post content as HTML.\n\nEach of these is highlighted in the following code snippet.\n\n```\n---export async function getStaticPaths() {  const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;  const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;  const { results: posts } = await fetch(    `https://cdn.builder.io/api/v3/content/${builderModel}?${new URLSearchParams(      {        apiKey: builderAPIpublicKey,        fields: [\"data.slug\", \"data.title\"].join(\",\"),        cachebust: \"true\",      }    ).toString()}`  )    .then((res) => res.json())    .catch    // ...catch some errors...);    ();  return posts.map(({ data: { slug, title } }) => ({    params: { slug },    props: { title },  }))}const { slug } = Astro.params;const { title } = Astro.props;const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;// Builder's API requires this field but for this use case the url doesn't seem to matter - the API returns the same HTMLconst encodedUrl = encodeURIComponent(\"moot\");const { html: postHTML } = await fetch(  `https://cdn.builder.io/api/v1/qwik/${builderModel}?${new URLSearchParams({    apiKey: builderAPIpublicKey,    url: encodedUrl,    \"query.data.slug\": slug,    cachebust: \"true\",  }).toString()}`)  .then((res) => res.json())  .catch();---<html lang=\"en\">  <head>    <title>{title}</title>  </head>  <body>    <header>This is your header</header>    <article>      <Fragment set:html={postHTML} />    </article>    <footer>This is your footer</footer>  </body></html>\n```\n\nNow when you click on a link on your index route, you will be taken to the individual blog post page.\n\n### Publishing your site\n\n[Section titled Publishing your site](https://docs.astro.build/en/guides/cms/builderio/#publishing-your-site)\n\nTo deploy your website, visit our [deployment guides](https://docs.astro.build/en/guides/deploy/) and follow the instructions for your preferred hosting provider.\n\n#### Rebuild on Builder changes\n\n[Section titled Rebuild on Builder changes](https://docs.astro.build/en/guides/cms/builderio/#rebuild-on-builder-changes)\n\nIf your project is using Astro’s default static mode, you will need to set up a webhook to trigger a new build when your content changes. If you are using Netlify or Vercel as your hosting provider, you can use its webhook feature to trigger a new build whenever you click **Publish** in the Builder editor.\n\n1.  Go to your site dashboard, then **Site Settings** and click on **Build & deploy**.\n    \n2.  Under the **Continuous Deployment** tab, find the **Build hooks** section and click on **Add build hook**.\n    \n3.  Provide a name for your webhook and select the branch you want to trigger the build on. Click on **Save** and copy the generated URL.\n    \n\n1.  Go to your project dashboard and click on **Settings**.\n    \n2.  Under the **Git** tab, find the **Deploy Hooks** section.\n    \n3.  Provide a name for your webhook and the branch you want to trigger the build on. Click **Add** and copy the generated URL.\n    \n\n##### Adding a webhook to Builder\n\n[Section titled Adding a webhook to Builder](https://docs.astro.build/en/guides/cms/builderio/#adding-a-webhook-to-builder)\n\n1.  In your Builder dashboard, go into your **`blogpost`** model. Under **Show More Options**, select **Edit Webhooks** at the bottom.\n    \n2.  Add a new webhook by clicking on **Webhook**. Paste the URL generated by your hosting provider into the **Url** field.\n    \n3.  Click on **Show Advanced** under the URL field and toggle the option to select **Disable Payload**. With the payload disabled, Builder sends a simpler POST request to your hosting provider, which can be helpful as your site grows. Click **Done** to save this selection.\n    \n\nWith this webhook in place, whenever you click the **Publish** button in the Builder editor, your hosting provider rebuilds your site - and Astro fetches the newly published data for you. Nothing to do but lean back and pump out that sweet sweet content!\n\nOfficial resources\n------------------\n\n[Section titled Official resources](https://docs.astro.build/en/guides/cms/builderio/#official-resources)\n\n*   Check out [the official Builder.io starter project](https://github.com/BuilderIO/builder/tree/main/examples/astro-solidjs), which uses Astro and SolidJS.\n*   The [official Builder quickstart guide](https://www.builder.io/c/docs/quickstart#step-1-add-builder-as-a-dependency) covers both the use of the REST API as well as data fetching through an integration with a JavaScript framework like Qwik, React or Vue.\n*   [Builder’s API explorer](https://builder.io/api-explorer) can help if you need to troubleshoot your API calls.\n\n*   Read [Connecting Builder.io’s Visual CMS to Astro](https://www.hamatoyogi.dev/blog/astro-log/connecting-builderio-to-astro) by Yoav Ganbar.\n\nMore CMS guides\n---------------\n\n*   ![Image 70](https://docs.astro.build/logos/apostrophecms.svg)\n    \n    ### [Apostrophe](https://docs.astro.build/en/guides/cms/apostrophecms/)\n    \n*   ![Image 71](https://docs.astro.build/logos/builderio.svg)\n    \n    ### [Builder.io](https://docs.astro.build/en/guides/cms/builderio/)\n    \n*   ![Image 72](https://docs.astro.build/logos/buttercms.svg)\n    \n    ### [ButterCMS](https://docs.astro.build/en/guides/cms/buttercms/)\n    \n*   ![Image 73](https://docs.astro.build/logos/caisy.svg)\n    \n    ### [Caisy](https://docs.astro.build/en/guides/cms/caisy/)\n    \n*   ![Image 74](https://docs.astro.build/logos/cloudcannon.svg)\n    \n    ### [CloudCannon](https://docs.astro.build/en/guides/cms/cloudcannon/)\n    \n*   ![Image 75](https://docs.astro.build/logos/contentful.svg)\n    \n    ### [Contentful](https://docs.astro.build/en/guides/cms/contentful/)\n    \n*   ![Image 76](https://docs.astro.build/logos/cosmic.svg)\n    \n    ### [Cosmic](https://docs.astro.build/en/guides/cms/cosmic/)\n    \n*   ![Image 77](https://docs.astro.build/logos/craft-cms.svg)\n    \n    ### [Craft CMS](https://docs.astro.build/en/guides/cms/craft-cms/)\n    \n*   ![Image 78](https://docs.astro.build/logos/crystallize.svg)\n    \n    ### [Crystallize](https://docs.astro.build/en/guides/cms/crystallize/)\n    \n*   ![Image 79](https://docs.astro.build/logos/datocms.svg)\n    \n    ### [DatoCMS](https://docs.astro.build/en/guides/cms/datocms/)\n    \n*   ![Image 80](https://docs.astro.build/logos/decap-cms.svg)\n    \n    ### [Decap CMS](https://docs.astro.build/en/guides/cms/decap-cms/)\n    \n*   ![Image 81](https://docs.astro.build/logos/directus.svg)\n    \n    ### [Directus](https://docs.astro.build/en/guides/cms/directus/)\n    \n*   ![Image 82](https://docs.astro.build/logos/drupal.svg)\n    \n    ### [Drupal](https://docs.astro.build/en/guides/cms/drupal/)\n    \n*   ![Image 83](https://docs.astro.build/logos/flotiq.svg)\n    \n    ### [Flotiq](https://docs.astro.build/en/guides/cms/flotiq/)\n    \n*   ![Image 84](https://docs.astro.build/logos/frontmatter-cms.svg)\n    \n    ### [Front Matter CMS](https://docs.astro.build/en/guides/cms/frontmatter-cms/)\n    \n*   ![Image 85](https://docs.astro.build/logos/ghost.png)\n    \n    ### [Ghost](https://docs.astro.build/en/guides/cms/ghost/)\n    \n*   ![Image 86](https://docs.astro.build/logos/hashnode.png)\n    \n    ### [Hashnode](https://docs.astro.build/en/guides/cms/hashnode/)\n    \n*   ![Image 87](https://docs.astro.build/logos/hygraph.svg)\n    \n    ### [Hygraph](https://docs.astro.build/en/guides/cms/hygraph/)\n    \n*   ![Image 88](https://docs.astro.build/logos/keystatic.svg)\n    \n    ### [Keystatic](https://docs.astro.build/en/guides/cms/keystatic/)\n    \n*   ![Image 89](https://docs.astro.build/logos/keystonejs.svg)\n    \n    ### [KeystoneJS](https://docs.astro.build/en/guides/cms/keystonejs/)\n    \n*   ![Image 90](https://docs.astro.build/logos/kontent-ai.svg)\n    \n    ### [Kontent.ai](https://docs.astro.build/en/guides/cms/kontent-ai/)\n    \n*   ![Image 91](https://docs.astro.build/logos/microcms.svg)\n    \n    ### [microCMS](https://docs.astro.build/en/guides/cms/microcms/)\n    \n*   ![Image 92](https://docs.astro.build/logos/payload.svg)\n    \n    ### [Payload CMS](https://docs.astro.build/en/guides/cms/payload/)\n    \n*   ![Image 93](https://docs.astro.build/logos/preprcms.svg)\n    \n    ### [Prepr CMS](https://docs.astro.build/en/guides/cms/preprcms/)\n    \n*   ![Image 94](https://docs.astro.build/logos/prismic.svg)\n    \n    ### [Prismic](https://docs.astro.build/en/guides/cms/prismic/)\n    \n*   ![Image 95](https://docs.astro.build/logos/sanity.svg)\n    \n    ### [Sanity](https://docs.astro.build/en/guides/cms/sanity/)\n    \n*   ![Image 96](https://docs.astro.build/logos/sitecore.svg)\n    \n    ### [Sitecore XM](https://docs.astro.build/en/guides/cms/sitecore/)\n    \n*   ![Image 97](https://docs.astro.build/logos/spinal.svg)\n    \n    ### [Spinal](https://docs.astro.build/en/guides/cms/spinal/)\n    \n*   ![Image 98](https://docs.astro.build/logos/statamic.svg)\n    \n    ### [Statamic](https://docs.astro.build/en/guides/cms/statamic/)\n    \n*   ![Image 99](https://docs.astro.build/logos/storyblok.svg)\n    \n    ### [Storyblok](https://docs.astro.build/en/guides/cms/storyblok/)\n    \n*   ![Image 100](https://docs.astro.build/logos/strapi.svg)\n    \n    ### [Strapi](https://docs.astro.build/en/guides/cms/strapi/)\n    \n*   ![Image 101](https://docs.astro.build/logos/tina-cms.svg)\n    \n    ### [Tina CMS](https://docs.astro.build/en/guides/cms/tina-cms/)\n    \n*   ![Image 102](https://docs.astro.build/logos/umbraco.svg)\n    \n    ### [Umbraco](https://docs.astro.build/en/guides/cms/umbraco/)\n    \n*   ![Image 103](https://docs.astro.build/logos/wordpress.svg)\n    \n    ### [WordPress](https://docs.astro.build/en/guides/cms/wordpress/)",
  "usage": {
    "tokens": 4747
  }
}
```
