---
title: Import Airtable • Rowy Docs
description: Rowy allows users to create a new table from an existing Airtable collection. This is useful if you have a pre-existing data on Airtable and want to import it to Rowy.
url: https://docs.rowy.io/import-export-data/import-airtable
timestamp: 2025-01-20T15:49:40.381Z
domain: docs.rowy.io
path: import-export-data_import-airtable
---

# Import Airtable • Rowy Docs


Rowy allows users to create a new table from an existing Airtable collection. This is useful if you have a pre-existing data on Airtable and want to import it to Rowy.


## Content

Rowy allows users to create a new table from an existing Airtable collection. This is useful if you have a pre-existing data on Airtable and want to import it to Rowy.

Rowy allows a lot of new functionalities that gives you more control over your data. Users can not just view their Firestore data in an Airtable-like UI, but also **build cloud functions**, **automations and workflows** based on their data. **Connect to any third-party tool**, use NPM and APIs right in the browser without the hassle of CLIs, terminals or native consoles.

1.  After creating a new table, click on the **Import Data** button.
    
2.  Select **Airtable** as the data source.
    
3.  Add the **Airtable API Key** and the **Table URL**. You can find how to generate the [API key](https://docs.rowy.io/import-export-data/import-airtable#retrieving-the-airtable-api-key) and the [Table URL](https://docs.rowy.io/import-export-data/import-airtable#obtaining-the-airtable-table-url) in the sections below.
    
4.  Click on **Continue** to start the import process.
    
5.  Select the columns to be imported to Rowy, click **Continue**.
    
6.  Review the data to be imported and click **Finish**.
    

1.  Go to your [Airtable account](https://airtable.com/account) and click on **Generate API key**.
    
    ![Image 21: Generating an API key](https://docs.rowy.io/assets/images/generate-api-key-006cad6a70f843a499cf2bf8a723cf38.png)
2.  Copy the API key and paste it in the **API Key** field in Rowy.
    

To extract the **Table URL**, you need to go to the **Airtable collection** you want to import and copy the URL from the browser. The URL is divided into three parts:

*   Base (app)
*   Table (tbl)
*   View (viw)

**NOTE:** The view the user is currently in is the one that will display in the link.

The format for this address will look like this:

![Image 22: Table URL](https://docs.rowy.io/assets/images/table-url-83a10867d9c0e1fbf27d450c9a4ae140.png)

Copy the URL, as shown below, and paste it in the **Table URL** field in Rowy.

![Image 23: Copy URL](https://docs.rowy.io/assets/images/copy-url-dd506251223cd53a2394226222683af3.png)

![Image 24: Sample Airtable Import](https://docs.rowy.io/assets/images/sample-keys-16b78ff694183ce432878068e9551b14.png)

Rowy supports importing images directly from Airtable and allows you to store them as a native Image field.

![Image 25: Airtable Base](https://docs.rowy.io/assets/images/airtable-base-7572ebb65a00584db3a5f3365a5c372c.png)

In the above image, the `assets` column is an **Attachement** type field in our Airtable project, which contains the images.

When we import the data from Airtable using the above steps, we see that the `assets` column is imported as a **JSON** type field in Rowy. This is because as the data is transfered through an API, the **images are stored as JSON objects**. The JSON objects in this field would contain the reference data of the images.

![Image 26: Assets JSON](https://docs.rowy.io/assets/images/assets-json-a5d9ed1ae8b319f744f56c5eab8bd080.png)

Now, the question arises **how to import the images from the JSON objects to Rowy**. To do this, we need to create a **Cloud Function** that will extract the images from the JSON objects and store them as a native Image field in Rowy.

**Follow the steps below to create a Cloud Function that will import the images from Airtable to Rowy:**

1.  Add a **Derivative** column and pick a suitable name for it. In this example, we have named it `image`.
    
2.  This will open up the **column config** modal. Set the following:
    
    *   **Listener Field**: The `assets` JSON column.
    *   **Output Field Type**: Image
3.  Paste the following code in the Derivative Script and click **Save**:
    
    ```
    const derivative:Derivative = async ({row,ref,db,storage,auth,logging})=>{    const file = await rowy.storage.upload.url(row.assets[0].url)    return [file]}
    ```
    

**Now, everytime you import your images from Airtable, the images will be stored as an Image field in Rowy!** 🚀

![Image 27: Airtable Image](https://docs.rowy.io/assets/images/airtable-image-db5f680362ced9a354d800a3c9a1754d.png)

## Metadata

```json
{
  "title": "Import Airtable • Rowy Docs",
  "description": "Rowy allows users to create a new table from an existing Airtable collection. This is useful if you have a pre-existing data on Airtable and want to import it to Rowy.",
  "url": "https://docs.rowy.io/import-export-data/import-airtable",
  "content": "Rowy allows users to create a new table from an existing Airtable collection. This is useful if you have a pre-existing data on Airtable and want to import it to Rowy.\n\nRowy allows a lot of new functionalities that gives you more control over your data. Users can not just view their Firestore data in an Airtable-like UI, but also **build cloud functions**, **automations and workflows** based on their data. **Connect to any third-party tool**, use NPM and APIs right in the browser without the hassle of CLIs, terminals or native consoles.\n\n1.  After creating a new table, click on the **Import Data** button.\n    \n2.  Select **Airtable** as the data source.\n    \n3.  Add the **Airtable API Key** and the **Table URL**. You can find how to generate the [API key](https://docs.rowy.io/import-export-data/import-airtable#retrieving-the-airtable-api-key) and the [Table URL](https://docs.rowy.io/import-export-data/import-airtable#obtaining-the-airtable-table-url) in the sections below.\n    \n4.  Click on **Continue** to start the import process.\n    \n5.  Select the columns to be imported to Rowy, click **Continue**.\n    \n6.  Review the data to be imported and click **Finish**.\n    \n\n1.  Go to your [Airtable account](https://airtable.com/account) and click on **Generate API key**.\n    \n    ![Image 21: Generating an API key](https://docs.rowy.io/assets/images/generate-api-key-006cad6a70f843a499cf2bf8a723cf38.png)\n2.  Copy the API key and paste it in the **API Key** field in Rowy.\n    \n\nTo extract the **Table URL**, you need to go to the **Airtable collection** you want to import and copy the URL from the browser. The URL is divided into three parts:\n\n*   Base (app)\n*   Table (tbl)\n*   View (viw)\n\n**NOTE:** The view the user is currently in is the one that will display in the link.\n\nThe format for this address will look like this:\n\n![Image 22: Table URL](https://docs.rowy.io/assets/images/table-url-83a10867d9c0e1fbf27d450c9a4ae140.png)\n\nCopy the URL, as shown below, and paste it in the **Table URL** field in Rowy.\n\n![Image 23: Copy URL](https://docs.rowy.io/assets/images/copy-url-dd506251223cd53a2394226222683af3.png)\n\n![Image 24: Sample Airtable Import](https://docs.rowy.io/assets/images/sample-keys-16b78ff694183ce432878068e9551b14.png)\n\nRowy supports importing images directly from Airtable and allows you to store them as a native Image field.\n\n![Image 25: Airtable Base](https://docs.rowy.io/assets/images/airtable-base-7572ebb65a00584db3a5f3365a5c372c.png)\n\nIn the above image, the `assets` column is an **Attachement** type field in our Airtable project, which contains the images.\n\nWhen we import the data from Airtable using the above steps, we see that the `assets` column is imported as a **JSON** type field in Rowy. This is because as the data is transfered through an API, the **images are stored as JSON objects**. The JSON objects in this field would contain the reference data of the images.\n\n![Image 26: Assets JSON](https://docs.rowy.io/assets/images/assets-json-a5d9ed1ae8b319f744f56c5eab8bd080.png)\n\nNow, the question arises **how to import the images from the JSON objects to Rowy**. To do this, we need to create a **Cloud Function** that will extract the images from the JSON objects and store them as a native Image field in Rowy.\n\n**Follow the steps below to create a Cloud Function that will import the images from Airtable to Rowy:**\n\n1.  Add a **Derivative** column and pick a suitable name for it. In this example, we have named it `image`.\n    \n2.  This will open up the **column config** modal. Set the following:\n    \n    *   **Listener Field**: The `assets` JSON column.\n    *   **Output Field Type**: Image\n3.  Paste the following code in the Derivative Script and click **Save**:\n    \n    ```\n    const derivative:Derivative = async ({row,ref,db,storage,auth,logging})=>{    const file = await rowy.storage.upload.url(row.assets[0].url)    return [file]}\n    ```\n    \n\n**Now, everytime you import your images from Airtable, the images will be stored as an Image field in Rowy!** 🚀\n\n![Image 27: Airtable Image](https://docs.rowy.io/assets/images/airtable-image-db5f680362ced9a354d800a3c9a1754d.png)",
  "usage": {
    "tokens": 1099
  }
}
```
