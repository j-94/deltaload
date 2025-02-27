---
title: Blazing fast Python Docker builds with Poetry 🏃 - Riccardo Albertazzi - Medium
description: Building Docker images for your project typically involves installing its dependencies in a reproducible and deterministic way. In the Python community Poetry is one of the most affirmed tools to…
url: https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0
timestamp: 2025-01-20T15:44:38.839Z
domain: medium.com
path: @albertazzir_blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0
---

# Blazing fast Python Docker builds with Poetry 🏃 - Riccardo Albertazzi - Medium


Building Docker images for your project typically involves installing its dependencies in a reproducible and deterministic way. In the Python community Poetry is one of the most affirmed tools to…


## Content

How we can turn slow and tedious Docker builds into seamless operations
-----------------------------------------------------------------------

[![Image 9: Riccardo Albertazzi](https://miro.medium.com/v2/resize:fill:88:88/1*e_3fOd_QVRZzWzJKXqZydw.jpeg)](https://medium.com/@albertazzir?source=post_page---byline--a78a66f5aed0--------------------------------)

![Image 10](https://miro.medium.com/v2/resize:fit:700/1*XWWuq095-KpaGUaWgH9u5g.jpeg)

A view of Annapurna from its south face. Legend says only people who know how to optimize Docker builds can reach the top.

Building Docker images for your project typically involves installing its dependencies in a reproducible and deterministic way. In the Python community [Poetry](https://python-poetry.org/) is one of the most affirmed tools to achieve that. However, a non-optimal usage of Poetry in your Docker builds can result in poor performance and long builds, which in the end hinder developer productivity.

This article assumes that you are already familiar with both Poetry and Docker — in particular how [Docker layer caching](https://docs.docker.com/build/cache/) works— and that you are looking for a way to optimize your builds. I structured the article from naive to more optimized solutions to let the reader understand the impact of each optimization. Enough about introduction, let’s see some Dockerfiles! 💪

0\. Project structure
---------------------

Let’s use a toy project to reason about. I randomly named it `annapurna` as one the best mountains I’ve ever seen ⛰ A minimal Poetry project would contain the `pyproject.toml` , the associated `poetry.lock`, your code and a `Dockerfile` .

.  
├── Dockerfile  
├── README.md  
├── annapurna  
│   ├── \_\_init\_\_.py  
│   └── main.py  
├── poetry.lock  
└── pyproject.toml

For simplicity I just installed the famous `fastapi` web server through `poetry add fastapi` and a couple linters that I typically use in my projects:

\[tool.poetry\]  
name = "annapurna"  
version = "1.0.0"  
description = ""  
authors = \["Riccardo Albertazzi <my@email.com\>"\]  
readme = "README.md"\[tool.poetry.dependencies\]  
python = "^3.11"

fastapi = "^0.95.1"

\[tool.poetry.group.dev.dependencies\]  
black = "^23.3.0"  
mypy = "^1.2.0"  
ruff = "^0.0.263"

\[build-system\]  
requires = \["poetry-core"\]  
build-backend = "poetry.core.masonry.api"

1\. The naive approach 😐
-------------------------

What our Docker build needs to do is having Python and Poetry installed, getting our code, installing the dependencies and setting the project’s entrypoint. This is exactly what we are doing in here:

FROM python:3.11-busterRUN pip install poetry

COPY . .

RUN poetry install

ENTRYPOINT \["poetry", "run", "python", "-m", "annapurna.main"\]

This simple Dockerfile does the job, and with a simple `docker build . `you’ll already get a working image. This is in fact the typical Dockerfile you see in tutorials and open-source projects, as it’s pretty easy to understand. But as your project grows it will lead you under a path of tedious builds and huge Docker images — my resulting Docker image is in fact 1.1GB! All the optimizations we’ll see go in the direction of exploiting caching and reducing the final image size.

2\. Warming up 🚶
-----------------

Let’s start with a few improvements to warm up:

*   Pin the `poetry`version. I suggest doing it as Poetry can contain breaking changes from one minor version to other, and you don’t want your builds to suddenly break when a new version is released. You should clearly pin it to the same version you are using locally.
*   Just `COPY` the data that you need, and nothing else. This will avoid for instance a useless copy of my local virtual environment (located at `.venv` ). Poetry will complain if a `README.md` is not found (I don’t really share this choice) and as such I create an empty one. I could have copied the local one but this would effectively prevent Docker layer caching every time I modify it.
*   Avoid installing development dependencies with `poetry install --without dev` , as you won’t need linters and tests suites in your production environment.

FROM python:3.11-busterRUN pip install poetry==1.4.2

WORKDIR /app

COPY pyproject.toml poetry.lock ./  
COPY annapurna ./annapurna  
RUN touch README.md

RUN poetry install --without dev

ENTRYPOINT \["poetry", "run", "python", "-m", "annapurna.main"\]

This already brings us down from 1.1 GB to 959 MB. _It ain’t much, but it’s honest work_.

3\. Cleaning Poetry cache 🧹
----------------------------

By default, Poetry caches downloaded packages so that they can be re-used for future installation commands. We clearly don’t care about this in a Docker build (do we?) and as such we can remove this duplicate storage.

*   Poetry also supports a `--no-cache` option, so why am I not using it? We’ll see it later ;)
*   When removing the cache folder make sure this is done in the same `RUN` command. If it’s done in a separate `RUN` command the cache will still be part of the previous Docker layer (the one containing `poetry install` ), effectively rendering your optimization useless.

While doing this I’m also setting a few Poetry environment variables to further strengthen the determinism of my build. The most controversial one is `POETRY_VIRTUALENVS_CREATE=1`. What’s the point why would I want to create a virtual environment inside a Docker container? I honestly prefer this solution over who disables this flag, as it makes sure that my environment will be as isolated as possible and above all that my installation will not mess up with the system Python or, even worse, with Poetry itself.

FROM python:3.11-busterRUN pip install poetry==1.4.2

ENV POETRY\_NO\_INTERACTION=1 \\  
    POETRY\_VIRTUALENVS\_IN\_PROJECT=1 \\  
    POETRY\_VIRTUALENVS\_CREATE=1 \\  
    POETRY\_CACHE\_DIR=/tmp/poetry\_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./  
COPY annapurna ./annapurna  
RUN touch README.md

RUN poetry install --without dev && rm -rf $POETRY\_CACHE\_DIR

ENTRYPOINT \["poetry", "run", "python", "-m", "annapurna.main"\]

4\. Installing dependencies before copying code 👏
--------------------------------------------------

So far so good, but our Docker build still suffers from a very painful point: every time we modify our code we’ll have to re-install our dependencies! That’s because we `COPY` our code (which is needed by Poetry to install the project) before the `RUN poetry install` instruction. Because of how Docker layer caching works, every time the `COPY` layer is invalidated we’ll also rebuild the successive ones. As your project grows this can get very tedious and result in very long builds even if you are just changing a single line of code.

The solution here is to provide Poetry with the minimal information needed to build the virtual environment and only _later_ `COPY` our codebase. We can achieve this with the `--no-root` option, which instructs Poetry to avoid installing the current project into the virtual environment.

FROM python:3.11-busterRUN pip install poetry==1.4.2

ENV POETRY\_NO\_INTERACTION=1 \\  
    POETRY\_VIRTUALENVS\_IN\_PROJECT=1 \\  
    POETRY\_VIRTUALENVS\_CREATE=1 \\  
    POETRY\_CACHE\_DIR=/tmp/poetry\_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./  
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $POETRY\_CACHE\_DIR

COPY annapurna ./annapurna

RUN poetry install --without dev

ENTRYPOINT \["poetry", "run", "python", "-m", "annapurna.main"\]

You can now try to modify the application code, and you’ll see that just the last 3 layers will be re-computed. Builds just got crazy fast! 🚀

*   The additional `RUN poetry install --without dev` instruction is needed to install your project in the virtual environment. This can be useful for example for installing any custom [script](https://python-poetry.org/docs/pyproject/#scripts). Depending on your project you may not even need this step. Anyways, this layer execution will be super fast since the project dependencies have already been installed.

5\. Using Docker multi-stage builds 🏃‍♀
----------------------------------------

Up to now builds are fast, but we still end up with big Docker images. We can win this fight by calling [multi-stage builds](https://docs.docker.com/build/building/multi-stage/) into the game. The optimization is achieved by using the right base image for the right job:

*   Python `buster`is a big image that comes with development dependencies, and we will use it to _install_ a virtual environment.
*   Python `slim-buster`is a smaller image that comes with the minimal dependencies to just run Python, and we will use it to _run_ our application.

Thanks to multi-stage builds we can pass information from one stage to the other, in particular the virtual environment being built. Note how:

*   Poetry isn’t even installed in the runtime stage. Poetry is in fact an unnecessary dependency for running your Python application once your virtual environment is built. We just need to play with environment variables (such as the `VIRTUAL_ENV` variable) to let Python recognize the right virtual environment.
*   For simplicity I removed the second installation step (`RUN poetry install --without dev` ) as I don’t need it for my toy project, although one could still add it in the runtime image in a single instruction: `RUN pip install poetry && poetry install --without dev && pip uninstall poetry` .

Once Dockerfiles get more complex I also suggest using [Buildkit](https://docs.docker.com/build/buildkit/), the new build backend plugged into the Docker CLI. If you are looking for fast and secure builds, that’s the tool to use.

DOCKER\_BUILDKIT=1 docker build --target=runtime .

\# The builder image, used to build the virtual environment  
FROM python:3.11-buster as builderRUN pip install poetry==1.4.2

ENV POETRY\_NO\_INTERACTION=1 \\  
    POETRY\_VIRTUALENVS\_IN\_PROJECT=1 \\  
    POETRY\_VIRTUALENVS\_CREATE=1 \\  
    POETRY\_CACHE\_DIR=/tmp/poetry\_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./  
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $POETRY\_CACHE\_DIR

\# The runtime image, used to just run the code provided its virtual environment  
FROM python:3.11-slim-buster as runtime

ENV VIRTUAL\_ENV=/app/.venv \\  
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL\_ENV} ${VIRTUAL\_ENV}

COPY annapurna ./annapurna

ENTRYPOINT \["python", "-m", "annapurna.main"\]

The result? Our runtime image just got 6x smaller! **Six times**! From \> 1.1 GB to 170 MB.

6\. Buildkit Cache Mounts ⛰
---------------------------

We already got a small Docker image and fast builds when code changes, what could we get more? Well… we can also get fast builds when dependencies change 😎

This final trick is not known to many as it’s rather newer compared to the other features I presented. It leverages [Buildkit cache mounts](https://docs.docker.com/build/cache/#keep-layers-small), which basically instruct Buildkit to mount and manage a folder for caching reasons. The interesting thing is that such cache will persist across builds!

By plugging this feature with Poetry cache (now you understand why I _did_ want to keep caching?) we basically get a dependency cache that is re-used every time we build our project. The result we obtain is a fast dependency build phase when building the same image multiple times on the same environment.

Note how the Poetry cache is not cleared after installation, as this would prevent to store and re-use the cache across builds. This is fine, as Buildkit will not persist the managed cache in the built image (plus, it’s not even our runtime image).

FROM python:3.11-buster as builderRUN pip install poetry==1.4.2

ENV POETRY\_NO\_INTERACTION=1 \\  
    POETRY\_VIRTUALENVS\_IN\_PROJECT=1 \\  
    POETRY\_VIRTUALENVS\_CREATE=1 \\  
    POETRY\_CACHE\_DIR=/tmp/poetry\_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./  
RUN touch README.md

RUN --mount=type=cache,target=$POETRY\_CACHE\_DIR poetry install --without dev --no-root

FROM python:3.11-slim-buster as runtime

ENV VIRTUAL\_ENV=/app/.venv \\  
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL\_ENV} ${VIRTUAL\_ENV}

COPY annapurna ./annapurna

ENTRYPOINT \["python", "-m", "annapurna.main"\]

The con of this optimization? Cache mounts are not very CI friendly at the moment, as Buildkit doesn’t allow you controlling the storage location of the cache. It’s unsuprising that this is the [most voted open GitHub issue](https://github.com/moby/buildkit/issues/1512) on the Buildkit repo 😄

Summary
-------

We saw how we can bring a simple but awful Dockerfile that produces \>1 GB images in minutes to an optimized version that produces images of a couple hundred MBs in a few seconds. All the optimizations mainly leverage some Docker build mantras:

*   Keep layers small, minimizing the amount of stuff you copy and install in it
*   Exploit Docker layer caching and reduce cache misses as much as possible
*   Slow-changing things (project dependencies) must be built before fast-changing things (application code)
*   Use Docker multi-stage builds to make your runtime image as slim as possible

This is how you can put them in practice in Python projects managed by Poetry, but the same principles can be applied to other dependency managers (such as [PDM](https://pdm.fming.dev/latest/)) and other languages.

I hope you’ll shed some tears of joy watching your builds become fast and small, and if you know some additional Docker tricks please leave them in the comments! 👋

## Metadata

```json
{
  "title": "Blazing fast Python Docker builds with Poetry 🏃 - Riccardo Albertazzi - Medium",
  "description": "Building Docker images for your project typically involves installing its dependencies in a reproducible and deterministic way. In the Python community Poetry is one of the most affirmed tools to…",
  "url": "https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0",
  "content": "How we can turn slow and tedious Docker builds into seamless operations\n-----------------------------------------------------------------------\n\n[![Image 9: Riccardo Albertazzi](https://miro.medium.com/v2/resize:fill:88:88/1*e_3fOd_QVRZzWzJKXqZydw.jpeg)](https://medium.com/@albertazzir?source=post_page---byline--a78a66f5aed0--------------------------------)\n\n![Image 10](https://miro.medium.com/v2/resize:fit:700/1*XWWuq095-KpaGUaWgH9u5g.jpeg)\n\nA view of Annapurna from its south face. Legend says only people who know how to optimize Docker builds can reach the top.\n\nBuilding Docker images for your project typically involves installing its dependencies in a reproducible and deterministic way. In the Python community [Poetry](https://python-poetry.org/) is one of the most affirmed tools to achieve that. However, a non-optimal usage of Poetry in your Docker builds can result in poor performance and long builds, which in the end hinder developer productivity.\n\nThis article assumes that you are already familiar with both Poetry and Docker — in particular how [Docker layer caching](https://docs.docker.com/build/cache/) works— and that you are looking for a way to optimize your builds. I structured the article from naive to more optimized solutions to let the reader understand the impact of each optimization. Enough about introduction, let’s see some Dockerfiles! 💪\n\n0\\. Project structure\n---------------------\n\nLet’s use a toy project to reason about. I randomly named it `annapurna` as one the best mountains I’ve ever seen ⛰ A minimal Poetry project would contain the `pyproject.toml` , the associated `poetry.lock`, your code and a `Dockerfile` .\n\n.  \n├── Dockerfile  \n├── README.md  \n├── annapurna  \n│   ├── \\_\\_init\\_\\_.py  \n│   └── main.py  \n├── poetry.lock  \n└── pyproject.toml\n\nFor simplicity I just installed the famous `fastapi` web server through `poetry add fastapi` and a couple linters that I typically use in my projects:\n\n\\[tool.poetry\\]  \nname = \"annapurna\"  \nversion = \"1.0.0\"  \ndescription = \"\"  \nauthors = \\[\"Riccardo Albertazzi <my@email.com\\>\"\\]  \nreadme = \"README.md\"\\[tool.poetry.dependencies\\]  \npython = \"^3.11\"\n\nfastapi = \"^0.95.1\"\n\n\\[tool.poetry.group.dev.dependencies\\]  \nblack = \"^23.3.0\"  \nmypy = \"^1.2.0\"  \nruff = \"^0.0.263\"\n\n\\[build-system\\]  \nrequires = \\[\"poetry-core\"\\]  \nbuild-backend = \"poetry.core.masonry.api\"\n\n1\\. The naive approach 😐\n-------------------------\n\nWhat our Docker build needs to do is having Python and Poetry installed, getting our code, installing the dependencies and setting the project’s entrypoint. This is exactly what we are doing in here:\n\nFROM python:3.11-busterRUN pip install poetry\n\nCOPY . .\n\nRUN poetry install\n\nENTRYPOINT \\[\"poetry\", \"run\", \"python\", \"-m\", \"annapurna.main\"\\]\n\nThis simple Dockerfile does the job, and with a simple `docker build . `you’ll already get a working image. This is in fact the typical Dockerfile you see in tutorials and open-source projects, as it’s pretty easy to understand. But as your project grows it will lead you under a path of tedious builds and huge Docker images — my resulting Docker image is in fact 1.1GB! All the optimizations we’ll see go in the direction of exploiting caching and reducing the final image size.\n\n2\\. Warming up 🚶\n-----------------\n\nLet’s start with a few improvements to warm up:\n\n*   Pin the `poetry`version. I suggest doing it as Poetry can contain breaking changes from one minor version to other, and you don’t want your builds to suddenly break when a new version is released. You should clearly pin it to the same version you are using locally.\n*   Just `COPY` the data that you need, and nothing else. This will avoid for instance a useless copy of my local virtual environment (located at `.venv` ). Poetry will complain if a `README.md` is not found (I don’t really share this choice) and as such I create an empty one. I could have copied the local one but this would effectively prevent Docker layer caching every time I modify it.\n*   Avoid installing development dependencies with `poetry install --without dev` , as you won’t need linters and tests suites in your production environment.\n\nFROM python:3.11-busterRUN pip install poetry==1.4.2\n\nWORKDIR /app\n\nCOPY pyproject.toml poetry.lock ./  \nCOPY annapurna ./annapurna  \nRUN touch README.md\n\nRUN poetry install --without dev\n\nENTRYPOINT \\[\"poetry\", \"run\", \"python\", \"-m\", \"annapurna.main\"\\]\n\nThis already brings us down from 1.1 GB to 959 MB. _It ain’t much, but it’s honest work_.\n\n3\\. Cleaning Poetry cache 🧹\n----------------------------\n\nBy default, Poetry caches downloaded packages so that they can be re-used for future installation commands. We clearly don’t care about this in a Docker build (do we?) and as such we can remove this duplicate storage.\n\n*   Poetry also supports a `--no-cache` option, so why am I not using it? We’ll see it later ;)\n*   When removing the cache folder make sure this is done in the same `RUN` command. If it’s done in a separate `RUN` command the cache will still be part of the previous Docker layer (the one containing `poetry install` ), effectively rendering your optimization useless.\n\nWhile doing this I’m also setting a few Poetry environment variables to further strengthen the determinism of my build. The most controversial one is `POETRY_VIRTUALENVS_CREATE=1`. What’s the point why would I want to create a virtual environment inside a Docker container? I honestly prefer this solution over who disables this flag, as it makes sure that my environment will be as isolated as possible and above all that my installation will not mess up with the system Python or, even worse, with Poetry itself.\n\nFROM python:3.11-busterRUN pip install poetry==1.4.2\n\nENV POETRY\\_NO\\_INTERACTION=1 \\\\  \n    POETRY\\_VIRTUALENVS\\_IN\\_PROJECT=1 \\\\  \n    POETRY\\_VIRTUALENVS\\_CREATE=1 \\\\  \n    POETRY\\_CACHE\\_DIR=/tmp/poetry\\_cache\n\nWORKDIR /app\n\nCOPY pyproject.toml poetry.lock ./  \nCOPY annapurna ./annapurna  \nRUN touch README.md\n\nRUN poetry install --without dev && rm -rf $POETRY\\_CACHE\\_DIR\n\nENTRYPOINT \\[\"poetry\", \"run\", \"python\", \"-m\", \"annapurna.main\"\\]\n\n4\\. Installing dependencies before copying code 👏\n--------------------------------------------------\n\nSo far so good, but our Docker build still suffers from a very painful point: every time we modify our code we’ll have to re-install our dependencies! That’s because we `COPY` our code (which is needed by Poetry to install the project) before the `RUN poetry install` instruction. Because of how Docker layer caching works, every time the `COPY` layer is invalidated we’ll also rebuild the successive ones. As your project grows this can get very tedious and result in very long builds even if you are just changing a single line of code.\n\nThe solution here is to provide Poetry with the minimal information needed to build the virtual environment and only _later_ `COPY` our codebase. We can achieve this with the `--no-root` option, which instructs Poetry to avoid installing the current project into the virtual environment.\n\nFROM python:3.11-busterRUN pip install poetry==1.4.2\n\nENV POETRY\\_NO\\_INTERACTION=1 \\\\  \n    POETRY\\_VIRTUALENVS\\_IN\\_PROJECT=1 \\\\  \n    POETRY\\_VIRTUALENVS\\_CREATE=1 \\\\  \n    POETRY\\_CACHE\\_DIR=/tmp/poetry\\_cache\n\nWORKDIR /app\n\nCOPY pyproject.toml poetry.lock ./  \nRUN touch README.md\n\nRUN poetry install --without dev --no-root && rm -rf $POETRY\\_CACHE\\_DIR\n\nCOPY annapurna ./annapurna\n\nRUN poetry install --without dev\n\nENTRYPOINT \\[\"poetry\", \"run\", \"python\", \"-m\", \"annapurna.main\"\\]\n\nYou can now try to modify the application code, and you’ll see that just the last 3 layers will be re-computed. Builds just got crazy fast! 🚀\n\n*   The additional `RUN poetry install --without dev` instruction is needed to install your project in the virtual environment. This can be useful for example for installing any custom [script](https://python-poetry.org/docs/pyproject/#scripts). Depending on your project you may not even need this step. Anyways, this layer execution will be super fast since the project dependencies have already been installed.\n\n5\\. Using Docker multi-stage builds 🏃‍♀\n----------------------------------------\n\nUp to now builds are fast, but we still end up with big Docker images. We can win this fight by calling [multi-stage builds](https://docs.docker.com/build/building/multi-stage/) into the game. The optimization is achieved by using the right base image for the right job:\n\n*   Python `buster`is a big image that comes with development dependencies, and we will use it to _install_ a virtual environment.\n*   Python `slim-buster`is a smaller image that comes with the minimal dependencies to just run Python, and we will use it to _run_ our application.\n\nThanks to multi-stage builds we can pass information from one stage to the other, in particular the virtual environment being built. Note how:\n\n*   Poetry isn’t even installed in the runtime stage. Poetry is in fact an unnecessary dependency for running your Python application once your virtual environment is built. We just need to play with environment variables (such as the `VIRTUAL_ENV` variable) to let Python recognize the right virtual environment.\n*   For simplicity I removed the second installation step (`RUN poetry install --without dev` ) as I don’t need it for my toy project, although one could still add it in the runtime image in a single instruction: `RUN pip install poetry && poetry install --without dev && pip uninstall poetry` .\n\nOnce Dockerfiles get more complex I also suggest using [Buildkit](https://docs.docker.com/build/buildkit/), the new build backend plugged into the Docker CLI. If you are looking for fast and secure builds, that’s the tool to use.\n\nDOCKER\\_BUILDKIT=1 docker build --target=runtime .\n\n\\# The builder image, used to build the virtual environment  \nFROM python:3.11-buster as builderRUN pip install poetry==1.4.2\n\nENV POETRY\\_NO\\_INTERACTION=1 \\\\  \n    POETRY\\_VIRTUALENVS\\_IN\\_PROJECT=1 \\\\  \n    POETRY\\_VIRTUALENVS\\_CREATE=1 \\\\  \n    POETRY\\_CACHE\\_DIR=/tmp/poetry\\_cache\n\nWORKDIR /app\n\nCOPY pyproject.toml poetry.lock ./  \nRUN touch README.md\n\nRUN poetry install --without dev --no-root && rm -rf $POETRY\\_CACHE\\_DIR\n\n\\# The runtime image, used to just run the code provided its virtual environment  \nFROM python:3.11-slim-buster as runtime\n\nENV VIRTUAL\\_ENV=/app/.venv \\\\  \n    PATH=\"/app/.venv/bin:$PATH\"\n\nCOPY --from=builder ${VIRTUAL\\_ENV} ${VIRTUAL\\_ENV}\n\nCOPY annapurna ./annapurna\n\nENTRYPOINT \\[\"python\", \"-m\", \"annapurna.main\"\\]\n\nThe result? Our runtime image just got 6x smaller! **Six times**! From \\> 1.1 GB to 170 MB.\n\n6\\. Buildkit Cache Mounts ⛰\n---------------------------\n\nWe already got a small Docker image and fast builds when code changes, what could we get more? Well… we can also get fast builds when dependencies change 😎\n\nThis final trick is not known to many as it’s rather newer compared to the other features I presented. It leverages [Buildkit cache mounts](https://docs.docker.com/build/cache/#keep-layers-small), which basically instruct Buildkit to mount and manage a folder for caching reasons. The interesting thing is that such cache will persist across builds!\n\nBy plugging this feature with Poetry cache (now you understand why I _did_ want to keep caching?) we basically get a dependency cache that is re-used every time we build our project. The result we obtain is a fast dependency build phase when building the same image multiple times on the same environment.\n\nNote how the Poetry cache is not cleared after installation, as this would prevent to store and re-use the cache across builds. This is fine, as Buildkit will not persist the managed cache in the built image (plus, it’s not even our runtime image).\n\nFROM python:3.11-buster as builderRUN pip install poetry==1.4.2\n\nENV POETRY\\_NO\\_INTERACTION=1 \\\\  \n    POETRY\\_VIRTUALENVS\\_IN\\_PROJECT=1 \\\\  \n    POETRY\\_VIRTUALENVS\\_CREATE=1 \\\\  \n    POETRY\\_CACHE\\_DIR=/tmp/poetry\\_cache\n\nWORKDIR /app\n\nCOPY pyproject.toml poetry.lock ./  \nRUN touch README.md\n\nRUN --mount=type=cache,target=$POETRY\\_CACHE\\_DIR poetry install --without dev --no-root\n\nFROM python:3.11-slim-buster as runtime\n\nENV VIRTUAL\\_ENV=/app/.venv \\\\  \n    PATH=\"/app/.venv/bin:$PATH\"\n\nCOPY --from=builder ${VIRTUAL\\_ENV} ${VIRTUAL\\_ENV}\n\nCOPY annapurna ./annapurna\n\nENTRYPOINT \\[\"python\", \"-m\", \"annapurna.main\"\\]\n\nThe con of this optimization? Cache mounts are not very CI friendly at the moment, as Buildkit doesn’t allow you controlling the storage location of the cache. It’s unsuprising that this is the [most voted open GitHub issue](https://github.com/moby/buildkit/issues/1512) on the Buildkit repo 😄\n\nSummary\n-------\n\nWe saw how we can bring a simple but awful Dockerfile that produces \\>1 GB images in minutes to an optimized version that produces images of a couple hundred MBs in a few seconds. All the optimizations mainly leverage some Docker build mantras:\n\n*   Keep layers small, minimizing the amount of stuff you copy and install in it\n*   Exploit Docker layer caching and reduce cache misses as much as possible\n*   Slow-changing things (project dependencies) must be built before fast-changing things (application code)\n*   Use Docker multi-stage builds to make your runtime image as slim as possible\n\nThis is how you can put them in practice in Python projects managed by Poetry, but the same principles can be applied to other dependency managers (such as [PDM](https://pdm.fming.dev/latest/)) and other languages.\n\nI hope you’ll shed some tears of joy watching your builds become fast and small, and if you know some additional Docker tricks please leave them in the comments! 👋",
  "publishedTime": "2023-04-28T18:51:32.538Z",
  "usage": {
    "tokens": 3323
  }
}
```
