---
title: Install Memgraph Lab and connect to a database
description: Connect to your graph data with ease using Memgraph. Explore our documentation page for detailed installation instructions and learn how to establish a seamless connection, enabling powerful graph computing and analysis.
url: https://memgraph.com/docs/data-visualization/install-and-connect
timestamp: 2025-01-20T15:45:30.302Z
domain: memgraph.com
path: docs_data-visualization_install-and-connect
---

# Install Memgraph Lab and connect to a database


Connect to your graph data with ease using Memgraph. Explore our documentation page for detailed installation instructions and learn how to establish a seamless connection, enabling powerful graph computing and analysis.


## Content

Install Memgraph Lab and connect to a database
===============

[![Image 16: Memgraph Logo](https://memgraph.com/docs/memgraph-logo-navigation.svg)](https://memgraph.com/)

[GitHub](https://github.com/memgraph/memgraph)[Discord](https://discord.gg/memgraph)

*   [Home](https://memgraph.com/docs)
*   [Getting started](https://memgraph.com/docs/getting-started)
    
    *   [Install Memgraph](https://memgraph.com/docs/getting-started/install-memgraph)
        
        *   [Docker](https://memgraph.com/docs/getting-started/install-memgraph/docker)
        *   [Debian](https://memgraph.com/docs/getting-started/install-memgraph/debian)
        *   [Ubuntu](https://memgraph.com/docs/getting-started/install-memgraph/ubuntu)
        *   [CentOS](https://memgraph.com/docs/getting-started/install-memgraph/centos)
        *   [Fedora](https://memgraph.com/docs/getting-started/install-memgraph/fedora)
        *   [Rocky](https://memgraph.com/docs/getting-started/install-memgraph/rocky)
        *   [Red Hat](https://memgraph.com/docs/getting-started/install-memgraph/redhat)
        *   [Amazon Linux](https://memgraph.com/docs/getting-started/install-memgraph/amazon-linux)
        *   [Memgraph Cloud](https://memgraph.com/docs/getting-started/install-memgraph/memgraph-cloud)
        *   [Docker Compose](https://memgraph.com/docs/getting-started/install-memgraph/docker-compose)
        *   [Kubernetes](https://memgraph.com/docs/getting-started/install-memgraph/kubernetes)
        *   [WSL](https://memgraph.com/docs/getting-started/install-memgraph/wsl)
        *   [Direct download links](https://memgraph.com/docs/getting-started/install-memgraph/direct-download-links)
        
    *   [CLI](https://memgraph.com/docs/getting-started/cli)
    *   [First steps with Docker](https://memgraph.com/docs/getting-started/first-steps-with-docker)
    *   [Building Memgraph from source](https://memgraph.com/docs/getting-started/build-memgraph-from-source)
    
*   [Client libraries](https://memgraph.com/docs/client-libraries)
    
    *   [C#](https://memgraph.com/docs/client-libraries/c-sharp)
    *   [Go](https://memgraph.com/docs/client-libraries/go)
    *   [GraphQL](https://memgraph.com/docs/client-libraries/graphql)
    *   [Java](https://memgraph.com/docs/client-libraries/java)
    *   [JavaScript](https://memgraph.com/docs/client-libraries/javascript)
    *   [Node.js](https://memgraph.com/docs/client-libraries/nodejs)
    *   [PHP](https://memgraph.com/docs/client-libraries/php)
    *   [Python](https://memgraph.com/docs/client-libraries/python)
    *   [Rust](https://memgraph.com/docs/client-libraries/rust)
    
*   [AI ecosystem](https://memgraph.com/docs/ai-ecosystem)
    
    *   [GraphRAG](https://memgraph.com/docs/ai-ecosystem/graph-rag)
    *   [Machine learning](https://memgraph.com/docs/ai-ecosystem/machine-learning)
    
*   [Fundamentals](https://memgraph.com/docs/fundamentals)
    
    *   [Constraints](https://memgraph.com/docs/fundamentals/constraints)
    *   [Data types](https://memgraph.com/docs/fundamentals/data-types)
    *   [Data durability](https://memgraph.com/docs/fundamentals/data-durability)
    *   [Indexes](https://memgraph.com/docs/fundamentals/indexes)
    *   [Storage memory usage](https://memgraph.com/docs/fundamentals/storage-memory-usage)
    *   [Telemetry](https://memgraph.com/docs/fundamentals/telemetry)
    *   [Transactions](https://memgraph.com/docs/fundamentals/transactions)
    *   [Triggers](https://memgraph.com/docs/fundamentals/triggers)
    
*   [Data modeling](https://memgraph.com/docs/data-modeling)
    
    *   [Knowledge graph](https://memgraph.com/docs/data-modeling/knowledge-graph)
    
*   [Data migration](https://memgraph.com/docs/data-migration)
    
    *   [Best practices](https://memgraph.com/docs/data-migration/best-practices)
    *   [CSV](https://memgraph.com/docs/data-migration/csv)
    *   [JSON](https://memgraph.com/docs/data-migration/json)
    *   [CYPHERL](https://memgraph.com/docs/data-migration/cypherl)
    *   [Migrate from Neo4j](https://memgraph.com/docs/data-migration/migrate-from-neo4j)
    *   [Migrate from RDBMS using CSV files](https://memgraph.com/docs/data-migration/migrate-from-rdbms)
    *   [Migrate from RDBMS using MAGE modules](https://memgraph.com/docs/data-migration/migrate-from-rdbms-directly)
    *   [Migrate from Memgraph Platform to Memgraph MAGE](https://memgraph.com/docs/data-migration/migrate-memgraph-platform)
    *   [Export data](https://memgraph.com/docs/data-migration/export-data)
    
*   [Querying](https://memgraph.com/docs/querying)
    
    *   [Best practices](https://memgraph.com/docs/querying/best-practices)
    *   [Differences in Cypher implementations](https://memgraph.com/docs/querying/differences-in-cypher-implementations)
    *   [Create graph objects](https://memgraph.com/docs/querying/create-graph-objects)
    *   [Read and modify data](https://memgraph.com/docs/querying/read-and-modify-data)
    *   [Clauses](https://memgraph.com/docs/querying/clauses)
        
        *   [ALTER](https://memgraph.com/docs/querying/clauses/alter)
        *   [CALL](https://memgraph.com/docs/querying/clauses/call)
        *   [CASE](https://memgraph.com/docs/querying/clauses/case)
        *   [CREATE](https://memgraph.com/docs/querying/clauses/create)
        *   [DELETE](https://memgraph.com/docs/querying/clauses/delete)
        *   [DROP GRAPH](https://memgraph.com/docs/querying/clauses/drop-graph)
        *   [EXPLAIN](https://memgraph.com/docs/querying/clauses/explain)
        *   [FOREACH](https://memgraph.com/docs/querying/clauses/foreach)
        *   [LOAD CSV](https://memgraph.com/docs/querying/clauses/load-csv)
        *   [MATCH](https://memgraph.com/docs/querying/clauses/match)
        *   [MERGE](https://memgraph.com/docs/querying/clauses/merge)
        *   [OPTIONAL MATCH](https://memgraph.com/docs/querying/clauses/optional-match)
        *   [PROFILE](https://memgraph.com/docs/querying/clauses/profile)
        *   [REMOVE](https://memgraph.com/docs/querying/clauses/remove)
        *   [RETURN](https://memgraph.com/docs/querying/clauses/return)
        *   [SET](https://memgraph.com/docs/querying/clauses/set)
        *   [UNION](https://memgraph.com/docs/querying/clauses/union)
        *   [UNWIND](https://memgraph.com/docs/querying/clauses/unwind)
        *   [WHERE](https://memgraph.com/docs/querying/clauses/where)
        *   [WITH](https://memgraph.com/docs/querying/clauses/with)
        
    *   [Functions](https://memgraph.com/docs/querying/functions)
    *   [Expressions](https://memgraph.com/docs/querying/expressions)
    *   [Schema](https://memgraph.com/docs/querying/schema)
    *   [Text search](https://memgraph.com/docs/querying/text-search)
    *   [Vector search](https://memgraph.com/docs/querying/vector-search)
    *   [Time to live](https://memgraph.com/docs/querying/time-to-live)
    *   [Query plan](https://memgraph.com/docs/querying/query-plan)
    *   [Exploring datasets](https://memgraph.com/docs/querying/exploring-datasets)
        
        *   [Analyzing TED talks](https://memgraph.com/docs/querying/exploring-datasets/analyzing-ted-talks)
        *   [Backpacking through Europe](https://memgraph.com/docs/querying/exploring-datasets/backpacking-through-europe)
        *   [Exploring the European road network](https://memgraph.com/docs/querying/exploring-datasets/exploring-the-european-road-network)
        *   [Football transfers](https://memgraph.com/docs/querying/exploring-datasets/football-transfers)
        *   [GoT deaths](https://memgraph.com/docs/querying/exploring-datasets/got-deaths)
        *   [Graphing the premier league](https://memgraph.com/docs/querying/exploring-datasets/graphing-the-premier-league)
        *   [Marvel universe](https://memgraph.com/docs/querying/exploring-datasets/marvel-universe)
        *   [Movie recommendation](https://memgraph.com/docs/querying/exploring-datasets/movie-recommendation)
        
    
*   [Advanced algorithms](https://memgraph.com/docs/advanced-algorithms)
    
    *   [Available algorithms](https://memgraph.com/docs/advanced-algorithms/available-algorithms)
        
        *   [algo](https://memgraph.com/docs/advanced-algorithms/available-algorithms/algo)
        *   [betweenness\_centrality\_online](https://memgraph.com/docs/advanced-algorithms/available-algorithms/betweenness_centrality_online)
        *   [betweenness\_centrality](https://memgraph.com/docs/advanced-algorithms/available-algorithms/betweenness_centrality)
        *   [biconnected\_components](https://memgraph.com/docs/advanced-algorithms/available-algorithms/biconnected_components)
        *   [bipartite\_matching](https://memgraph.com/docs/advanced-algorithms/available-algorithms/bipartite_matching)
        *   [bridges](https://memgraph.com/docs/advanced-algorithms/available-algorithms/bridges)
        *   [collections](https://memgraph.com/docs/advanced-algorithms/available-algorithms/collections)
        *   [community\_detection\_online](https://memgraph.com/docs/advanced-algorithms/available-algorithms/community_detection_online)
        *   [community\_detection](https://memgraph.com/docs/advanced-algorithms/available-algorithms/community_detection)
        *   [conditional\_execution](https://memgraph.com/docs/advanced-algorithms/available-algorithms/conditional_execution)
        *   [create](https://memgraph.com/docs/advanced-algorithms/available-algorithms/create)
        *   [cugraph](https://memgraph.com/docs/advanced-algorithms/available-algorithms/cugraph)
        *   [cycles](https://memgraph.com/docs/advanced-algorithms/available-algorithms/cycles)
        *   [date](https://memgraph.com/docs/advanced-algorithms/available-algorithms/date)
        *   [degree\_centrality](https://memgraph.com/docs/advanced-algorithms/available-algorithms/degree_centrality)
        *   [distance\_calculator](https://memgraph.com/docs/advanced-algorithms/available-algorithms/distance_calculator)
        *   [elasticsearch\_synchronization](https://memgraph.com/docs/advanced-algorithms/available-algorithms/elasticsearch_synchronization)
        *   [export\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/export_util)
        *   [gnn\_link\_prediction](https://memgraph.com/docs/advanced-algorithms/available-algorithms/gnn_link_prediction)
        *   [gnn\_node\_classification](https://memgraph.com/docs/advanced-algorithms/available-algorithms/gnn_node_classification)
        *   [graph\_analyzer](https://memgraph.com/docs/advanced-algorithms/available-algorithms/graph_analyzer)
        *   [graph\_coloring](https://memgraph.com/docs/advanced-algorithms/available-algorithms/graph_coloring)
        *   [graph\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/graph_util)
        *   [igraphalg](https://memgraph.com/docs/advanced-algorithms/available-algorithms/igraphalg)
        *   [import\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/import_util)
        *   [json\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/json_util)
        *   [katz\_centrality\_online](https://memgraph.com/docs/advanced-algorithms/available-algorithms/katz_centrality_online)
        *   [katz\_centrality](https://memgraph.com/docs/advanced-algorithms/available-algorithms/katz_centrality)
        *   [kmeans\_clustering](https://memgraph.com/docs/advanced-algorithms/available-algorithms/kmeans_clustering)
        *   [label](https://memgraph.com/docs/advanced-algorithms/available-algorithms/label)
        *   [leiden\_community\_detection](https://memgraph.com/docs/advanced-algorithms/available-algorithms/leiden_community_detection)
        *   [llm\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/llm_util)
        *   [map](https://memgraph.com/docs/advanced-algorithms/available-algorithms/map)
        *   [max\_flow](https://memgraph.com/docs/advanced-algorithms/available-algorithms/max_flow)
        *   [merge](https://memgraph.com/docs/advanced-algorithms/available-algorithms/merge)
        *   [meta\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/meta_util)
        *   [meta](https://memgraph.com/docs/advanced-algorithms/available-algorithms/meta)
        *   [migrate](https://memgraph.com/docs/advanced-algorithms/available-algorithms/migrate)
        *   [neighbors](https://memgraph.com/docs/advanced-algorithms/available-algorithms/neighbors)
        *   [node\_similarity](https://memgraph.com/docs/advanced-algorithms/available-algorithms/node_similarity)
        *   [node](https://memgraph.com/docs/advanced-algorithms/available-algorithms/node)
        *   [node2vec\_online](https://memgraph.com/docs/advanced-algorithms/available-algorithms/node2vec_online)
        *   [node2vec](https://memgraph.com/docs/advanced-algorithms/available-algorithms/node2vec)
        *   [nodes](https://memgraph.com/docs/advanced-algorithms/available-algorithms/nodes)
        *   [nxalg](https://memgraph.com/docs/advanced-algorithms/available-algorithms/nxalg)
        *   [pagerank\_online](https://memgraph.com/docs/advanced-algorithms/available-algorithms/pagerank_online)
        *   [pagerank](https://memgraph.com/docs/advanced-algorithms/available-algorithms/pagerank)
        *   [path](https://memgraph.com/docs/advanced-algorithms/available-algorithms/path)
        *   [periodic](https://memgraph.com/docs/advanced-algorithms/available-algorithms/periodic)
        *   [refactor](https://memgraph.com/docs/advanced-algorithms/available-algorithms/refactor)
        *   [set\_cover](https://memgraph.com/docs/advanced-algorithms/available-algorithms/set_cover)
        *   [set\_property](https://memgraph.com/docs/advanced-algorithms/available-algorithms/set_property)
        *   [temporal](https://memgraph.com/docs/advanced-algorithms/available-algorithms/temporal)
        *   [text](https://memgraph.com/docs/advanced-algorithms/available-algorithms/text)
        *   [temporal\_graph\_networks](https://memgraph.com/docs/advanced-algorithms/available-algorithms/tgn)
        *   [tsp](https://memgraph.com/docs/advanced-algorithms/available-algorithms/tsp)
        *   [union\_find](https://memgraph.com/docs/advanced-algorithms/available-algorithms/union_find)
        *   [util\_module](https://memgraph.com/docs/advanced-algorithms/available-algorithms/util_module)
        *   [uuid\_generator](https://memgraph.com/docs/advanced-algorithms/available-algorithms/uuid_generator)
        *   [vrp](https://memgraph.com/docs/advanced-algorithms/available-algorithms/vrp)
        *   [weakly\_connected\_components](https://memgraph.com/docs/advanced-algorithms/available-algorithms/weakly_connected_components)
        *   [xml\_module](https://memgraph.com/docs/advanced-algorithms/available-algorithms/xml_module)
        
    *   [Deep path traversal algorithms](https://memgraph.com/docs/advanced-algorithms/deep-path-traversal)
    *   [Install MAGE](https://memgraph.com/docs/advanced-algorithms/install-mage)
    *   [Run algorithms](https://memgraph.com/docs/advanced-algorithms/run-algorithms)
    *   [Utilize NetworkX](https://memgraph.com/docs/advanced-algorithms/utilize-networkx)
    
*   [Custom query modules](https://memgraph.com/docs/custom-query-modules)
    
    *   [C](https://memgraph.com/docs/custom-query-modules/c)
        
        *   [C API](https://memgraph.com/docs/custom-query-modules/c/c-api)
        *   [C example](https://memgraph.com/docs/custom-query-modules/c/c-example)
        
    *   [C++](https://memgraph.com/docs/custom-query-modules/cpp)
        
        *   [C++ API](https://memgraph.com/docs/custom-query-modules/cpp/cpp-api)
        *   [C++ example](https://memgraph.com/docs/custom-query-modules/cpp/cpp-example)
        
    *   [Python](https://memgraph.com/docs/custom-query-modules/python)
        
        *   [Python API](https://memgraph.com/docs/custom-query-modules/python/python-api)
        *   [Mock Python API](https://memgraph.com/docs/custom-query-modules/python/mock-python-api)
        *   [Python example](https://memgraph.com/docs/custom-query-modules/python/python-example)
        *   [Implement custom query module in Python](https://memgraph.com/docs/custom-query-modules/python/implement-custom-query-module-in-python)
        *   [Understanding music with modules](https://memgraph.com/docs/custom-query-modules/python/understanding-music-with-modules)
        
    *   Rust
        
        *   [Rust API](https://memgraph.com/docs/custom-query-modules/rust/rust-api)
        *   [Rust example](https://memgraph.com/docs/custom-query-modules/rust/rust-example)
        
    *   [Manage query modules](https://memgraph.com/docs/custom-query-modules/manage-query-modules)
    *   [Contributing](https://memgraph.com/docs/custom-query-modules/contributing)
    
*   [Data visualization](https://memgraph.com/docs/data-visualization)
    
    *   [Install and connect](https://memgraph.com/docs/data-visualization/install-and-connect)
    *   [User manual](https://memgraph.com/docs/data-visualization/user-manual)
        
        *   [Connection types](https://memgraph.com/docs/data-visualization/user-manual/connection-types)
        *   [CSV file import tool](https://memgraph.com/docs/data-visualization/user-manual/csv-file-import)
        *   [Custom base path](https://memgraph.com/docs/data-visualization/user-manual/custom-base-path)
        *   [Custom SSL certificates](https://memgraph.com/docs/data-visualization/user-manual/custom-ssl-certificates)
        *   [GraphChat](https://memgraph.com/docs/data-visualization/user-manual/graphchat)
        *   [Query sharing](https://memgraph.com/docs/data-visualization/user-manual/query-sharing)
        *   [Single sign-on (SSO)](https://memgraph.com/docs/data-visualization/user-manual/single-sign-on)
        
    *   [Graph style script](https://memgraph.com/docs/data-visualization/graph-style-script)
        
        *   [Built-in elements](https://memgraph.com/docs/data-visualization/graph-style-script/built-in-elements)
        *   [Directive properties](https://memgraph.com/docs/data-visualization/graph-style-script/directive-properties)
        
    *   [Style your graphs in Memgraph Lab](https://memgraph.com/docs/data-visualization/style-your-graphs-in-memgraph-lab)
    
*   [Database management](https://memgraph.com/docs/database-management)
    
    *   [Authentication and authorization](https://memgraph.com/docs/database-management/authentication-and-authorization)
        
        *   [Users](https://memgraph.com/docs/database-management/authentication-and-authorization/users)
        *   [Role-based access control](https://memgraph.com/docs/database-management/authentication-and-authorization/role-based-access-control)
        *   [Auth system integrations](https://memgraph.com/docs/database-management/authentication-and-authorization/auth-system-integrations)
        
    *   [Backup and restore](https://memgraph.com/docs/database-management/backup-and-restore)
    *   [Configuration](https://memgraph.com/docs/database-management/configuration)
    *   [Debugging](https://memgraph.com/docs/database-management/debugging)
    *   [Enabling Memgraph Enterprise](https://memgraph.com/docs/database-management/enabling-memgraph-enterprise)
    *   [Experimental features](https://memgraph.com/docs/database-management/experimental-features)
    *   [Logs](https://memgraph.com/docs/database-management/logs)
    *   [Monitoring](https://memgraph.com/docs/database-management/monitoring)
    *   [Multi-tenancy](https://memgraph.com/docs/database-management/multi-tenancy)
    *   [Query metadata](https://memgraph.com/docs/database-management/query-metadata)
    *   [Server stats](https://memgraph.com/docs/database-management/server-stats)
    *   [SSL encryption](https://memgraph.com/docs/database-management/ssl-encryption)
    *   [System configuration](https://memgraph.com/docs/database-management/system-configuration)
    
*   [Deployment](https://memgraph.com/docs/deployment)
    
    *   [Docker](https://memgraph.com/docs/deployment/docker)
    *   [Linux](https://memgraph.com/docs/deployment/linux)
    *   [AWS](https://memgraph.com/docs/deployment/aws)
    *   [GCP](https://memgraph.com/docs/deployment/gcp)
    *   [Azure](https://memgraph.com/docs/deployment/azure)
    
*   [Clustering](https://memgraph.com/docs/clustering)
    
    *   [High availability](https://memgraph.com/docs/clustering/high-availability)
    *   [Replication](https://memgraph.com/docs/clustering/replication)
        
        *   [System replication](https://memgraph.com/docs/clustering/replication/system-replication)
        
    
*   [Data streams](https://memgraph.com/docs/data-streams)
    
    *   [Transformation modules](https://memgraph.com/docs/data-streams/transformation-modules)
        
        *   [Transformation modules C API](https://memgraph.com/docs/data-streams/transformation-modules/c-api)
        *   [Transformations Python API](https://memgraph.com/docs/data-streams/transformation-modules/python-api)
        
    *   [Manage streams with queries](https://memgraph.com/docs/data-streams/manage-streams-query)
    *   [Manage streams with UI](https://memgraph.com/docs/data-streams/manage-streams-lab)
    *   [Graph stream processing with Kafka](https://memgraph.com/docs/data-streams/graph-stream-processing-with-kafka)
    *   [Kafka Connect](https://memgraph.com/docs/data-streams/kafka)
    
*   [Help center](https://memgraph.com/docs/help-center)
    
    *   [FAQ](https://memgraph.com/docs/help-center/faq)
    *   [Errors](https://memgraph.com/docs/help-center/errors)
        
        *   [Auth](https://memgraph.com/docs/help-center/errors/auth)
        *   [Durability](https://memgraph.com/docs/help-center/errors/durability)
        *   [Memory](https://memgraph.com/docs/help-center/errors/memory)
        *   [Modules](https://memgraph.com/docs/help-center/errors/modules)
        *   [Ports](https://memgraph.com/docs/help-center/errors/ports)
        *   [Python modules](https://memgraph.com/docs/help-center/errors/python-modules)
        *   [Replication](https://memgraph.com/docs/help-center/errors/replication)
        *   [Snapshots](https://memgraph.com/docs/help-center/errors/snapshots)
        *   [Socket](https://memgraph.com/docs/help-center/errors/socket)
        *   [SSL](https://memgraph.com/docs/help-center/errors/ssl)
        *   [Transactions](https://memgraph.com/docs/help-center/errors/transactions)
        *   [Unknown](https://memgraph.com/docs/help-center/errors/unknown)
        
    
*   [Release notes](https://memgraph.com/docs/release-notes)
*   [What's coming soon to Memgraph?](https://memgraph.com/docs/coming-soon)

Light

On This Page

*   [Install Memgraph Lab desktop application](https://memgraph.com/docs/data-visualization/install-and-connect#install-memgraph-lab-desktop-application)
*   [Run Memgraph Lab with Docker](https://memgraph.com/docs/data-visualization/install-and-connect#run-memgraph-lab-with-docker)
*   [Issues when connecting to Memgraph](https://memgraph.com/docs/data-visualization/install-and-connect#issues-when-connecting-to-memgraph)
*   [Environment variables](https://memgraph.com/docs/data-visualization/install-and-connect#environment-variables)

[Question? Give us feedback →](https://github.com/memgraph/documentation/issues/new?title=Feedback%20for%20%E2%80%9CInstall%20Memgraph%20Lab%20and%20connect%20to%20a%20database%E2%80%9D&labels=feedback)[Edit this page](https://github.com/memgraph/documentation/tree/main/pages/data-visualization/install-and-connect.mdx)Scroll to top

[Data visualization](https://memgraph.com/docs/data-visualization "Data visualization")Install and connect

Install Memgraph Lab and connect to a database
==============================================

We recommend you use the [Memgraph Platform](https://memgraph.com/docs/getting-started/install-memgraph/docker-compose) and get the complete streaming graph application platform that includes:

*   **Memgraph** - the database that holds your data
*   **Memgraph Lab** - visual user interface for running queries and visualizing graph data
*   **mgconsole** - command-line interface for running queries
*   **MAGE** - graph algorithms and modules library

After running the image, mgconsole will open in the terminal while Memgraph Lab is available on `http://localhost:3000`.

If you want to install Memgraph Lab as a desktop application, check out the [installation instructions](https://memgraph.com/docs/data-visualization/install-and-connect#install-memgraph-lab-desktop-application) for Windows, macOS and Linux, and if you have a public Memgraph database instance you can access the Lab web application at [https://lab.memgraph.com/](https://lab.memgraph.com/).

Install Memgraph Lab desktop application[](https://memgraph.com/docs/data-visualization/install-and-connect#install-memgraph-lab-desktop-application)
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Download and install Memgraph

Memgraph Lab requires a [running Memgraph database instance](https://memgraph.com/docs/getting-started).

If you installed Memgraph using Docker and wish to connect to it with the Memgraph Lab desktop application, ensure that ports 7687, used for instance connections (`-p 7687:7687`), and 7444, used for logs (`-p 7444:7444`), are exposed in the `docker run ...` command.

Connecting Memgraph Lab to Memgraph may vary depending on the deployment method or operating system. The handling of the `QUICK_CONNECT_MG_HOST` environment variable [varies by operating system](https://memgraph.com/docs/getting-started/install-memgraph/docker#issues-when-connecting-to-memgraph-lab-to-memgraph).

### Download Memgraph Lab

Visit the [Download Hub](https://memgraph.com/download/#individual) and download the Memgraph Lab desktop application.

### Install Memgraph Lab

You can install Memgraph Lab by double clicking the downloaded installer and following the instructions.

If you downloaded Memgraph Lab on Linux, you can execute:

```
sudo dpkg -i MemgraphLab-x.x.x.deb
```

💡

If you encounter a security warning while installing Memgraph Lab on Windows, you may see a message similar to the ones shown in the images below.

![Image 17](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Fmemgraph-lab-install-windows-1.5e124baf.png&w=1080&q=75)

1.  Click **More info**.
    
2.  Verify that Memgraph is listed as the Publisher.
    

![Image 18](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Fmemgraph-lab-install-windows-2.b21101dd.png&w=1080&q=75)

3.  Click **Run anyway** to proceed with the installation of Memgraph Lab.

### Set up connection

After starting Memgraph Lab, you will see the login screen. Follow these steps to connect:

1.  Click on “New connection” in the sidebar.
2.  Select “Memgraph instance: Connect to a standalone instance”. Feel free to check [other connections types](https://memgraph.com/docs/data-visualization/user-manual/connection-types).

Now, input the connection information:

*   **Host**: Enter `localhost`, `host.docker.internal`, `127.0.0.1`, `0.0.0.0`, or modify it as needed.
*   **Port**: Enter `7687`, which Memgraph uses by default.
*   **Database name**: Leave empty unless connecting to a [multi-tenant Memgraph instance](https://memgraph.com/docs/database-management/multi-tenancy).
*   **Logs port**: Default is `7444`, the port for the web socket logs.
*   **Encrypted**: Ensure this option is disabled by default. Enable it if your Memgraph has SSL enabled.

### Connect

Click on Connect, and you should be presented with the following dashboard:

![Image 19: lab-dashboard](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Flab-dashboard.7d3ba961.png&w=3840&q=75)

Congratulations! You have successfully installed Memgraph Lab and connected it to Memgraph. You are now ready to start building your graph and querying it.

⚠️

You might receive the following error message when trying to connect.

![Image 20: failed_connection](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Ffailed_connection.2679930f.png&w=1920&q=75)

In this case, make sure that Memgraph is properly up and running and that you have entered the correct port number.

### Execute queries

Now, you can execute Cypher queries on Memgraph. Open the **Query** tab, located in the left sidebar, copy the following query and press the **Run query** button:

```
CREATE (u:User {name: "Alice"})-[:Likes]->(m:Software {name: "Memgraph"});
```

The query above will create 2 nodes in the database, one labeled “User” with name “Alice” and the other labeled “Software” with name “Memgraph”. It will also create a relationship that “Alice” _likes_ “Memgraph”.

To find created nodes and relationships, execute the following query:

```
MATCH p=()-[]->() RETURN p;
```

You should get the following result:

![Image 21: graph_result](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Flab-graph.e0c85525.png&w=3840&q=75)

Run Memgraph Lab with Docker[](https://memgraph.com/docs/data-visualization/install-and-connect#run-memgraph-lab-with-docker)
-----------------------------------------------------------------------------------------------------------------------------

Run the Memgraph Lab Docker image using the following command:

```
docker run -d -p 3000:3000  --name lab memgraph/lab
```

Once the container is up you can access Memgraph Lab on [localhost:3000](https://localhost:3000/).

#### Issues when connecting to Memgraph[](https://memgraph.com/docs/data-visualization/install-and-connect#issues-when-connecting-to-memgraph)

Memgraph Lab detects if Memgraph is running on `localhost:7687` by default for the Quick Connect. The environment variables that are responsible for Quick Connect working as expected are `QUICK_CONNECT_MG_HOST`, `QUICK_CONNECT_MG_PORT` and `QUICK_CONNECT_MG_IS_ENCRYPTED`. The handling of the `QUICK_CONNECT_MG_HOST` environment variable differs based on the operating system:

*   **Mac or Windows**: The `host.docker.internal` hostname allows Docker containers to connect to the host machine. Set this as the value for `QUICK_CONNECT_MG_HOST` when running Lab on Mac or Windows to enable connection to Memgraph running on the host:
    
    ```
    docker run -d -p 3000:3000 -e QUICK_CONNECT_MG_HOST=host.docker.internal --name lab memgraph/lab
    ```
    
*   **Linux**: There’s no need to set `QUICK_CONNECT_MG_HOST` as it defaults to `localhost`, assuming Memgraph is running locally on the host machine.
    

You can also use the `QUICK_CONNECT_MG_PORT` environment variable to specify the quick connect port number, e.g. `- e QUICK_CONNECT_MG_PORT=7688`.

💡

To connect to a running Memgraph instance, you don’t need to set `QUICK_CONNECT_MG_HOST` to `host.docker.internal`. Instead, create a new connection in Memgraph Lab and specify `host.docker.internal` as the Host.

![Image 22: Setting host.docker.internal as the Host](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Fmemgraph-host-docker-internal.3e857281.png&w=1920&q=75)

Environment variables[](https://memgraph.com/docs/data-visualization/install-and-connect#environment-variables)
---------------------------------------------------------------------------------------------------------------

The desktop application version of Memgraph Lab does not support receiving environment variables.

Configure Memgraph Lab using the following environment variables when running it through Docker, including Docker Compose:

| Variable | Description | Type | Default |
| --- | --- | --- | --- |
| `AUTH_NATIVE_IS_DISABLED` | Enable or disable native authentication (username, password) | `boolean` | `false` |
| `AUTH_OIDC_ENTRA_ID_IS_ENABLED` | Enable or disable Entra ID SSO authentication via OIDC | `boolean` | `false` |
| `AUTH_OIDC_ENTRA_ID_DISPLAY_NAME` | Entra ID OIDC display name “Sign in with `<name>`” | `string` | `"Entra ID"` |
| `AUTH_OIDC_ENTRA_ID_ISSUER` | Entra ID OIDC issuer | `string` |  |
| `AUTH_OIDC_ENTRA_ID_AUTHORIZATION_URL` | Entra ID OIDC authorization URL | `string` |  |
| `AUTH_OIDC_ENTRA_ID_TOKEN_URL` | Entra ID OIDC token URL | `string` |  |
| `AUTH_OIDC_ENTRA_ID_USER_INFO_URL` | Entra ID OIDC user info URL | `string` |  |
| `AUTH_OIDC_ENTRA_ID_CLIENT_ID` | Entra ID OIDC client ID | `string` |  |
| `AUTH_OIDC_ENTRA_ID_CLIENT_SECRET` | Entra ID OIDC client secret | `string` |  |
| `AUTH_OIDC_ENTRA_ID_CALLBACK_URL` | Entra ID OIDC callback URL | `string` |  |
| `AUTH_OIDC_ENTRA_ID_SCOPE` | Entra ID OIDC scope | `string` | `"openid profile"` |
| `AUTH_OIDC_OKTA_IS_ENABLED` | Enable or disable Okta SSO authentication via OIDC | `boolean` | `false` |
| `AUTH_OIDC_OKTA_DISPLAY_NAME` | Okta OIDC display name “Sign in with `<name>`” | `string` | `"Okta"` |
| `AUTH_OIDC_OKTA_ISSUER` | Okta OIDC issuer | `string` |  |
| `AUTH_OIDC_OKTA_AUTHORIZATION_URL` | Okta OIDC authorization URL | `string` |  |
| `AUTH_OIDC_OKTA_TOKEN_URL` | Okta OIDC token URL | `string` |  |
| `AUTH_OIDC_OKTA_USER_INFO_URL` | Okta OIDC user info URL | `string` |  |
| `AUTH_OIDC_OKTA_CLIENT_ID` | Okta OIDC client ID | `string` |  |
| `AUTH_OIDC_OKTA_CLIENT_SECRET` | Okta OIDC client secret | `string` |  |
| `AUTH_OIDC_OKTA_CALLBACK_URL` | Okta OIDC callback URL | `string` |  |
| `AUTH_OIDC_OKTA_SCOPE` | Okta OIDC scope | `string` | `"openid profile"` |
| `AUTH_SAML_ENTRA_ID_IS_ENABLED` | Enable or disable Entra ID SSO authentication via SAML | `boolean` | `false` |
| `AUTH_SAML_ENTRA_ID_DISPLAY_NAME` | Entra ID SAML display name “Sign in with `<name>`” | `string` | `"Entra ID"` |
| `AUTH_SAML_ENTRA_ID_ENTRY_POINT` | Entra ID SAML entry point | `string` |  |
| `AUTH_SAML_ENTRA_ID_CALLBACK_URL` | Entra ID SAML callback URL | `string` |  |
| `AUTH_SAML_ENTRA_ID_APP_ID` | Entra ID SAML application ID | `string` |  |
| `AUTH_SAML_ENTRA_ID_SIGNATURE_ALGORITHM` | Entra ID SAML signature algorithm | `string` | `"sha256"` |
| `AUTH_SAML_OKTA_IS_ENABLED` | Enable or disable Okta SSO authentication via SAML | `boolean` | `false` |
| `AUTH_SAML_OKTA_DISPLAY_NAME` | Okta SAML display name “Sign in with `<name>`” | `string` | `"Okta"` |
| `AUTH_SAML_OKTA_ENTRY_POINT` | Okta SAML entry point | `string` |  |
| `AUTH_SAML_OKTA_CALLBACK_URL` | Okta SAML callback URL | `string` |  |
| `AUTH_SAML_OKTA_ISSUER` | Okta SAML issuer | `string` |  |
| `AUTH_SAML_OKTA_SIGNATURE_ALGORITHM` | Okta SAML signature algorithm | `string` | `"sha256"` |
| `ENTERPRISE_LICENSE_ORG_NAME` | Enterprise license organization name. Refer to [documentation](https://memgraph.com/docs/database-management/enabling-memgraph-enterprise) for details on obtaining and configuring the license | `string` |  |
| `ENTERPRISE_LICENSE_KEY` | Enterprise license key. Refer to [documentation](https://memgraph.com/docs/database-management/enabling-memgraph-enterprise) for details on obtaining and configuring the license | `string` |  |
| `KEEP_ALIVE_TIMEOUT_MS` | Max time in milliseconds during which Lab will hold the connection | `integer` | `65000` |
| `LOG_LEVEL` | Set the log level: `debug`, `info`, `warn`, `error`. | `string` | `"info"` |
| `LOG_IS_ENABLED` | Enable or disable logging | `boolean` | `true` |
| `LOG_IS_PRETTY_PRINT` | Pretty print logs and error stacktraces in multi-line JSON format | `boolean` | `true` |
| `LOG_CONTEXT_IS_ENABLED` | Enable or disable logging of context information (e.g., identifiers, input data, output data) | `boolean` | `false` |
| `LOG_STACKTRACE_IS_ENABLED` | Enable or disable error stacktraces in the logs | `boolean` | `false` |
| `MODULE_CONTENT_MAX_LEN` | Max length of a query module content | `integer` | `50000` |
| `MODULE_NAME_MAX_LEN` | Max length of the query module name | `integer` | `1000` |
| `MODULE_VALIDATION_IS_ENABLED` | State of module validation | `boolean` | `false` |
| `NODE_LABEL_MAX_LEN` | Max length of the node label | `integer` | `1000` |
| `NODE_LABEL_VALIDATION_IS_ENABLED` | State of node label validation | `boolean` | `false` |
| `NODE_PROPERTY_MAX_LEN` | Max length of the node property | `integer` | `1000` |
| `NODE_PROPERTY_VALIDATION_IS_ENABLED` | State of node property validation | `boolean` | `false` |
| `QUERY_MAX_LEN` | Max length of a Cypher query | `integer` | `5000` |
| `QUERY_VALIDATION_IS_ENABLED` | State of query validation | `boolean` | `false` |
| `QUICK_CONNECT_IS_DISABLED` | State of quick connect feature | `boolean` | `false` |
| `QUICK_CONNECT_MG_HOST` | Host address for quick connect | `string` | `"127.0.0.1"` |
| `QUICK_CONNECT_MG_PORT` | Port for quick connect | `integer` | `7687` |
| `QUICK_CONNECT_MG_IS_ENCRYPTED` | Turn SSL on/off for quick connect | `boolean` | `false` |
| `PORT` | Lab app default listening port | `integer` | `3000` |
| `REQUEST_BODY_LIMIT_MB` | Limit for request body size in MB | `integer` | `20` |
| `SSL_IS_ENABLED` | Enable or disable SSL | `boolean` | `false` |
| `SSL_CERT_PATH` | Path to SSL certificate to be used | `string` | `./ssl/cert.pem` |
| `SSL_KEY_PATH` | Path to SSL key to be used | `string` | `./ssl/key.pem` |
| `STORAGE_MG_HOST` | `(Enterprise only)` Memgraph host for the Lab remote storage | `string` |  |
| `STORAGE_MG_PORT` | `(Enterprise only)` Memgraph port for the Lab remote storage | `number` |  |
| `STORAGE_MG_IS_ENCRYPTED` | `(Enterprise only)` Memgraph SSL on/off for the Lab remote storage | `boolean` |  |
| `STORAGE_MG_DATABASE_NAME` | `(Enterprise only)` Memgraph database name for the Lab remote storage | `string` |  |
| `STORAGE_MG_USERNAME` | `(Enterprise only)` Memgraph username for the Lab remote storage | `string` |  |
| `STORAGE_MG_PASSWORD` | `(Enterprise only)` Memgraph password for the Lab remote storage | `string` |  |
| `STORAGE_MG_CONNECT_TIMEOUT_MS` | `(Enterprise only)` Connection timeout in milliseconds for remote storage | `integer` | `10000` |
| `STREAM_NAME_MAX_LEN` | Max length of the stream name | `integer` | `500` |
| `STREAM_VALIDATION_IS_ENABLED` | State of stream validation | `boolean` | `false` |

When running Memgraph Lab using Docker, configure the environment variables to adjust settings. Use the Docker `run` command as follows to set these variables:

```
docker run -d -p 3000:3000 --name lab -e QUERY_MAX_LEN=10000 -e MODULE_NAME_MAX_LEN=2500 memgraph/lab
```

For Docker Compose, define the same environment variables within the `environment` section of your service configuration in the `docker-compose.yml` file:

```
environment:
  - QUERY_MAX_LEN=10000
  - MODULE_NAME_MAX_LEN=2500
```

[Data visualization](https://memgraph.com/docs/data-visualization "Data visualization")[User manual](https://memgraph.com/docs/data-visualization/user-manual "User manual")

[![Image 23: Memgraph Logo](https://memgraph.com/docs/_next/image?url=%2Fdocs%2Fmemgraph-logo-background.png&w=384&q=75)](https://memgraph.com/)

Documentation

[Get started](https://memgraph.com/docs/getting-started)

[Migrate data](https://memgraph.com/docs/data-migration)

[Query data](https://memgraph.com/docs/querying)

[Create an app](https://memgraph.com/docs/custom-query-modules)

[Visualize data](https://memgraph.com/docs/data-visualization)

[Use advanced algorithms](https://memgraph.com/docs/advanced-algorithms)

Community

[Discord![Image 24: External Link](https://memgraph.com/docs/external-link.svg)](https://discord.gg/memgraph)

[Stack Overflow![Image 25: External Link](https://memgraph.com/docs/external-link.svg)](https://stackoverflow.com/questions/tagged/memgraphdb)

[Twitter![Image 26: External Link](https://memgraph.com/docs/external-link.svg)](https://twitter.com/memgraphdb)

More

[Memgraph Cloud![Image 27: External Link](https://memgraph.com/docs/external-link.svg)](https://cloud.memgraph.com/login)

[Memgraph Playground![Image 28: External Link](https://memgraph.com/docs/external-link.svg)](https://playground.memgraph.com/)

[GitHub![Image 29: External Link](https://memgraph.com/docs/external-link.svg)](https://github.com/memgraph/memgraph)

[YouTube![Image 30: External Link](https://memgraph.com/docs/external-link.svg)](https://www.youtube.com/channel/UCZ3HOJvHGxtQ_JHxOselBYg)

Copyright © 2025 Memgraph

## Metadata

```json
{
  "title": "Install Memgraph Lab and connect to a database",
  "description": "Connect to your graph data with ease using Memgraph. Explore our documentation page for detailed installation instructions and learn how to establish a seamless connection, enabling powerful graph computing and analysis.",
  "url": "https://memgraph.com/docs/data-visualization/install-and-connect",
  "content": "Install Memgraph Lab and connect to a database\n===============\n\n[![Image 16: Memgraph Logo](https://memgraph.com/docs/memgraph-logo-navigation.svg)](https://memgraph.com/)\n\n[GitHub](https://github.com/memgraph/memgraph)[Discord](https://discord.gg/memgraph)\n\n*   [Home](https://memgraph.com/docs)\n*   [Getting started](https://memgraph.com/docs/getting-started)\n    \n    *   [Install Memgraph](https://memgraph.com/docs/getting-started/install-memgraph)\n        \n        *   [Docker](https://memgraph.com/docs/getting-started/install-memgraph/docker)\n        *   [Debian](https://memgraph.com/docs/getting-started/install-memgraph/debian)\n        *   [Ubuntu](https://memgraph.com/docs/getting-started/install-memgraph/ubuntu)\n        *   [CentOS](https://memgraph.com/docs/getting-started/install-memgraph/centos)\n        *   [Fedora](https://memgraph.com/docs/getting-started/install-memgraph/fedora)\n        *   [Rocky](https://memgraph.com/docs/getting-started/install-memgraph/rocky)\n        *   [Red Hat](https://memgraph.com/docs/getting-started/install-memgraph/redhat)\n        *   [Amazon Linux](https://memgraph.com/docs/getting-started/install-memgraph/amazon-linux)\n        *   [Memgraph Cloud](https://memgraph.com/docs/getting-started/install-memgraph/memgraph-cloud)\n        *   [Docker Compose](https://memgraph.com/docs/getting-started/install-memgraph/docker-compose)\n        *   [Kubernetes](https://memgraph.com/docs/getting-started/install-memgraph/kubernetes)\n        *   [WSL](https://memgraph.com/docs/getting-started/install-memgraph/wsl)\n        *   [Direct download links](https://memgraph.com/docs/getting-started/install-memgraph/direct-download-links)\n        \n    *   [CLI](https://memgraph.com/docs/getting-started/cli)\n    *   [First steps with Docker](https://memgraph.com/docs/getting-started/first-steps-with-docker)\n    *   [Building Memgraph from source](https://memgraph.com/docs/getting-started/build-memgraph-from-source)\n    \n*   [Client libraries](https://memgraph.com/docs/client-libraries)\n    \n    *   [C#](https://memgraph.com/docs/client-libraries/c-sharp)\n    *   [Go](https://memgraph.com/docs/client-libraries/go)\n    *   [GraphQL](https://memgraph.com/docs/client-libraries/graphql)\n    *   [Java](https://memgraph.com/docs/client-libraries/java)\n    *   [JavaScript](https://memgraph.com/docs/client-libraries/javascript)\n    *   [Node.js](https://memgraph.com/docs/client-libraries/nodejs)\n    *   [PHP](https://memgraph.com/docs/client-libraries/php)\n    *   [Python](https://memgraph.com/docs/client-libraries/python)\n    *   [Rust](https://memgraph.com/docs/client-libraries/rust)\n    \n*   [AI ecosystem](https://memgraph.com/docs/ai-ecosystem)\n    \n    *   [GraphRAG](https://memgraph.com/docs/ai-ecosystem/graph-rag)\n    *   [Machine learning](https://memgraph.com/docs/ai-ecosystem/machine-learning)\n    \n*   [Fundamentals](https://memgraph.com/docs/fundamentals)\n    \n    *   [Constraints](https://memgraph.com/docs/fundamentals/constraints)\n    *   [Data types](https://memgraph.com/docs/fundamentals/data-types)\n    *   [Data durability](https://memgraph.com/docs/fundamentals/data-durability)\n    *   [Indexes](https://memgraph.com/docs/fundamentals/indexes)\n    *   [Storage memory usage](https://memgraph.com/docs/fundamentals/storage-memory-usage)\n    *   [Telemetry](https://memgraph.com/docs/fundamentals/telemetry)\n    *   [Transactions](https://memgraph.com/docs/fundamentals/transactions)\n    *   [Triggers](https://memgraph.com/docs/fundamentals/triggers)\n    \n*   [Data modeling](https://memgraph.com/docs/data-modeling)\n    \n    *   [Knowledge graph](https://memgraph.com/docs/data-modeling/knowledge-graph)\n    \n*   [Data migration](https://memgraph.com/docs/data-migration)\n    \n    *   [Best practices](https://memgraph.com/docs/data-migration/best-practices)\n    *   [CSV](https://memgraph.com/docs/data-migration/csv)\n    *   [JSON](https://memgraph.com/docs/data-migration/json)\n    *   [CYPHERL](https://memgraph.com/docs/data-migration/cypherl)\n    *   [Migrate from Neo4j](https://memgraph.com/docs/data-migration/migrate-from-neo4j)\n    *   [Migrate from RDBMS using CSV files](https://memgraph.com/docs/data-migration/migrate-from-rdbms)\n    *   [Migrate from RDBMS using MAGE modules](https://memgraph.com/docs/data-migration/migrate-from-rdbms-directly)\n    *   [Migrate from Memgraph Platform to Memgraph MAGE](https://memgraph.com/docs/data-migration/migrate-memgraph-platform)\n    *   [Export data](https://memgraph.com/docs/data-migration/export-data)\n    \n*   [Querying](https://memgraph.com/docs/querying)\n    \n    *   [Best practices](https://memgraph.com/docs/querying/best-practices)\n    *   [Differences in Cypher implementations](https://memgraph.com/docs/querying/differences-in-cypher-implementations)\n    *   [Create graph objects](https://memgraph.com/docs/querying/create-graph-objects)\n    *   [Read and modify data](https://memgraph.com/docs/querying/read-and-modify-data)\n    *   [Clauses](https://memgraph.com/docs/querying/clauses)\n        \n        *   [ALTER](https://memgraph.com/docs/querying/clauses/alter)\n        *   [CALL](https://memgraph.com/docs/querying/clauses/call)\n        *   [CASE](https://memgraph.com/docs/querying/clauses/case)\n        *   [CREATE](https://memgraph.com/docs/querying/clauses/create)\n        *   [DELETE](https://memgraph.com/docs/querying/clauses/delete)\n        *   [DROP GRAPH](https://memgraph.com/docs/querying/clauses/drop-graph)\n        *   [EXPLAIN](https://memgraph.com/docs/querying/clauses/explain)\n        *   [FOREACH](https://memgraph.com/docs/querying/clauses/foreach)\n        *   [LOAD CSV](https://memgraph.com/docs/querying/clauses/load-csv)\n        *   [MATCH](https://memgraph.com/docs/querying/clauses/match)\n        *   [MERGE](https://memgraph.com/docs/querying/clauses/merge)\n        *   [OPTIONAL MATCH](https://memgraph.com/docs/querying/clauses/optional-match)\n        *   [PROFILE](https://memgraph.com/docs/querying/clauses/profile)\n        *   [REMOVE](https://memgraph.com/docs/querying/clauses/remove)\n        *   [RETURN](https://memgraph.com/docs/querying/clauses/return)\n        *   [SET](https://memgraph.com/docs/querying/clauses/set)\n        *   [UNION](https://memgraph.com/docs/querying/clauses/union)\n        *   [UNWIND](https://memgraph.com/docs/querying/clauses/unwind)\n        *   [WHERE](https://memgraph.com/docs/querying/clauses/where)\n        *   [WITH](https://memgraph.com/docs/querying/clauses/with)\n        \n    *   [Functions](https://memgraph.com/docs/querying/functions)\n    *   [Expressions](https://memgraph.com/docs/querying/expressions)\n    *   [Schema](https://memgraph.com/docs/querying/schema)\n    *   [Text search](https://memgraph.com/docs/querying/text-search)\n    *   [Vector search](https://memgraph.com/docs/querying/vector-search)\n    *   [Time to live](https://memgraph.com/docs/querying/time-to-live)\n    *   [Query plan](https://memgraph.com/docs/querying/query-plan)\n    *   [Exploring datasets](https://memgraph.com/docs/querying/exploring-datasets)\n        \n        *   [Analyzing TED talks](https://memgraph.com/docs/querying/exploring-datasets/analyzing-ted-talks)\n        *   [Backpacking through Europe](https://memgraph.com/docs/querying/exploring-datasets/backpacking-through-europe)\n        *   [Exploring the European road network](https://memgraph.com/docs/querying/exploring-datasets/exploring-the-european-road-network)\n        *   [Football transfers](https://memgraph.com/docs/querying/exploring-datasets/football-transfers)\n        *   [GoT deaths](https://memgraph.com/docs/querying/exploring-datasets/got-deaths)\n        *   [Graphing the premier league](https://memgraph.com/docs/querying/exploring-datasets/graphing-the-premier-league)\n        *   [Marvel universe](https://memgraph.com/docs/querying/exploring-datasets/marvel-universe)\n        *   [Movie recommendation](https://memgraph.com/docs/querying/exploring-datasets/movie-recommendation)\n        \n    \n*   [Advanced algorithms](https://memgraph.com/docs/advanced-algorithms)\n    \n    *   [Available algorithms](https://memgraph.com/docs/advanced-algorithms/available-algorithms)\n        \n        *   [algo](https://memgraph.com/docs/advanced-algorithms/available-algorithms/algo)\n        *   [betweenness\\_centrality\\_online](https://memgraph.com/docs/advanced-algorithms/available-algorithms/betweenness_centrality_online)\n        *   [betweenness\\_centrality](https://memgraph.com/docs/advanced-algorithms/available-algorithms/betweenness_centrality)\n        *   [biconnected\\_components](https://memgraph.com/docs/advanced-algorithms/available-algorithms/biconnected_components)\n        *   [bipartite\\_matching](https://memgraph.com/docs/advanced-algorithms/available-algorithms/bipartite_matching)\n        *   [bridges](https://memgraph.com/docs/advanced-algorithms/available-algorithms/bridges)\n        *   [collections](https://memgraph.com/docs/advanced-algorithms/available-algorithms/collections)\n        *   [community\\_detection\\_online](https://memgraph.com/docs/advanced-algorithms/available-algorithms/community_detection_online)\n        *   [community\\_detection](https://memgraph.com/docs/advanced-algorithms/available-algorithms/community_detection)\n        *   [conditional\\_execution](https://memgraph.com/docs/advanced-algorithms/available-algorithms/conditional_execution)\n        *   [create](https://memgraph.com/docs/advanced-algorithms/available-algorithms/create)\n        *   [cugraph](https://memgraph.com/docs/advanced-algorithms/available-algorithms/cugraph)\n        *   [cycles](https://memgraph.com/docs/advanced-algorithms/available-algorithms/cycles)\n        *   [date](https://memgraph.com/docs/advanced-algorithms/available-algorithms/date)\n        *   [degree\\_centrality](https://memgraph.com/docs/advanced-algorithms/available-algorithms/degree_centrality)\n        *   [distance\\_calculator](https://memgraph.com/docs/advanced-algorithms/available-algorithms/distance_calculator)\n        *   [elasticsearch\\_synchronization](https://memgraph.com/docs/advanced-algorithms/available-algorithms/elasticsearch_synchronization)\n        *   [export\\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/export_util)\n        *   [gnn\\_link\\_prediction](https://memgraph.com/docs/advanced-algorithms/available-algorithms/gnn_link_prediction)\n        *   [gnn\\_node\\_classification](https://memgraph.com/docs/advanced-algorithms/available-algorithms/gnn_node_classification)\n        *   [graph\\_analyzer](https://memgraph.com/docs/advanced-algorithms/available-algorithms/graph_analyzer)\n        *   [graph\\_coloring](https://memgraph.com/docs/advanced-algorithms/available-algorithms/graph_coloring)\n        *   [graph\\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/graph_util)\n        *   [igraphalg](https://memgraph.com/docs/advanced-algorithms/available-algorithms/igraphalg)\n        *   [import\\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/import_util)\n        *   [json\\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/json_util)\n        *   [katz\\_centrality\\_online](https://memgraph.com/docs/advanced-algorithms/available-algorithms/katz_centrality_online)\n        *   [katz\\_centrality](https://memgraph.com/docs/advanced-algorithms/available-algorithms/katz_centrality)\n        *   [kmeans\\_clustering](https://memgraph.com/docs/advanced-algorithms/available-algorithms/kmeans_clustering)\n        *   [label](https://memgraph.com/docs/advanced-algorithms/available-algorithms/label)\n        *   [leiden\\_community\\_detection](https://memgraph.com/docs/advanced-algorithms/available-algorithms/leiden_community_detection)\n        *   [llm\\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/llm_util)\n        *   [map](https://memgraph.com/docs/advanced-algorithms/available-algorithms/map)\n        *   [max\\_flow](https://memgraph.com/docs/advanced-algorithms/available-algorithms/max_flow)\n        *   [merge](https://memgraph.com/docs/advanced-algorithms/available-algorithms/merge)\n        *   [meta\\_util](https://memgraph.com/docs/advanced-algorithms/available-algorithms/meta_util)\n        *   [meta](https://memgraph.com/docs/advanced-algorithms/available-algorithms/meta)\n        *   [migrate](https://memgraph.com/docs/advanced-algorithms/available-algorithms/migrate)\n        *   [neighbors](https://memgraph.com/docs/advanced-algorithms/available-algorithms/neighbors)\n        *   [node\\_similarity](https://memgraph.com/docs/advanced-algorithms/available-algorithms/node_similarity)\n        *   [node](https://memgraph.com/docs/advanced-algorithms/available-algorithms/node)\n        *   [node2vec\\_online](https://memgraph.com/docs/advanced-algorithms/available-algorithms/node2vec_online)\n        *   [node2vec](https://memgraph.com/docs/advanced-algorithms/available-algorithms/node2vec)\n        *   [nodes](https://memgraph.com/docs/advanced-algorithms/available-algorithms/nodes)\n        *   [nxalg](https://memgraph.com/docs/advanced-algorithms/available-algorithms/nxalg)\n        *   [pagerank\\_online](https://memgraph.com/docs/advanced-algorithms/available-algorithms/pagerank_online)\n        *   [pagerank](https://memgraph.com/docs/advanced-algorithms/available-algorithms/pagerank)\n        *   [path](https://memgraph.com/docs/advanced-algorithms/available-algorithms/path)\n        *   [periodic](https://memgraph.com/docs/advanced-algorithms/available-algorithms/periodic)\n        *   [refactor](https://memgraph.com/docs/advanced-algorithms/available-algorithms/refactor)\n        *   [set\\_cover](https://memgraph.com/docs/advanced-algorithms/available-algorithms/set_cover)\n        *   [set\\_property](https://memgraph.com/docs/advanced-algorithms/available-algorithms/set_property)\n        *   [temporal](https://memgraph.com/docs/advanced-algorithms/available-algorithms/temporal)\n        *   [text](https://memgraph.com/docs/advanced-algorithms/available-algorithms/text)\n        *   [temporal\\_graph\\_networks](https://memgraph.com/docs/advanced-algorithms/available-algorithms/tgn)\n        *   [tsp](https://memgraph.com/docs/advanced-algorithms/available-algorithms/tsp)\n        *   [union\\_find](https://memgraph.com/docs/advanced-algorithms/available-algorithms/union_find)\n        *   [util\\_module](https://memgraph.com/docs/advanced-algorithms/available-algorithms/util_module)\n        *   [uuid\\_generator](https://memgraph.com/docs/advanced-algorithms/available-algorithms/uuid_generator)\n        *   [vrp](https://memgraph.com/docs/advanced-algorithms/available-algorithms/vrp)\n        *   [weakly\\_connected\\_components](https://memgraph.com/docs/advanced-algorithms/available-algorithms/weakly_connected_components)\n        *   [xml\\_module](https://memgraph.com/docs/advanced-algorithms/available-algorithms/xml_module)\n        \n    *   [Deep path traversal algorithms](https://memgraph.com/docs/advanced-algorithms/deep-path-traversal)\n    *   [Install MAGE](https://memgraph.com/docs/advanced-algorithms/install-mage)\n    *   [Run algorithms](https://memgraph.com/docs/advanced-algorithms/run-algorithms)\n    *   [Utilize NetworkX](https://memgraph.com/docs/advanced-algorithms/utilize-networkx)\n    \n*   [Custom query modules](https://memgraph.com/docs/custom-query-modules)\n    \n    *   [C](https://memgraph.com/docs/custom-query-modules/c)\n        \n        *   [C API](https://memgraph.com/docs/custom-query-modules/c/c-api)\n        *   [C example](https://memgraph.com/docs/custom-query-modules/c/c-example)\n        \n    *   [C++](https://memgraph.com/docs/custom-query-modules/cpp)\n        \n        *   [C++ API](https://memgraph.com/docs/custom-query-modules/cpp/cpp-api)\n        *   [C++ example](https://memgraph.com/docs/custom-query-modules/cpp/cpp-example)\n        \n    *   [Python](https://memgraph.com/docs/custom-query-modules/python)\n        \n        *   [Python API](https://memgraph.com/docs/custom-query-modules/python/python-api)\n        *   [Mock Python API](https://memgraph.com/docs/custom-query-modules/python/mock-python-api)\n        *   [Python example](https://memgraph.com/docs/custom-query-modules/python/python-example)\n        *   [Implement custom query module in Python](https://memgraph.com/docs/custom-query-modules/python/implement-custom-query-module-in-python)\n        *   [Understanding music with modules](https://memgraph.com/docs/custom-query-modules/python/understanding-music-with-modules)\n        \n    *   Rust\n        \n        *   [Rust API](https://memgraph.com/docs/custom-query-modules/rust/rust-api)\n        *   [Rust example](https://memgraph.com/docs/custom-query-modules/rust/rust-example)\n        \n    *   [Manage query modules](https://memgraph.com/docs/custom-query-modules/manage-query-modules)\n    *   [Contributing](https://memgraph.com/docs/custom-query-modules/contributing)\n    \n*   [Data visualization](https://memgraph.com/docs/data-visualization)\n    \n    *   [Install and connect](https://memgraph.com/docs/data-visualization/install-and-connect)\n    *   [User manual](https://memgraph.com/docs/data-visualization/user-manual)\n        \n        *   [Connection types](https://memgraph.com/docs/data-visualization/user-manual/connection-types)\n        *   [CSV file import tool](https://memgraph.com/docs/data-visualization/user-manual/csv-file-import)\n        *   [Custom base path](https://memgraph.com/docs/data-visualization/user-manual/custom-base-path)\n        *   [Custom SSL certificates](https://memgraph.com/docs/data-visualization/user-manual/custom-ssl-certificates)\n        *   [GraphChat](https://memgraph.com/docs/data-visualization/user-manual/graphchat)\n        *   [Query sharing](https://memgraph.com/docs/data-visualization/user-manual/query-sharing)\n        *   [Single sign-on (SSO)](https://memgraph.com/docs/data-visualization/user-manual/single-sign-on)\n        \n    *   [Graph style script](https://memgraph.com/docs/data-visualization/graph-style-script)\n        \n        *   [Built-in elements](https://memgraph.com/docs/data-visualization/graph-style-script/built-in-elements)\n        *   [Directive properties](https://memgraph.com/docs/data-visualization/graph-style-script/directive-properties)\n        \n    *   [Style your graphs in Memgraph Lab](https://memgraph.com/docs/data-visualization/style-your-graphs-in-memgraph-lab)\n    \n*   [Database management](https://memgraph.com/docs/database-management)\n    \n    *   [Authentication and authorization](https://memgraph.com/docs/database-management/authentication-and-authorization)\n        \n        *   [Users](https://memgraph.com/docs/database-management/authentication-and-authorization/users)\n        *   [Role-based access control](https://memgraph.com/docs/database-management/authentication-and-authorization/role-based-access-control)\n        *   [Auth system integrations](https://memgraph.com/docs/database-management/authentication-and-authorization/auth-system-integrations)\n        \n    *   [Backup and restore](https://memgraph.com/docs/database-management/backup-and-restore)\n    *   [Configuration](https://memgraph.com/docs/database-management/configuration)\n    *   [Debugging](https://memgraph.com/docs/database-management/debugging)\n    *   [Enabling Memgraph Enterprise](https://memgraph.com/docs/database-management/enabling-memgraph-enterprise)\n    *   [Experimental features](https://memgraph.com/docs/database-management/experimental-features)\n    *   [Logs](https://memgraph.com/docs/database-management/logs)\n    *   [Monitoring](https://memgraph.com/docs/database-management/monitoring)\n    *   [Multi-tenancy](https://memgraph.com/docs/database-management/multi-tenancy)\n    *   [Query metadata](https://memgraph.com/docs/database-management/query-metadata)\n    *   [Server stats](https://memgraph.com/docs/database-management/server-stats)\n    *   [SSL encryption](https://memgraph.com/docs/database-management/ssl-encryption)\n    *   [System configuration](https://memgraph.com/docs/database-management/system-configuration)\n    \n*   [Deployment](https://memgraph.com/docs/deployment)\n    \n    *   [Docker](https://memgraph.com/docs/deployment/docker)\n    *   [Linux](https://memgraph.com/docs/deployment/linux)\n    *   [AWS](https://memgraph.com/docs/deployment/aws)\n    *   [GCP](https://memgraph.com/docs/deployment/gcp)\n    *   [Azure](https://memgraph.com/docs/deployment/azure)\n    \n*   [Clustering](https://memgraph.com/docs/clustering)\n    \n    *   [High availability](https://memgraph.com/docs/clustering/high-availability)\n    *   [Replication](https://memgraph.com/docs/clustering/replication)\n        \n        *   [System replication](https://memgraph.com/docs/clustering/replication/system-replication)\n        \n    \n*   [Data streams](https://memgraph.com/docs/data-streams)\n    \n    *   [Transformation modules](https://memgraph.com/docs/data-streams/transformation-modules)\n        \n        *   [Transformation modules C API](https://memgraph.com/docs/data-streams/transformation-modules/c-api)\n        *   [Transformations Python API](https://memgraph.com/docs/data-streams/transformation-modules/python-api)\n        \n    *   [Manage streams with queries](https://memgraph.com/docs/data-streams/manage-streams-query)\n    *   [Manage streams with UI](https://memgraph.com/docs/data-streams/manage-streams-lab)\n    *   [Graph stream processing with Kafka](https://memgraph.com/docs/data-streams/graph-stream-processing-with-kafka)\n    *   [Kafka Connect](https://memgraph.com/docs/data-streams/kafka)\n    \n*   [Help center](https://memgraph.com/docs/help-center)\n    \n    *   [FAQ](https://memgraph.com/docs/help-center/faq)\n    *   [Errors](https://memgraph.com/docs/help-center/errors)\n        \n        *   [Auth](https://memgraph.com/docs/help-center/errors/auth)\n        *   [Durability](https://memgraph.com/docs/help-center/errors/durability)\n        *   [Memory](https://memgraph.com/docs/help-center/errors/memory)\n        *   [Modules](https://memgraph.com/docs/help-center/errors/modules)\n        *   [Ports](https://memgraph.com/docs/help-center/errors/ports)\n        *   [Python modules](https://memgraph.com/docs/help-center/errors/python-modules)\n        *   [Replication](https://memgraph.com/docs/help-center/errors/replication)\n        *   [Snapshots](https://memgraph.com/docs/help-center/errors/snapshots)\n        *   [Socket](https://memgraph.com/docs/help-center/errors/socket)\n        *   [SSL](https://memgraph.com/docs/help-center/errors/ssl)\n        *   [Transactions](https://memgraph.com/docs/help-center/errors/transactions)\n        *   [Unknown](https://memgraph.com/docs/help-center/errors/unknown)\n        \n    \n*   [Release notes](https://memgraph.com/docs/release-notes)\n*   [What's coming soon to Memgraph?](https://memgraph.com/docs/coming-soon)\n\nLight\n\nOn This Page\n\n*   [Install Memgraph Lab desktop application](https://memgraph.com/docs/data-visualization/install-and-connect#install-memgraph-lab-desktop-application)\n*   [Run Memgraph Lab with Docker](https://memgraph.com/docs/data-visualization/install-and-connect#run-memgraph-lab-with-docker)\n*   [Issues when connecting to Memgraph](https://memgraph.com/docs/data-visualization/install-and-connect#issues-when-connecting-to-memgraph)\n*   [Environment variables](https://memgraph.com/docs/data-visualization/install-and-connect#environment-variables)\n\n[Question? Give us feedback →](https://github.com/memgraph/documentation/issues/new?title=Feedback%20for%20%E2%80%9CInstall%20Memgraph%20Lab%20and%20connect%20to%20a%20database%E2%80%9D&labels=feedback)[Edit this page](https://github.com/memgraph/documentation/tree/main/pages/data-visualization/install-and-connect.mdx)Scroll to top\n\n[Data visualization](https://memgraph.com/docs/data-visualization \"Data visualization\")Install and connect\n\nInstall Memgraph Lab and connect to a database\n==============================================\n\nWe recommend you use the [Memgraph Platform](https://memgraph.com/docs/getting-started/install-memgraph/docker-compose) and get the complete streaming graph application platform that includes:\n\n*   **Memgraph** - the database that holds your data\n*   **Memgraph Lab** - visual user interface for running queries and visualizing graph data\n*   **mgconsole** - command-line interface for running queries\n*   **MAGE** - graph algorithms and modules library\n\nAfter running the image, mgconsole will open in the terminal while Memgraph Lab is available on `http://localhost:3000`.\n\nIf you want to install Memgraph Lab as a desktop application, check out the [installation instructions](https://memgraph.com/docs/data-visualization/install-and-connect#install-memgraph-lab-desktop-application) for Windows, macOS and Linux, and if you have a public Memgraph database instance you can access the Lab web application at [https://lab.memgraph.com/](https://lab.memgraph.com/).\n\nInstall Memgraph Lab desktop application[](https://memgraph.com/docs/data-visualization/install-and-connect#install-memgraph-lab-desktop-application)\n-----------------------------------------------------------------------------------------------------------------------------------------------------\n\n### Download and install Memgraph\n\nMemgraph Lab requires a [running Memgraph database instance](https://memgraph.com/docs/getting-started).\n\nIf you installed Memgraph using Docker and wish to connect to it with the Memgraph Lab desktop application, ensure that ports 7687, used for instance connections (`-p 7687:7687`), and 7444, used for logs (`-p 7444:7444`), are exposed in the `docker run ...` command.\n\nConnecting Memgraph Lab to Memgraph may vary depending on the deployment method or operating system. The handling of the `QUICK_CONNECT_MG_HOST` environment variable [varies by operating system](https://memgraph.com/docs/getting-started/install-memgraph/docker#issues-when-connecting-to-memgraph-lab-to-memgraph).\n\n### Download Memgraph Lab\n\nVisit the [Download Hub](https://memgraph.com/download/#individual) and download the Memgraph Lab desktop application.\n\n### Install Memgraph Lab\n\nYou can install Memgraph Lab by double clicking the downloaded installer and following the instructions.\n\nIf you downloaded Memgraph Lab on Linux, you can execute:\n\n```\nsudo dpkg -i MemgraphLab-x.x.x.deb\n```\n\n💡\n\nIf you encounter a security warning while installing Memgraph Lab on Windows, you may see a message similar to the ones shown in the images below.\n\n![Image 17](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Fmemgraph-lab-install-windows-1.5e124baf.png&w=1080&q=75)\n\n1.  Click **More info**.\n    \n2.  Verify that Memgraph is listed as the Publisher.\n    \n\n![Image 18](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Fmemgraph-lab-install-windows-2.b21101dd.png&w=1080&q=75)\n\n3.  Click **Run anyway** to proceed with the installation of Memgraph Lab.\n\n### Set up connection\n\nAfter starting Memgraph Lab, you will see the login screen. Follow these steps to connect:\n\n1.  Click on “New connection” in the sidebar.\n2.  Select “Memgraph instance: Connect to a standalone instance”. Feel free to check [other connections types](https://memgraph.com/docs/data-visualization/user-manual/connection-types).\n\nNow, input the connection information:\n\n*   **Host**: Enter `localhost`, `host.docker.internal`, `127.0.0.1`, `0.0.0.0`, or modify it as needed.\n*   **Port**: Enter `7687`, which Memgraph uses by default.\n*   **Database name**: Leave empty unless connecting to a [multi-tenant Memgraph instance](https://memgraph.com/docs/database-management/multi-tenancy).\n*   **Logs port**: Default is `7444`, the port for the web socket logs.\n*   **Encrypted**: Ensure this option is disabled by default. Enable it if your Memgraph has SSL enabled.\n\n### Connect\n\nClick on Connect, and you should be presented with the following dashboard:\n\n![Image 19: lab-dashboard](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Flab-dashboard.7d3ba961.png&w=3840&q=75)\n\nCongratulations! You have successfully installed Memgraph Lab and connected it to Memgraph. You are now ready to start building your graph and querying it.\n\n⚠️\n\nYou might receive the following error message when trying to connect.\n\n![Image 20: failed_connection](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Ffailed_connection.2679930f.png&w=1920&q=75)\n\nIn this case, make sure that Memgraph is properly up and running and that you have entered the correct port number.\n\n### Execute queries\n\nNow, you can execute Cypher queries on Memgraph. Open the **Query** tab, located in the left sidebar, copy the following query and press the **Run query** button:\n\n```\nCREATE (u:User {name: \"Alice\"})-[:Likes]->(m:Software {name: \"Memgraph\"});\n```\n\nThe query above will create 2 nodes in the database, one labeled “User” with name “Alice” and the other labeled “Software” with name “Memgraph”. It will also create a relationship that “Alice” _likes_ “Memgraph”.\n\nTo find created nodes and relationships, execute the following query:\n\n```\nMATCH p=()-[]->() RETURN p;\n```\n\nYou should get the following result:\n\n![Image 21: graph_result](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Flab-graph.e0c85525.png&w=3840&q=75)\n\nRun Memgraph Lab with Docker[](https://memgraph.com/docs/data-visualization/install-and-connect#run-memgraph-lab-with-docker)\n-----------------------------------------------------------------------------------------------------------------------------\n\nRun the Memgraph Lab Docker image using the following command:\n\n```\ndocker run -d -p 3000:3000  --name lab memgraph/lab\n```\n\nOnce the container is up you can access Memgraph Lab on [localhost:3000](https://localhost:3000/).\n\n#### Issues when connecting to Memgraph[](https://memgraph.com/docs/data-visualization/install-and-connect#issues-when-connecting-to-memgraph)\n\nMemgraph Lab detects if Memgraph is running on `localhost:7687` by default for the Quick Connect. The environment variables that are responsible for Quick Connect working as expected are `QUICK_CONNECT_MG_HOST`, `QUICK_CONNECT_MG_PORT` and `QUICK_CONNECT_MG_IS_ENCRYPTED`. The handling of the `QUICK_CONNECT_MG_HOST` environment variable differs based on the operating system:\n\n*   **Mac or Windows**: The `host.docker.internal` hostname allows Docker containers to connect to the host machine. Set this as the value for `QUICK_CONNECT_MG_HOST` when running Lab on Mac or Windows to enable connection to Memgraph running on the host:\n    \n    ```\n    docker run -d -p 3000:3000 -e QUICK_CONNECT_MG_HOST=host.docker.internal --name lab memgraph/lab\n    ```\n    \n*   **Linux**: There’s no need to set `QUICK_CONNECT_MG_HOST` as it defaults to `localhost`, assuming Memgraph is running locally on the host machine.\n    \n\nYou can also use the `QUICK_CONNECT_MG_PORT` environment variable to specify the quick connect port number, e.g. `- e QUICK_CONNECT_MG_PORT=7688`.\n\n💡\n\nTo connect to a running Memgraph instance, you don’t need to set `QUICK_CONNECT_MG_HOST` to `host.docker.internal`. Instead, create a new connection in Memgraph Lab and specify `host.docker.internal` as the Host.\n\n![Image 22: Setting host.docker.internal as the Host](https://memgraph.com/docs/_next/image?url=%2Fdocs%2F_next%2Fstatic%2Fmedia%2Fmemgraph-host-docker-internal.3e857281.png&w=1920&q=75)\n\nEnvironment variables[](https://memgraph.com/docs/data-visualization/install-and-connect#environment-variables)\n---------------------------------------------------------------------------------------------------------------\n\nThe desktop application version of Memgraph Lab does not support receiving environment variables.\n\nConfigure Memgraph Lab using the following environment variables when running it through Docker, including Docker Compose:\n\n| Variable | Description | Type | Default |\n| --- | --- | --- | --- |\n| `AUTH_NATIVE_IS_DISABLED` | Enable or disable native authentication (username, password) | `boolean` | `false` |\n| `AUTH_OIDC_ENTRA_ID_IS_ENABLED` | Enable or disable Entra ID SSO authentication via OIDC | `boolean` | `false` |\n| `AUTH_OIDC_ENTRA_ID_DISPLAY_NAME` | Entra ID OIDC display name “Sign in with `<name>`” | `string` | `\"Entra ID\"` |\n| `AUTH_OIDC_ENTRA_ID_ISSUER` | Entra ID OIDC issuer | `string` |  |\n| `AUTH_OIDC_ENTRA_ID_AUTHORIZATION_URL` | Entra ID OIDC authorization URL | `string` |  |\n| `AUTH_OIDC_ENTRA_ID_TOKEN_URL` | Entra ID OIDC token URL | `string` |  |\n| `AUTH_OIDC_ENTRA_ID_USER_INFO_URL` | Entra ID OIDC user info URL | `string` |  |\n| `AUTH_OIDC_ENTRA_ID_CLIENT_ID` | Entra ID OIDC client ID | `string` |  |\n| `AUTH_OIDC_ENTRA_ID_CLIENT_SECRET` | Entra ID OIDC client secret | `string` |  |\n| `AUTH_OIDC_ENTRA_ID_CALLBACK_URL` | Entra ID OIDC callback URL | `string` |  |\n| `AUTH_OIDC_ENTRA_ID_SCOPE` | Entra ID OIDC scope | `string` | `\"openid profile\"` |\n| `AUTH_OIDC_OKTA_IS_ENABLED` | Enable or disable Okta SSO authentication via OIDC | `boolean` | `false` |\n| `AUTH_OIDC_OKTA_DISPLAY_NAME` | Okta OIDC display name “Sign in with `<name>`” | `string` | `\"Okta\"` |\n| `AUTH_OIDC_OKTA_ISSUER` | Okta OIDC issuer | `string` |  |\n| `AUTH_OIDC_OKTA_AUTHORIZATION_URL` | Okta OIDC authorization URL | `string` |  |\n| `AUTH_OIDC_OKTA_TOKEN_URL` | Okta OIDC token URL | `string` |  |\n| `AUTH_OIDC_OKTA_USER_INFO_URL` | Okta OIDC user info URL | `string` |  |\n| `AUTH_OIDC_OKTA_CLIENT_ID` | Okta OIDC client ID | `string` |  |\n| `AUTH_OIDC_OKTA_CLIENT_SECRET` | Okta OIDC client secret | `string` |  |\n| `AUTH_OIDC_OKTA_CALLBACK_URL` | Okta OIDC callback URL | `string` |  |\n| `AUTH_OIDC_OKTA_SCOPE` | Okta OIDC scope | `string` | `\"openid profile\"` |\n| `AUTH_SAML_ENTRA_ID_IS_ENABLED` | Enable or disable Entra ID SSO authentication via SAML | `boolean` | `false` |\n| `AUTH_SAML_ENTRA_ID_DISPLAY_NAME` | Entra ID SAML display name “Sign in with `<name>`” | `string` | `\"Entra ID\"` |\n| `AUTH_SAML_ENTRA_ID_ENTRY_POINT` | Entra ID SAML entry point | `string` |  |\n| `AUTH_SAML_ENTRA_ID_CALLBACK_URL` | Entra ID SAML callback URL | `string` |  |\n| `AUTH_SAML_ENTRA_ID_APP_ID` | Entra ID SAML application ID | `string` |  |\n| `AUTH_SAML_ENTRA_ID_SIGNATURE_ALGORITHM` | Entra ID SAML signature algorithm | `string` | `\"sha256\"` |\n| `AUTH_SAML_OKTA_IS_ENABLED` | Enable or disable Okta SSO authentication via SAML | `boolean` | `false` |\n| `AUTH_SAML_OKTA_DISPLAY_NAME` | Okta SAML display name “Sign in with `<name>`” | `string` | `\"Okta\"` |\n| `AUTH_SAML_OKTA_ENTRY_POINT` | Okta SAML entry point | `string` |  |\n| `AUTH_SAML_OKTA_CALLBACK_URL` | Okta SAML callback URL | `string` |  |\n| `AUTH_SAML_OKTA_ISSUER` | Okta SAML issuer | `string` |  |\n| `AUTH_SAML_OKTA_SIGNATURE_ALGORITHM` | Okta SAML signature algorithm | `string` | `\"sha256\"` |\n| `ENTERPRISE_LICENSE_ORG_NAME` | Enterprise license organization name. Refer to [documentation](https://memgraph.com/docs/database-management/enabling-memgraph-enterprise) for details on obtaining and configuring the license | `string` |  |\n| `ENTERPRISE_LICENSE_KEY` | Enterprise license key. Refer to [documentation](https://memgraph.com/docs/database-management/enabling-memgraph-enterprise) for details on obtaining and configuring the license | `string` |  |\n| `KEEP_ALIVE_TIMEOUT_MS` | Max time in milliseconds during which Lab will hold the connection | `integer` | `65000` |\n| `LOG_LEVEL` | Set the log level: `debug`, `info`, `warn`, `error`. | `string` | `\"info\"` |\n| `LOG_IS_ENABLED` | Enable or disable logging | `boolean` | `true` |\n| `LOG_IS_PRETTY_PRINT` | Pretty print logs and error stacktraces in multi-line JSON format | `boolean` | `true` |\n| `LOG_CONTEXT_IS_ENABLED` | Enable or disable logging of context information (e.g., identifiers, input data, output data) | `boolean` | `false` |\n| `LOG_STACKTRACE_IS_ENABLED` | Enable or disable error stacktraces in the logs | `boolean` | `false` |\n| `MODULE_CONTENT_MAX_LEN` | Max length of a query module content | `integer` | `50000` |\n| `MODULE_NAME_MAX_LEN` | Max length of the query module name | `integer` | `1000` |\n| `MODULE_VALIDATION_IS_ENABLED` | State of module validation | `boolean` | `false` |\n| `NODE_LABEL_MAX_LEN` | Max length of the node label | `integer` | `1000` |\n| `NODE_LABEL_VALIDATION_IS_ENABLED` | State of node label validation | `boolean` | `false` |\n| `NODE_PROPERTY_MAX_LEN` | Max length of the node property | `integer` | `1000` |\n| `NODE_PROPERTY_VALIDATION_IS_ENABLED` | State of node property validation | `boolean` | `false` |\n| `QUERY_MAX_LEN` | Max length of a Cypher query | `integer` | `5000` |\n| `QUERY_VALIDATION_IS_ENABLED` | State of query validation | `boolean` | `false` |\n| `QUICK_CONNECT_IS_DISABLED` | State of quick connect feature | `boolean` | `false` |\n| `QUICK_CONNECT_MG_HOST` | Host address for quick connect | `string` | `\"127.0.0.1\"` |\n| `QUICK_CONNECT_MG_PORT` | Port for quick connect | `integer` | `7687` |\n| `QUICK_CONNECT_MG_IS_ENCRYPTED` | Turn SSL on/off for quick connect | `boolean` | `false` |\n| `PORT` | Lab app default listening port | `integer` | `3000` |\n| `REQUEST_BODY_LIMIT_MB` | Limit for request body size in MB | `integer` | `20` |\n| `SSL_IS_ENABLED` | Enable or disable SSL | `boolean` | `false` |\n| `SSL_CERT_PATH` | Path to SSL certificate to be used | `string` | `./ssl/cert.pem` |\n| `SSL_KEY_PATH` | Path to SSL key to be used | `string` | `./ssl/key.pem` |\n| `STORAGE_MG_HOST` | `(Enterprise only)` Memgraph host for the Lab remote storage | `string` |  |\n| `STORAGE_MG_PORT` | `(Enterprise only)` Memgraph port for the Lab remote storage | `number` |  |\n| `STORAGE_MG_IS_ENCRYPTED` | `(Enterprise only)` Memgraph SSL on/off for the Lab remote storage | `boolean` |  |\n| `STORAGE_MG_DATABASE_NAME` | `(Enterprise only)` Memgraph database name for the Lab remote storage | `string` |  |\n| `STORAGE_MG_USERNAME` | `(Enterprise only)` Memgraph username for the Lab remote storage | `string` |  |\n| `STORAGE_MG_PASSWORD` | `(Enterprise only)` Memgraph password for the Lab remote storage | `string` |  |\n| `STORAGE_MG_CONNECT_TIMEOUT_MS` | `(Enterprise only)` Connection timeout in milliseconds for remote storage | `integer` | `10000` |\n| `STREAM_NAME_MAX_LEN` | Max length of the stream name | `integer` | `500` |\n| `STREAM_VALIDATION_IS_ENABLED` | State of stream validation | `boolean` | `false` |\n\nWhen running Memgraph Lab using Docker, configure the environment variables to adjust settings. Use the Docker `run` command as follows to set these variables:\n\n```\ndocker run -d -p 3000:3000 --name lab -e QUERY_MAX_LEN=10000 -e MODULE_NAME_MAX_LEN=2500 memgraph/lab\n```\n\nFor Docker Compose, define the same environment variables within the `environment` section of your service configuration in the `docker-compose.yml` file:\n\n```\nenvironment:\n  - QUERY_MAX_LEN=10000\n  - MODULE_NAME_MAX_LEN=2500\n```\n\n[Data visualization](https://memgraph.com/docs/data-visualization \"Data visualization\")[User manual](https://memgraph.com/docs/data-visualization/user-manual \"User manual\")\n\n[![Image 23: Memgraph Logo](https://memgraph.com/docs/_next/image?url=%2Fdocs%2Fmemgraph-logo-background.png&w=384&q=75)](https://memgraph.com/)\n\nDocumentation\n\n[Get started](https://memgraph.com/docs/getting-started)\n\n[Migrate data](https://memgraph.com/docs/data-migration)\n\n[Query data](https://memgraph.com/docs/querying)\n\n[Create an app](https://memgraph.com/docs/custom-query-modules)\n\n[Visualize data](https://memgraph.com/docs/data-visualization)\n\n[Use advanced algorithms](https://memgraph.com/docs/advanced-algorithms)\n\nCommunity\n\n[Discord![Image 24: External Link](https://memgraph.com/docs/external-link.svg)](https://discord.gg/memgraph)\n\n[Stack Overflow![Image 25: External Link](https://memgraph.com/docs/external-link.svg)](https://stackoverflow.com/questions/tagged/memgraphdb)\n\n[Twitter![Image 26: External Link](https://memgraph.com/docs/external-link.svg)](https://twitter.com/memgraphdb)\n\nMore\n\n[Memgraph Cloud![Image 27: External Link](https://memgraph.com/docs/external-link.svg)](https://cloud.memgraph.com/login)\n\n[Memgraph Playground![Image 28: External Link](https://memgraph.com/docs/external-link.svg)](https://playground.memgraph.com/)\n\n[GitHub![Image 29: External Link](https://memgraph.com/docs/external-link.svg)](https://github.com/memgraph/memgraph)\n\n[YouTube![Image 30: External Link](https://memgraph.com/docs/external-link.svg)](https://www.youtube.com/channel/UCZ3HOJvHGxtQ_JHxOselBYg)\n\nCopyright © 2025 Memgraph",
  "usage": {
    "tokens": 10144
  }
}
```
