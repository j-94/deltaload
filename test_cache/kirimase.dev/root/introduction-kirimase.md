---
title: Introduction – Kirimase
description: 
url: https://kirimase.dev/
timestamp: 2025-01-20T15:50:23.371Z
domain: kirimase.dev
path: root
---

# Introduction – Kirimase



## Content

What is Kirimase?[](https://kirimase.dev/#what-is-kirimase)
-----------------------------------------------------------

Kirimase is a command-line tool (CLI) for **building full-stack Next.js apps faster**. It supercharges your development workflow, allowing you to quickly integrate packages and scaffold resources for your application with best practices in mind.

In a matter of seconds, Kirimase installs and configures your choice of ORM (Prisma or Drizzle), Authentication (Auth.js, Clerk, Lucia, Kinde), Component Library (Shadcn-UI), Payments (Stripe) and Email (Resend). Kirimase also sets up tRPC with both client and server side implementation ready to go. Unlike template repos, each option is modular, meaning you can pick any combination of packages you would like.

With Kirimase's `generate` command, developers can jump right into building actual features without the need to manually create boilerplate code. After defining a new data entity, the command swiftly generates all boilerplate necessary for basic CRUD operations, including everything from the schema to server actions to routes & components. Build at the speed of thought!

Kirimase demo

Motivation[](https://kirimase.dev/#motivation)
----------------------------------------------

### TL;DR[](https://kirimase.dev/#tldr)

I love the Ruby on Rails CLI and always yearned for something like it for Next.js.

### Longer Story[](https://kirimase.dev/#longer-story)

I’ve always loved building with Next.js. The quality of the learning materials and simplicity of the git deployment workflow made it a dream to go from localhost to production. However, one of Next.js’ selling points, its lack of opinion on what tools to use with it, also led to an undesirable DX. More specifically, before writing a single line of code, I felt overwhelmed in my search for the best email/orm/analytics/test/etc. package. Once I did land on the right combination, I would need to spend a few hours sifting through documentation to configure everything to work together. In almost every case, I would find myself disheartened and eventually disinterested enough to push the task to another day.

Having heard great things about Rails in this regard, I gave it a go and was overjoyed by the simplicity that came with setting up new applications: namely, how quickly I went from `rails new` to actually building the business logic of the application. Ultimately, while I loved the rails CLI, I was excited to go back to Next.js as building UIs with React always felt more natural and enjoyable than ERB.

Ever since that experience there were two main things that I kept thinking about:

1.  **gems**: why is it so damn complicated to install and configure packages in the JS ecosystem? Why can’t installing and configuring a package be as easy as `bundle add package`?
2.  **scaffold**: why do I keep writing the same boilerplate for only slightly different db resources? It’s boring and error prone.

And with that Kirimase was born 😊

Why Kirimase?[](https://kirimase.dev/#why-kirimase)
---------------------------------------------------

The name is a funny story. Kirimase, in its original form, started as a way to quickly scaffold the files and packages necessary to get up and running with Drizzle ORM (similar to running npx prisma init). When it came time to brainstorm a name, I immediately thought, I want a cool name like Jotai. I was on my phone at the time and I fired up Google Translate with English to Japanese and typed in drizzle. Result: kirimase. I thought to myself, “Kirimase”, that’s exactly what I’m looking for, but a cool name like that has probably already been taken by _n_ projects before me. So I check NPM and to my surprise, it was available. So I quickly changed the package name and published the first version.

Later that day, as I excitedly recounted this exact story to a friend, I pulled out Google Translate and up came my previous search result:

> **English**: drizzle  
> **Japanese**: Kiri_same_

… turns out, I can’t read!

![Image 4: Gorlami](https://kirimase.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fkirimase_gorlami.1fc73489.png&w=1920&q=75)

Quick Overview[](https://kirimase.dev/#quick-overview)
------------------------------------------------------

Kirimase has three main commands:

*   `init`: configures the initial `kirimase.config.json` file that will be used for the `add` and `generate` commands
*   `add`: select packages to install and configure
*   `generate`: describe your data model and Kirimase will generate DB schema, migration, service files (queries and mutations), API Routes, tRPC routes, and basic UI to perform all crud operations

Explore More[](https://kirimase.dev/#explore-more)
--------------------------------------------------

*   [Kirimase: The Tutorial](https://kirimase.dev/the-tutorial)
*   [Getting Started](https://kirimase.dev/getting-started)
*   [Commands](https://kirimase.dev/commands/init)
*   [Tutorials and Demos](https://kirimase.dev/tutorials)

Feedback and Contributions[](https://kirimase.dev/#feedback-and-contributions)
------------------------------------------------------------------------------

Your feedback and contributions are valuable! Explore the [contributing guide](https://kirimase.dev/contributing) to learn more about how you can contribute to Kirimase.

[The Tutorial](https://kirimase.dev/the-tutorial "The Tutorial")

## Metadata

```json
{
  "title": "Introduction – Kirimase",
  "description": "",
  "url": "https://kirimase.dev/",
  "content": "What is Kirimase?[](https://kirimase.dev/#what-is-kirimase)\n-----------------------------------------------------------\n\nKirimase is a command-line tool (CLI) for **building full-stack Next.js apps faster**. It supercharges your development workflow, allowing you to quickly integrate packages and scaffold resources for your application with best practices in mind.\n\nIn a matter of seconds, Kirimase installs and configures your choice of ORM (Prisma or Drizzle), Authentication (Auth.js, Clerk, Lucia, Kinde), Component Library (Shadcn-UI), Payments (Stripe) and Email (Resend). Kirimase also sets up tRPC with both client and server side implementation ready to go. Unlike template repos, each option is modular, meaning you can pick any combination of packages you would like.\n\nWith Kirimase's `generate` command, developers can jump right into building actual features without the need to manually create boilerplate code. After defining a new data entity, the command swiftly generates all boilerplate necessary for basic CRUD operations, including everything from the schema to server actions to routes & components. Build at the speed of thought!\n\nKirimase demo\n\nMotivation[](https://kirimase.dev/#motivation)\n----------------------------------------------\n\n### TL;DR[](https://kirimase.dev/#tldr)\n\nI love the Ruby on Rails CLI and always yearned for something like it for Next.js.\n\n### Longer Story[](https://kirimase.dev/#longer-story)\n\nI’ve always loved building with Next.js. The quality of the learning materials and simplicity of the git deployment workflow made it a dream to go from localhost to production. However, one of Next.js’ selling points, its lack of opinion on what tools to use with it, also led to an undesirable DX. More specifically, before writing a single line of code, I felt overwhelmed in my search for the best email/orm/analytics/test/etc. package. Once I did land on the right combination, I would need to spend a few hours sifting through documentation to configure everything to work together. In almost every case, I would find myself disheartened and eventually disinterested enough to push the task to another day.\n\nHaving heard great things about Rails in this regard, I gave it a go and was overjoyed by the simplicity that came with setting up new applications: namely, how quickly I went from `rails new` to actually building the business logic of the application. Ultimately, while I loved the rails CLI, I was excited to go back to Next.js as building UIs with React always felt more natural and enjoyable than ERB.\n\nEver since that experience there were two main things that I kept thinking about:\n\n1.  **gems**: why is it so damn complicated to install and configure packages in the JS ecosystem? Why can’t installing and configuring a package be as easy as `bundle add package`?\n2.  **scaffold**: why do I keep writing the same boilerplate for only slightly different db resources? It’s boring and error prone.\n\nAnd with that Kirimase was born 😊\n\nWhy Kirimase?[](https://kirimase.dev/#why-kirimase)\n---------------------------------------------------\n\nThe name is a funny story. Kirimase, in its original form, started as a way to quickly scaffold the files and packages necessary to get up and running with Drizzle ORM (similar to running npx prisma init). When it came time to brainstorm a name, I immediately thought, I want a cool name like Jotai. I was on my phone at the time and I fired up Google Translate with English to Japanese and typed in drizzle. Result: kirimase. I thought to myself, “Kirimase”, that’s exactly what I’m looking for, but a cool name like that has probably already been taken by _n_ projects before me. So I check NPM and to my surprise, it was available. So I quickly changed the package name and published the first version.\n\nLater that day, as I excitedly recounted this exact story to a friend, I pulled out Google Translate and up came my previous search result:\n\n> **English**: drizzle  \n> **Japanese**: Kiri_same_\n\n… turns out, I can’t read!\n\n![Image 4: Gorlami](https://kirimase.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fkirimase_gorlami.1fc73489.png&w=1920&q=75)\n\nQuick Overview[](https://kirimase.dev/#quick-overview)\n------------------------------------------------------\n\nKirimase has three main commands:\n\n*   `init`: configures the initial `kirimase.config.json` file that will be used for the `add` and `generate` commands\n*   `add`: select packages to install and configure\n*   `generate`: describe your data model and Kirimase will generate DB schema, migration, service files (queries and mutations), API Routes, tRPC routes, and basic UI to perform all crud operations\n\nExplore More[](https://kirimase.dev/#explore-more)\n--------------------------------------------------\n\n*   [Kirimase: The Tutorial](https://kirimase.dev/the-tutorial)\n*   [Getting Started](https://kirimase.dev/getting-started)\n*   [Commands](https://kirimase.dev/commands/init)\n*   [Tutorials and Demos](https://kirimase.dev/tutorials)\n\nFeedback and Contributions[](https://kirimase.dev/#feedback-and-contributions)\n------------------------------------------------------------------------------\n\nYour feedback and contributions are valuable! Explore the [contributing guide](https://kirimase.dev/contributing) to learn more about how you can contribute to Kirimase.\n\n[The Tutorial](https://kirimase.dev/the-tutorial \"The Tutorial\")",
  "usage": {
    "tokens": 1191
  }
}
```
