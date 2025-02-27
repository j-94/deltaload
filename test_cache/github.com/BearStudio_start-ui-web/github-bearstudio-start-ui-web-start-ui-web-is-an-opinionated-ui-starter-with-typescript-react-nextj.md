---
title: GitHub - BearStudio/start-ui-web: 🚀 Start UI [web] is an opinionated UI starter with 🟦 TypeScript, ⚛️ React, ⚫️ NextJS, ⚡️ Chakra UI, 🟦 tRPC, 🔐 Lucia Auth,  ▲ Prisma, 🏖️ TanStack Query, 📕 Storybook, 🎭 Playwright,📋 React Hook Form,◽From the 🐻  BearStudio Team
description: 🚀 Start UI [web] is an opinionated UI starter with 🟦 TypeScript, ⚛️ React, ⚫️ NextJS, ⚡️ Chakra UI, 🟦 tRPC, 🔐 Lucia Auth,  ▲ Prisma, 🏖️ TanStack Query, 📕 Storybook, 🎭 Playwright,📋 React Hook Form,◽From the 🐻  BearStudio Team - BearStudio/start-ui-web
url: https://github.com/BearStudio/start-ui-web
timestamp: 2025-01-20T15:31:33.955Z
domain: github.com
path: BearStudio_start-ui-web
---

# GitHub - BearStudio/start-ui-web: 🚀 Start UI [web] is an opinionated UI starter with 🟦 TypeScript, ⚛️ React, ⚫️ NextJS, ⚡️ Chakra UI, 🟦 tRPC, 🔐 Lucia Auth,  ▲ Prisma, 🏖️ TanStack Query, 📕 Storybook, 🎭 Playwright,📋 React Hook Form,◽From the 🐻  BearStudio Team


🚀 Start UI [web] is an opinionated UI starter with 🟦 TypeScript, ⚛️ React, ⚫️ NextJS, ⚡️ Chakra UI, 🟦 tRPC, 🔐 Lucia Auth,  ▲ Prisma, 🏖️ TanStack Query, 📕 Storybook, 🎭 Playwright,📋 React Hook Form,◽From the 🐻  BearStudio Team - BearStudio/start-ui-web


## Content

