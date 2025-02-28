---
title: Building a Job Board with Next.js, Chakra UI, and Directus
description: This article covers the development of the core components of a job board step-by-step, using Next.js for the frontend and Directus as the backend tool to manage job data.
url: https://docs.directus.io/blog/building-a-job-board.html
timestamp: 2025-01-20T15:52:48.635Z
domain: docs.directus.io
path: blog_building-a-job-board.html
---

# Building a Job Board with Next.js, Chakra UI, and Directus


This article covers the development of the core components of a job board step-by-step, using Next.js for the frontend and Directus as the backend tool to manage job data.


## Content

[Developer Blog](https://docs.directus.io/blog/)

Published September 12th, 2023

Written By

![Image 11: Esther Agbaje](https://marketing.directus.app/assets/6b059120-24b2-4f99-8bd5-c91fec7c687e?key=circle)

Esther Agbaje

Developer Advocate

With Thanks To

Kevin Lewis

Job boards are an ideal way to connect job seekers to career opportunities. However, creating one involves far more than putting up postings. As developers, we need to incorporate essential features like job listing management, search functionality, and more.

A well-designed job board allows employers to effortlessly post and manage job openings. It also enables job seekers to browse through jobs using intuitive filtering and searching.

In this tutorial, we will cover the development of the core components of a job board step-by-step, using Next.js for the frontend and Directus as the backend tool to manage job data.

Here's a quick overview of how the job board looks to job seekers:

![Image 12: Job Portal Overview](https://marketing.directus.app/assets/57e3e75d-d240-4a6f-b751-0af945983d73.gif)

**TL;DR: If you'd like to immediately access the code repository, get it [here](https://github.com/directus-community/job-board)**

Prerequisites [​](https://docs.directus.io/blog/building-a-job-board.html#prerequisites)
----------------------------------------------------------------------------------------

To follow along with this tutorial, you need to have the following:

*   A Directus self-hosted or cloud account
*   Familiarity with TypeScript, React and Next.js
*   Basic knowledge of Chakra UI - a React component library.

Setting up the Jobs Collection in Directus [​](https://docs.directus.io/blog/building-a-job-board.html#setting-up-the-jobs-collection-in-directus)
--------------------------------------------------------------------------------------------------------------------------------------------------

Before we can start fetching and displaying job listings, we need to define the data model that will store our job data in Directus.

Log in to your Directus app and navigate to Settings \> Data Model. Click the + icon to create a new collection called “jobs”.

Add the following fields and save:

*   **title** (Type: String, Interface: Input)
*   **company** (Type: String, Interface: Input)
*   **location** (Type: String, Interface: Input)
*   **logo** (Type: UUID, Interface: Image)
*   **tags** (Type: JSON, Interface: Tags)
*   **remote** (Type: Boolean, Interface: Toggle)
*   **datePosted** (Type: DateTime, Interface: DateTime)
*   **salaryRange** (Type: String, Interface: Input)
*   **content** (Type: Text, Interface: WYSIWYG)

### Adding Content to the Jobs Collection [​](https://docs.directus.io/blog/building-a-job-board.html#adding-content-to-the-jobs-collection)

With the data model in place, we're now ready to populate our collection with some real job listings.

From the Directus sidebar, navigate to "Content Module" and select the "Jobs" collection we created earlier.

Go ahead and add a few sample jobs to have content to work with as we build out the frontend interface. You can always come back later to enter more postings as needed.

Building the Frontend Application [​](https://docs.directus.io/blog/building-a-job-board.html#building-the-frontend-application)
--------------------------------------------------------------------------------------------------------------------------------

With the backend in place, we need to set up a working frontend interface to display the job listings.

### Installing Next.js [​](https://docs.directus.io/blog/building-a-job-board.html#installing-next-js)

In your terminal, run the following command:

```
npx create-next-app@latest job-board

cd job-board
```

```
npx create-next-app@latest job-board

cd job-board
```

On installation, choose the following:

```
Would you like to use TypeScript? Yes
Would you like to use ESLint? Yes
Would you like to use Tailwind CSS? No 
Would you like to use `src/` directory? Yes
Would you like to use App Router? (recommended) No
Would you like to customize the default import alias?  Yes
What import alias would you like configured? @/*
```

```
Would you like to use TypeScript? Yes
Would you like to use ESLint? Yes
Would you like to use Tailwind CSS? No 
Would you like to use `src/` directory? Yes
Would you like to use App Router? (recommended) No
Would you like to customize the default import alias?  Yes
What import alias would you like configured? @/*
```

Remove boilerplate code from `index.tsx` and update meta tags:

tsx

```
import Head from 'next/head';

export default function Home() {
  return (
    <>
      <Head>
        <title>Job Board</title>
        <meta name='description' content='Job board app to connect job seekers to opportunities' />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <main>
            <h1>Find Your Dream Job</h1>
      </main>
    </>
  );
}
```

```
import Head from 'next/head';

export default function Home() {
  return (
    <>
      <Head>
        <title>Job Board</title>
        <meta name='description' content='Job board app to connect job seekers to opportunities' />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <main>
            <h1>Find Your Dream Job</h1>
      </main>
    </>
  );
}
```

Start your local server using the command:

You should have your app running at **[http://localhost:3000](http://localhost:3000/)**

### Installing the required dependencies [​](https://docs.directus.io/blog/building-a-job-board.html#installing-the-required-dependencies)

Run the following command in your terminal:

```
npm install @directus/sdk @chakra-ui/react @emotion/react @emotion/styled framer-motion react-icons
```

```
npm install @directus/sdk @chakra-ui/react @emotion/react @emotion/styled framer-motion react-icons
```

*   Directus SDK for fetching jobs
*   Chakra UI for styling (Emotion and Framer are Chakra UI dependencies)
*   React icons

### Setting up Chakra UI [​](https://docs.directus.io/blog/building-a-job-board.html#setting-up-chakra-ui)

To use Chakra UI in your project, you need to set up the `ChakraProvider` at the root of your application.

Go to `pages/_app.tsx` and wrap the Component with the `ChakraProvider`.

tsx

```
// pages/_app.tsx
import type { AppProps } from 'next/app';
import { ChakraProvider } from '@chakra-ui/react'

export default function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <Component {...pageProps} />
    </ChakraProvider>
  );
}
```

```
// pages/_app.tsx
import type { AppProps } from 'next/app';
import { ChakraProvider } from '@chakra-ui/react'

export default function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <Component {...pageProps} />
    </ChakraProvider>
  );
}
```

Displaying the Job Listings [​](https://docs.directus.io/blog/building-a-job-board.html#displaying-the-job-listings)
--------------------------------------------------------------------------------------------------------------------

To display the job listings from Directus, we need to set up the types for our jobs and also create two components: the `JobCard` and `JobList` components.

### Defining the Types for the Jobs [​](https://docs.directus.io/blog/building-a-job-board.html#defining-the-types-for-the-jobs)

Since we’re working with TypeScript, to ensure type safety when working with job data from Directus, let’s set up an interface that defines the expected shape of each job object.

At the root of your project, create a new directory called lib, and inside it, a new file called `directus.ts`.

js

```
export type Job = {
  id: number;
  title: string;
  company: string;
  content: string;
  location: string;
  datePosted: string;
  logo: string;
  tags: string[];
  remote: boolean;
  salaryRange: string;
};

type Schema = {
  jobs: Job[];
};
```

```
export type Job = {
  id: number;
  title: string;
  company: string;
  content: string;
  location: string;
  datePosted: string;
  logo: string;
  tags: string[];
  remote: boolean;
  salaryRange: string;
};

type Schema = {
  jobs: Job[];
};
```

### Building the Job Card Component [​](https://docs.directus.io/blog/building-a-job-board.html#building-the-job-card-component)

Create a `src/job-card.tsx` file and input this code:

tsx

```
import { Avatar, Box, HStack, Heading, Icon, LinkBox, LinkOverlay, Stack, Tag, Text } from '@chakra-ui/react';
import NextLink from 'next/link';
import { MdBusiness, MdLocationPin, MdOutlineAttachMoney } from 'react-icons/md';
import { Job } from '@/lib/directus';
import { friendlyTime } from '@/lib/friendly-time';

type JobCardProps = {
  data: Job;
};

export function JobCard(props: JobCardProps) {
  const { data, ...rest } = props;
  const { id, title, company, location, datePosted, logo, tags, remote, salaryRange  } = data;

  return (
    <Box
      border='1px solid'
      borderColor='gray.300'
      borderRadius='md'
      _hover={{ borderColor: 'black', boxShadow: 'sm' }}
      p='6'
      {...rest}
    >
      <LinkBox as='article'>
        <Stack direction={{ base: 'column', lg: 'row' }} spacing='8'>
          <Avatar size='lg' name={title} src={logo} />
          <Box>
            <LinkOverlay as={NextLink} href={`/${id}`}>
              <Heading size='md'>{title}</Heading>
            </LinkOverlay>
            <Text>{company}</Text>
            <Stack mt='2' spacing={1}>
              <HStack spacing={1}>
                <Icon as={MdLocationPin} boxSize={4} />
                <Text>{location}</Text>
              </HStack>
              <HStack spacing={1}>
                <Icon as={MdBusiness} boxSize={4} />
                <Text>{remote === 'true' ? 'Remote' : 'Onsite'}</Text>
              </HStack>
              <HStack spacing={1}>
                <Icon as={MdOutlineAttachMoney} boxSize={4} />
                <Text>{salaryRange}</Text>
              </HStack>
            </Stack>
          </Box>
          <HStack spacing={2} flex='1'>
            {tags.map((tag, index) => (
              <Tag key={index} colorScheme='gray'>
                {tag}
              </Tag>
            ))}
          </HStack>
          <Text alignSelf={{ base: 'left', lg: 'center' }}>
            Posted {friendlyTime(new Date(datePosted))}
          </Text>
        </Stack>
      </LinkBox>
    </Box>
  );
}
```

```
import { Avatar, Box, HStack, Heading, Icon, LinkBox, LinkOverlay, Stack, Tag, Text } from '@chakra-ui/react';
import NextLink from 'next/link';
import { MdBusiness, MdLocationPin, MdOutlineAttachMoney } from 'react-icons/md';
import { Job } from '@/lib/directus';
import { friendlyTime } from '@/lib/friendly-time';

type JobCardProps = {
  data: Job;
};

export function JobCard(props: JobCardProps) {
  const { data, ...rest } = props;
  const { id, title, company, location, datePosted, logo, tags, remote, salaryRange  } = data;

  return (
    <Box
      border='1px solid'
      borderColor='gray.300'
      borderRadius='md'
      _hover={{ borderColor: 'black', boxShadow: 'sm' }}
      p='6'
      {...rest}
    >
      <LinkBox as='article'>
        <Stack direction={{ base: 'column', lg: 'row' }} spacing='8'>
          <Avatar size='lg' name={title} src={logo} />
          <Box>
            <LinkOverlay as={NextLink} href={`/${id}`}>
              <Heading size='md'>{title}</Heading>
            </LinkOverlay>
            <Text>{company}</Text>
            <Stack mt='2' spacing={1}>
              <HStack spacing={1}>
                <Icon as={MdLocationPin} boxSize={4} />
                <Text>{location}</Text>
              </HStack>
              <HStack spacing={1}>
                <Icon as={MdBusiness} boxSize={4} />
                <Text>{remote === 'true' ? 'Remote' : 'Onsite'}</Text>
              </HStack>
              <HStack spacing={1}>
                <Icon as={MdOutlineAttachMoney} boxSize={4} />
                <Text>{salaryRange}</Text>
              </HStack>
            </Stack>
          </Box>
          <HStack spacing={2} flex='1'>
            {tags.map((tag, index) => (
              <Tag key={index} colorScheme='gray'>
                {tag}
              </Tag>
            ))}
          </HStack>
          <Text alignSelf={{ base: 'left', lg: 'center' }}>
            Posted {friendlyTime(new Date(datePosted))}
          </Text>
        </Stack>
      </LinkBox>
    </Box>
  );
}
```

Inside the `lib` directory and add a `friendly-time.ts` file to format the code:

js

```
export const friendlyTime = (date: Date) => {
  const seconds = Math.floor((new Date().getTime() - date.getTime()) / 1000);

  let interval = seconds / 31536000;

  if (interval > 1) {
    return Math.floor(interval) + ' years ago';
  }
  interval = seconds / 2592000;
  if (interval > 1) {
    return Math.floor(interval) + ' months ago';
  }
  interval = seconds / 86400;
  if (interval > 1) {
    return Math.floor(interval) + ' days ago';
  }
  interval = seconds / 3600;
  if (interval > 1) {
    return Math.floor(interval) + ' hours ago';
  }
  interval = seconds / 60;
  if (interval > 1) {
    return Math.floor(interval) + ' minutes ago';
  }
  return Math.floor(seconds) + ' seconds ago';
};
```

```
export const friendlyTime = (date: Date) => {
  const seconds = Math.floor((new Date().getTime() - date.getTime()) / 1000);

  let interval = seconds / 31536000;

  if (interval > 1) {
    return Math.floor(interval) + ' years ago';
  }
  interval = seconds / 2592000;
  if (interval > 1) {
    return Math.floor(interval) + ' months ago';
  }
  interval = seconds / 86400;
  if (interval > 1) {
    return Math.floor(interval) + ' days ago';
  }
  interval = seconds / 3600;
  if (interval > 1) {
    return Math.floor(interval) + ' hours ago';
  }
  interval = seconds / 60;
  if (interval > 1) {
    return Math.floor(interval) + ' minutes ago';
  }
  return Math.floor(seconds) + ' seconds ago';
};
```

*   This component is styled and built using the `Box`,` Stack`, `HStack`, and more components from Chakra UI
*   The posted date is displayed using the `friendlyTime` code to format the `datePosted` into a user-friendly time format (e.g., "2 days ago")

### Building the Job List Component [​](https://docs.directus.io/blog/building-a-job-board.html#building-the-job-list-component)

Inside the components directory, create a `job-list.tsx` file that shows the list of jobs

tsx

```
import { Stack } from '@chakra-ui/react';
import { JobCard } from './job-card';
import { Job } from '@/lib/directus';

type JobListProps = {
  data: Job[];
};

export function JobList(props: JobListProps) {
  const { data } = props;

  return (
    <Stack spacing='4'>
      {data.map((job, index) => (
        <JobCard key={index} data={job} />
      ))}
    </Stack>
  );
}
```

```
import { Stack } from '@chakra-ui/react';
import { JobCard } from './job-card';
import { Job } from '@/lib/directus';

type JobListProps = {
  data: Job[];
};

export function JobList(props: JobListProps) {
  const { data } = props;

  return (
    <Stack spacing='4'>
      {data.map((job, index) => (
        <JobCard key={index} data={job} />
      ))}
    </Stack>
  );
}
```

### Fetching the Jobs from Directus [​](https://docs.directus.io/blog/building-a-job-board.html#fetching-the-jobs-from-directus)

A crucial part of the job board is being able to fetch and display the latest job listings. To accomplish this, we’re going to use the Directus SDK.

At the root of your project, create a `.env` file and add your Directus URL

```
DIRECTUS_URL=add-your-directus-url-here
```

```
DIRECTUS_URL=add-your-directus-url-here
```

To share a single instance of the Directus SDK between multiple pages in this project, we need to set up a helper file that can be imported later.

Inside the `directus.ts` file, create a Directus client by importing the `createDirectus` hook and `rest` composable.

js

```
import { createDirectus, rest } from '@directus/sdk';

export interface Job {
  id: number;
  title: string;
  company: string;
  content: string;
  location: string;
  datePosted: string;
  logo: string;
  tags: string[];
  remote: boolean;
  salaryRange: string;
}

interface Schema {
  jobs: Job[];
}

const directus = createDirectus<Schema>(process.env.DIRECTUS_URL!).with(rest());

export default directus;
```

```
import { createDirectus, rest } from '@directus/sdk';

export interface Job {
  id: number;
  title: string;
  company: string;
  content: string;
  location: string;
  datePosted: string;
  logo: string;
  tags: string[];
  remote: boolean;
  salaryRange: string;
}

interface Schema {
  jobs: Job[];
}

const directus = createDirectus<Schema>(process.env.DIRECTUS_URL!).with(rest());

export default directus;
```

Now, go over to `index.tsx` and update the code to render the jobs

tsx

```
import { JobList } from '@/components/job-list';
import { Box, Heading, Stack } from '@chakra-ui/react';
import { readItems } from '@directus/sdk';
import Head from 'next/head';
import directus, { Job } from '../lib/directus';

export default function Home({ jobs }: { jobs: Job[] }) {
  return (
    <>
      <Head>
        <title>Job Board</title>
        <meta
          name='description'
          content='Job board app to connect job seekers to opportunities'
        />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <main>
        <Box p={{ base: '12', lg: '24' }}>
          <Stack mb='8' maxW='sm'>
            <Heading>Find Your Dream Job</Heading>
          </Stack>
          <JobList data={jobs} />
        </Box>
      </main>
    </>
  );
}

export async function getStaticProps() {
  try {
    const jobs = await directus.request(
      readItems('jobs', {
        limit: -1,
        fields: ['*'],
      })
    );

    if (!jobs) {
      return {
        notFound: true,
      };
    }

    // Format the image field to have the full URL
    jobs.forEach((job) => {
      job.logo = `${process.env.DIRECTUS_URL}assets/${job.logo}`;
    });

    return {
      props: {
        jobs,
      },
    };
  } catch (error) {
    console.error('Error fetching jobs:', error);
    return {
      notFound: true,
    };
  }
}
```

```
import { JobList } from '@/components/job-list';
import { Box, Heading, Stack } from '@chakra-ui/react';
import { readItems } from '@directus/sdk';
import Head from 'next/head';
import directus, { Job } from '../lib/directus';

export default function Home({ jobs }: { jobs: Job[] }) {
  return (
    <>
      <Head>
        <title>Job Board</title>
        <meta
          name='description'
          content='Job board app to connect job seekers to opportunities'
        />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <main>
        <Box p={{ base: '12', lg: '24' }}>
          <Stack mb='8' maxW='sm'>
            <Heading>Find Your Dream Job</Heading>
          </Stack>
          <JobList data={jobs} />
        </Box>
      </main>
    </>
  );
}

export async function getStaticProps() {
  try {
    const jobs = await directus.request(
      readItems('jobs', {
        limit: -1,
        fields: ['*'],
      })
    );

    if (!jobs) {
      return {
        notFound: true,
      };
    }

    // Format the image field to have the full URL
    jobs.forEach((job) => {
      job.logo = `${process.env.DIRECTUS_URL}assets/${job.logo}`;
    });

    return {
      props: {
        jobs,
      },
    };
  } catch (error) {
    console.error('Error fetching jobs:', error);
    return {
      notFound: true,
    };
  }
}
```

You should have something like this on your frontend

![Image 13: Job Board ](https://marketing.directus.app/assets/9fb98c51-69e4-4e0e-940d-33028f8270eb.png)

Displaying the Job Detail [​](https://docs.directus.io/blog/building-a-job-board.html#displaying-the-job-detail)
----------------------------------------------------------------------------------------------------------------

With the ability to fetch job listings from Directus established, the next step is to dynamically display each job's content on individual job pages. Next.js provides a streamlined way to do this through its automatic static and server-side rendering features.

But first, we need to build out a `JobContent` Component.

### Building the Job Content Component [​](https://docs.directus.io/blog/building-a-job-board.html#building-the-job-content-component)

Within the `components` folder, create a `job-content.tsx` file to show the job content for each job

tsx

```
import { Job } from '@/lib/directus';
import { Avatar, Box, Button, HStack, Heading } from '@chakra-ui/react';
import Link from 'next/link';

type JobContentProps = {
  data: Job;
};

export function JobContent(props: JobContentProps) {
  const { data } = props;
  const { content, logo, title, company } = data;

  return (
    <Box px={{ base: '12', lg: '24' }}>
      <Button as={Link} href='/'>
        Back to jobs
      </Button>
      <Box py='16'>
        <HStack spacing='4'>
          <Avatar size='lg' name={title} src={logo} />
          <Heading size='lg'>{company}</Heading>
        </HStack>
        <Box maxW='3xl' dangerouslySetInnerHTML={{ __html: content }} />
      </Box>
    </Box>
  );
}
```

```
import { Job } from '@/lib/directus';
import { Avatar, Box, Button, HStack, Heading } from '@chakra-ui/react';
import Link from 'next/link';

type JobContentProps = {
  data: Job;
};

export function JobContent(props: JobContentProps) {
  const { data } = props;
  const { content, logo, title, company } = data;

  return (
    <Box px={{ base: '12', lg: '24' }}>
      <Button as={Link} href='/'>
        Back to jobs
      </Button>
      <Box py='16'>
        <HStack spacing='4'>
          <Avatar size='lg' name={title} src={logo} />
          <Heading size='lg'>{company}</Heading>
        </HStack>
        <Box maxW='3xl' dangerouslySetInnerHTML={{ __html: content }} />
      </Box>
    </Box>
  );
}
```

To dynamically render the job pages, create a `[jobId].tsx` in the `pages` directory and put the following code in it:

tsx

```
import { readItem, readItems } from '@directus/sdk';
import { GetStaticPaths, GetStaticProps } from 'next';
import directus from '../lib/directus';
import { Box } from '@chakra-ui/react';
import { JobContent } from '@/components/job-content';
import { Job } from '../lib/directus';

type JobDetailsProps = {
  job: Job;
};

export default function JobDetails(props: JobDetailsProps) {
  const { job } = props;
  return (
    <Box p={{ base: '12', lg: '24' }}>
      <JobContent data={job} />
    </Box>
  );
}

export const getStaticPaths: GetStaticPaths = async () => {
  try {
    const jobs = await directus.request(
      readItems('jobs', {
        limit: -1,
        fields: ['id'],
      })
    );
    const paths = jobs.map((job) => {
      // Access the data property to get the array of jobs
      return {
        params: { jobId: job.id.toString() },
      };
    });
    return {
      paths: paths || [],
      fallback: false,
    };
  } catch (error) {
    console.error('Error fetching paths:', error);
    return {
      paths: [],
      fallback: false,
    };
  }
};

export const getStaticProps: GetStaticProps = async (context) => {
  try {
    const jobId = context.params?.jobId as string;

    const job = await directus.request(
      readItem('jobs', jobId, {
        fields: ['*'],
      })
    );

    if (job) {
      job.logo = `${process.env.DIRECTUS_URL}assets/${job.logo}`;
    }

    return {
      props: {
        job,
      },
    };
  } catch (error) {
    console.error('Error fetching job:', error);
    return {
      notFound: true,
    };
  }
};
```

```
import { readItem, readItems } from '@directus/sdk';
import { GetStaticPaths, GetStaticProps } from 'next';
import directus from '../lib/directus';
import { Box } from '@chakra-ui/react';
import { JobContent } from '@/components/job-content';
import { Job } from '../lib/directus';

type JobDetailsProps = {
  job: Job;
};

export default function JobDetails(props: JobDetailsProps) {
  const { job } = props;
  return (
    <Box p={{ base: '12', lg: '24' }}>
      <JobContent data={job} />
    </Box>
  );
}

export const getStaticPaths: GetStaticPaths = async () => {
  try {
    const jobs = await directus.request(
      readItems('jobs', {
        limit: -1,
        fields: ['id'],
      })
    );
    const paths = jobs.map((job) => {
      // Access the data property to get the array of jobs
      return {
        params: { jobId: job.id.toString() },
      };
    });
    return {
      paths: paths || [],
      fallback: false,
    };
  } catch (error) {
    console.error('Error fetching paths:', error);
    return {
      paths: [],
      fallback: false,
    };
  }
};

export const getStaticProps: GetStaticProps = async (context) => {
  try {
    const jobId = context.params?.jobId as string;

    const job = await directus.request(
      readItem('jobs', jobId, {
        fields: ['*'],
      })
    );

    if (job) {
      job.logo = `${process.env.DIRECTUS_URL}assets/${job.logo}`;
    }

    return {
      props: {
        job,
      },
    };
  } catch (error) {
    console.error('Error fetching job:', error);
    return {
      notFound: true,
    };
  }
};
```

The code fetches and renders dynamic job details using static site generation with Next.js.

*   Static Paths Generation (`getStaticPaths`):
    
    *   Implements the `getStaticPath`s function, a part of Next.js's static site generation.
    *   Requests job data using Directus's `readItems` function with `limit: -1` to fetch all job IDs.
    *   Maps retrieved job IDs to an array of `params` objects to generate dynamic routes.
    *   Sets the paths array to the generated paths and `fallback` to` false` (no fallback behavior).
*   Static Props Generation (`getStaticProps`):
    
    *   Implements the `getStaticProps` function, used in static site generation to fetch data for a specific page.
    *   Extracts the`jobId` parameter from the context object to identify the requested job.
    *   Requests detailed job information using Directus's `readItem` function for the specified job.
    *   Modifies the job object by appending the `logo` URL with the `DIRECTUS_URL`.
    *   Returns fetched job data within the `props` object.

Now, whenever you click on a job, you’ll be able to see all the details about that job

![Image 14: Job Detail](https://marketing.directus.app/assets/3699c2b7-b8b4-4443-af40-f1e4557fa6e1.png)

Implementing the Search Functionality [​](https://docs.directus.io/blog/building-a-job-board.html#implementing-the-search-functionality)
----------------------------------------------------------------------------------------------------------------------------------------

To enable users to search for jobs by title in our application, we need to build out the functionality for querying the jobs data store based on the job title field. We also need to build out the search input UI to handle this.

In `index.tsx` update the code as follows:

tsx

```
export default function Home(props: { jobs: Job[] }) {
  const { jobs } = props;
  const router = useRouter();

  const searchQuery = router.query.search?.toString();
  const searchResult = searchQuery
    ? jobs.filter((job) => {
        return job.title.toLowerCase().includes(searchQuery.toLowerCase());
      })
    : jobs;

  return (
    <>
      <Head>
        <title>Job Board</title>
        <meta
          name='description'
          content='Job board app to connect job seekers to opportunities'
        />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <main>
        <Box p={{ base: '12', lg: '24' }}>
          <Stack mb='8' direction={{ base: 'column', md: 'row' }}>
            <Heading flex='1'>Find Your Dream Job</Heading>
            <InputGroup w='auto'>
              <InputLeftElement color='gray.400'>
                <FaSearch />
              </InputLeftElement>
              <Input
                placeholder='Search jobs...'
                onChange={(event) => {
                  const value = event.target.value;

                  router.replace({
                    query: { search: value },
                  });
                }}
              />
            </InputGroup>
          </Stack>
          <JobList data={searchResult} />
        </Box>
      </main>
    </>
  );
}
```

```
export default function Home(props: { jobs: Job[] }) {
  const { jobs } = props;
  const router = useRouter();

  const searchQuery = router.query.search?.toString();
  const searchResult = searchQuery
    ? jobs.filter((job) => {
        return job.title.toLowerCase().includes(searchQuery.toLowerCase());
      })
    : jobs;

  return (
    <>
      <Head>
        <title>Job Board</title>
        <meta
          name='description'
          content='Job board app to connect job seekers to opportunities'
        />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <link rel='icon' href='/favicon.ico' />
      </Head>
      <main>
        <Box p={{ base: '12', lg: '24' }}>
          <Stack mb='8' direction={{ base: 'column', md: 'row' }}>
            <Heading flex='1'>Find Your Dream Job</Heading>
            <InputGroup w='auto'>
              <InputLeftElement color='gray.400'>
                <FaSearch />
              </InputLeftElement>
              <Input
                placeholder='Search jobs...'
                onChange={(event) => {
                  const value = event.target.value;

                  router.replace({
                    query: { search: value },
                  });
                }}
              />
            </InputGroup>
          </Stack>
          <JobList data={searchResult} />
        </Box>
      </main>
    </>
  );
}
```

*   We use the `useRouter` hook from Next.js to access the query parameters from the URL.
*   If a search query was provided, we filter the jobs array to only include those whose title matched the search query in a case-insensitive manner. If no search query was present, we simply set the `searchResult` to the original jobs array without any filtering.

[Here's the repository to find the code](https://github.com/directus-community/job-board)

Conclusion [​](https://docs.directus.io/blog/building-a-job-board.html#conclusion)
----------------------------------------------------------------------------------

In this tutorial, you've learned how to fetch job data from a Directus instance, display it on your app, and implement search functionality.

Some natural next steps could include:

*   Implementing user authentication via JWT tokens to allow job seekers to create custom profiles, save jobs, and track application status
*   Integrating email and notification systems to allow job alerts to be automatically sent to users when new jobs are posted
*   Adding advanced filtering and sorting of job results beyond just search title

If you have any questions or need further assistance, please feel free to drop by our [Discord server](https://directus.chat/).

## Metadata

```json
{
  "title": "Building a Job Board with Next.js, Chakra UI, and Directus",
  "description": "This article covers the development of the core components of a job board step-by-step, using Next.js for the frontend and Directus as the backend tool to manage job data.",
  "url": "https://docs.directus.io/blog/building-a-job-board.html",
  "content": "[Developer Blog](https://docs.directus.io/blog/)\n\nPublished September 12th, 2023\n\nWritten By\n\n![Image 11: Esther Agbaje](https://marketing.directus.app/assets/6b059120-24b2-4f99-8bd5-c91fec7c687e?key=circle)\n\nEsther Agbaje\n\nDeveloper Advocate\n\nWith Thanks To\n\nKevin Lewis\n\nJob boards are an ideal way to connect job seekers to career opportunities. However, creating one involves far more than putting up postings. As developers, we need to incorporate essential features like job listing management, search functionality, and more.\n\nA well-designed job board allows employers to effortlessly post and manage job openings. It also enables job seekers to browse through jobs using intuitive filtering and searching.\n\nIn this tutorial, we will cover the development of the core components of a job board step-by-step, using Next.js for the frontend and Directus as the backend tool to manage job data.\n\nHere's a quick overview of how the job board looks to job seekers:\n\n![Image 12: Job Portal Overview](https://marketing.directus.app/assets/57e3e75d-d240-4a6f-b751-0af945983d73.gif)\n\n**TL;DR: If you'd like to immediately access the code repository, get it [here](https://github.com/directus-community/job-board)**\n\nPrerequisites [​](https://docs.directus.io/blog/building-a-job-board.html#prerequisites)\n----------------------------------------------------------------------------------------\n\nTo follow along with this tutorial, you need to have the following:\n\n*   A Directus self-hosted or cloud account\n*   Familiarity with TypeScript, React and Next.js\n*   Basic knowledge of Chakra UI - a React component library.\n\nSetting up the Jobs Collection in Directus [​](https://docs.directus.io/blog/building-a-job-board.html#setting-up-the-jobs-collection-in-directus)\n--------------------------------------------------------------------------------------------------------------------------------------------------\n\nBefore we can start fetching and displaying job listings, we need to define the data model that will store our job data in Directus.\n\nLog in to your Directus app and navigate to Settings \\> Data Model. Click the + icon to create a new collection called “jobs”.\n\nAdd the following fields and save:\n\n*   **title** (Type: String, Interface: Input)\n*   **company** (Type: String, Interface: Input)\n*   **location** (Type: String, Interface: Input)\n*   **logo** (Type: UUID, Interface: Image)\n*   **tags** (Type: JSON, Interface: Tags)\n*   **remote** (Type: Boolean, Interface: Toggle)\n*   **datePosted** (Type: DateTime, Interface: DateTime)\n*   **salaryRange** (Type: String, Interface: Input)\n*   **content** (Type: Text, Interface: WYSIWYG)\n\n### Adding Content to the Jobs Collection [​](https://docs.directus.io/blog/building-a-job-board.html#adding-content-to-the-jobs-collection)\n\nWith the data model in place, we're now ready to populate our collection with some real job listings.\n\nFrom the Directus sidebar, navigate to \"Content Module\" and select the \"Jobs\" collection we created earlier.\n\nGo ahead and add a few sample jobs to have content to work with as we build out the frontend interface. You can always come back later to enter more postings as needed.\n\nBuilding the Frontend Application [​](https://docs.directus.io/blog/building-a-job-board.html#building-the-frontend-application)\n--------------------------------------------------------------------------------------------------------------------------------\n\nWith the backend in place, we need to set up a working frontend interface to display the job listings.\n\n### Installing Next.js [​](https://docs.directus.io/blog/building-a-job-board.html#installing-next-js)\n\nIn your terminal, run the following command:\n\n```\nnpx create-next-app@latest job-board\n\ncd job-board\n```\n\n```\nnpx create-next-app@latest job-board\n\ncd job-board\n```\n\nOn installation, choose the following:\n\n```\nWould you like to use TypeScript? Yes\nWould you like to use ESLint? Yes\nWould you like to use Tailwind CSS? No \nWould you like to use `src/` directory? Yes\nWould you like to use App Router? (recommended) No\nWould you like to customize the default import alias?  Yes\nWhat import alias would you like configured? @/*\n```\n\n```\nWould you like to use TypeScript? Yes\nWould you like to use ESLint? Yes\nWould you like to use Tailwind CSS? No \nWould you like to use `src/` directory? Yes\nWould you like to use App Router? (recommended) No\nWould you like to customize the default import alias?  Yes\nWhat import alias would you like configured? @/*\n```\n\nRemove boilerplate code from `index.tsx` and update meta tags:\n\ntsx\n\n```\nimport Head from 'next/head';\n\nexport default function Home() {\n  return (\n    <>\n      <Head>\n        <title>Job Board</title>\n        <meta name='description' content='Job board app to connect job seekers to opportunities' />\n        <meta name='viewport' content='width=device-width, initial-scale=1' />\n        <link rel='icon' href='/favicon.ico' />\n      </Head>\n      <main>\n            <h1>Find Your Dream Job</h1>\n      </main>\n    </>\n  );\n}\n```\n\n```\nimport Head from 'next/head';\n\nexport default function Home() {\n  return (\n    <>\n      <Head>\n        <title>Job Board</title>\n        <meta name='description' content='Job board app to connect job seekers to opportunities' />\n        <meta name='viewport' content='width=device-width, initial-scale=1' />\n        <link rel='icon' href='/favicon.ico' />\n      </Head>\n      <main>\n            <h1>Find Your Dream Job</h1>\n      </main>\n    </>\n  );\n}\n```\n\nStart your local server using the command:\n\nYou should have your app running at **[http://localhost:3000](http://localhost:3000/)**\n\n### Installing the required dependencies [​](https://docs.directus.io/blog/building-a-job-board.html#installing-the-required-dependencies)\n\nRun the following command in your terminal:\n\n```\nnpm install @directus/sdk @chakra-ui/react @emotion/react @emotion/styled framer-motion react-icons\n```\n\n```\nnpm install @directus/sdk @chakra-ui/react @emotion/react @emotion/styled framer-motion react-icons\n```\n\n*   Directus SDK for fetching jobs\n*   Chakra UI for styling (Emotion and Framer are Chakra UI dependencies)\n*   React icons\n\n### Setting up Chakra UI [​](https://docs.directus.io/blog/building-a-job-board.html#setting-up-chakra-ui)\n\nTo use Chakra UI in your project, you need to set up the `ChakraProvider` at the root of your application.\n\nGo to `pages/_app.tsx` and wrap the Component with the `ChakraProvider`.\n\ntsx\n\n```\n// pages/_app.tsx\nimport type { AppProps } from 'next/app';\nimport { ChakraProvider } from '@chakra-ui/react'\n\nexport default function App({ Component, pageProps }: AppProps) {\n  return (\n    <ChakraProvider>\n      <Component {...pageProps} />\n    </ChakraProvider>\n  );\n}\n```\n\n```\n// pages/_app.tsx\nimport type { AppProps } from 'next/app';\nimport { ChakraProvider } from '@chakra-ui/react'\n\nexport default function App({ Component, pageProps }: AppProps) {\n  return (\n    <ChakraProvider>\n      <Component {...pageProps} />\n    </ChakraProvider>\n  );\n}\n```\n\nDisplaying the Job Listings [​](https://docs.directus.io/blog/building-a-job-board.html#displaying-the-job-listings)\n--------------------------------------------------------------------------------------------------------------------\n\nTo display the job listings from Directus, we need to set up the types for our jobs and also create two components: the `JobCard` and `JobList` components.\n\n### Defining the Types for the Jobs [​](https://docs.directus.io/blog/building-a-job-board.html#defining-the-types-for-the-jobs)\n\nSince we’re working with TypeScript, to ensure type safety when working with job data from Directus, let’s set up an interface that defines the expected shape of each job object.\n\nAt the root of your project, create a new directory called lib, and inside it, a new file called `directus.ts`.\n\njs\n\n```\nexport type Job = {\n  id: number;\n  title: string;\n  company: string;\n  content: string;\n  location: string;\n  datePosted: string;\n  logo: string;\n  tags: string[];\n  remote: boolean;\n  salaryRange: string;\n};\n\ntype Schema = {\n  jobs: Job[];\n};\n```\n\n```\nexport type Job = {\n  id: number;\n  title: string;\n  company: string;\n  content: string;\n  location: string;\n  datePosted: string;\n  logo: string;\n  tags: string[];\n  remote: boolean;\n  salaryRange: string;\n};\n\ntype Schema = {\n  jobs: Job[];\n};\n```\n\n### Building the Job Card Component [​](https://docs.directus.io/blog/building-a-job-board.html#building-the-job-card-component)\n\nCreate a `src/job-card.tsx` file and input this code:\n\ntsx\n\n```\nimport { Avatar, Box, HStack, Heading, Icon, LinkBox, LinkOverlay, Stack, Tag, Text } from '@chakra-ui/react';\nimport NextLink from 'next/link';\nimport { MdBusiness, MdLocationPin, MdOutlineAttachMoney } from 'react-icons/md';\nimport { Job } from '@/lib/directus';\nimport { friendlyTime } from '@/lib/friendly-time';\n\ntype JobCardProps = {\n  data: Job;\n};\n\nexport function JobCard(props: JobCardProps) {\n  const { data, ...rest } = props;\n  const { id, title, company, location, datePosted, logo, tags, remote, salaryRange  } = data;\n\n  return (\n    <Box\n      border='1px solid'\n      borderColor='gray.300'\n      borderRadius='md'\n      _hover={{ borderColor: 'black', boxShadow: 'sm' }}\n      p='6'\n      {...rest}\n    >\n      <LinkBox as='article'>\n        <Stack direction={{ base: 'column', lg: 'row' }} spacing='8'>\n          <Avatar size='lg' name={title} src={logo} />\n          <Box>\n            <LinkOverlay as={NextLink} href={`/${id}`}>\n              <Heading size='md'>{title}</Heading>\n            </LinkOverlay>\n            <Text>{company}</Text>\n            <Stack mt='2' spacing={1}>\n              <HStack spacing={1}>\n                <Icon as={MdLocationPin} boxSize={4} />\n                <Text>{location}</Text>\n              </HStack>\n              <HStack spacing={1}>\n                <Icon as={MdBusiness} boxSize={4} />\n                <Text>{remote === 'true' ? 'Remote' : 'Onsite'}</Text>\n              </HStack>\n              <HStack spacing={1}>\n                <Icon as={MdOutlineAttachMoney} boxSize={4} />\n                <Text>{salaryRange}</Text>\n              </HStack>\n            </Stack>\n          </Box>\n          <HStack spacing={2} flex='1'>\n            {tags.map((tag, index) => (\n              <Tag key={index} colorScheme='gray'>\n                {tag}\n              </Tag>\n            ))}\n          </HStack>\n          <Text alignSelf={{ base: 'left', lg: 'center' }}>\n            Posted {friendlyTime(new Date(datePosted))}\n          </Text>\n        </Stack>\n      </LinkBox>\n    </Box>\n  );\n}\n```\n\n```\nimport { Avatar, Box, HStack, Heading, Icon, LinkBox, LinkOverlay, Stack, Tag, Text } from '@chakra-ui/react';\nimport NextLink from 'next/link';\nimport { MdBusiness, MdLocationPin, MdOutlineAttachMoney } from 'react-icons/md';\nimport { Job } from '@/lib/directus';\nimport { friendlyTime } from '@/lib/friendly-time';\n\ntype JobCardProps = {\n  data: Job;\n};\n\nexport function JobCard(props: JobCardProps) {\n  const { data, ...rest } = props;\n  const { id, title, company, location, datePosted, logo, tags, remote, salaryRange  } = data;\n\n  return (\n    <Box\n      border='1px solid'\n      borderColor='gray.300'\n      borderRadius='md'\n      _hover={{ borderColor: 'black', boxShadow: 'sm' }}\n      p='6'\n      {...rest}\n    >\n      <LinkBox as='article'>\n        <Stack direction={{ base: 'column', lg: 'row' }} spacing='8'>\n          <Avatar size='lg' name={title} src={logo} />\n          <Box>\n            <LinkOverlay as={NextLink} href={`/${id}`}>\n              <Heading size='md'>{title}</Heading>\n            </LinkOverlay>\n            <Text>{company}</Text>\n            <Stack mt='2' spacing={1}>\n              <HStack spacing={1}>\n                <Icon as={MdLocationPin} boxSize={4} />\n                <Text>{location}</Text>\n              </HStack>\n              <HStack spacing={1}>\n                <Icon as={MdBusiness} boxSize={4} />\n                <Text>{remote === 'true' ? 'Remote' : 'Onsite'}</Text>\n              </HStack>\n              <HStack spacing={1}>\n                <Icon as={MdOutlineAttachMoney} boxSize={4} />\n                <Text>{salaryRange}</Text>\n              </HStack>\n            </Stack>\n          </Box>\n          <HStack spacing={2} flex='1'>\n            {tags.map((tag, index) => (\n              <Tag key={index} colorScheme='gray'>\n                {tag}\n              </Tag>\n            ))}\n          </HStack>\n          <Text alignSelf={{ base: 'left', lg: 'center' }}>\n            Posted {friendlyTime(new Date(datePosted))}\n          </Text>\n        </Stack>\n      </LinkBox>\n    </Box>\n  );\n}\n```\n\nInside the `lib` directory and add a `friendly-time.ts` file to format the code:\n\njs\n\n```\nexport const friendlyTime = (date: Date) => {\n  const seconds = Math.floor((new Date().getTime() - date.getTime()) / 1000);\n\n  let interval = seconds / 31536000;\n\n  if (interval > 1) {\n    return Math.floor(interval) + ' years ago';\n  }\n  interval = seconds / 2592000;\n  if (interval > 1) {\n    return Math.floor(interval) + ' months ago';\n  }\n  interval = seconds / 86400;\n  if (interval > 1) {\n    return Math.floor(interval) + ' days ago';\n  }\n  interval = seconds / 3600;\n  if (interval > 1) {\n    return Math.floor(interval) + ' hours ago';\n  }\n  interval = seconds / 60;\n  if (interval > 1) {\n    return Math.floor(interval) + ' minutes ago';\n  }\n  return Math.floor(seconds) + ' seconds ago';\n};\n```\n\n```\nexport const friendlyTime = (date: Date) => {\n  const seconds = Math.floor((new Date().getTime() - date.getTime()) / 1000);\n\n  let interval = seconds / 31536000;\n\n  if (interval > 1) {\n    return Math.floor(interval) + ' years ago';\n  }\n  interval = seconds / 2592000;\n  if (interval > 1) {\n    return Math.floor(interval) + ' months ago';\n  }\n  interval = seconds / 86400;\n  if (interval > 1) {\n    return Math.floor(interval) + ' days ago';\n  }\n  interval = seconds / 3600;\n  if (interval > 1) {\n    return Math.floor(interval) + ' hours ago';\n  }\n  interval = seconds / 60;\n  if (interval > 1) {\n    return Math.floor(interval) + ' minutes ago';\n  }\n  return Math.floor(seconds) + ' seconds ago';\n};\n```\n\n*   This component is styled and built using the `Box`,` Stack`, `HStack`, and more components from Chakra UI\n*   The posted date is displayed using the `friendlyTime` code to format the `datePosted` into a user-friendly time format (e.g., \"2 days ago\")\n\n### Building the Job List Component [​](https://docs.directus.io/blog/building-a-job-board.html#building-the-job-list-component)\n\nInside the components directory, create a `job-list.tsx` file that shows the list of jobs\n\ntsx\n\n```\nimport { Stack } from '@chakra-ui/react';\nimport { JobCard } from './job-card';\nimport { Job } from '@/lib/directus';\n\ntype JobListProps = {\n  data: Job[];\n};\n\nexport function JobList(props: JobListProps) {\n  const { data } = props;\n\n  return (\n    <Stack spacing='4'>\n      {data.map((job, index) => (\n        <JobCard key={index} data={job} />\n      ))}\n    </Stack>\n  );\n}\n```\n\n```\nimport { Stack } from '@chakra-ui/react';\nimport { JobCard } from './job-card';\nimport { Job } from '@/lib/directus';\n\ntype JobListProps = {\n  data: Job[];\n};\n\nexport function JobList(props: JobListProps) {\n  const { data } = props;\n\n  return (\n    <Stack spacing='4'>\n      {data.map((job, index) => (\n        <JobCard key={index} data={job} />\n      ))}\n    </Stack>\n  );\n}\n```\n\n### Fetching the Jobs from Directus [​](https://docs.directus.io/blog/building-a-job-board.html#fetching-the-jobs-from-directus)\n\nA crucial part of the job board is being able to fetch and display the latest job listings. To accomplish this, we’re going to use the Directus SDK.\n\nAt the root of your project, create a `.env` file and add your Directus URL\n\n```\nDIRECTUS_URL=add-your-directus-url-here\n```\n\n```\nDIRECTUS_URL=add-your-directus-url-here\n```\n\nTo share a single instance of the Directus SDK between multiple pages in this project, we need to set up a helper file that can be imported later.\n\nInside the `directus.ts` file, create a Directus client by importing the `createDirectus` hook and `rest` composable.\n\njs\n\n```\nimport { createDirectus, rest } from '@directus/sdk';\n\nexport interface Job {\n  id: number;\n  title: string;\n  company: string;\n  content: string;\n  location: string;\n  datePosted: string;\n  logo: string;\n  tags: string[];\n  remote: boolean;\n  salaryRange: string;\n}\n\ninterface Schema {\n  jobs: Job[];\n}\n\nconst directus = createDirectus<Schema>(process.env.DIRECTUS_URL!).with(rest());\n\nexport default directus;\n```\n\n```\nimport { createDirectus, rest } from '@directus/sdk';\n\nexport interface Job {\n  id: number;\n  title: string;\n  company: string;\n  content: string;\n  location: string;\n  datePosted: string;\n  logo: string;\n  tags: string[];\n  remote: boolean;\n  salaryRange: string;\n}\n\ninterface Schema {\n  jobs: Job[];\n}\n\nconst directus = createDirectus<Schema>(process.env.DIRECTUS_URL!).with(rest());\n\nexport default directus;\n```\n\nNow, go over to `index.tsx` and update the code to render the jobs\n\ntsx\n\n```\nimport { JobList } from '@/components/job-list';\nimport { Box, Heading, Stack } from '@chakra-ui/react';\nimport { readItems } from '@directus/sdk';\nimport Head from 'next/head';\nimport directus, { Job } from '../lib/directus';\n\nexport default function Home({ jobs }: { jobs: Job[] }) {\n  return (\n    <>\n      <Head>\n        <title>Job Board</title>\n        <meta\n          name='description'\n          content='Job board app to connect job seekers to opportunities'\n        />\n        <meta name='viewport' content='width=device-width, initial-scale=1' />\n        <link rel='icon' href='/favicon.ico' />\n      </Head>\n      <main>\n        <Box p={{ base: '12', lg: '24' }}>\n          <Stack mb='8' maxW='sm'>\n            <Heading>Find Your Dream Job</Heading>\n          </Stack>\n          <JobList data={jobs} />\n        </Box>\n      </main>\n    </>\n  );\n}\n\nexport async function getStaticProps() {\n  try {\n    const jobs = await directus.request(\n      readItems('jobs', {\n        limit: -1,\n        fields: ['*'],\n      })\n    );\n\n    if (!jobs) {\n      return {\n        notFound: true,\n      };\n    }\n\n    // Format the image field to have the full URL\n    jobs.forEach((job) => {\n      job.logo = `${process.env.DIRECTUS_URL}assets/${job.logo}`;\n    });\n\n    return {\n      props: {\n        jobs,\n      },\n    };\n  } catch (error) {\n    console.error('Error fetching jobs:', error);\n    return {\n      notFound: true,\n    };\n  }\n}\n```\n\n```\nimport { JobList } from '@/components/job-list';\nimport { Box, Heading, Stack } from '@chakra-ui/react';\nimport { readItems } from '@directus/sdk';\nimport Head from 'next/head';\nimport directus, { Job } from '../lib/directus';\n\nexport default function Home({ jobs }: { jobs: Job[] }) {\n  return (\n    <>\n      <Head>\n        <title>Job Board</title>\n        <meta\n          name='description'\n          content='Job board app to connect job seekers to opportunities'\n        />\n        <meta name='viewport' content='width=device-width, initial-scale=1' />\n        <link rel='icon' href='/favicon.ico' />\n      </Head>\n      <main>\n        <Box p={{ base: '12', lg: '24' }}>\n          <Stack mb='8' maxW='sm'>\n            <Heading>Find Your Dream Job</Heading>\n          </Stack>\n          <JobList data={jobs} />\n        </Box>\n      </main>\n    </>\n  );\n}\n\nexport async function getStaticProps() {\n  try {\n    const jobs = await directus.request(\n      readItems('jobs', {\n        limit: -1,\n        fields: ['*'],\n      })\n    );\n\n    if (!jobs) {\n      return {\n        notFound: true,\n      };\n    }\n\n    // Format the image field to have the full URL\n    jobs.forEach((job) => {\n      job.logo = `${process.env.DIRECTUS_URL}assets/${job.logo}`;\n    });\n\n    return {\n      props: {\n        jobs,\n      },\n    };\n  } catch (error) {\n    console.error('Error fetching jobs:', error);\n    return {\n      notFound: true,\n    };\n  }\n}\n```\n\nYou should have something like this on your frontend\n\n![Image 13: Job Board ](https://marketing.directus.app/assets/9fb98c51-69e4-4e0e-940d-33028f8270eb.png)\n\nDisplaying the Job Detail [​](https://docs.directus.io/blog/building-a-job-board.html#displaying-the-job-detail)\n----------------------------------------------------------------------------------------------------------------\n\nWith the ability to fetch job listings from Directus established, the next step is to dynamically display each job's content on individual job pages. Next.js provides a streamlined way to do this through its automatic static and server-side rendering features.\n\nBut first, we need to build out a `JobContent` Component.\n\n### Building the Job Content Component [​](https://docs.directus.io/blog/building-a-job-board.html#building-the-job-content-component)\n\nWithin the `components` folder, create a `job-content.tsx` file to show the job content for each job\n\ntsx\n\n```\nimport { Job } from '@/lib/directus';\nimport { Avatar, Box, Button, HStack, Heading } from '@chakra-ui/react';\nimport Link from 'next/link';\n\ntype JobContentProps = {\n  data: Job;\n};\n\nexport function JobContent(props: JobContentProps) {\n  const { data } = props;\n  const { content, logo, title, company } = data;\n\n  return (\n    <Box px={{ base: '12', lg: '24' }}>\n      <Button as={Link} href='/'>\n        Back to jobs\n      </Button>\n      <Box py='16'>\n        <HStack spacing='4'>\n          <Avatar size='lg' name={title} src={logo} />\n          <Heading size='lg'>{company}</Heading>\n        </HStack>\n        <Box maxW='3xl' dangerouslySetInnerHTML={{ __html: content }} />\n      </Box>\n    </Box>\n  );\n}\n```\n\n```\nimport { Job } from '@/lib/directus';\nimport { Avatar, Box, Button, HStack, Heading } from '@chakra-ui/react';\nimport Link from 'next/link';\n\ntype JobContentProps = {\n  data: Job;\n};\n\nexport function JobContent(props: JobContentProps) {\n  const { data } = props;\n  const { content, logo, title, company } = data;\n\n  return (\n    <Box px={{ base: '12', lg: '24' }}>\n      <Button as={Link} href='/'>\n        Back to jobs\n      </Button>\n      <Box py='16'>\n        <HStack spacing='4'>\n          <Avatar size='lg' name={title} src={logo} />\n          <Heading size='lg'>{company}</Heading>\n        </HStack>\n        <Box maxW='3xl' dangerouslySetInnerHTML={{ __html: content }} />\n      </Box>\n    </Box>\n  );\n}\n```\n\nTo dynamically render the job pages, create a `[jobId].tsx` in the `pages` directory and put the following code in it:\n\ntsx\n\n```\nimport { readItem, readItems } from '@directus/sdk';\nimport { GetStaticPaths, GetStaticProps } from 'next';\nimport directus from '../lib/directus';\nimport { Box } from '@chakra-ui/react';\nimport { JobContent } from '@/components/job-content';\nimport { Job } from '../lib/directus';\n\ntype JobDetailsProps = {\n  job: Job;\n};\n\nexport default function JobDetails(props: JobDetailsProps) {\n  const { job } = props;\n  return (\n    <Box p={{ base: '12', lg: '24' }}>\n      <JobContent data={job} />\n    </Box>\n  );\n}\n\nexport const getStaticPaths: GetStaticPaths = async () => {\n  try {\n    const jobs = await directus.request(\n      readItems('jobs', {\n        limit: -1,\n        fields: ['id'],\n      })\n    );\n    const paths = jobs.map((job) => {\n      // Access the data property to get the array of jobs\n      return {\n        params: { jobId: job.id.toString() },\n      };\n    });\n    return {\n      paths: paths || [],\n      fallback: false,\n    };\n  } catch (error) {\n    console.error('Error fetching paths:', error);\n    return {\n      paths: [],\n      fallback: false,\n    };\n  }\n};\n\nexport const getStaticProps: GetStaticProps = async (context) => {\n  try {\n    const jobId = context.params?.jobId as string;\n\n    const job = await directus.request(\n      readItem('jobs', jobId, {\n        fields: ['*'],\n      })\n    );\n\n    if (job) {\n      job.logo = `${process.env.DIRECTUS_URL}assets/${job.logo}`;\n    }\n\n    return {\n      props: {\n        job,\n      },\n    };\n  } catch (error) {\n    console.error('Error fetching job:', error);\n    return {\n      notFound: true,\n    };\n  }\n};\n```\n\n```\nimport { readItem, readItems } from '@directus/sdk';\nimport { GetStaticPaths, GetStaticProps } from 'next';\nimport directus from '../lib/directus';\nimport { Box } from '@chakra-ui/react';\nimport { JobContent } from '@/components/job-content';\nimport { Job } from '../lib/directus';\n\ntype JobDetailsProps = {\n  job: Job;\n};\n\nexport default function JobDetails(props: JobDetailsProps) {\n  const { job } = props;\n  return (\n    <Box p={{ base: '12', lg: '24' }}>\n      <JobContent data={job} />\n    </Box>\n  );\n}\n\nexport const getStaticPaths: GetStaticPaths = async () => {\n  try {\n    const jobs = await directus.request(\n      readItems('jobs', {\n        limit: -1,\n        fields: ['id'],\n      })\n    );\n    const paths = jobs.map((job) => {\n      // Access the data property to get the array of jobs\n      return {\n        params: { jobId: job.id.toString() },\n      };\n    });\n    return {\n      paths: paths || [],\n      fallback: false,\n    };\n  } catch (error) {\n    console.error('Error fetching paths:', error);\n    return {\n      paths: [],\n      fallback: false,\n    };\n  }\n};\n\nexport const getStaticProps: GetStaticProps = async (context) => {\n  try {\n    const jobId = context.params?.jobId as string;\n\n    const job = await directus.request(\n      readItem('jobs', jobId, {\n        fields: ['*'],\n      })\n    );\n\n    if (job) {\n      job.logo = `${process.env.DIRECTUS_URL}assets/${job.logo}`;\n    }\n\n    return {\n      props: {\n        job,\n      },\n    };\n  } catch (error) {\n    console.error('Error fetching job:', error);\n    return {\n      notFound: true,\n    };\n  }\n};\n```\n\nThe code fetches and renders dynamic job details using static site generation with Next.js.\n\n*   Static Paths Generation (`getStaticPaths`):\n    \n    *   Implements the `getStaticPath`s function, a part of Next.js's static site generation.\n    *   Requests job data using Directus's `readItems` function with `limit: -1` to fetch all job IDs.\n    *   Maps retrieved job IDs to an array of `params` objects to generate dynamic routes.\n    *   Sets the paths array to the generated paths and `fallback` to` false` (no fallback behavior).\n*   Static Props Generation (`getStaticProps`):\n    \n    *   Implements the `getStaticProps` function, used in static site generation to fetch data for a specific page.\n    *   Extracts the`jobId` parameter from the context object to identify the requested job.\n    *   Requests detailed job information using Directus's `readItem` function for the specified job.\n    *   Modifies the job object by appending the `logo` URL with the `DIRECTUS_URL`.\n    *   Returns fetched job data within the `props` object.\n\nNow, whenever you click on a job, you’ll be able to see all the details about that job\n\n![Image 14: Job Detail](https://marketing.directus.app/assets/3699c2b7-b8b4-4443-af40-f1e4557fa6e1.png)\n\nImplementing the Search Functionality [​](https://docs.directus.io/blog/building-a-job-board.html#implementing-the-search-functionality)\n----------------------------------------------------------------------------------------------------------------------------------------\n\nTo enable users to search for jobs by title in our application, we need to build out the functionality for querying the jobs data store based on the job title field. We also need to build out the search input UI to handle this.\n\nIn `index.tsx` update the code as follows:\n\ntsx\n\n```\nexport default function Home(props: { jobs: Job[] }) {\n  const { jobs } = props;\n  const router = useRouter();\n\n  const searchQuery = router.query.search?.toString();\n  const searchResult = searchQuery\n    ? jobs.filter((job) => {\n        return job.title.toLowerCase().includes(searchQuery.toLowerCase());\n      })\n    : jobs;\n\n  return (\n    <>\n      <Head>\n        <title>Job Board</title>\n        <meta\n          name='description'\n          content='Job board app to connect job seekers to opportunities'\n        />\n        <meta name='viewport' content='width=device-width, initial-scale=1' />\n        <link rel='icon' href='/favicon.ico' />\n      </Head>\n      <main>\n        <Box p={{ base: '12', lg: '24' }}>\n          <Stack mb='8' direction={{ base: 'column', md: 'row' }}>\n            <Heading flex='1'>Find Your Dream Job</Heading>\n            <InputGroup w='auto'>\n              <InputLeftElement color='gray.400'>\n                <FaSearch />\n              </InputLeftElement>\n              <Input\n                placeholder='Search jobs...'\n                onChange={(event) => {\n                  const value = event.target.value;\n\n                  router.replace({\n                    query: { search: value },\n                  });\n                }}\n              />\n            </InputGroup>\n          </Stack>\n          <JobList data={searchResult} />\n        </Box>\n      </main>\n    </>\n  );\n}\n```\n\n```\nexport default function Home(props: { jobs: Job[] }) {\n  const { jobs } = props;\n  const router = useRouter();\n\n  const searchQuery = router.query.search?.toString();\n  const searchResult = searchQuery\n    ? jobs.filter((job) => {\n        return job.title.toLowerCase().includes(searchQuery.toLowerCase());\n      })\n    : jobs;\n\n  return (\n    <>\n      <Head>\n        <title>Job Board</title>\n        <meta\n          name='description'\n          content='Job board app to connect job seekers to opportunities'\n        />\n        <meta name='viewport' content='width=device-width, initial-scale=1' />\n        <link rel='icon' href='/favicon.ico' />\n      </Head>\n      <main>\n        <Box p={{ base: '12', lg: '24' }}>\n          <Stack mb='8' direction={{ base: 'column', md: 'row' }}>\n            <Heading flex='1'>Find Your Dream Job</Heading>\n            <InputGroup w='auto'>\n              <InputLeftElement color='gray.400'>\n                <FaSearch />\n              </InputLeftElement>\n              <Input\n                placeholder='Search jobs...'\n                onChange={(event) => {\n                  const value = event.target.value;\n\n                  router.replace({\n                    query: { search: value },\n                  });\n                }}\n              />\n            </InputGroup>\n          </Stack>\n          <JobList data={searchResult} />\n        </Box>\n      </main>\n    </>\n  );\n}\n```\n\n*   We use the `useRouter` hook from Next.js to access the query parameters from the URL.\n*   If a search query was provided, we filter the jobs array to only include those whose title matched the search query in a case-insensitive manner. If no search query was present, we simply set the `searchResult` to the original jobs array without any filtering.\n\n[Here's the repository to find the code](https://github.com/directus-community/job-board)\n\nConclusion [​](https://docs.directus.io/blog/building-a-job-board.html#conclusion)\n----------------------------------------------------------------------------------\n\nIn this tutorial, you've learned how to fetch job data from a Directus instance, display it on your app, and implement search functionality.\n\nSome natural next steps could include:\n\n*   Implementing user authentication via JWT tokens to allow job seekers to create custom profiles, save jobs, and track application status\n*   Integrating email and notification systems to allow job alerts to be automatically sent to users when new jobs are posted\n*   Adding advanced filtering and sorting of job results beyond just search title\n\nIf you have any questions or need further assistance, please feel free to drop by our [Discord server](https://directus.chat/).",
  "usage": {
    "tokens": 7706
  }
}
```
