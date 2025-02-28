---
title: GitHub - alexluong/gatsby-theme-comments: Drop-in comment functionality for static Gatsby site, powered by Firebase
description: Drop-in comment functionality for static Gatsby site, powered by Firebase - alexluong/gatsby-theme-comments
url: https://github.com/alexluong/gatsby-theme-comments
timestamp: 2025-01-20T15:31:16.248Z
domain: github.com
path: alexluong_gatsby-theme-comments
---

# GitHub - alexluong/gatsby-theme-comments: Drop-in comment functionality for static Gatsby site, powered by Firebase


Drop-in comment functionality for static Gatsby site, powered by Firebase - alexluong/gatsby-theme-comments


## Content

gatsby-theme-comments
---------------------

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#gatsby-theme-comments)

Provides drop-in comment functionality for static Gatsby site, powered by Firebase

The problem
-----------

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#the-problem)

You want to drive engagement for your Gatsby blog via comments.

This solution
-------------

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#this-solution)

This is a Gatsby theme that let you add comment section to your blog.

This differs from other solutions in that it gives you complete control of your data and UI. You store your data on your own database, and you can modify the design as you see fit.

Table of Contents
-----------------

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#table-of-contents)

*   [gatsby-theme-comments](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#gatsby-theme-comments)
    *   [The problem](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#the-problem)
    *   [This solution](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#this-solution)
    *   [Table of Contents](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#table-of-contents)
    *   [Installation](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#installation)
    *   [Usage](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usage)
        *   [1\. Register plugins](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#1-register-plugins)
        *   [2\. Set up Firestore and environment variables](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#2-set-up-firestore-and-environment-variables)
        *   [3\. Use in React](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#3-use-in-react)
    *   [Showcase](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#showcase)
        *   [UI child themes of `gatsby-theme-comments`](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#ui-child-themes-of-gatsby-theme-comments)
        *   [Sites that uses `gatsby-theme-comments`](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#sites-that-uses-gatsby-theme-comments)
    *   [APIs](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#apis)
        *   [Comment](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#comment)
        *   [Exports](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#exports)
            *   [CommentSection](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#commentsection)
                *   [id](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#id)
            *   [CommentCount](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#commentcount)
                *   [id](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#id-1)
            *   [useComments](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usecomments)
            *   [useCommentCount](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usecommentcount)
            *   [useAddComment](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#useaddcomment)
        *   [Shadowable Components](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#shadowable-components)
        *   [Demo](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#demo)
    *   [License](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#license)

Installation
------------

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#installation)

```
npm install gatsby-theme-comments gatsby-plugin-firebase
npm install -D dotenv
```

Usage
-----

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usage)

### 1\. Register plugins

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#1-register-plugins)

In `gatsby-config.js`:

require("dotenv").config()

module.exports \= {
  plugins: \[
    ...otherPlugins,

    "gatsby-plugin-firebase",
    "gatsby-theme-comments",
  \],
}

### 2\. Set up Firestore and environment variables

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#2-set-up-firestore-and-environment-variables)

*   Create a Firebase project
*   Create a new Firestore database
*   Inside the `Database` page, open the `Indexes` tab and add a composite index like so:

[![Image 7: Firestore index instruction](https://github.com/alexluong/gatsby-theme-comments/raw/master/firestore-index.png?raw=true)](https://github.com/alexluong/gatsby-theme-comments/blob/master/firestore-index.png?raw=true)

*   Create a `.env` in your root directory:

```
GATSBY_FIREBASE_API_KEY=<YOUR_FIREBASE_API_KEY>
GATSBY_FIREBASE_AUTH_DOMAIN=<YOUR_FIREBASE_AUTH_DOMAIN>
GATSBY_FIREBASE_DATABASE_URL=<YOUR_FIREBASE_DATABASE_URL>
GATSBY_FIREBASE_PROJECT_ID=<YOUR_FIREBASE_PROJECT_ID>
GATSBY_FIREBASE_STORAGE_BUCKET=<YOUR_FIREBASE_STORAGE_BUCKET>
GATSBY_FIREBASE_MESSAGING_SENDER_ID=<YOUR_FIREBASE_MESSAGING_SENDER_ID>
GATSBY_FIREBASE_APP_ID=<YOUR_FIREBASE_APP_ID>
```

### 3\. Use in React

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#3-use-in-react)

In your post template (`src/templates/post.js`), you can use `CommentSection` in your JSX:

import { CommentSection } from "gatsby-theme-comments"

...

return (
  <Layout\>
    <Article /\>
    <Author /\>

    <CommentSection id\={slug} /\>
  </Layout\>
)

The `id` prop must be a unique string or number that identifies the post. It can be the post's id, slug, or title, but do be aware that you'd lose track of the comments if you change that id.

For example, let's say that you use `slug` as the identifier. If you want to change the post's slug, remember to go into your Firebase database and change that value too.

Showcase
--------

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#showcase)

### UI child themes of `gatsby-theme-comments`

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#ui-child-themes-of-gatsby-theme-comments)

*   [Barebone/Core](https://npmjs.com/package/gatsby-theme-comments)
*   [Minimal UI](https://npmjs.com/package/gatsby-theme-comments-ui)

If you wrote a child theme for `gatsby-theme-comments`, please submit a [PR](https://github.com/alexluong/gatsby-theme-comments/edit/master/README.md) to add your theme to the list.

### Sites that uses `gatsby-theme-comments`

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#sites-that-uses-gatsby-theme-comments)

Nobody is using this plugin. Sad face 😢

If you use `gatsby-theme-comments`, please submit a [PR](https://github.com/alexluong/gatsby-theme-comments/edit/master/README.md) to add your site to the list.

Feel free to reach out or open an issue if you're interested in using this. I'm available to answer any questions or take feature requests.

APIs
----

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#apis)

### Comment

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#comment)

The `Comment` interface is an object that looks like this:

interface Comment {
  id: string;
  content: string;
  name: string;
  createdAt: Timestamp;
  updatedAt: Timestamp;
}

interface Timestamp {
  nanoseconds: number;
  milliseconds: number;
  toDate: function;
}

### Exports

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#exports)

#### CommentSection

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#commentsection)

A component that renders a form for users to add comment as well as all the comments of the post. This is the simplest way to use `gatsby-theme-comments`. You can use this component in your `Post` template.

##### id

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#id)

> `string` | _required_

A unique identifier used to identify each post. It cannot contain special characters such as "/".

#### CommentCount

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#commentcount)

A component that renders the comment count of the post

##### id

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#id-1)

> `string` | _required_

A unique identifier used to identify each post

#### useComments

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usecomments)

> `function(id: string): { loading: boolean, error: Error, comments: Array<Comment> }`

This hook takes the identifier as argument and gives you the corresponding array of comments.

If the identifier is invalid, the comment array is empty.

function Comments({ id }) {
  const { loading, comments } \= useComments()

  if (loading) {
    return <p\>Loading...</p\>
  }

  return (
    <ul\>
      {comments.map(comment) \=\> (
        <li key\={comment.id}\>{comment.content}</li\>
      )}
    </ul\>
  )
}

#### useCommentCount

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usecommentcount)

> `function(id: string): { loading: boolean, error: Error, commentCount: number }`

This hook takes the identifier as argument and gives you the corresponding number of comments.

If the identifier is invalid, the count is 0. The reason for this is that the plugin only keeps track of posts with at least 1 comment. Therefore, if a post doesn't have any, its `id` would not be available in database.

function CommentCount({ id }) {
  const { loading, commentCount } \= useCommentCount()

  if (loading) {
    return <p\>0 comment</p\>
  }

  return <p\>{commentCount} comment{commentCount \> 1 ? "s" : ""}</p\>
}

#### useAddComment

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#useaddcomment)

> `function(): { loading: boolean, error: Error, addComment: function(comment: Comment): void }`

This hook returns a function for you to add comment to database.

function AddComment({ comment }) {
  const { addComment } \= useAddComment()

  return (
    <button onClick\={() \=\> addComment(comment)}\>Add</button\>
  )
}

_Note_: The `Comment` you pass to the `addComment` function is one without `Timestamp`. The `createdAt` field will be included whenever the plugin makes a call to Firebase. You don't have to construct that value.

### Shadowable Components

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#shadowable-components)

Here is a list of recommended components that you can shadow:

*   `components/Button.js`
*   `components/Comment.js`
*   `components/CommentCount.js`
*   `components/Comments.js`
*   `components/Form.js`
*   `components/Loading.js`
*   `components/TextField.js`

Demo
----

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#demo)

To run the demo,

*   Clone this project
*   `cd` into `examples/demo`
*   Add your Firebase details to `.env`
*   Create an index in Firestore as shown in the second section
*   Run `npm start`
*   Try out the project on `localhost:8000`

**Note**: Depending on how you've set up your Firestore project, you may have to change the permissions first. A good starting point would be:

service cloud.firestore {
  match /databases/{database}/documents {
    match /{document\=\*\*} {
      allow read, write: if true;
    }
  }
}

Just don't use it in production.

License
-------

[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#license)

MIT

## Metadata

```json
{
  "title": "GitHub - alexluong/gatsby-theme-comments: Drop-in comment functionality for static Gatsby site, powered by Firebase",
  "description": "Drop-in comment functionality for static Gatsby site, powered by Firebase - alexluong/gatsby-theme-comments",
  "url": "https://github.com/alexluong/gatsby-theme-comments?screenshot=true",
  "content": "gatsby-theme-comments\n---------------------\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#gatsby-theme-comments)\n\nProvides drop-in comment functionality for static Gatsby site, powered by Firebase\n\nThe problem\n-----------\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#the-problem)\n\nYou want to drive engagement for your Gatsby blog via comments.\n\nThis solution\n-------------\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#this-solution)\n\nThis is a Gatsby theme that let you add comment section to your blog.\n\nThis differs from other solutions in that it gives you complete control of your data and UI. You store your data on your own database, and you can modify the design as you see fit.\n\nTable of Contents\n-----------------\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#table-of-contents)\n\n*   [gatsby-theme-comments](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#gatsby-theme-comments)\n    *   [The problem](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#the-problem)\n    *   [This solution](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#this-solution)\n    *   [Table of Contents](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#table-of-contents)\n    *   [Installation](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#installation)\n    *   [Usage](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usage)\n        *   [1\\. Register plugins](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#1-register-plugins)\n        *   [2\\. Set up Firestore and environment variables](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#2-set-up-firestore-and-environment-variables)\n        *   [3\\. Use in React](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#3-use-in-react)\n    *   [Showcase](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#showcase)\n        *   [UI child themes of `gatsby-theme-comments`](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#ui-child-themes-of-gatsby-theme-comments)\n        *   [Sites that uses `gatsby-theme-comments`](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#sites-that-uses-gatsby-theme-comments)\n    *   [APIs](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#apis)\n        *   [Comment](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#comment)\n        *   [Exports](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#exports)\n            *   [CommentSection](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#commentsection)\n                *   [id](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#id)\n            *   [CommentCount](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#commentcount)\n                *   [id](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#id-1)\n            *   [useComments](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usecomments)\n            *   [useCommentCount](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usecommentcount)\n            *   [useAddComment](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#useaddcomment)\n        *   [Shadowable Components](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#shadowable-components)\n        *   [Demo](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#demo)\n    *   [License](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#license)\n\nInstallation\n------------\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#installation)\n\n```\nnpm install gatsby-theme-comments gatsby-plugin-firebase\nnpm install -D dotenv\n```\n\nUsage\n-----\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usage)\n\n### 1\\. Register plugins\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#1-register-plugins)\n\nIn `gatsby-config.js`:\n\nrequire(\"dotenv\").config()\n\nmodule.exports \\= {\n  plugins: \\[\n    ...otherPlugins,\n\n    \"gatsby-plugin-firebase\",\n    \"gatsby-theme-comments\",\n  \\],\n}\n\n### 2\\. Set up Firestore and environment variables\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#2-set-up-firestore-and-environment-variables)\n\n*   Create a Firebase project\n*   Create a new Firestore database\n*   Inside the `Database` page, open the `Indexes` tab and add a composite index like so:\n\n[![Image 7: Firestore index instruction](https://github.com/alexluong/gatsby-theme-comments/raw/master/firestore-index.png?raw=true)](https://github.com/alexluong/gatsby-theme-comments/blob/master/firestore-index.png?raw=true)\n\n*   Create a `.env` in your root directory:\n\n```\nGATSBY_FIREBASE_API_KEY=<YOUR_FIREBASE_API_KEY>\nGATSBY_FIREBASE_AUTH_DOMAIN=<YOUR_FIREBASE_AUTH_DOMAIN>\nGATSBY_FIREBASE_DATABASE_URL=<YOUR_FIREBASE_DATABASE_URL>\nGATSBY_FIREBASE_PROJECT_ID=<YOUR_FIREBASE_PROJECT_ID>\nGATSBY_FIREBASE_STORAGE_BUCKET=<YOUR_FIREBASE_STORAGE_BUCKET>\nGATSBY_FIREBASE_MESSAGING_SENDER_ID=<YOUR_FIREBASE_MESSAGING_SENDER_ID>\nGATSBY_FIREBASE_APP_ID=<YOUR_FIREBASE_APP_ID>\n```\n\n### 3\\. Use in React\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#3-use-in-react)\n\nIn your post template (`src/templates/post.js`), you can use `CommentSection` in your JSX:\n\nimport { CommentSection } from \"gatsby-theme-comments\"\n\n...\n\nreturn (\n  <Layout\\>\n    <Article /\\>\n    <Author /\\>\n\n    <CommentSection id\\={slug} /\\>\n  </Layout\\>\n)\n\nThe `id` prop must be a unique string or number that identifies the post. It can be the post's id, slug, or title, but do be aware that you'd lose track of the comments if you change that id.\n\nFor example, let's say that you use `slug` as the identifier. If you want to change the post's slug, remember to go into your Firebase database and change that value too.\n\nShowcase\n--------\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#showcase)\n\n### UI child themes of `gatsby-theme-comments`\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#ui-child-themes-of-gatsby-theme-comments)\n\n*   [Barebone/Core](https://npmjs.com/package/gatsby-theme-comments)\n*   [Minimal UI](https://npmjs.com/package/gatsby-theme-comments-ui)\n\nIf you wrote a child theme for `gatsby-theme-comments`, please submit a [PR](https://github.com/alexluong/gatsby-theme-comments/edit/master/README.md) to add your theme to the list.\n\n### Sites that uses `gatsby-theme-comments`\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#sites-that-uses-gatsby-theme-comments)\n\nNobody is using this plugin. Sad face 😢\n\nIf you use `gatsby-theme-comments`, please submit a [PR](https://github.com/alexluong/gatsby-theme-comments/edit/master/README.md) to add your site to the list.\n\nFeel free to reach out or open an issue if you're interested in using this. I'm available to answer any questions or take feature requests.\n\nAPIs\n----\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#apis)\n\n### Comment\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#comment)\n\nThe `Comment` interface is an object that looks like this:\n\ninterface Comment {\n  id: string;\n  content: string;\n  name: string;\n  createdAt: Timestamp;\n  updatedAt: Timestamp;\n}\n\ninterface Timestamp {\n  nanoseconds: number;\n  milliseconds: number;\n  toDate: function;\n}\n\n### Exports\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#exports)\n\n#### CommentSection\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#commentsection)\n\nA component that renders a form for users to add comment as well as all the comments of the post. This is the simplest way to use `gatsby-theme-comments`. You can use this component in your `Post` template.\n\n##### id\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#id)\n\n> `string` | _required_\n\nA unique identifier used to identify each post. It cannot contain special characters such as \"/\".\n\n#### CommentCount\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#commentcount)\n\nA component that renders the comment count of the post\n\n##### id\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#id-1)\n\n> `string` | _required_\n\nA unique identifier used to identify each post\n\n#### useComments\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usecomments)\n\n> `function(id: string): { loading: boolean, error: Error, comments: Array<Comment> }`\n\nThis hook takes the identifier as argument and gives you the corresponding array of comments.\n\nIf the identifier is invalid, the comment array is empty.\n\nfunction Comments({ id }) {\n  const { loading, comments } \\= useComments()\n\n  if (loading) {\n    return <p\\>Loading...</p\\>\n  }\n\n  return (\n    <ul\\>\n      {comments.map(comment) \\=\\> (\n        <li key\\={comment.id}\\>{comment.content}</li\\>\n      )}\n    </ul\\>\n  )\n}\n\n#### useCommentCount\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#usecommentcount)\n\n> `function(id: string): { loading: boolean, error: Error, commentCount: number }`\n\nThis hook takes the identifier as argument and gives you the corresponding number of comments.\n\nIf the identifier is invalid, the count is 0. The reason for this is that the plugin only keeps track of posts with at least 1 comment. Therefore, if a post doesn't have any, its `id` would not be available in database.\n\nfunction CommentCount({ id }) {\n  const { loading, commentCount } \\= useCommentCount()\n\n  if (loading) {\n    return <p\\>0 comment</p\\>\n  }\n\n  return <p\\>{commentCount} comment{commentCount \\> 1 ? \"s\" : \"\"}</p\\>\n}\n\n#### useAddComment\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#useaddcomment)\n\n> `function(): { loading: boolean, error: Error, addComment: function(comment: Comment): void }`\n\nThis hook returns a function for you to add comment to database.\n\nfunction AddComment({ comment }) {\n  const { addComment } \\= useAddComment()\n\n  return (\n    <button onClick\\={() \\=\\> addComment(comment)}\\>Add</button\\>\n  )\n}\n\n_Note_: The `Comment` you pass to the `addComment` function is one without `Timestamp`. The `createdAt` field will be included whenever the plugin makes a call to Firebase. You don't have to construct that value.\n\n### Shadowable Components\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#shadowable-components)\n\nHere is a list of recommended components that you can shadow:\n\n*   `components/Button.js`\n*   `components/Comment.js`\n*   `components/CommentCount.js`\n*   `components/Comments.js`\n*   `components/Form.js`\n*   `components/Loading.js`\n*   `components/TextField.js`\n\nDemo\n----\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#demo)\n\nTo run the demo,\n\n*   Clone this project\n*   `cd` into `examples/demo`\n*   Add your Firebase details to `.env`\n*   Create an index in Firestore as shown in the second section\n*   Run `npm start`\n*   Try out the project on `localhost:8000`\n\n**Note**: Depending on how you've set up your Firestore project, you may have to change the permissions first. A good starting point would be:\n\nservice cloud.firestore {\n  match /databases/{database}/documents {\n    match /{document\\=\\*\\*} {\n      allow read, write: if true;\n    }\n  }\n}\n\nJust don't use it in production.\n\nLicense\n-------\n\n[](https://github.com/alexluong/gatsby-theme-comments?screenshot=true#license)\n\nMIT",
  "usage": {
    "tokens": 2825
  }
}
```
