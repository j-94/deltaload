---
title: PocketBase - Open Source backend in 1 file
description: Open Source backend in 1 file with realtime database, authentication, file storage and admin dashboard
url: https://pocketbase.io/
timestamp: 2025-01-20T15:57:28.156Z
domain: pocketbase.io
path: root
---

# PocketBase - Open Source backend in 1 file


Open Source backend in 1 file with realtime database, authentication, file storage and admin dashboard


## Content

Open Source backend

**in 1 file**

Realtime database

Authentication

File storage

Admin dashboard

![Image 16: Gopher](blob:https://pocketbase.io/6423885fd1dc1ff3158f95ef3d26e589)

![Image 17: PocketBase dashboard preview](blob:https://pocketbase.io/da1d1e5b54f60fd4d48c1a06a7b03276)

Ready to use out of the box
---------------------------

[Explore all features](https://pocketbase.io/docs)

```
// JavaScript SDK
import PocketBase from 'pocketbase';

const pb = new PocketBase('http://127.0.0.1:8090');

...

// list and search for 'example' collection records
const list = await pb.collection('example').getList(1, 100, {
    filter: 'title != "" && created > "2022-08-01"',
    sort: '-created,title',
});

// or fetch a single 'example' collection record
const record = await pb.collection('example').getOne('RECORD_ID');

// delete a single 'example' collection record
await pb.collection('example').delete('RECORD_ID');

// create a new 'example' collection record
const newRecord = await pb.collection('example').create({
    title: 'Lorem ipsum dolor sit amet',
});

// subscribe to changes in any record from the 'example' collection
pb.collection('example').subscribe('*', function (e) {
    console.log(e.record);
});

// stop listening for changes in the 'example' collection
pb.collection('example').unsubscribe();
```

Integrate nicely with your favorite frontend stack
--------------------------------------------------

[![Image 18: Flutter logo](https://pocketbase.io/images/flutter_logo.svg?v2)](https://github.com/pocketbase/dart-sdk) [![Image 19: Svelte logo](https://pocketbase.io/images/svelte_logo.svg?v2)](https://github.com/pocketbase/js-sdk) [![Image 20: Vue logo](https://pocketbase.io/images/vue_logo.svg?v2)](https://github.com/pocketbase/js-sdk) [![Image 21: React logo](https://pocketbase.io/images/react_logo.svg?v2)](https://github.com/pocketbase/js-sdk) [![Image 22: Angular logo](https://pocketbase.io/images/angular_logo.svg?v2)](https://github.com/pocketbase/js-sdk)

## Metadata

```json
{
  "title": "PocketBase - Open Source backend in 1 file",
  "description": "Open Source backend in 1 file with realtime database, authentication, file storage and admin dashboard",
  "url": "https://pocketbase.io/",
  "content": "Open Source backend\n\n**in 1 file**\n\nRealtime database\n\nAuthentication\n\nFile storage\n\nAdmin dashboard\n\n![Image 16: Gopher](blob:https://pocketbase.io/6423885fd1dc1ff3158f95ef3d26e589)\n\n![Image 17: PocketBase dashboard preview](blob:https://pocketbase.io/da1d1e5b54f60fd4d48c1a06a7b03276)\n\nReady to use out of the box\n---------------------------\n\n[Explore all features](https://pocketbase.io/docs)\n\n```\n// JavaScript SDK\nimport PocketBase from 'pocketbase';\n\nconst pb = new PocketBase('http://127.0.0.1:8090');\n\n...\n\n// list and search for 'example' collection records\nconst list = await pb.collection('example').getList(1, 100, {\n    filter: 'title != \"\" && created > \"2022-08-01\"',\n    sort: '-created,title',\n});\n\n// or fetch a single 'example' collection record\nconst record = await pb.collection('example').getOne('RECORD_ID');\n\n// delete a single 'example' collection record\nawait pb.collection('example').delete('RECORD_ID');\n\n// create a new 'example' collection record\nconst newRecord = await pb.collection('example').create({\n    title: 'Lorem ipsum dolor sit amet',\n});\n\n// subscribe to changes in any record from the 'example' collection\npb.collection('example').subscribe('*', function (e) {\n    console.log(e.record);\n});\n\n// stop listening for changes in the 'example' collection\npb.collection('example').unsubscribe();\n```\n\nIntegrate nicely with your favorite frontend stack\n--------------------------------------------------\n\n[![Image 18: Flutter logo](https://pocketbase.io/images/flutter_logo.svg?v2)](https://github.com/pocketbase/dart-sdk) [![Image 19: Svelte logo](https://pocketbase.io/images/svelte_logo.svg?v2)](https://github.com/pocketbase/js-sdk) [![Image 20: Vue logo](https://pocketbase.io/images/vue_logo.svg?v2)](https://github.com/pocketbase/js-sdk) [![Image 21: React logo](https://pocketbase.io/images/react_logo.svg?v2)](https://github.com/pocketbase/js-sdk) [![Image 22: Angular logo](https://pocketbase.io/images/angular_logo.svg?v2)](https://github.com/pocketbase/js-sdk)",
  "usage": {
    "tokens": 529
  }
}
```
