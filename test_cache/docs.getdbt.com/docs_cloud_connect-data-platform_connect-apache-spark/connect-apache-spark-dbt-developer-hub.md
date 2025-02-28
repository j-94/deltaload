---
title: Connect Apache Spark | dbt Developer Hub
description: Setup instructions for connecting Apache Spark to dbt Cloud
url: https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark#connect-databricks
timestamp: 2025-01-20T15:48:11.192Z
domain: docs.getdbt.com
path: docs_cloud_connect-data-platform_connect-apache-spark
---

# Connect Apache Spark | dbt Developer Hub


Setup instructions for connecting Apache Spark to dbt Cloud


## Content

Connect Apache Spark | dbt Developer Hub
===============            

[Skip to main content](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark#__docusaurus_skipToContent_fallback)

[Join our biweekly demos and see dbt Cloud in action!](https://www.getdbt.com/resources/webinars/dbt-cloud-demos-with-experts/?utm_medium=i[%E2%80%A6]ly-demos_aw&utm_content=biweekly-demos____&utm_term=all_all__)

[![Image 7: dbt Logo](https://docs.getdbt.com/img/dbt-logo.svg)![Image 8: dbt Logo](https://docs.getdbt.com/img/dbt-logo-light.svg)](https://docs.getdbt.com/)

[Docs](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark)

*   [Product docs](https://docs.getdbt.com/docs/introduction)
*   [API docs](https://docs.getdbt.com/docs/dbt-cloud-apis/overview)
*   [Best practices](https://docs.getdbt.com/best-practices)
*   [Release notes](https://docs.getdbt.com/docs/dbt-versions/dbt-cloud-release-notes)

[Guides](https://docs.getdbt.com/guides)[Reference](https://docs.getdbt.com/reference/references-overview)

[v](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark)

*   Cloud (Latest)
*   1.9 (Compatible)
*   1.8
*   1.7

[Resources](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark)

*   [Courses](https://learn.getdbt.com/)
*   [Best practices](https://docs.getdbt.com/best-practices)
*   [Developer blog](https://docs.getdbt.com/blog)

[Community](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark)

*   [Join the dbt Community](https://docs.getdbt.com/community/join)
*   [Become a contributor](https://docs.getdbt.com/community/contribute)
*   [Community forum](https://docs.getdbt.com/community/forum)
*   [Events](https://docs.getdbt.com/community/events)
*   [Spotlight](https://docs.getdbt.com/community/spotlight)

[Create a free account](https://www.getdbt.com/signup/)

Search

[![Image 9: dbt Logo](https://docs.getdbt.com/img/dbt-logo.svg)![Image 10: dbt Logo](https://docs.getdbt.com/img/dbt-logo-light.svg)](https://docs.getdbt.com/)

*   [What is dbt?](https://docs.getdbt.com/docs/introduction)
*   [Get started with dbt](https://docs.getdbt.com/docs/get-started-dbt)
    
*   [Supported data platforms](https://docs.getdbt.com/docs/supported-data-platforms)
    
*   [About dbt Cloud](https://docs.getdbt.com/docs/cloud/about-cloud/dbt-cloud-features)
    
*   [Set up dbt](https://docs.getdbt.com/docs/about-setup)
    
    *   [About dbt setup](https://docs.getdbt.com/docs/about-setup)
    *   [About environments](https://docs.getdbt.com/docs/environments-in-dbt)
    *   [dbt Cloud](https://docs.getdbt.com/docs/cloud/about-cloud-setup)
        
        *   [About dbt Cloud setup](https://docs.getdbt.com/docs/cloud/about-cloud-setup)
        *   [Account settings](https://docs.getdbt.com/docs/cloud/account-settings)
        *   [Account integrations](https://docs.getdbt.com/docs/cloud/account-integrations)
        *   [dbt Cloud environments](https://docs.getdbt.com/docs/dbt-cloud-environments)
        *   [Multi-cell migration checklist](https://docs.getdbt.com/docs/cloud/migration)
        *   [Connect data platform](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections)
            
            *   [About data platform connections](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections)
            *   [Connect Apache Spark](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark)
            *   [Connect Amazon Athena](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-amazon-athena)
            *   [Connect Azure Synapse Analytics](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-azure-synapse-analytics)
            *   [Connect BigQuery](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-bigquery)
            *   [Connect Databricks](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-databricks)
            *   [Connect Microsoft Fabric](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-microsoft-fabric)
            *   [Connect Redshift, PostgreSQL, and AlloyDB](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-redshift-postgresql-alloydb)
            *   [Connect Starburst or Trino](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-starburst-trino)
            *   [Connect Snowflake](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-snowflake)
            *   [Connect Teradata](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-teradata)
        *   [Manage access](https://docs.getdbt.com/docs/cloud/manage-access/about-user-access)
            
        *   [Configure Git](https://docs.getdbt.com/docs/cloud/git/git-configuration-in-dbt-cloud)
            
        *   [Secure your tenant](https://docs.getdbt.com/docs/cloud/secure/secure-your-tenant)
            
        *   [Billing](https://docs.getdbt.com/docs/cloud/billing)
    *   [dbt Core](https://docs.getdbt.com/docs/core/about-core-setup)
        
    *   [Run your dbt projects](https://docs.getdbt.com/docs/running-a-dbt-project/run-your-dbt-projects)
    *   [Use threads](https://docs.getdbt.com/docs/running-a-dbt-project/using-threads)
*   [Develop with dbt Cloud](https://docs.getdbt.com/docs/cloud/about-develop-dbt)
    
*   [Build dbt projects](https://docs.getdbt.com/docs/build/projects)
    
*   [Deploy dbt](https://docs.getdbt.com/docs/deploy/deployments)
    
*   [Collaborate with others](https://docs.getdbt.com/docs/collaborate/collaborate-with-others)
    
*   [Use the dbt Semantic Layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl)
    
*   [dbt Cloud APIs](https://docs.getdbt.com/docs/dbt-cloud-apis/overview)
    
*   [dbt Cloud integrations](https://docs.getdbt.com/docs/cloud-integrations/overview)
    
*   [Available dbt versions](https://docs.getdbt.com/docs/dbt-versions/core)
    
*   [dbt support](https://docs.getdbt.com/docs/dbt-support)
*   [Frequently asked questions](https://docs.getdbt.com/docs/faqs)
    

*   [](https://docs.getdbt.com/)
*   [Set up dbt](https://docs.getdbt.com/docs/about-setup)
*   [dbt Cloud](https://docs.getdbt.com/docs/cloud/about-cloud-setup)
*   [Connect data platform](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections)
*   Connect Apache Spark

Connect Apache Spark
====================

If you're using Databricks, use `dbt-databricks`

If you're using Databricks, the `dbt-databricks` adapter is recommended over `dbt-spark`. If you're still using dbt-spark with Databricks consider [migrating from the dbt-spark adapter to the dbt-databricks adapter](https://docs.getdbt.com/guides/migrate-from-spark-to-databricks).

For the Databricks version of this page, refer to [Databricks setup](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark#databricks-setup).

note

See [Connect Databricks](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark#connect-databricks) for the Databricks version of this page.

dbt Cloud supports connecting to an Apache Spark cluster using the HTTP method or the Thrift method. Note: While the HTTP method can be used to connect to an all-purpose Databricks cluster, the ODBC method is recommended for all Databricks connections. For further details on configuring these connection parameters, please see the [dbt-spark documentation](https://github.com/dbt-labs/dbt-spark#configuring-your-profile).

To learn how to optimize performance with data platform-specific configurations in dbt Cloud, refer to [Apache Spark-specific configuration](https://docs.getdbt.com/reference/resource-configs/spark-configs).

The following fields are available when creating an Apache Spark connection using the HTTP and Thrift connection methods:

| Field | Description | Examples |
| --- | --- | --- |
| Host Name | The hostname of the Spark cluster to connect to | `yourorg.sparkhost.com` |
| Port | The port to connect to Spark on | 443 |
| Organization | Optional (default: 0) | 0123456789 |
| Cluster | The ID of the cluster to connect to | 1234-567890-abc12345 |
| Connection Timeout | Number of seconds after which to timeout a connection | 10 |
| Connection Retries | Number of times to attempt connecting to cluster before failing | 10 |
| User | Optional | dbt\_cloud\_user |
| Auth | Optional, supply if using Kerberos | `KERBEROS` |
| Kerberos Service Name | Optional, supply if using Kerberos | `hive` |

[![Image 11: Configuring a Spark connection](https://docs.getdbt.com/img/docs/dbt-cloud/cloud-configuring-dbt-cloud/spark-connection.png?v=2)](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark#)Configuring a Spark connection

0

[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/cloud/connect-data-platform/connect-apache-spark.md)

Last updated on **Jan 17, 2025**

[Previous About data platform connections](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections)

[Terms of Service](https://www.getdbt.com/terms-of-use/) [Privacy Policy](https://www.getdbt.com/cloud/privacy-policy/) [Security](https://www.getdbt.com/security/) Cookie Settings

[](https://twitter.com/getdbt "X")[](https://www.getdbt.com/community/join-the-community/ "Community Slack")[](https://github.com/dbt-labs/dbt-core "GitHub")

© 2025 dbt Labs, Inc. All Rights Reserved.

## Metadata

```json
{
  "title": "Connect Apache Spark | dbt Developer Hub",
  "description": "Setup instructions for connecting Apache Spark to dbt Cloud",
  "url": "https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark#connect-databricks",
  "content": "Connect Apache Spark | dbt Developer Hub\n===============            \n\n[Skip to main content](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark#__docusaurus_skipToContent_fallback)\n\n[Join our biweekly demos and see dbt Cloud in action!](https://www.getdbt.com/resources/webinars/dbt-cloud-demos-with-experts/?utm_medium=i[%E2%80%A6]ly-demos_aw&utm_content=biweekly-demos____&utm_term=all_all__)\n\n[![Image 7: dbt Logo](https://docs.getdbt.com/img/dbt-logo.svg)![Image 8: dbt Logo](https://docs.getdbt.com/img/dbt-logo-light.svg)](https://docs.getdbt.com/)\n\n[Docs](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark)\n\n*   [Product docs](https://docs.getdbt.com/docs/introduction)\n*   [API docs](https://docs.getdbt.com/docs/dbt-cloud-apis/overview)\n*   [Best practices](https://docs.getdbt.com/best-practices)\n*   [Release notes](https://docs.getdbt.com/docs/dbt-versions/dbt-cloud-release-notes)\n\n[Guides](https://docs.getdbt.com/guides)[Reference](https://docs.getdbt.com/reference/references-overview)\n\n[v](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark)\n\n*   Cloud (Latest)\n*   1.9 (Compatible)\n*   1.8\n*   1.7\n\n[Resources](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark)\n\n*   [Courses](https://learn.getdbt.com/)\n*   [Best practices](https://docs.getdbt.com/best-practices)\n*   [Developer blog](https://docs.getdbt.com/blog)\n\n[Community](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark)\n\n*   [Join the dbt Community](https://docs.getdbt.com/community/join)\n*   [Become a contributor](https://docs.getdbt.com/community/contribute)\n*   [Community forum](https://docs.getdbt.com/community/forum)\n*   [Events](https://docs.getdbt.com/community/events)\n*   [Spotlight](https://docs.getdbt.com/community/spotlight)\n\n[Create a free account](https://www.getdbt.com/signup/)\n\nSearch\n\n[![Image 9: dbt Logo](https://docs.getdbt.com/img/dbt-logo.svg)![Image 10: dbt Logo](https://docs.getdbt.com/img/dbt-logo-light.svg)](https://docs.getdbt.com/)\n\n*   [What is dbt?](https://docs.getdbt.com/docs/introduction)\n*   [Get started with dbt](https://docs.getdbt.com/docs/get-started-dbt)\n    \n*   [Supported data platforms](https://docs.getdbt.com/docs/supported-data-platforms)\n    \n*   [About dbt Cloud](https://docs.getdbt.com/docs/cloud/about-cloud/dbt-cloud-features)\n    \n*   [Set up dbt](https://docs.getdbt.com/docs/about-setup)\n    \n    *   [About dbt setup](https://docs.getdbt.com/docs/about-setup)\n    *   [About environments](https://docs.getdbt.com/docs/environments-in-dbt)\n    *   [dbt Cloud](https://docs.getdbt.com/docs/cloud/about-cloud-setup)\n        \n        *   [About dbt Cloud setup](https://docs.getdbt.com/docs/cloud/about-cloud-setup)\n        *   [Account settings](https://docs.getdbt.com/docs/cloud/account-settings)\n        *   [Account integrations](https://docs.getdbt.com/docs/cloud/account-integrations)\n        *   [dbt Cloud environments](https://docs.getdbt.com/docs/dbt-cloud-environments)\n        *   [Multi-cell migration checklist](https://docs.getdbt.com/docs/cloud/migration)\n        *   [Connect data platform](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections)\n            \n            *   [About data platform connections](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections)\n            *   [Connect Apache Spark](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark)\n            *   [Connect Amazon Athena](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-amazon-athena)\n            *   [Connect Azure Synapse Analytics](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-azure-synapse-analytics)\n            *   [Connect BigQuery](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-bigquery)\n            *   [Connect Databricks](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-databricks)\n            *   [Connect Microsoft Fabric](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-microsoft-fabric)\n            *   [Connect Redshift, PostgreSQL, and AlloyDB](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-redshift-postgresql-alloydb)\n            *   [Connect Starburst or Trino](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-starburst-trino)\n            *   [Connect Snowflake](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-snowflake)\n            *   [Connect Teradata](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-teradata)\n        *   [Manage access](https://docs.getdbt.com/docs/cloud/manage-access/about-user-access)\n            \n        *   [Configure Git](https://docs.getdbt.com/docs/cloud/git/git-configuration-in-dbt-cloud)\n            \n        *   [Secure your tenant](https://docs.getdbt.com/docs/cloud/secure/secure-your-tenant)\n            \n        *   [Billing](https://docs.getdbt.com/docs/cloud/billing)\n    *   [dbt Core](https://docs.getdbt.com/docs/core/about-core-setup)\n        \n    *   [Run your dbt projects](https://docs.getdbt.com/docs/running-a-dbt-project/run-your-dbt-projects)\n    *   [Use threads](https://docs.getdbt.com/docs/running-a-dbt-project/using-threads)\n*   [Develop with dbt Cloud](https://docs.getdbt.com/docs/cloud/about-develop-dbt)\n    \n*   [Build dbt projects](https://docs.getdbt.com/docs/build/projects)\n    \n*   [Deploy dbt](https://docs.getdbt.com/docs/deploy/deployments)\n    \n*   [Collaborate with others](https://docs.getdbt.com/docs/collaborate/collaborate-with-others)\n    \n*   [Use the dbt Semantic Layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl)\n    \n*   [dbt Cloud APIs](https://docs.getdbt.com/docs/dbt-cloud-apis/overview)\n    \n*   [dbt Cloud integrations](https://docs.getdbt.com/docs/cloud-integrations/overview)\n    \n*   [Available dbt versions](https://docs.getdbt.com/docs/dbt-versions/core)\n    \n*   [dbt support](https://docs.getdbt.com/docs/dbt-support)\n*   [Frequently asked questions](https://docs.getdbt.com/docs/faqs)\n    \n\n*   [](https://docs.getdbt.com/)\n*   [Set up dbt](https://docs.getdbt.com/docs/about-setup)\n*   [dbt Cloud](https://docs.getdbt.com/docs/cloud/about-cloud-setup)\n*   [Connect data platform](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections)\n*   Connect Apache Spark\n\nConnect Apache Spark\n====================\n\nIf you're using Databricks, use `dbt-databricks`\n\nIf you're using Databricks, the `dbt-databricks` adapter is recommended over `dbt-spark`. If you're still using dbt-spark with Databricks consider [migrating from the dbt-spark adapter to the dbt-databricks adapter](https://docs.getdbt.com/guides/migrate-from-spark-to-databricks).\n\nFor the Databricks version of this page, refer to [Databricks setup](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark#databricks-setup).\n\nnote\n\nSee [Connect Databricks](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark#connect-databricks) for the Databricks version of this page.\n\ndbt Cloud supports connecting to an Apache Spark cluster using the HTTP method or the Thrift method. Note: While the HTTP method can be used to connect to an all-purpose Databricks cluster, the ODBC method is recommended for all Databricks connections. For further details on configuring these connection parameters, please see the [dbt-spark documentation](https://github.com/dbt-labs/dbt-spark#configuring-your-profile).\n\nTo learn how to optimize performance with data platform-specific configurations in dbt Cloud, refer to [Apache Spark-specific configuration](https://docs.getdbt.com/reference/resource-configs/spark-configs).\n\nThe following fields are available when creating an Apache Spark connection using the HTTP and Thrift connection methods:\n\n| Field | Description | Examples |\n| --- | --- | --- |\n| Host Name | The hostname of the Spark cluster to connect to | `yourorg.sparkhost.com` |\n| Port | The port to connect to Spark on | 443 |\n| Organization | Optional (default: 0) | 0123456789 |\n| Cluster | The ID of the cluster to connect to | 1234-567890-abc12345 |\n| Connection Timeout | Number of seconds after which to timeout a connection | 10 |\n| Connection Retries | Number of times to attempt connecting to cluster before failing | 10 |\n| User | Optional | dbt\\_cloud\\_user |\n| Auth | Optional, supply if using Kerberos | `KERBEROS` |\n| Kerberos Service Name | Optional, supply if using Kerberos | `hive` |\n\n[![Image 11: Configuring a Spark connection](https://docs.getdbt.com/img/docs/dbt-cloud/cloud-configuring-dbt-cloud/spark-connection.png?v=2)](https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-apache-spark#)Configuring a Spark connection\n\n0\n\n[Edit this page](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/cloud/connect-data-platform/connect-apache-spark.md)\n\nLast updated on **Jan 17, 2025**\n\n[Previous About data platform connections](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections)\n\n[Terms of Service](https://www.getdbt.com/terms-of-use/) [Privacy Policy](https://www.getdbt.com/cloud/privacy-policy/) [Security](https://www.getdbt.com/security/) Cookie Settings\n\n[](https://twitter.com/getdbt \"X\")[](https://www.getdbt.com/community/join-the-community/ \"Community Slack\")[](https://github.com/dbt-labs/dbt-core \"GitHub\")\n\n© 2025 dbt Labs, Inc. All Rights Reserved.",
  "usage": {
    "tokens": 2439
  }
}
```
