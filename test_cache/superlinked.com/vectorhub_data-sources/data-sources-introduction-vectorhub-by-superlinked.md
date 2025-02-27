---
title: Data Sources: Introduction | VectorHub by Superlinked
description: Understand the different data sources and considerations for processing that data to build a robust information retrieval system.
url: https://superlinked.com/vectorhub/data-sources
timestamp: 2025-01-20T16:00:38.458Z
domain: superlinked.com
path: vectorhub_data-sources
---

# Data Sources: Introduction | VectorHub by Superlinked


Understand the different data sources and considerations for processing that data to build a robust information retrieval system.


## Content

A robust vector retrieval system relies on a thoughtful selection of data sources that align with the system’s objectives. Different use cases demand different kinds and combinations of data.

If, for example, your organization runs a personalized movie recommendation system, you need data on customer preferences and viewing history. Whereas if you operate an automatic fraud detection system, your primary data source is transactional data.

In other words, data sources form the bedrock upon which your retrieval system stands. It’s important, therefore, to understand what different types and combinations of data are available, and what they make possible – both generally and in your specific instance. You need a data map.

The Data Map - A Mosaic of Data Types and Combinations
------------------------------------------------------

An organization’s data is rarely uniform. Instead, the data landscape of any organization is a mosaic that can be characterized in terms of its **velocity** (ranging from stream to batch data), its **modality** / type (spanning structured to unstructured data), and its **sources** (originating from in-house systems and/or third-party providers).

Where your data falls along these three dimensions (velocity, modality, source) determines what you can do with it – that is, what use cases you can accommodate, and how you should configure your data retrieval stack to meet your objectives. In order to shape your data retrieval stack optimally, you need to build a mental model of your available data and understand its potential.

### Example: Pinterest technology stack

What you choose for your data and ML stack can make or break your whole product. Let’s look at an example of how your product strategy and use case can prescribe the kinds of decisions you make about your data and your ML Stack.

