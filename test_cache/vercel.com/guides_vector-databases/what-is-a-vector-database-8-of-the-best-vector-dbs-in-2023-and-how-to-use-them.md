---
title: What is a Vector Database? 8 of the best Vector DBs in 2023 and how to use them
description: Learn about vector databases: what they are, 8 of the best examples and how to build an AI semantic search app with them.
url: https://vercel.com/guides/vector-databases#building-a-semantic-search-app-with-vercel-postgres-and-pgvector
timestamp: 2025-01-20T15:45:14.880Z
domain: vercel.com
path: guides_vector-databases
---

# What is a Vector Database? 8 of the best Vector DBs in 2023 and how to use them


Learn about vector databases: what they are, 8 of the best examples and how to build an AI semantic search app with them.


## Content

Learn about vector databases: what they are, 8 of the best examples and how to build an AI semantic search app with them.

Last updated on

September 29, 2023

AI

* * *

With the rise of [Large Language Models (LLMs)](https://vercel.com/guides/what-is-a-large-language-model) like [OpenAI's GPT-4](https://vercel.com/docs/integrations/openai) and [Anthropic's Claude](https://sdk.vercel.ai/docs/guides/providers/anthropic), the demand for efficient ways to handle and process the vast amounts of data they utilize has surged. Many might be familiar with the standard relational databases, but the unique requirements of LLMs often require the use of more specialized tools.

Because of this, we've seen a new type of database emerge: Vector databases.

A vector database is a specific kind of database designed to convert data – usually textual data – into multi-dimensional vectors (also known as [_vector embeddings_](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)) and store them accordingly. These vectors act as mathematical depictions of characteristics or qualities. The number of dimensions in each vector can vary widely, spanning from just a few to several thousands, based on the data's intricacy and detail level.

This allows for efficient and effective analysis and comparison of data points, enabling tasks such as similarity searches and clustering. The use of vectors in a database can greatly enhance data processing capabilities and enable advanced data-driven applications.

![Image 9: A diagram showing how vector databases work: user query, text documents, and web pages are converted to Vector embeddings using OpenAI embeddings and stored in Vector databases.](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F768hHVmuTb6Nu3pBbNjZD8%2Fc6b50dd73a6309948e49752afe8689f3%2FCleanShot_2023-09-08_at_17.22.27_2x.png&w=3840&q=75)

A diagram showing how vector databases work: user query, text documents, and web pages are converted to Vector embeddings using OpenAI embeddings and stored in Vector databases.

Imagine you're writing a lengthy research paper, and instead of reading each page individually, you have a special folder that turns every page into a unique bar code. These bar codes represent the main points and details of each page. Some bar codes might be simple with just a few lines, while others are incredibly complex with thousands of lines, depending on the depth of the content on that page.

Now, if you want to find pages with similar themes or group them by topics, you just have to compare their bar codes quickly. This method makes managing and understanding your research much easier and more efficient, just like how vector databases handle and analyze data.

![Image 10: vector-db.png](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F2Wx0d9uTOZ98mUKzVlsoQz%2F47060d5585a9faa8e6e62006fab45b95%2Fvector-db.png&w=3840&q=75)

There are several vector databases available in the market today. Here are some of the most popular ones, based on the usage we've seen in AI apps built on Vercel:

Using a vector database is not very different from using any other kind of database, though the operations you'd perform might vary based on the specific nature of vector data. Here's a simple guide to get started:

1.  **Installation & Setup**: Begin by choosing the right vector database for your needs. Once chosen, follow the provided installation guide. Many databases offer cloud-based solutions, so setup can be as simple as creating an account.
2.  **Data Ingestion**: Import your vector data into the database. This step might require you to convert your data into a vector format if it isn't already.
3.  **Querying**: Once your data is in place, you can start querying the database to find similar vectors or perform analytical operations. Most vector databases will provide you with a query language or an API that's tailored to handle vector operations.
4.  **Maintenance & Scaling**: As with any database, you'd need to monitor performance, handle backups, and ensure that your database scales with your needs.

In this guide, we will learn how to build a semantic search pokedex app using Vercel Postgres and `pgvector` as the vector database.

You can check out a [live demo](https://postgres-pgvector.vercel.app/), or [deploy your own](https://vercel.com/templates/next.js/postgres-pgvector) version of the template with one click.

First, [clone the repository](https://github.com/vercel/examples/tree/main/storage/postgres-pgvector) and download it locally.

```
git clone https://github.com/vercel/examples/tree/main/storage/postgres-pgvector
```

Next, you'll need to set up environment variables in your repo's `.env.local` file. Copy the `.env.example` file to `.env.local`. You will then need to add the following environment variables: OpenAI API key, which you can find [here](https://platform.openai.com/account/api-keys), as well as your Postgres credentials.

```
OPENAI_API_KEY=POSTGRES_URL=POSTGRES_URL_NON_POOLING=POSTGRES_USER=POSTGRES_HOST=POSTGRES_PASSWORD=POSTGRES_DATABASE=
```

For the purpose of this guide, we'll use a free Postgres database hosted on Vercel. First, go to your [Vercel dashboard](https://vercel.com/dashboard) select the **Storage** tab. Then select the **Create Database** button, select **Postgres** and then the **Continue** button.

To create a new database, do the following in the dialog that opens:

1.  Enter `sample_postgres_db `(or any other name you wish) under **Store Name**. The name can only contain alphanumeric letters, "\_" and "-" and can't exceed 32 characters.
2.  Select a region. We recommend choosing a region geographically close to your function region (defaults to US East) for reduced latency.
3.  Click **Create**.

Our empty database is now created in the region specified.

Going back to your terminal, run `npm i -g vercel@latest` to install the Vercel CLI. Then, pull down the latest environment variables to get your local project working with the Postgres database.

Pull down all the required environment variables locally from the Vercel project

We now have a fully functioning Vercel Postgres database and have all the environment variables to run it locally and on Vercel.

Finally, install the required packages using your preferred package manager (e.g. `pnpm`). Once that's done, build the app and run the development server:

Behind the scenes, the build command runs a [seed script](https://github.com/vercel/examples/blob/main/storage/postgres-pgvector/prisma/seed.ts) that automatically seeds your database with a list of Pokémons in the Pokédex, represented as vector embeddings.

```
for (const record of (pokemon as any).data) {    const { embedding, ...p } = record    // Create the pokemon in the database    const pokemon = await prisma.pokemon.create({      data: p,    })    // Add the embedding    await prisma.$executeRaw`        UPDATE pokemon        SET embedding = ${embedding}::vector        WHERE id = ${pokemon.id}    `    console.log(`Added ${pokemon.number} ${pokemon.name}`)}
```

To save time, we are seeding the database with the pre-processed embeddings for each Pokémon. If you want to generate them yourself, you can use a `generateEmbedding` function to generate them on the fly:

```
async function generateEmbedding(_input: string) {  const input = _input.replace(/\n/g, ' ')  const embeddingData = await openai.embeddings.create({    model: 'text-embedding-ada-002',    input,  })  const [{ embedding }] = (embeddingData as any).data  return embedding}for (const record of (pokemon as any).data) {    const embedding = await generateEmbedding(p.name);;    // Create the pokemon in the database    const pokemon = await prisma.pokemon.create({      data: p,    })    // Add the embedding    await prisma.$executeRaw`        UPDATE pokemon        SET embedding = ${embedding}::vector        WHERE id = ${pokemon.id}    `    console.log(`Added ${pokemon.number} ${pokemon.name}`)    await new Promise((r) => setTimeout(r, 500)); // Wait 500ms between requests}
```

Once you've seeded the database with all the vector embeddings, you can now run your application.

Open [http://localhost:3000](http://localhost:3000/) with your browser to check out the running app. You can search for a given Pokémon based on their attributes or name:

![Image 11: CleanShot 2023-09-27 at 13.30.07@2x.png](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F5llNJWHmdtz3mEzh3hBhC0%2Fb553ee72c89e6710f5e113c1b5318a68%2FCleanShot_2023-09-27_at_13.30.07_2x.png&w=1920&q=75)

For the final step, you can deploy this application to Vercel – via Git or the Vercel CLI. Check out the [docs on deploying an application to Vercel](https://vercel.com/docs/deployments/overview) for more details.

Vector databases are incredibly powerful for extending the capabilities of [large language models](https://vercel.com/guides/what-is-a-large-language-model) and building AI-enhanced product experiences. In this article, we learned about some of the best vector databases available in the market today, as well as how to leverage them to build a semantic search app using Vercel Postgres and pgvector.

## Metadata

```json
{
  "title": "What is a Vector Database? 8 of the best Vector DBs in 2023 and how to use them",
  "description": "Learn about vector databases: what they are, 8 of the best examples and how to build an AI semantic search app with them.",
  "url": "https://vercel.com/guides/vector-databases#building-a-semantic-search-app-with-vercel-postgres-and-pgvector",
  "content": "Learn about vector databases: what they are, 8 of the best examples and how to build an AI semantic search app with them.\n\nLast updated on\n\nSeptember 29, 2023\n\nAI\n\n* * *\n\nWith the rise of [Large Language Models (LLMs)](https://vercel.com/guides/what-is-a-large-language-model) like [OpenAI's GPT-4](https://vercel.com/docs/integrations/openai) and [Anthropic's Claude](https://sdk.vercel.ai/docs/guides/providers/anthropic), the demand for efficient ways to handle and process the vast amounts of data they utilize has surged. Many might be familiar with the standard relational databases, but the unique requirements of LLMs often require the use of more specialized tools.\n\nBecause of this, we've seen a new type of database emerge: Vector databases.\n\nA vector database is a specific kind of database designed to convert data – usually textual data – into multi-dimensional vectors (also known as [_vector embeddings_](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)) and store them accordingly. These vectors act as mathematical depictions of characteristics or qualities. The number of dimensions in each vector can vary widely, spanning from just a few to several thousands, based on the data's intricacy and detail level.\n\nThis allows for efficient and effective analysis and comparison of data points, enabling tasks such as similarity searches and clustering. The use of vectors in a database can greatly enhance data processing capabilities and enable advanced data-driven applications.\n\n![Image 9: A diagram showing how vector databases work: user query, text documents, and web pages are converted to Vector embeddings using OpenAI embeddings and stored in Vector databases.](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F768hHVmuTb6Nu3pBbNjZD8%2Fc6b50dd73a6309948e49752afe8689f3%2FCleanShot_2023-09-08_at_17.22.27_2x.png&w=3840&q=75)\n\nA diagram showing how vector databases work: user query, text documents, and web pages are converted to Vector embeddings using OpenAI embeddings and stored in Vector databases.\n\nImagine you're writing a lengthy research paper, and instead of reading each page individually, you have a special folder that turns every page into a unique bar code. These bar codes represent the main points and details of each page. Some bar codes might be simple with just a few lines, while others are incredibly complex with thousands of lines, depending on the depth of the content on that page.\n\nNow, if you want to find pages with similar themes or group them by topics, you just have to compare their bar codes quickly. This method makes managing and understanding your research much easier and more efficient, just like how vector databases handle and analyze data.\n\n![Image 10: vector-db.png](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F2Wx0d9uTOZ98mUKzVlsoQz%2F47060d5585a9faa8e6e62006fab45b95%2Fvector-db.png&w=3840&q=75)\n\nThere are several vector databases available in the market today. Here are some of the most popular ones, based on the usage we've seen in AI apps built on Vercel:\n\nUsing a vector database is not very different from using any other kind of database, though the operations you'd perform might vary based on the specific nature of vector data. Here's a simple guide to get started:\n\n1.  **Installation & Setup**: Begin by choosing the right vector database for your needs. Once chosen, follow the provided installation guide. Many databases offer cloud-based solutions, so setup can be as simple as creating an account.\n2.  **Data Ingestion**: Import your vector data into the database. This step might require you to convert your data into a vector format if it isn't already.\n3.  **Querying**: Once your data is in place, you can start querying the database to find similar vectors or perform analytical operations. Most vector databases will provide you with a query language or an API that's tailored to handle vector operations.\n4.  **Maintenance & Scaling**: As with any database, you'd need to monitor performance, handle backups, and ensure that your database scales with your needs.\n\nIn this guide, we will learn how to build a semantic search pokedex app using Vercel Postgres and `pgvector` as the vector database.\n\nYou can check out a [live demo](https://postgres-pgvector.vercel.app/), or [deploy your own](https://vercel.com/templates/next.js/postgres-pgvector) version of the template with one click.\n\nFirst, [clone the repository](https://github.com/vercel/examples/tree/main/storage/postgres-pgvector) and download it locally.\n\n```\ngit clone https://github.com/vercel/examples/tree/main/storage/postgres-pgvector\n```\n\nNext, you'll need to set up environment variables in your repo's `.env.local` file. Copy the `.env.example` file to `.env.local`. You will then need to add the following environment variables: OpenAI API key, which you can find [here](https://platform.openai.com/account/api-keys), as well as your Postgres credentials.\n\n```\nOPENAI_API_KEY=POSTGRES_URL=POSTGRES_URL_NON_POOLING=POSTGRES_USER=POSTGRES_HOST=POSTGRES_PASSWORD=POSTGRES_DATABASE=\n```\n\nFor the purpose of this guide, we'll use a free Postgres database hosted on Vercel. First, go to your [Vercel dashboard](https://vercel.com/dashboard) select the **Storage** tab. Then select the **Create Database** button, select **Postgres** and then the **Continue** button.\n\nTo create a new database, do the following in the dialog that opens:\n\n1.  Enter `sample_postgres_db `(or any other name you wish) under **Store Name**. The name can only contain alphanumeric letters, \"\\_\" and \"-\" and can't exceed 32 characters.\n2.  Select a region. We recommend choosing a region geographically close to your function region (defaults to US East) for reduced latency.\n3.  Click **Create**.\n\nOur empty database is now created in the region specified.\n\nGoing back to your terminal, run `npm i -g vercel@latest` to install the Vercel CLI. Then, pull down the latest environment variables to get your local project working with the Postgres database.\n\nPull down all the required environment variables locally from the Vercel project\n\nWe now have a fully functioning Vercel Postgres database and have all the environment variables to run it locally and on Vercel.\n\nFinally, install the required packages using your preferred package manager (e.g. `pnpm`). Once that's done, build the app and run the development server:\n\nBehind the scenes, the build command runs a [seed script](https://github.com/vercel/examples/blob/main/storage/postgres-pgvector/prisma/seed.ts) that automatically seeds your database with a list of Pokémons in the Pokédex, represented as vector embeddings.\n\n```\nfor (const record of (pokemon as any).data) {    const { embedding, ...p } = record    // Create the pokemon in the database    const pokemon = await prisma.pokemon.create({      data: p,    })    // Add the embedding    await prisma.$executeRaw`        UPDATE pokemon        SET embedding = ${embedding}::vector        WHERE id = ${pokemon.id}    `    console.log(`Added ${pokemon.number} ${pokemon.name}`)}\n```\n\nTo save time, we are seeding the database with the pre-processed embeddings for each Pokémon. If you want to generate them yourself, you can use a `generateEmbedding` function to generate them on the fly:\n\n```\nasync function generateEmbedding(_input: string) {  const input = _input.replace(/\\n/g, ' ')  const embeddingData = await openai.embeddings.create({    model: 'text-embedding-ada-002',    input,  })  const [{ embedding }] = (embeddingData as any).data  return embedding}for (const record of (pokemon as any).data) {    const embedding = await generateEmbedding(p.name);;    // Create the pokemon in the database    const pokemon = await prisma.pokemon.create({      data: p,    })    // Add the embedding    await prisma.$executeRaw`        UPDATE pokemon        SET embedding = ${embedding}::vector        WHERE id = ${pokemon.id}    `    console.log(`Added ${pokemon.number} ${pokemon.name}`)    await new Promise((r) => setTimeout(r, 500)); // Wait 500ms between requests}\n```\n\nOnce you've seeded the database with all the vector embeddings, you can now run your application.\n\nOpen [http://localhost:3000](http://localhost:3000/) with your browser to check out the running app. You can search for a given Pokémon based on their attributes or name:\n\n![Image 11: CleanShot 2023-09-27 at 13.30.07@2x.png](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F5llNJWHmdtz3mEzh3hBhC0%2Fb553ee72c89e6710f5e113c1b5318a68%2FCleanShot_2023-09-27_at_13.30.07_2x.png&w=1920&q=75)\n\nFor the final step, you can deploy this application to Vercel – via Git or the Vercel CLI. Check out the [docs on deploying an application to Vercel](https://vercel.com/docs/deployments/overview) for more details.\n\nVector databases are incredibly powerful for extending the capabilities of [large language models](https://vercel.com/guides/what-is-a-large-language-model) and building AI-enhanced product experiences. In this article, we learned about some of the best vector databases available in the market today, as well as how to leverage them to build a semantic search app using Vercel Postgres and pgvector.",
  "usage": {
    "tokens": 2246
  }
}
```
