---
title: GitHub - Project-OSRM/osrm-backend: Open Source Routing Machine - C++ backend
description: Open Source Routing Machine - C++ backend. Contribute to Project-OSRM/osrm-backend development by creating an account on GitHub.
url: https://github.com/Project-OSRM/osrm-backend
timestamp: 2025-01-20T15:30:03.100Z
domain: github.com
path: Project-OSRM_osrm-backend
---

# GitHub - Project-OSRM/osrm-backend: Open Source Routing Machine - C++ backend


Open Source Routing Machine - C++ backend. Contribute to Project-OSRM/osrm-backend development by creating an account on GitHub.


## Content

Open Source Routing Machine
---------------------------

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#open-source-routing-machine)

[![Image 21: osrm-backend CI](https://github.com/Project-OSRM/osrm-backend/actions/workflows/osrm-backend.yml/badge.svg)](https://github.com/Project-OSRM/osrm-backend/actions/workflows/osrm-backend.yml) [![Image 22: Codecov](https://camo.githubusercontent.com/c73dfeaf275a249d1a04a3f66a412e20e1d2970eba020edc04bcc4f0f7cb81b9/68747470733a2f2f636f6465636f762e696f2f67682f50726f6a6563742d4f53524d2f6f73726d2d6261636b656e642f6272616e63682f6d61737465722f67726170682f62616467652e737667)](https://codecov.io/gh/Project-OSRM/osrm-backend) [![Image 23: Discord](https://camo.githubusercontent.com/20f83d12829e761c2c0e7365021f9e991e44ec8e96a3b9874dd7c7b98f217900/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f31303334343837383430323139383630393932)](https://discord.gg/es9CdcCXcb)

High performance routing engine written in C++ designed to run on OpenStreetMap data.

The following services are available via HTTP API, C++ library interface and NodeJs wrapper:

*   Nearest - Snaps coordinates to the street network and returns the nearest matches
*   Route - Finds the fastest route between coordinates
*   Table - Computes the duration or distances of the fastest route between all pairs of supplied coordinates
*   Match - Snaps noisy GPS traces to the road network in the most plausible way
*   Trip - Solves the Traveling Salesman Problem using a greedy heuristic
*   Tile - Generates Mapbox Vector Tiles with internal routing metadata

To quickly try OSRM use our [demo server](http://map.project-osrm.org/) which comes with both the backend and a frontend on top.

For a quick introduction about how the road network is represented in OpenStreetMap and how to map specific road network features have a look at [the OSM wiki on routing](https://wiki.openstreetmap.org/wiki/Routing) or [this guide about mapping for navigation](https://web.archive.org/web/20221206013651/https://labs.mapbox.com/mapping/mapping-for-navigation/).

Related [Project-OSRM](https://github.com/Project-OSRM) repositories:

*   [osrm-frontend](https://github.com/Project-OSRM/osrm-frontend) - User-facing frontend with map. The demo server runs this on top of the backend
*   [osrm-text-instructions](https://github.com/Project-OSRM/osrm-text-instructions) - Text instructions from OSRM route response
*   [osrm-backend-docker](https://github.com/project-osrm/osrm-backend/pkgs/container/osrm-backend) - Ready to use Docker images

Documentation
-------------

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#documentation)

### Full documentation

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#full-documentation)

*   [Hosted documentation](http://project-osrm.org/)
*   [osrm-routed HTTP API documentation](https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md)
*   [libosrm API documentation](https://github.com/Project-OSRM/osrm-backend/blob/master/docs/libosrm.md)

Contact
-------

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#contact)

*   Discord: [join](https://discord.gg/es9CdcCXcb)
*   IRC: `irc.oftc.net`, channel: `#osrm` ([Webchat](https://webchat.oftc.net/))
*   Mailinglist: `https://lists.openstreetmap.org/listinfo/osrm-talk`

Quick Start
-----------

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#quick-start)

The easiest and quickest way to setup your own routing engine is to use Docker images we provide.

There are two pre-processing pipelines available:

*   Contraction Hierarchies (CH)
*   Multi-Level Dijkstra (MLD)

we recommend using MLD by default except for special use-cases such as very large distance matrices where CH is still a better fit for the time being. In the following we explain the MLD pipeline. If you want to use the CH pipeline instead replace `osrm-partition` and `osrm-customize` with a single `osrm-contract` and change the algorithm option for `osrm-routed` to `--algorithm ch`.

### Using Docker

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#using-docker)

We base our Docker images ([backend](https://github.com/Project-OSRM/osrm-backend/pkgs/container/osrm-backend), [frontend](https://hub.docker.com/r/osrm/osrm-frontend/)) on Debian and make sure they are as lightweight as possible. Older backend versions can be found on [Docker Hub](https://hub.docker.com/r/osrm/osrm-backend/).

Download OpenStreetMap extracts for example from [Geofabrik](http://download.geofabrik.de/)

```
wget http://download.geofabrik.de/europe/germany/berlin-latest.osm.pbf
```

Pre-process the extract with the car profile and start a routing engine HTTP server on port 5000

```
docker run -t -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-extract -p /opt/car.lua /data/berlin-latest.osm.pbf || echo "osrm-extract failed"
```

The flag `-v "${PWD}:/data"` creates the directory `/data` inside the docker container and makes the current working directory `"${PWD}"` available there. The file `/data/berlin-latest.osm.pbf` inside the container is referring to `"${PWD}/berlin-latest.osm.pbf"` on the host.

```
docker run -t -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-partition /data/berlin-latest.osrm || echo "osrm-partition failed"
docker run -t -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-customize /data/berlin-latest.osrm || echo "osrm-customize failed"
```

Note there is no `berlin-latest.osrm` file, but multiple `berlin-latest.osrm.*` files, i.e. `berlin-latest.osrm` is not file path, but "base" path referring to set of files and there is an option to omit this `.osrm` suffix completely(e.g. `osrm-partition /data/berlin-latest`).

```
docker run -t -i -p 5000:5000 -v "${PWD}:/data" ghcr.io/project-osrm/osrm-backend osrm-routed --algorithm mld /data/berlin-latest.osrm
```

Make requests against the HTTP server

```
curl "http://127.0.0.1:5000/route/v1/driving/13.388860,52.517037;13.385983,52.496891?steps=true"
```

Optionally start a user-friendly frontend on port 9966, and open it up in your browser

```
docker run -p 9966:9966 osrm/osrm-frontend
xdg-open 'http://127.0.0.1:9966'
```

In case Docker complains about not being able to connect to the Docker daemon make sure you are in the `docker` group.

```
sudo usermod -aG docker $USER
```

After adding yourself to the `docker` group make sure to log out and back in again with your terminal.

We support the following images in the Container Registry:

| Name | Description |
| --- | --- |
| `latest` | `master` compiled with release flag |
| `latest-assertions` | `master` compiled with with release flag, assertions enabled and debug symbols |
| `latest-debug` | `master` compiled with debug flag |
| `<tag>` | specific tag compiled with release flag |
| `<tag>-debug` | specific tag compiled with debug flag |

### Building from Source

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#building-from-source)

The following targets Ubuntu 22.04. For instructions how to build on different distributions, macOS or Windows see our [Wiki](https://github.com/Project-OSRM/osrm-backend/wiki).

Install dependencies

sudo apt install build-essential git cmake pkg-config \\
libbz2-dev libxml2-dev libzip-dev libboost-all-dev \\
lua5.2 liblua5.2-dev libtbb-dev

Compile and install OSRM binaries

mkdir -p build
cd build
cmake ..
cmake --build .
sudo cmake --build . --target install

### Request Against the Demo Server

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#request-against-the-demo-server)

Read the [API usage policy](https://github.com/Project-OSRM/osrm-backend/wiki/Demo-server).

Simple query with instructions and alternatives on Berlin:

```
curl "https://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.385983,52.496891?steps=true&alternatives=true"
```

### Using the Node.js Bindings

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#using-the-nodejs-bindings)

The Node.js bindings provide read-only access to the routing engine. We provide API documentation and examples [here](https://github.com/Project-OSRM/osrm-backend/blob/master/docs/nodejs/api.md).

You will need a modern `libstdc++` toolchain (`>= GLIBCXX_3.4.26`) for binary compatibility if you want to use the pre-built binaries. For older Ubuntu systems you can upgrade your standard library for example with:

```
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update -y
sudo apt-get install -y libstdc++-9-dev
```

You can install the Node.js bindings via `npm install @project-osrm/osrm` or from this repository either via

which will check and use pre-built binaries if they're available for this release and your Node version, or via

```
npm install --build-from-source
```

to always force building the Node.js bindings from source.

#### Unscoped packages

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#unscoped-packages)

Prior to v5.27.0, the `osrm` Node package was unscoped. If you are upgrading from an old package, you will need to do the following:

```
npm uninstall osrm --save
npm install @project-osrm/osrm --save
```

#### Package docs

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#package-docs)

For usage details have a look [these API docs](https://github.com/Project-OSRM/osrm-backend/blob/master/docs/nodejs/api.md).

An exemplary implementation by a 3rd party with Docker and Node.js can be found [here](https://github.com/door2door-io/osrm-express-server-demo).

References in publications
--------------------------

[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#references-in-publications)

When using the code in a (scientific) publication, please cite

```
@inproceedings{luxen-vetter-2011,
 author = {Luxen, Dennis and Vetter, Christian},
 title = {Real-time routing with OpenStreetMap data},
 booktitle = {Proceedings of the 19th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems},
 series = {GIS '11},
 year = {2011},
 isbn = {978-1-4503-1031-4},
 location = {Chicago, Illinois},
 pages = {513--516},
 numpages = {4},
 url = {http://doi.acm.org/10.1145/2093973.2094062},
 doi = {10.1145/2093973.2094062},
 acmid = {2094062},
 publisher = {ACM},
 address = {New York, NY, USA},
}
```

## Metadata

```json
{
  "title": "GitHub - Project-OSRM/osrm-backend: Open Source Routing Machine - C++ backend",
  "description": "Open Source Routing Machine - C++ backend. Contribute to Project-OSRM/osrm-backend development by creating an account on GitHub.",
  "url": "https://github.com/Project-OSRM/osrm-backend?screenshot=true",
  "content": "Open Source Routing Machine\n---------------------------\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#open-source-routing-machine)\n\n[![Image 21: osrm-backend CI](https://github.com/Project-OSRM/osrm-backend/actions/workflows/osrm-backend.yml/badge.svg)](https://github.com/Project-OSRM/osrm-backend/actions/workflows/osrm-backend.yml) [![Image 22: Codecov](https://camo.githubusercontent.com/c73dfeaf275a249d1a04a3f66a412e20e1d2970eba020edc04bcc4f0f7cb81b9/68747470733a2f2f636f6465636f762e696f2f67682f50726f6a6563742d4f53524d2f6f73726d2d6261636b656e642f6272616e63682f6d61737465722f67726170682f62616467652e737667)](https://codecov.io/gh/Project-OSRM/osrm-backend) [![Image 23: Discord](https://camo.githubusercontent.com/20f83d12829e761c2c0e7365021f9e991e44ec8e96a3b9874dd7c7b98f217900/68747470733a2f2f696d672e736869656c64732e696f2f646973636f72642f31303334343837383430323139383630393932)](https://discord.gg/es9CdcCXcb)\n\nHigh performance routing engine written in C++ designed to run on OpenStreetMap data.\n\nThe following services are available via HTTP API, C++ library interface and NodeJs wrapper:\n\n*   Nearest - Snaps coordinates to the street network and returns the nearest matches\n*   Route - Finds the fastest route between coordinates\n*   Table - Computes the duration or distances of the fastest route between all pairs of supplied coordinates\n*   Match - Snaps noisy GPS traces to the road network in the most plausible way\n*   Trip - Solves the Traveling Salesman Problem using a greedy heuristic\n*   Tile - Generates Mapbox Vector Tiles with internal routing metadata\n\nTo quickly try OSRM use our [demo server](http://map.project-osrm.org/) which comes with both the backend and a frontend on top.\n\nFor a quick introduction about how the road network is represented in OpenStreetMap and how to map specific road network features have a look at [the OSM wiki on routing](https://wiki.openstreetmap.org/wiki/Routing) or [this guide about mapping for navigation](https://web.archive.org/web/20221206013651/https://labs.mapbox.com/mapping/mapping-for-navigation/).\n\nRelated [Project-OSRM](https://github.com/Project-OSRM) repositories:\n\n*   [osrm-frontend](https://github.com/Project-OSRM/osrm-frontend) - User-facing frontend with map. The demo server runs this on top of the backend\n*   [osrm-text-instructions](https://github.com/Project-OSRM/osrm-text-instructions) - Text instructions from OSRM route response\n*   [osrm-backend-docker](https://github.com/project-osrm/osrm-backend/pkgs/container/osrm-backend) - Ready to use Docker images\n\nDocumentation\n-------------\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#documentation)\n\n### Full documentation\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#full-documentation)\n\n*   [Hosted documentation](http://project-osrm.org/)\n*   [osrm-routed HTTP API documentation](https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md)\n*   [libosrm API documentation](https://github.com/Project-OSRM/osrm-backend/blob/master/docs/libosrm.md)\n\nContact\n-------\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#contact)\n\n*   Discord: [join](https://discord.gg/es9CdcCXcb)\n*   IRC: `irc.oftc.net`, channel: `#osrm` ([Webchat](https://webchat.oftc.net/))\n*   Mailinglist: `https://lists.openstreetmap.org/listinfo/osrm-talk`\n\nQuick Start\n-----------\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#quick-start)\n\nThe easiest and quickest way to setup your own routing engine is to use Docker images we provide.\n\nThere are two pre-processing pipelines available:\n\n*   Contraction Hierarchies (CH)\n*   Multi-Level Dijkstra (MLD)\n\nwe recommend using MLD by default except for special use-cases such as very large distance matrices where CH is still a better fit for the time being. In the following we explain the MLD pipeline. If you want to use the CH pipeline instead replace `osrm-partition` and `osrm-customize` with a single `osrm-contract` and change the algorithm option for `osrm-routed` to `--algorithm ch`.\n\n### Using Docker\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#using-docker)\n\nWe base our Docker images ([backend](https://github.com/Project-OSRM/osrm-backend/pkgs/container/osrm-backend), [frontend](https://hub.docker.com/r/osrm/osrm-frontend/)) on Debian and make sure they are as lightweight as possible. Older backend versions can be found on [Docker Hub](https://hub.docker.com/r/osrm/osrm-backend/).\n\nDownload OpenStreetMap extracts for example from [Geofabrik](http://download.geofabrik.de/)\n\n```\nwget http://download.geofabrik.de/europe/germany/berlin-latest.osm.pbf\n```\n\nPre-process the extract with the car profile and start a routing engine HTTP server on port 5000\n\n```\ndocker run -t -v \"${PWD}:/data\" ghcr.io/project-osrm/osrm-backend osrm-extract -p /opt/car.lua /data/berlin-latest.osm.pbf || echo \"osrm-extract failed\"\n```\n\nThe flag `-v \"${PWD}:/data\"` creates the directory `/data` inside the docker container and makes the current working directory `\"${PWD}\"` available there. The file `/data/berlin-latest.osm.pbf` inside the container is referring to `\"${PWD}/berlin-latest.osm.pbf\"` on the host.\n\n```\ndocker run -t -v \"${PWD}:/data\" ghcr.io/project-osrm/osrm-backend osrm-partition /data/berlin-latest.osrm || echo \"osrm-partition failed\"\ndocker run -t -v \"${PWD}:/data\" ghcr.io/project-osrm/osrm-backend osrm-customize /data/berlin-latest.osrm || echo \"osrm-customize failed\"\n```\n\nNote there is no `berlin-latest.osrm` file, but multiple `berlin-latest.osrm.*` files, i.e. `berlin-latest.osrm` is not file path, but \"base\" path referring to set of files and there is an option to omit this `.osrm` suffix completely(e.g. `osrm-partition /data/berlin-latest`).\n\n```\ndocker run -t -i -p 5000:5000 -v \"${PWD}:/data\" ghcr.io/project-osrm/osrm-backend osrm-routed --algorithm mld /data/berlin-latest.osrm\n```\n\nMake requests against the HTTP server\n\n```\ncurl \"http://127.0.0.1:5000/route/v1/driving/13.388860,52.517037;13.385983,52.496891?steps=true\"\n```\n\nOptionally start a user-friendly frontend on port 9966, and open it up in your browser\n\n```\ndocker run -p 9966:9966 osrm/osrm-frontend\nxdg-open 'http://127.0.0.1:9966'\n```\n\nIn case Docker complains about not being able to connect to the Docker daemon make sure you are in the `docker` group.\n\n```\nsudo usermod -aG docker $USER\n```\n\nAfter adding yourself to the `docker` group make sure to log out and back in again with your terminal.\n\nWe support the following images in the Container Registry:\n\n| Name | Description |\n| --- | --- |\n| `latest` | `master` compiled with release flag |\n| `latest-assertions` | `master` compiled with with release flag, assertions enabled and debug symbols |\n| `latest-debug` | `master` compiled with debug flag |\n| `<tag>` | specific tag compiled with release flag |\n| `<tag>-debug` | specific tag compiled with debug flag |\n\n### Building from Source\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#building-from-source)\n\nThe following targets Ubuntu 22.04. For instructions how to build on different distributions, macOS or Windows see our [Wiki](https://github.com/Project-OSRM/osrm-backend/wiki).\n\nInstall dependencies\n\nsudo apt install build-essential git cmake pkg-config \\\\\nlibbz2-dev libxml2-dev libzip-dev libboost-all-dev \\\\\nlua5.2 liblua5.2-dev libtbb-dev\n\nCompile and install OSRM binaries\n\nmkdir -p build\ncd build\ncmake ..\ncmake --build .\nsudo cmake --build . --target install\n\n### Request Against the Demo Server\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#request-against-the-demo-server)\n\nRead the [API usage policy](https://github.com/Project-OSRM/osrm-backend/wiki/Demo-server).\n\nSimple query with instructions and alternatives on Berlin:\n\n```\ncurl \"https://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.385983,52.496891?steps=true&alternatives=true\"\n```\n\n### Using the Node.js Bindings\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#using-the-nodejs-bindings)\n\nThe Node.js bindings provide read-only access to the routing engine. We provide API documentation and examples [here](https://github.com/Project-OSRM/osrm-backend/blob/master/docs/nodejs/api.md).\n\nYou will need a modern `libstdc++` toolchain (`>= GLIBCXX_3.4.26`) for binary compatibility if you want to use the pre-built binaries. For older Ubuntu systems you can upgrade your standard library for example with:\n\n```\nsudo add-apt-repository ppa:ubuntu-toolchain-r/test\nsudo apt-get update -y\nsudo apt-get install -y libstdc++-9-dev\n```\n\nYou can install the Node.js bindings via `npm install @project-osrm/osrm` or from this repository either via\n\nwhich will check and use pre-built binaries if they're available for this release and your Node version, or via\n\n```\nnpm install --build-from-source\n```\n\nto always force building the Node.js bindings from source.\n\n#### Unscoped packages\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#unscoped-packages)\n\nPrior to v5.27.0, the `osrm` Node package was unscoped. If you are upgrading from an old package, you will need to do the following:\n\n```\nnpm uninstall osrm --save\nnpm install @project-osrm/osrm --save\n```\n\n#### Package docs\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#package-docs)\n\nFor usage details have a look [these API docs](https://github.com/Project-OSRM/osrm-backend/blob/master/docs/nodejs/api.md).\n\nAn exemplary implementation by a 3rd party with Docker and Node.js can be found [here](https://github.com/door2door-io/osrm-express-server-demo).\n\nReferences in publications\n--------------------------\n\n[](https://github.com/Project-OSRM/osrm-backend?screenshot=true#references-in-publications)\n\nWhen using the code in a (scientific) publication, please cite\n\n```\n@inproceedings{luxen-vetter-2011,\n author = {Luxen, Dennis and Vetter, Christian},\n title = {Real-time routing with OpenStreetMap data},\n booktitle = {Proceedings of the 19th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems},\n series = {GIS '11},\n year = {2011},\n isbn = {978-1-4503-1031-4},\n location = {Chicago, Illinois},\n pages = {513--516},\n numpages = {4},\n url = {http://doi.acm.org/10.1145/2093973.2094062},\n doi = {10.1145/2093973.2094062},\n acmid = {2094062},\n publisher = {ACM},\n address = {New York, NY, USA},\n}\n```",
  "usage": {
    "tokens": 2791
  }
}
```