[![Image 21: Start UI Web](https://github.com/BearStudio/start-ui-web/raw/master/.github/assets/thumbnail.png)](https://github.com/BearStudio/start-ui-web/blob/master/.github/assets/thumbnail.png)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[](https://github.com/BearStudio/start-ui-web?screenshot=true#)

[![Image 22: Discord](https://camo.githubusercontent.com/6df6778e1c86f69553916d5957c5b20ac071d10275d4d9588f2e7a279a52aecd/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f343532373938343038343931363633333631)](https://go.bearstudio.fr/discord)

🚀 Start UI \[web\] is an opinionated frontend starter repository created & maintained by the [BearStudio Team](https://www.bearstudio.fr/team) and other contributors. It represents our team's up-to-date stack that we use when creating web apps for our clients.

Documentation
-------------

[](https://github.com/BearStudio/start-ui-web?screenshot=true#documentation)

For detailed information on how to use this project, please refer to the [documentation](https://docs.web.start-ui.com/). The documentation contains all the necessary information on installation, usage, and some guides.

Demo
----

[](https://github.com/BearStudio/start-ui-web?screenshot=true#demo)

A live read-only demonstration of what you will have when starting a project with 🚀 Start UI \[web\] is available on [demo.start-ui.com](https://demo.start-ui.com/).

Technologies
------------

[](https://github.com/BearStudio/start-ui-web?screenshot=true#technologies)

[![Image 23: Technologies logos of the starter](https://github.com/BearStudio/start-ui-web/raw/master/.github/assets/tech-logos.png)](https://github.com/BearStudio/start-ui-web/blob/master/.github/assets/tech-logos.png)

[🟦 TypeScript](https://www.typescriptlang.org/), [⚛️ React](https://react.dev/), [⚫️ NextJS](https://nextjs.org/), [⚡️ Chakra UI](https://chakra-ui.com/), [🟦 tRPC](https://trpc.io/), [▲ Prisma](https://www.prisma.io/), [🏖️ TanStack Query](https://react-query.tanstack.com/), [📕 Storybook](https://storybook.js.org/), [🎭 Playwright](https://playwright.dev/), [📋 React Hook Form](https://react-hook-form.com/) , [🌍 React i18next](https://react.i18next.com/)

Requirements
------------

[](https://github.com/BearStudio/start-ui-web?screenshot=true#requirements)

*   [NodeJS](https://nodejs.org/) \>\=20
*   [Pnpm](https://pnpm.io/)
*   [Docker](https://www.docker.com/) (or a [PostgreSQL](https://www.postgresql.org/) database)

Getting Started
---------------

[](https://github.com/BearStudio/start-ui-web?screenshot=true#getting-started)

pnpm create start-ui --web myApp

That will scaffold a new folder with the latest version of 🚀 Start UI \[web\] 🎉

Installation
------------

[](https://github.com/BearStudio/start-ui-web?screenshot=true#installation)

1.  Duplicate the `.env.example` file to a new `.env` file, and update the environment variables

Note

**Quick advices for local development**

*   **DON'T update** the **EMAIL\_SERVER** variable, because the default value will be used to catch the emails during the development.

2.  Install dependencies

3.  Setup and start the db with docker

Note

**Don't want to use docker?**

Setup a PostgreSQL database (locally or online) and replace the **DATABASE\_URL** environment variable. Then you can run `pnpm db:push` to update your database schema and then run `pnpm db:seed` to seed your database.

Development
-----------

[](https://github.com/BearStudio/start-ui-web?screenshot=true#development)

# Run the database in Docker (if not already started)
pnpm dk:start
# Run the development server
pnpm dev

### Emails in development

[](https://github.com/BearStudio/start-ui-web?screenshot=true#emails-in-development)

#### Maildev to catch emails

[](https://github.com/BearStudio/start-ui-web?screenshot=true#maildev-to-catch-emails)

In development, the emails will not be sent and will be catched by [maildev](https://github.com/maildev/maildev).

The maildev UI is available at [0.0.0.0:1080](http://0.0.0.0:1080/).

#### Preview emails

[](https://github.com/BearStudio/start-ui-web?screenshot=true#preview-emails)

Emails templates are built with `react-email` components in the `src/emails` folder.

You can preview an email template at `http://localhost:3000/devtools/email/{template}` where `{template}` is the name of the template file in the `src/emails/templates` folder.

Example: [Login Code](http://localhost:3000/devtools/email/login-code)

##### Email translation preview

[](https://github.com/BearStudio/start-ui-web?screenshot=true#email-translation-preview)

Add the language in the preview url like `http://localhost:3000/devtools/email/{template}/{language}` where `{language}` is the language key (`en`, `fr`, ...)

#### Email props preview

[](https://github.com/BearStudio/start-ui-web?screenshot=true#email-props-preview)

You can add search params to the preview url to pass as props to the template. `http://localhost:3000/devtools/email/{template}/?{propsName}={propsValue}`

### Storybook

[](https://github.com/BearStudio/start-ui-web?screenshot=true#storybook)

### Update theme typing

[](https://github.com/BearStudio/start-ui-web?screenshot=true#update-theme-typing)

When adding or updating theme components, component variations, sizes, colors and other theme foundations, you can extend the internal theme typings to provide nice autocomplete.

Just run the following command after updating the theme:

pnpm theme:generate-typing

### Generate custom icons components from svg files

[](https://github.com/BearStudio/start-ui-web?screenshot=true#generate-custom-icons-components-from-svg-files)

Put the custom svg files into the `src/components/Icons/svg-sources` folder and then run the following command:

pnpm theme:generate-icons

Warning

All svg icons should be svg files prefixed by `icon-` (example: `icon-externel-link`) with **24x24px** size, only **one shape** and **filled with `#000` color** (will be replaced by `currentColor`).

### Update color mode storage key

[](https://github.com/BearStudio/start-ui-web?screenshot=true#update-color-mode-storage-key)

You can update the storage key used to detect the color mode by updating this constant in the `src/theme/config.ts` file:

export const COLOR\_MODE\_STORAGE\_KEY \= 'start-ui-color-mode'; // Update the key according to your needs

### E2E Tests

[](https://github.com/BearStudio/start-ui-web?screenshot=true#e2e-tests)

E2E tests are setup with Playwright.

pnpm e2e     # Run tests in headless mode, this is the command executed in CI
pnpm e2e:ui  # Open a UI which allow you to run specific tests and see test execution

Tests are written in the `e2e` folder; there is also a `e2e/utils` folder which contains some utils to help writing tests.

Show hint on development environments
-------------------------------------

[](https://github.com/BearStudio/start-ui-web?screenshot=true#show-hint-on-development-environments)

Setup the `NEXT_PUBLIC_ENV_NAME` env variable with the name of the environment.

```
NEXT_PUBLIC_ENV_NAME="staging"
NEXT_PUBLIC_ENV_EMOJI="🔬"
NEXT_PUBLIC_ENV_COLOR_SCHEME="teal"
```

Translations
------------

[](https://github.com/BearStudio/start-ui-web?screenshot=true#translations)

### Setup the i18n Ally extension

[](https://github.com/BearStudio/start-ui-web?screenshot=true#setup-the-i18n-ally-extension)

We recommended using the [i18n Ally](https://marketplace.visualstudio.com/items?itemName=lokalise.i18n-ally) plugin for VS Code for translations management.

Create or edit the `.vscode/settings.json` file with the following settings:

{
  "i18n-ally.localesPaths": \["src/locales"\],
  "i18n-ally.keystyle": "nested",
  "i18n-ally.enabledFrameworks": \["general", "react", "i18next"\],
  "i18n-ally.namespace": true,
  "i18n-ally.defaultNamespace": "common",
  "i18n-ally.extract.autoDetect": true,
  "i18n-ally.keysInUse": \["common.languages.\*"\]
}

Production
----------

[](https://github.com/BearStudio/start-ui-web?screenshot=true#production)

pnpm install
pnpm storybook:build # Optional: Will expose the Storybook at \`/storybook\`
pnpm build
pnpm start

### Deploy with Docker

[](https://github.com/BearStudio/start-ui-web?screenshot=true#deploy-with-docker)

1.  Build the Docker image (replace `start-ui-web` with your project name)

```
docker build -t start-ui-web .
```

2.  Run the Docker image (replace `start-ui-web` with your project name)

```
docker run -p 80:3000 start-ui-web
```

Application will be exposed on port 80 ([http://localhost](http://localhost/))

## Metadata

```json
{
  "title": "GitHub - BearStudio/start-ui-web: 🚀 Start UI [web] is an opinionated UI starter with 🟦 TypeScript, ⚛️ React, ⚫️ NextJS, ⚡️ Chakra UI, 🟦 tRPC, 🔐 Lucia Auth,  ▲ Prisma, 🏖️ TanStack Query, 📕 Storybook, 🎭 Playwright,📋 React Hook Form,◽From the 🐻  BearStudio Team",
  "description": "🚀 Start UI [web] is an opinionated UI starter with 🟦 TypeScript, ⚛️ React, ⚫️ NextJS, ⚡️ Chakra UI, 🟦 tRPC, 🔐 Lucia Auth,  ▲ Prisma, 🏖️ TanStack Query, 📕 Storybook, 🎭 Playwright,📋 React Hook Form,◽From the 🐻  BearStudio Team - BearStudio/start-ui-web",
  "url": "https://github.com/BearStudio/start-ui-web?screenshot=true",
  "content": "[![Image 21: Start UI Web](https://github.com/BearStudio/start-ui-web/raw/master/.github/assets/thumbnail.png)](https://github.com/BearStudio/start-ui-web/blob/master/.github/assets/thumbnail.png)\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#)\n\n[![Image 22: Discord](https://camo.githubusercontent.com/6df6778e1c86f69553916d5957c5b20ac071d10275d4d9588f2e7a279a52aecd/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f343532373938343038343931363633333631)](https://go.bearstudio.fr/discord)\n\n🚀 Start UI \\[web\\] is an opinionated frontend starter repository created & maintained by the [BearStudio Team](https://www.bearstudio.fr/team) and other contributors. It represents our team's up-to-date stack that we use when creating web apps for our clients.\n\nDocumentation\n-------------\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#documentation)\n\nFor detailed information on how to use this project, please refer to the [documentation](https://docs.web.start-ui.com/). The documentation contains all the necessary information on installation, usage, and some guides.\n\nDemo\n----\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#demo)\n\nA live read-only demonstration of what you will have when starting a project with 🚀 Start UI \\[web\\] is available on [demo.start-ui.com](https://demo.start-ui.com/).\n\nTechnologies\n------------\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#technologies)\n\n[![Image 23: Technologies logos of the starter](https://github.com/BearStudio/start-ui-web/raw/master/.github/assets/tech-logos.png)](https://github.com/BearStudio/start-ui-web/blob/master/.github/assets/tech-logos.png)\n\n[🟦 TypeScript](https://www.typescriptlang.org/), [⚛️ React](https://react.dev/), [⚫️ NextJS](https://nextjs.org/), [⚡️ Chakra UI](https://chakra-ui.com/), [🟦 tRPC](https://trpc.io/), [▲ Prisma](https://www.prisma.io/), [🏖️ TanStack Query](https://react-query.tanstack.com/), [📕 Storybook](https://storybook.js.org/), [🎭 Playwright](https://playwright.dev/), [📋 React Hook Form](https://react-hook-form.com/) , [🌍 React i18next](https://react.i18next.com/)\n\nRequirements\n------------\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#requirements)\n\n*   [NodeJS](https://nodejs.org/) \\>\\=20\n*   [Pnpm](https://pnpm.io/)\n*   [Docker](https://www.docker.com/) (or a [PostgreSQL](https://www.postgresql.org/) database)\n\nGetting Started\n---------------\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#getting-started)\n\npnpm create start-ui --web myApp\n\nThat will scaffold a new folder with the latest version of 🚀 Start UI \\[web\\] 🎉\n\nInstallation\n------------\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#installation)\n\n1.  Duplicate the `.env.example` file to a new `.env` file, and update the environment variables\n\nNote\n\n**Quick advices for local development**\n\n*   **DON'T update** the **EMAIL\\_SERVER** variable, because the default value will be used to catch the emails during the development.\n\n2.  Install dependencies\n\n3.  Setup and start the db with docker\n\nNote\n\n**Don't want to use docker?**\n\nSetup a PostgreSQL database (locally or online) and replace the **DATABASE\\_URL** environment variable. Then you can run `pnpm db:push` to update your database schema and then run `pnpm db:seed` to seed your database.\n\nDevelopment\n-----------\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#development)\n\n# Run the database in Docker (if not already started)\npnpm dk:start\n# Run the development server\npnpm dev\n\n### Emails in development\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#emails-in-development)\n\n#### Maildev to catch emails\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#maildev-to-catch-emails)\n\nIn development, the emails will not be sent and will be catched by [maildev](https://github.com/maildev/maildev).\n\nThe maildev UI is available at [0.0.0.0:1080](http://0.0.0.0:1080/).\n\n#### Preview emails\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#preview-emails)\n\nEmails templates are built with `react-email` components in the `src/emails` folder.\n\nYou can preview an email template at `http://localhost:3000/devtools/email/{template}` where `{template}` is the name of the template file in the `src/emails/templates` folder.\n\nExample: [Login Code](http://localhost:3000/devtools/email/login-code)\n\n##### Email translation preview\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#email-translation-preview)\n\nAdd the language in the preview url like `http://localhost:3000/devtools/email/{template}/{language}` where `{language}` is the language key (`en`, `fr`, ...)\n\n#### Email props preview\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#email-props-preview)\n\nYou can add search params to the preview url to pass as props to the template. `http://localhost:3000/devtools/email/{template}/?{propsName}={propsValue}`\n\n### Storybook\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#storybook)\n\n### Update theme typing\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#update-theme-typing)\n\nWhen adding or updating theme components, component variations, sizes, colors and other theme foundations, you can extend the internal theme typings to provide nice autocomplete.\n\nJust run the following command after updating the theme:\n\npnpm theme:generate-typing\n\n### Generate custom icons components from svg files\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#generate-custom-icons-components-from-svg-files)\n\nPut the custom svg files into the `src/components/Icons/svg-sources` folder and then run the following command:\n\npnpm theme:generate-icons\n\nWarning\n\nAll svg icons should be svg files prefixed by `icon-` (example: `icon-externel-link`) with **24x24px** size, only **one shape** and **filled with `#000` color** (will be replaced by `currentColor`).\n\n### Update color mode storage key\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#update-color-mode-storage-key)\n\nYou can update the storage key used to detect the color mode by updating this constant in the `src/theme/config.ts` file:\n\nexport const COLOR\\_MODE\\_STORAGE\\_KEY \\= 'start-ui-color-mode'; // Update the key according to your needs\n\n### E2E Tests\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#e2e-tests)\n\nE2E tests are setup with Playwright.\n\npnpm e2e     # Run tests in headless mode, this is the command executed in CI\npnpm e2e:ui  # Open a UI which allow you to run specific tests and see test execution\n\nTests are written in the `e2e` folder; there is also a `e2e/utils` folder which contains some utils to help writing tests.\n\nShow hint on development environments\n-------------------------------------\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#show-hint-on-development-environments)\n\nSetup the `NEXT_PUBLIC_ENV_NAME` env variable with the name of the environment.\n\n```\nNEXT_PUBLIC_ENV_NAME=\"staging\"\nNEXT_PUBLIC_ENV_EMOJI=\"🔬\"\nNEXT_PUBLIC_ENV_COLOR_SCHEME=\"teal\"\n```\n\nTranslations\n------------\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#translations)\n\n### Setup the i18n Ally extension\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#setup-the-i18n-ally-extension)\n\nWe recommended using the [i18n Ally](https://marketplace.visualstudio.com/items?itemName=lokalise.i18n-ally) plugin for VS Code for translations management.\n\nCreate or edit the `.vscode/settings.json` file with the following settings:\n\n{\n  \"i18n-ally.localesPaths\": \\[\"src/locales\"\\],\n  \"i18n-ally.keystyle\": \"nested\",\n  \"i18n-ally.enabledFrameworks\": \\[\"general\", \"react\", \"i18next\"\\],\n  \"i18n-ally.namespace\": true,\n  \"i18n-ally.defaultNamespace\": \"common\",\n  \"i18n-ally.extract.autoDetect\": true,\n  \"i18n-ally.keysInUse\": \\[\"common.languages.\\*\"\\]\n}\n\nProduction\n----------\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#production)\n\npnpm install\npnpm storybook:build # Optional: Will expose the Storybook at \\`/storybook\\`\npnpm build\npnpm start\n\n### Deploy with Docker\n\n[](https://github.com/BearStudio/start-ui-web?screenshot=true#deploy-with-docker)\n\n1.  Build the Docker image (replace `start-ui-web` with your project name)\n\n```\ndocker build -t start-ui-web .\n```\n\n2.  Run the Docker image (replace `start-ui-web` with your project name)\n\n```\ndocker run -p 80:3000 start-ui-web\n```\n\nApplication will be exposed on port 80 ([http://localhost](http://localhost/))",
  "usage": {
    "tokens": 2183
  }
}
```
