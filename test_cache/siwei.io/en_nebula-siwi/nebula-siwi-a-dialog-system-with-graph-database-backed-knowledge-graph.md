---
title: Nebula Siwi: A Dialog System With Graph Database Backed Knowledge Graph
description: 
url: https://siwei.io/en/nebula-siwi/
timestamp: 2025-01-20T15:46:13.462Z
domain: siwei.io
path: en_nebula-siwi
---

# Nebula Siwi: A Dialog System With Graph Database Backed Knowledge Graph



## Content

> a PoC of Dialog System With Graph Database Backed Knowledge Graph.

Related GitHub Repo: [https://github.com/wey-gu/nebula-siwi/](https://github.com/wey-gu/nebula-siwi/)

> I created the Katacoda Interactive Env for this project 👉🏻 [https://siwei.io/cources/](https://siwei.io/cources/)

> Now you can play with the data on Nebula Playground: [https://nebula-graph.io/demo/](https://nebula-graph.io/demo/)

Siwi (/ˈsɪwi/) is a PoC of Dialog System With Graph Database Backed Knowledge Graph.

For now, it’s a demo for task-driven(not general purpose) dialog bots with KG(Knowledge Graph) leveraging Nebula Graph with the minimal/sample dataset from [Nebula Graph Manual](https://docs.nebula-graph.io/2.0.1/3.ngql-guide/1.nGQL-overview/1.overview/#basketballplayer)/ [NG中文手册](https://docs.nebula-graph.com.cn/2.0.1/3.ngql-guide/1.nGQL-overview/1.overview/#basketballplayer).

> Tips: Now you can play with the graph online without installing yourself!
> 
> [Nebula Playground](https://playground.nebula-graph.io/) | [Nebula Playground - China Mainland](https://playground.nebula-graph.com.cn/)

Supported queries:

`relation`:

*   What is the relationship between Yao Ming and Lakers?
*   How does Yao Ming and Lakers connected?

`serving`:

*   Which team had Yao Ming served?

`friendship`:

*   Whom does Tim Duncan follow?
*   Who are Yao Ming’s friends?

[](https://siwei.io/en/nebula-siwi/#deploy-and-try)1 Deploy and Try
-------------------------------------------------------------------

TBD (leveraging docker and nebula-up)

This is one of the most naive pipeline for a specific domain/ single purpose chat bot built on a Knowledge Graph.

![Image 10: backend-demo](https://siwei.io/nebula-siwi/backend-demo.webp)

The Backend(Siwi API) is a Flask based API server:

*   Flask API server takes questions in HTTP POST, and calls the bot API.
    
*   In bot API part there are classfier(Symentic Parsing, Intent Matching, Slot Filling), and question actors(Call corresponding actions to query Knowledge Graph with intents and slots).
    
*   Knowledge Graph is built on an Open-Source Graph Database: [Nebula Graph](https://github.com/vesoft-inc/nebula-graph)
    

![Image 11: demo](https://siwei.io/nebula-siwi/demo.webp)

The Frontend is a VueJS Single Page Applicaiton(SPA):

*   I reused a Vue Bot UI to showcase a chat window in this human-agent interaction, typing is supported.
*   In addtion, leverating Chrome’s [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API), a button to listen to human voice is introduced

```
┌────────────────┬──────────────────────────────────────┐
│                │                                      │
│                │  Speech                              │
│     ┌──────────▼──────────┐                           │
│     │            Frontend │   Siwi, /ˈsɪwi/           │
│     │ Web_Speech_API      │   A PoC of                │
│     │                     │   Dialog System           │
│     │ Vue.JS              │   With Graph Database     │
│     │                     │   Backed Knowledge Graph  │
│     └──────────┬──────────┘                           │
│                │  Sentence                            │
│                │                                      │
│   ┌────────────┼──────────────────────────────┐       │
│   │            │                              │       │
│   │            │              Backend         │       │
│   │ ┌──────────▼──────────┐                   │       │
│   │ │ Web API, Flask      │   ./app/          │       │
│   │ └──────────┬──────────┘                   │       │
│   │            │  Sentence    ./bot/          │       │
│   │ ┌──────────▼──────────┐                   │       │
│   │ │                     │                   │       │
│   │ │ Intent matching,    │   ./bot/classifier│       │
│   │ │ Symentic Processing │                   │       │
│   │ │                     │                   │       │
│   │ └──────────┬──────────┘                   │       │
│   │            │  Intent, Entities            │       │
│   │ ┌──────────▼──────────┐                   │       │
│   │ │                     │                   │       │
│   │ │ Intent Actor        │   ./bot/actions   │       │
│   │ │                     │                   │       │
│   └─┴──────────┬──────────┴───────────────────┘       │
│                │  Graph Query                         │
│     ┌──────────▼──────────┐                           │
│     │                     │                           │
│     │ Graph Database      │    Nebula Graph           │
│     │                     │                           │
│     └─────────────────────┘                           │
│                                                       │
│                                                       │
│                                                       │
└───────────────────────────────────────────────────────┘
```

```
.
├── README.md
├── src
│   ├── siwi                        # Siwi-API Backend
│   │   ├── app                     # Web Server, take HTTP requests and calls Bot API
│   │   └── bot                     # Bot API
│   │       ├── actions             # Take Intent, Slots, Query Knowledge Graph here
│   │       ├── bot                 # Entrypoint of the Bot API
│   │       ├── classifier          # Symentic Parsing, Intent Matching, Slot Filling
│   │       └── test                # Example Data Source as equivalent/mocked module
│   └── siwi_frontend               # Browser End
│       ├── README.md
│       ├── package.json
│       └── src
│           ├── App.vue             # Listening to user and pass Questions to Siwi-API
│           └── main.js
└── wsgi.py
```

Install and run.

```
# Install siwi backend
python3 -m build

# Configure Nebula Graph Endpoint
export NG_ENDPOINTS=127.0.0.1:9669

# Run Backend API server
gunicorn --bind :5000 wsgi --workers 1 --threads 1 --timeout 60
```

> For OpenFunction/ KNative

```
docker build -t weygu/siwi-api .
docker run --rm --name siwi-api \
     --env=PORT=5000 \
     --env=NG_ENDPOINTS=127.0.0.1:9669 \
     --net=host \
     weygu/siwi-api
```

Try it out Web API:

```
$ curl --header "Content-Type: application/json" \
       --request POST \
       --data '{"question": "What is the relationship between Yao Ming and Lakers?"}' \
       http://192.168.8.128:5000/query | jq

{
  "answer": "There are at least 23 relations between Yao Ming and Lakers, one relation path is: Yao Ming follows Shaquille O'Neal serves Lakers."
}
```

Call Bot Python API:

```
from nebula2.gclient.net import ConnectionPool
from nebula2.Config import Config

# define a config
config = Config()
config.max_connection_pool_size = 10
# init connection pool
connection_pool = ConnectionPool()
# if the given servers are ok, return true, else return false
ok = connection_pool.init([('127.0.0.1', 9669)], config)

# import siwi bot
from siwi.bot import bot

# instantiate a bot
b = bot.SiwiBot(connection_pool)

# make the question query
b.query("Which team had Jonathon Simmons served?")
```

Then a response will be like this:

```
In [4]: b.query("Which team had Jonathon Simmons serv
   ...: ed?")

[DEBUG] ServeAction intent: {'entities': {'Jonathon Simmons': 'player'}, 'intents': ('serve',)}

[DEBUG] query for RelationshipAction:
	USE basketballplayer;
  MATCH p=(v)-[e:serve*1]->(v1) WHERE id(v) == "player112"
  RETURN p LIMIT 100;

[2021-07-02 02:59:36,392]:Get connection to ('127.0.0.1', 9669)

Out[4]: 'Jonathon Simmons had served 3 teams. Spurs from 2015 to 2015; 76ers from 2019 to 2019; Magic from 2017 to 2017; '
```

Referring to [siwi\_frontend](https://github.com/wey-gu/nebula-siwi/tree/main/src/siwi_frontend)

*   Use [NBA-API](https://github.com/swar/nba_api) to fallback undefined pattern questions
*   Wrap and manage sessions instead of get and release session per request, this is somehow costly actually.
*   Use NLP methods to implement proper Symentic Parsing, Intent Matching, Slot Filling
*   Build Graph to help with Intent Matching, especially for a general purpose bot
*   Use larger Dataset i.e. from [wyattowalsh/basketball](https://www.kaggle.com/wyattowalsh/basketball)

*   I learnt a lot from the [KGQA on MedicalKG](https://github.com/liuhuanyong/QASystemOnMedicalKG) created by [Huanyong Liu](https://liuhuanyong.github.io/)
*   [Flask](https://github.com/pallets/flask)
*   [pyahocorasick](https://github.com/WojciechMula/pyahocorasick) created by [Wojciech Muła](http://0x80.pl/)
*   [PyYaml](https://pyyaml.org/)

*   [VueJS](https://vuejs.org/) for frontend framework
*   [Vue Bot UI](https://github.com/juzser/vue-bot-ui), as a lovely bot UI in vue
*   [Vue Web Speech](https://github.com/Drackokacka/vue-web-speech), for speech API vue wrapper
*   [Axios](https://github.com/axios/axios) for browser http client
*   [Solarized](https://en.wikipedia.org/wiki/Solarized_%28color_scheme%29) for color scheme
*   [Vitesome](https://github.com/alvarosaburido/vitesome) for landing page design

> Image credit goes to [https://unsplash.com/photos/0E\_vhMVqL9g](https://unsplash.com/photos/0E_vhMVqL9g)

## Metadata

```json
{
  "title": "Nebula Siwi: A Dialog System With Graph Database Backed Knowledge Graph",
  "description": "",
  "url": "https://siwei.io/en/nebula-siwi/",
  "content": "> a PoC of Dialog System With Graph Database Backed Knowledge Graph.\n\nRelated GitHub Repo: [https://github.com/wey-gu/nebula-siwi/](https://github.com/wey-gu/nebula-siwi/)\n\n> I created the Katacoda Interactive Env for this project 👉🏻 [https://siwei.io/cources/](https://siwei.io/cources/)\n\n> Now you can play with the data on Nebula Playground: [https://nebula-graph.io/demo/](https://nebula-graph.io/demo/)\n\nSiwi (/ˈsɪwi/) is a PoC of Dialog System With Graph Database Backed Knowledge Graph.\n\nFor now, it’s a demo for task-driven(not general purpose) dialog bots with KG(Knowledge Graph) leveraging Nebula Graph with the minimal/sample dataset from [Nebula Graph Manual](https://docs.nebula-graph.io/2.0.1/3.ngql-guide/1.nGQL-overview/1.overview/#basketballplayer)/ [NG中文手册](https://docs.nebula-graph.com.cn/2.0.1/3.ngql-guide/1.nGQL-overview/1.overview/#basketballplayer).\n\n> Tips: Now you can play with the graph online without installing yourself!\n> \n> [Nebula Playground](https://playground.nebula-graph.io/) | [Nebula Playground - China Mainland](https://playground.nebula-graph.com.cn/)\n\nSupported queries:\n\n`relation`:\n\n*   What is the relationship between Yao Ming and Lakers?\n*   How does Yao Ming and Lakers connected?\n\n`serving`:\n\n*   Which team had Yao Ming served?\n\n`friendship`:\n\n*   Whom does Tim Duncan follow?\n*   Who are Yao Ming’s friends?\n\n[](https://siwei.io/en/nebula-siwi/#deploy-and-try)1 Deploy and Try\n-------------------------------------------------------------------\n\nTBD (leveraging docker and nebula-up)\n\nThis is one of the most naive pipeline for a specific domain/ single purpose chat bot built on a Knowledge Graph.\n\n![Image 10: backend-demo](https://siwei.io/nebula-siwi/backend-demo.webp)\n\nThe Backend(Siwi API) is a Flask based API server:\n\n*   Flask API server takes questions in HTTP POST, and calls the bot API.\n    \n*   In bot API part there are classfier(Symentic Parsing, Intent Matching, Slot Filling), and question actors(Call corresponding actions to query Knowledge Graph with intents and slots).\n    \n*   Knowledge Graph is built on an Open-Source Graph Database: [Nebula Graph](https://github.com/vesoft-inc/nebula-graph)\n    \n\n![Image 11: demo](https://siwei.io/nebula-siwi/demo.webp)\n\nThe Frontend is a VueJS Single Page Applicaiton(SPA):\n\n*   I reused a Vue Bot UI to showcase a chat window in this human-agent interaction, typing is supported.\n*   In addtion, leverating Chrome’s [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API), a button to listen to human voice is introduced\n\n```\n┌────────────────┬──────────────────────────────────────┐\n│                │                                      │\n│                │  Speech                              │\n│     ┌──────────▼──────────┐                           │\n│     │            Frontend │   Siwi, /ˈsɪwi/           │\n│     │ Web_Speech_API      │   A PoC of                │\n│     │                     │   Dialog System           │\n│     │ Vue.JS              │   With Graph Database     │\n│     │                     │   Backed Knowledge Graph  │\n│     └──────────┬──────────┘                           │\n│                │  Sentence                            │\n│                │                                      │\n│   ┌────────────┼──────────────────────────────┐       │\n│   │            │                              │       │\n│   │            │              Backend         │       │\n│   │ ┌──────────▼──────────┐                   │       │\n│   │ │ Web API, Flask      │   ./app/          │       │\n│   │ └──────────┬──────────┘                   │       │\n│   │            │  Sentence    ./bot/          │       │\n│   │ ┌──────────▼──────────┐                   │       │\n│   │ │                     │                   │       │\n│   │ │ Intent matching,    │   ./bot/classifier│       │\n│   │ │ Symentic Processing │                   │       │\n│   │ │                     │                   │       │\n│   │ └──────────┬──────────┘                   │       │\n│   │            │  Intent, Entities            │       │\n│   │ ┌──────────▼──────────┐                   │       │\n│   │ │                     │                   │       │\n│   │ │ Intent Actor        │   ./bot/actions   │       │\n│   │ │                     │                   │       │\n│   └─┴──────────┬──────────┴───────────────────┘       │\n│                │  Graph Query                         │\n│     ┌──────────▼──────────┐                           │\n│     │                     │                           │\n│     │ Graph Database      │    Nebula Graph           │\n│     │                     │                           │\n│     └─────────────────────┘                           │\n│                                                       │\n│                                                       │\n│                                                       │\n└───────────────────────────────────────────────────────┘\n```\n\n```\n.\n├── README.md\n├── src\n│   ├── siwi                        # Siwi-API Backend\n│   │   ├── app                     # Web Server, take HTTP requests and calls Bot API\n│   │   └── bot                     # Bot API\n│   │       ├── actions             # Take Intent, Slots, Query Knowledge Graph here\n│   │       ├── bot                 # Entrypoint of the Bot API\n│   │       ├── classifier          # Symentic Parsing, Intent Matching, Slot Filling\n│   │       └── test                # Example Data Source as equivalent/mocked module\n│   └── siwi_frontend               # Browser End\n│       ├── README.md\n│       ├── package.json\n│       └── src\n│           ├── App.vue             # Listening to user and pass Questions to Siwi-API\n│           └── main.js\n└── wsgi.py\n```\n\nInstall and run.\n\n```\n# Install siwi backend\npython3 -m build\n\n# Configure Nebula Graph Endpoint\nexport NG_ENDPOINTS=127.0.0.1:9669\n\n# Run Backend API server\ngunicorn --bind :5000 wsgi --workers 1 --threads 1 --timeout 60\n```\n\n> For OpenFunction/ KNative\n\n```\ndocker build -t weygu/siwi-api .\ndocker run --rm --name siwi-api \\\n     --env=PORT=5000 \\\n     --env=NG_ENDPOINTS=127.0.0.1:9669 \\\n     --net=host \\\n     weygu/siwi-api\n```\n\nTry it out Web API:\n\n```\n$ curl --header \"Content-Type: application/json\" \\\n       --request POST \\\n       --data '{\"question\": \"What is the relationship between Yao Ming and Lakers?\"}' \\\n       http://192.168.8.128:5000/query | jq\n\n{\n  \"answer\": \"There are at least 23 relations between Yao Ming and Lakers, one relation path is: Yao Ming follows Shaquille O'Neal serves Lakers.\"\n}\n```\n\nCall Bot Python API:\n\n```\nfrom nebula2.gclient.net import ConnectionPool\nfrom nebula2.Config import Config\n\n# define a config\nconfig = Config()\nconfig.max_connection_pool_size = 10\n# init connection pool\nconnection_pool = ConnectionPool()\n# if the given servers are ok, return true, else return false\nok = connection_pool.init([('127.0.0.1', 9669)], config)\n\n# import siwi bot\nfrom siwi.bot import bot\n\n# instantiate a bot\nb = bot.SiwiBot(connection_pool)\n\n# make the question query\nb.query(\"Which team had Jonathon Simmons served?\")\n```\n\nThen a response will be like this:\n\n```\nIn [4]: b.query(\"Which team had Jonathon Simmons serv\n   ...: ed?\")\n\n[DEBUG] ServeAction intent: {'entities': {'Jonathon Simmons': 'player'}, 'intents': ('serve',)}\n\n[DEBUG] query for RelationshipAction:\n\tUSE basketballplayer;\n  MATCH p=(v)-[e:serve*1]->(v1) WHERE id(v) == \"player112\"\n  RETURN p LIMIT 100;\n\n[2021-07-02 02:59:36,392]:Get connection to ('127.0.0.1', 9669)\n\nOut[4]: 'Jonathon Simmons had served 3 teams. Spurs from 2015 to 2015; 76ers from 2019 to 2019; Magic from 2017 to 2017; '\n```\n\nReferring to [siwi\\_frontend](https://github.com/wey-gu/nebula-siwi/tree/main/src/siwi_frontend)\n\n*   Use [NBA-API](https://github.com/swar/nba_api) to fallback undefined pattern questions\n*   Wrap and manage sessions instead of get and release session per request, this is somehow costly actually.\n*   Use NLP methods to implement proper Symentic Parsing, Intent Matching, Slot Filling\n*   Build Graph to help with Intent Matching, especially for a general purpose bot\n*   Use larger Dataset i.e. from [wyattowalsh/basketball](https://www.kaggle.com/wyattowalsh/basketball)\n\n*   I learnt a lot from the [KGQA on MedicalKG](https://github.com/liuhuanyong/QASystemOnMedicalKG) created by [Huanyong Liu](https://liuhuanyong.github.io/)\n*   [Flask](https://github.com/pallets/flask)\n*   [pyahocorasick](https://github.com/WojciechMula/pyahocorasick) created by [Wojciech Muła](http://0x80.pl/)\n*   [PyYaml](https://pyyaml.org/)\n\n*   [VueJS](https://vuejs.org/) for frontend framework\n*   [Vue Bot UI](https://github.com/juzser/vue-bot-ui), as a lovely bot UI in vue\n*   [Vue Web Speech](https://github.com/Drackokacka/vue-web-speech), for speech API vue wrapper\n*   [Axios](https://github.com/axios/axios) for browser http client\n*   [Solarized](https://en.wikipedia.org/wiki/Solarized_%28color_scheme%29) for color scheme\n*   [Vitesome](https://github.com/alvarosaburido/vitesome) for landing page design\n\n> Image credit goes to [https://unsplash.com/photos/0E\\_vhMVqL9g](https://unsplash.com/photos/0E_vhMVqL9g)",
  "publishedTime": "2021-09-18T13:53:20+08:00",
  "usage": {
    "tokens": 2449
  }
}
```
