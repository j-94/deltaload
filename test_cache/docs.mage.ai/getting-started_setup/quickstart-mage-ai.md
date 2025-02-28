---
title: Quickstart - Mage AI
description: Go from zero to Mage hero in under a minute. We'll walk you through installing Mage and running your first pipeline. 🦸‍♀️
url: https://docs.mage.ai/getting-started/setup#docker-compose-template
timestamp: 2025-01-20T16:13:55.855Z
domain: docs.mage.ai
path: getting-started_setup
---

# Quickstart - Mage AI


Go from zero to Mage hero in under a minute. We'll walk you through installing Mage and running your first pipeline. 🦸‍♀️


## Content

Mage Pro overview
-----------------

After creating a Mage Pro account or logging into Mage Pro you are directed to the cluster management portal. Here you can manage your Mage clusters.

### Cluster Pages

1.  **Creating a New Cluster**:
    *   On the clusters page, you can create a new cluster by clicking the “Launch new cluster” button.
    *   Fill in the required field **Cluster Name**. Note that environment variables can be customized after the cluster is created.

2.  **Viewing Cluster List**:
    *   The cluster list page provides an overview of all your clusters, displaying essential information such as the cluster status, ID, UUID, cloud provider, and the number of replicas.
3.  **Cluster Details**:
    *   Click the “Open cluster” button to view detailed information about the cluster. Here, you can see various metrics and statuses that help you monitor and manage your cluster effectively.
    *   Follow the [environment variables](https://docs.mage.ai/development/variables/environment-variables) documentation to customize your Mage Pro cluster.

### Cluster login

1.  **Accessing the cluster**:
    *   Click the “Open cluster” button to navigate to the actual Mage cluster page. Here, you can interact with your cluster and use the Mage tool as you normally would.
    *   Currently, we use separate databases for each cluster for enhanced security. The users credentials in the Mage Pro cluster are managed inside the cluster. Use the default owner credentials (email: [admin@admin.com](mailto:admin@admin.com), password: **admin**) to log in. After you login, you should either update the password of the default owner user or create your own owner user.

### Run your first pipeline

*   **Step 1**: From the pipeline editor page click the “New pipeline” button
*   **Step 2**: Select a template for inspiration or start from scratch by clicking the “Start from scratch” button
*   **Step 3**: Select your pipeline type and give it an optional new name, description, and tag
*   **Step 4**: Click the create new pipline button
*   **Step 5**: Add your blocks by following the Youtube video below

⛵️ Mage OSS overview
--------------------

We recommend using Docker to get started.

Docker is a tool that allows you to run Mage in a containerized environment: you can run Mage on any operating system that supports Docker, including Windows, Mac, and Linux. Using Docker means that you don’t have to worry about installing dependencies or configuring your environment. If you’d like to install Mage without Docker, you can use `pip` or `conda`.

If you’re familiar with [Docker Compose](https://docs.docker.com/compose/) or plan on adding or extending images (e.g. Postgres) in your project, we recommend starting from the _Docker compose template_. Otherwise, we recommend _Docker run_.

🪄 Get Mage
-----------

🏃‍♂️ Run your first pipeline
-----------------------------

If you haven’t already, open a browser to `http://localhost:6789`. From the pipelines page, select `example_pipeline` and open the notebook view by selecting `Edit pipeline` from the left side nav.

Select the first block by clicking it and select the “play” icon in the top right to run the block. You’ve just ran your first Mage block & loaded data from a dataset!

Do the same for the following cells in the pipeline to transform and export the data. Congrats, you’re now a Mage ninja! 🥷

🧙🏻‍♂️ Install Mage dependencies (optional)
--------------------------------------------

Mage also has the following add-on packages:

| Package | Install | Description |
| --- | --- | --- |
| all | `mage-ai[all]` | install all add-ons |
| azure | `mage-ai[azure]` | install Azure related packages |
| clickhouse | `mage-ai[clickhouse]` | use Clickhouse for data import or export |
| dbt | `mage-ai[dbt]` | install dbt packages |
| google-cloud-storage | `mage-ai[google-cloud-storage]` | use Google Cloud Storage for data import or export |
| hdf5 | `mage-ai[hdf5]` | process data in HDF5 file format |
| mysql | `mage-ai[mysql]` | use MySQL for data import or export |
| postgres | `mage-ai[postgres]` | use PostgreSQL for data import or export |
| redshift | `mage-ai[redshift]` | use Redshift for data import or export |
| s3 | `mage-ai[s3]` | use S3 for data import or export |
| snowflake | `mage-ai[snowflake]` | use Snowflake for data import or export |
| spark | `mage-ai[spark]` | use Spark (EMR) in your Mage pipeline |
| streaming | `mage-ai[streaming]` | use Streaming pipelines |

To install these, run the following command from the Mage terminal:

or add the following to your `requirements.txt` file:

You can access the terminal from the side nav on the right in the pipeline editor page. Read more about installing from `requirements.txt` [here](https://docs.mage.ai/development/dependencies/requirements).

🧭 Journey on
-------------

Navigate to our [tutorials](https://docs.mage.ai/guides/overview) to learn more about Mage and how to build your own pipelines or continue exploring our docs for advanced configuration and deployment options.

If you’re interested in connecting a database in Docker, check out our [guide](https://docs.mage.ai/guides/docker/connecting-a-database) for more information.

## Metadata

```json
{
  "title": "Quickstart - Mage AI",
  "description": "Go from zero to Mage hero in under a minute. We'll walk you through installing Mage and running your first pipeline. 🦸‍♀️",
  "url": "https://docs.mage.ai/getting-started/setup#docker-compose-template",
  "content": "Mage Pro overview\n-----------------\n\nAfter creating a Mage Pro account or logging into Mage Pro you are directed to the cluster management portal. Here you can manage your Mage clusters.\n\n### Cluster Pages\n\n1.  **Creating a New Cluster**:\n    *   On the clusters page, you can create a new cluster by clicking the “Launch new cluster” button.\n    *   Fill in the required field **Cluster Name**. Note that environment variables can be customized after the cluster is created.\n\n2.  **Viewing Cluster List**:\n    *   The cluster list page provides an overview of all your clusters, displaying essential information such as the cluster status, ID, UUID, cloud provider, and the number of replicas.\n3.  **Cluster Details**:\n    *   Click the “Open cluster” button to view detailed information about the cluster. Here, you can see various metrics and statuses that help you monitor and manage your cluster effectively.\n    *   Follow the [environment variables](https://docs.mage.ai/development/variables/environment-variables) documentation to customize your Mage Pro cluster.\n\n### Cluster login\n\n1.  **Accessing the cluster**:\n    *   Click the “Open cluster” button to navigate to the actual Mage cluster page. Here, you can interact with your cluster and use the Mage tool as you normally would.\n    *   Currently, we use separate databases for each cluster for enhanced security. The users credentials in the Mage Pro cluster are managed inside the cluster. Use the default owner credentials (email: [admin@admin.com](mailto:admin@admin.com), password: **admin**) to log in. After you login, you should either update the password of the default owner user or create your own owner user.\n\n### Run your first pipeline\n\n*   **Step 1**: From the pipeline editor page click the “New pipeline” button\n*   **Step 2**: Select a template for inspiration or start from scratch by clicking the “Start from scratch” button\n*   **Step 3**: Select your pipeline type and give it an optional new name, description, and tag\n*   **Step 4**: Click the create new pipline button\n*   **Step 5**: Add your blocks by following the Youtube video below\n\n⛵️ Mage OSS overview\n--------------------\n\nWe recommend using Docker to get started.\n\nDocker is a tool that allows you to run Mage in a containerized environment: you can run Mage on any operating system that supports Docker, including Windows, Mac, and Linux. Using Docker means that you don’t have to worry about installing dependencies or configuring your environment. If you’d like to install Mage without Docker, you can use `pip` or `conda`.\n\nIf you’re familiar with [Docker Compose](https://docs.docker.com/compose/) or plan on adding or extending images (e.g. Postgres) in your project, we recommend starting from the _Docker compose template_. Otherwise, we recommend _Docker run_.\n\n🪄 Get Mage\n-----------\n\n🏃‍♂️ Run your first pipeline\n-----------------------------\n\nIf you haven’t already, open a browser to `http://localhost:6789`. From the pipelines page, select `example_pipeline` and open the notebook view by selecting `Edit pipeline` from the left side nav.\n\nSelect the first block by clicking it and select the “play” icon in the top right to run the block. You’ve just ran your first Mage block & loaded data from a dataset!\n\nDo the same for the following cells in the pipeline to transform and export the data. Congrats, you’re now a Mage ninja! 🥷\n\n🧙🏻‍♂️ Install Mage dependencies (optional)\n--------------------------------------------\n\nMage also has the following add-on packages:\n\n| Package | Install | Description |\n| --- | --- | --- |\n| all | `mage-ai[all]` | install all add-ons |\n| azure | `mage-ai[azure]` | install Azure related packages |\n| clickhouse | `mage-ai[clickhouse]` | use Clickhouse for data import or export |\n| dbt | `mage-ai[dbt]` | install dbt packages |\n| google-cloud-storage | `mage-ai[google-cloud-storage]` | use Google Cloud Storage for data import or export |\n| hdf5 | `mage-ai[hdf5]` | process data in HDF5 file format |\n| mysql | `mage-ai[mysql]` | use MySQL for data import or export |\n| postgres | `mage-ai[postgres]` | use PostgreSQL for data import or export |\n| redshift | `mage-ai[redshift]` | use Redshift for data import or export |\n| s3 | `mage-ai[s3]` | use S3 for data import or export |\n| snowflake | `mage-ai[snowflake]` | use Snowflake for data import or export |\n| spark | `mage-ai[spark]` | use Spark (EMR) in your Mage pipeline |\n| streaming | `mage-ai[streaming]` | use Streaming pipelines |\n\nTo install these, run the following command from the Mage terminal:\n\nor add the following to your `requirements.txt` file:\n\nYou can access the terminal from the side nav on the right in the pipeline editor page. Read more about installing from `requirements.txt` [here](https://docs.mage.ai/development/dependencies/requirements).\n\n🧭 Journey on\n-------------\n\nNavigate to our [tutorials](https://docs.mage.ai/guides/overview) to learn more about Mage and how to build your own pipelines or continue exploring our docs for advanced configuration and deployment options.\n\nIf you’re interested in connecting a database in Docker, check out our [guide](https://docs.mage.ai/guides/docker/connecting-a-database) for more information.",
  "usage": {
    "tokens": 1218
  }
}
```