Pinterest used a product-led growth strategy that relied upon a curated feed of recommended “Pins”. Due to the highly viral nature of the product, this strategy allowed Pinterest to raise [$564 million pre-revenue](https://www.entrepreneur.com/science-technology/no-revenue-no-problem-pinterest-raises-another-225/229597), ultimately growing to over 72.8 million users.

Pinterest uses diverse data types to improve the recommendation performance of its feed, including mechanisms to handle: - **Structured data** (e.g., user profiles): This includes well-defined attributes with specific formats. - **Semi-structured data** (e.g., event logs): These follow a general structure but may have varying fields or additional context. - **Unstructured data** (e.g., images): These are typically files without a fixed schema.

Below is an overview of the data & ML stack Pinterest uses to convert all this data (above) to product value.

![Image 11: Pinterest Tech Stack](https://raw.githubusercontent.com/superlinked/VectorHub/main/docs/assets/building_blocks/data_sources/bb1-1.png)

1.  **Event Streaming Platform**:
    
    *   Pinterest relies on an **event streaming platform**, [Flink](https://medium.com/pinterest-engineering/unified-flink-source-at-pinterest-streaming-data-processing-c9d4e89f2ed6#:~:text=To%20best%20serve%20Pinners%2C%20creators,as%20its%20stream%20processing%20engine), to collect real-time event data. This platform allows them to easily collect, enrich, and transform event attributes.
    *   In practice, the event streaming system handles real-time data ingestion, ensuring that events from user interactions, content uploads, and other actions are captured efficiently.
    *   These events can be considered **semi-structured** – they follow a specific format (e.g., JSON) but may vary in content.
2.  **Data Storage and Querying**:
    
    *   For **persistent storage**, Pinterest utilizes technologies like **DynamoDB** (a NoSQL database service by AWS). DynamoDB provides scalability, reliability, and security for Pinterest’s massive dataset.
    *   The architecture supports various querying needs:
        *   Real-time exploration of raw incoming data for monitoring and analytics (semi-structured data).
        *   Cached queries that can instantly be loaded into applications and reports for customer-facing metrics (structured data).
        *   The data stored in DynamoDB includes:
            *   User profiles (structured data).
            *   Event logs (semi-structured data).
            *   Images and other media (unstructured data).
3.  **Data Analysis**:
    
    *   Pinterest’s engineers use [**Querybook**](https://medium.com/pinterest-engineering/open-sourcing-querybook-pinterests-collaborative-big-data-hub-ba2605558883), a collaborative big data hub that allows internal users to query and analyze data efficiently. Each **DataDoc** in Querybook consists of cells (text, query, or chart) that facilitate exploration and visualization.
    *   The system supports complex queries for trend analysis, anomaly detection, recommendation algorithms, and personalized content delivery.

For precise details about Pinterest’s specific data types and components, check out their [engineering blog](https://medium.com/@Pinterest_Engineering).

Now let's dive into the details.

### **1.1 Data Velocity**

The choice of data processing velocity is pivotal in determining the kind of data retrieval and vector compute tasks you can perform. Different velocities offer distinct advantages and make different use cases possible.

[Read more about different data velocities, here](https://superlinked.com/vectorhub/building-blocks/data-sources/data-modality)

### **1.2 Data Modality**

Whether your data is structured, unstructured, or hybrid is crucial when evaluating data sources. The nature of the data source your vector retrieval system uses shapes how that data should be managed and processed.

[Read more about how to manage different data types/modalities, here](https://superlinked.com/vectorhub/building-blocks/data-sources/data-velocity)

### **1.3 Conclusions & Next Steps**

So what does this all mean?

[Read our conclusions and recommended next steps, here](https://superlinked.com/vectorhub/building-blocks/data-sources/conclusion)

Contributors
------------

*   [Daniel Svonava](https://www.linkedin.com/in/svonava/)
*   [Paolo Perrone](https://www.linkedin.com/in/paoloperrone/)
*   [Robert Turner, editor](https://robertturner.co/copyedit)

## Metadata

```json
{
  "title": "Data Sources: Introduction | VectorHub by Superlinked",
  "description": "Understand the different data sources and considerations for processing that data to build a robust information retrieval system.",
  "url": "https://superlinked.com/vectorhub/data-sources",
  "content": "A robust vector retrieval system relies on a thoughtful selection of data sources that align with the system’s objectives. Different use cases demand different kinds and combinations of data.\n\nIf, for example, your organization runs a personalized movie recommendation system, you need data on customer preferences and viewing history. Whereas if you operate an automatic fraud detection system, your primary data source is transactional data.\n\nIn other words, data sources form the bedrock upon which your retrieval system stands. It’s important, therefore, to understand what different types and combinations of data are available, and what they make possible – both generally and in your specific instance. You need a data map.\n\nThe Data Map - A Mosaic of Data Types and Combinations\n------------------------------------------------------\n\nAn organization’s data is rarely uniform. Instead, the data landscape of any organization is a mosaic that can be characterized in terms of its **velocity** (ranging from stream to batch data), its **modality** / type (spanning structured to unstructured data), and its **sources** (originating from in-house systems and/or third-party providers).\n\nWhere your data falls along these three dimensions (velocity, modality, source) determines what you can do with it – that is, what use cases you can accommodate, and how you should configure your data retrieval stack to meet your objectives. In order to shape your data retrieval stack optimally, you need to build a mental model of your available data and understand its potential.\n\n### Example: Pinterest technology stack\n\nWhat you choose for your data and ML stack can make or break your whole product. Let’s look at an example of how your product strategy and use case can prescribe the kinds of decisions you make about your data and your ML Stack.\n\nPinterest used a product-led growth strategy that relied upon a curated feed of recommended “Pins”. Due to the highly viral nature of the product, this strategy allowed Pinterest to raise [$564 million pre-revenue](https://www.entrepreneur.com/science-technology/no-revenue-no-problem-pinterest-raises-another-225/229597), ultimately growing to over 72.8 million users.\n\nPinterest uses diverse data types to improve the recommendation performance of its feed, including mechanisms to handle: - **Structured data** (e.g., user profiles): This includes well-defined attributes with specific formats. - **Semi-structured data** (e.g., event logs): These follow a general structure but may have varying fields or additional context. - **Unstructured data** (e.g., images): These are typically files without a fixed schema.\n\nBelow is an overview of the data & ML stack Pinterest uses to convert all this data (above) to product value.\n\n![Image 11: Pinterest Tech Stack](https://raw.githubusercontent.com/superlinked/VectorHub/main/docs/assets/building_blocks/data_sources/bb1-1.png)\n\n1.  **Event Streaming Platform**:\n    \n    *   Pinterest relies on an **event streaming platform**, [Flink](https://medium.com/pinterest-engineering/unified-flink-source-at-pinterest-streaming-data-processing-c9d4e89f2ed6#:~:text=To%20best%20serve%20Pinners%2C%20creators,as%20its%20stream%20processing%20engine), to collect real-time event data. This platform allows them to easily collect, enrich, and transform event attributes.\n    *   In practice, the event streaming system handles real-time data ingestion, ensuring that events from user interactions, content uploads, and other actions are captured efficiently.\n    *   These events can be considered **semi-structured** – they follow a specific format (e.g., JSON) but may vary in content.\n2.  **Data Storage and Querying**:\n    \n    *   For **persistent storage**, Pinterest utilizes technologies like **DynamoDB** (a NoSQL database service by AWS). DynamoDB provides scalability, reliability, and security for Pinterest’s massive dataset.\n    *   The architecture supports various querying needs:\n        *   Real-time exploration of raw incoming data for monitoring and analytics (semi-structured data).\n        *   Cached queries that can instantly be loaded into applications and reports for customer-facing metrics (structured data).\n        *   The data stored in DynamoDB includes:\n            *   User profiles (structured data).\n            *   Event logs (semi-structured data).\n            *   Images and other media (unstructured data).\n3.  **Data Analysis**:\n    \n    *   Pinterest’s engineers use [**Querybook**](https://medium.com/pinterest-engineering/open-sourcing-querybook-pinterests-collaborative-big-data-hub-ba2605558883), a collaborative big data hub that allows internal users to query and analyze data efficiently. Each **DataDoc** in Querybook consists of cells (text, query, or chart) that facilitate exploration and visualization.\n    *   The system supports complex queries for trend analysis, anomaly detection, recommendation algorithms, and personalized content delivery.\n\nFor precise details about Pinterest’s specific data types and components, check out their [engineering blog](https://medium.com/@Pinterest_Engineering).\n\nNow let's dive into the details.\n\n### **1.1 Data Velocity**\n\nThe choice of data processing velocity is pivotal in determining the kind of data retrieval and vector compute tasks you can perform. Different velocities offer distinct advantages and make different use cases possible.\n\n[Read more about different data velocities, here](https://superlinked.com/vectorhub/building-blocks/data-sources/data-modality)\n\n### **1.2 Data Modality**\n\nWhether your data is structured, unstructured, or hybrid is crucial when evaluating data sources. The nature of the data source your vector retrieval system uses shapes how that data should be managed and processed.\n\n[Read more about how to manage different data types/modalities, here](https://superlinked.com/vectorhub/building-blocks/data-sources/data-velocity)\n\n### **1.3 Conclusions & Next Steps**\n\nSo what does this all mean?\n\n[Read our conclusions and recommended next steps, here](https://superlinked.com/vectorhub/building-blocks/data-sources/conclusion)\n\nContributors\n------------\n\n*   [Daniel Svonava](https://www.linkedin.com/in/svonava/)\n*   [Paolo Perrone](https://www.linkedin.com/in/paoloperrone/)\n*   [Robert Turner, editor](https://robertturner.co/copyedit)",
  "usage": {
    "tokens": 1322
  }
}
```
