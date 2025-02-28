---
title: GitHub - fedden/poker_ai: 🤖 An Open Source Texas Hold'em AI
description: 🤖 An Open Source Texas Hold'em AI. Contribute to fedden/poker_ai development by creating an account on GitHub.
url: https://github.com/fedden/poker_ai
timestamp: 2025-01-20T15:31:38.758Z
domain: github.com
path: fedden_poker_ai
---

# GitHub - fedden/poker_ai: 🤖 An Open Source Texas Hold'em AI


🤖 An Open Source Texas Hold'em AI. Contribute to fedden/poker_ai development by creating an account on GitHub.


## Content

| code-thing | status |
| --- | --- |
| master | [![Image 26: Build Status](https://camo.githubusercontent.com/1aab2c0e0eb1cfb751c5b6941b6570bffc1fc5b685f247008eac68e5556868b4/68747470733a2f2f7472617669732d63692e6f72672f66656464656e2f706f6b65725f61692e7376673f6272616e63683d6d6173746572)](https://travis-ci.org/fedden/poker_ai) |
| develop | [![Image 27: Build Status](https://camo.githubusercontent.com/0a9fb074d8cc44e3196c0af2c6c76be4d5e364fae552ee7c816d8a0c10abc648/68747470733a2f2f7472617669732d63692e6f72672f66656464656e2f706f6b65725f61692e7376673f6272616e63683d646576656c6f70)](https://travis-ci.org/fedden/poker_ai) |
| maintainability | [![Image 28: Maintainability](https://camo.githubusercontent.com/9000f7351d9478175bc4e62920219d6a8aaf3bb69309cdc0674d14bbbb8f8790/68747470733a2f2f6170692e636f6465636c696d6174652e636f6d2f76312f6261646765732f63356135353664616530393762383039623464392f6d61696e7461696e6162696c697479)](https://codeclimate.com/github/fedden/poker_ai/maintainability) |
| coverage | [![Image 29: Test Coverage](https://camo.githubusercontent.com/f00890caccc5e5a54b356435c815b7252e519e2c59b33f7246c4c66ebc85f74f/68747470733a2f2f6170692e636f6465636c696d6174652e636f6d2f76312f6261646765732f63356135353664616530393762383039623464392f746573745f636f766572616765)](https://codeclimate.com/github/fedden/poker_ai/test_coverage) |
| license | [![Image 30: License: GPL v3](https://camo.githubusercontent.com/8a398fc9fbf479a323d2d91b9fcb6fb9c6b4d08e96dbb544488ccbed312115fc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d47504c76332d626c75652e737667)](https://www.gnu.org/licenses/gpl-3.0) |

[Read the documentation](https://github.com/fedden/poker_ai/blob/develop)

🤖 Poker AI
-----------

[](https://github.com/fedden/poker_ai?screenshot=true#-poker-ai)

This repository will contain a best effort open source implementation of a poker AI using the ideas of Counterfactual Regret.

[![Image 31](https://github.com/fedden/poker_ai/raw/develop/assets/poker.jpg)](https://github.com/fedden/poker_ai/blob/develop/assets/poker.jpg)

_Made with love from the developers [Leon](https://www.leonfedden.co.uk/) and [Colin](http://www.colinmanko.com/)._

_A special thank you to [worldveil](https://github.com/worldveil) for originally writing [this awesome hand evaluator python2 module](https://github.com/worldveil/deuces), which was ported to python3 and [maintained here](https://github.com/fedden/poker_ai/tree/master/poker_ai/poker/evaluation)._

Join the Community
------------------

[](https://github.com/fedden/poker_ai?screenshot=true#join-the-community)

[https://thepoker.ai](https://thepoker.ai/)

Prerequisites
-------------

[](https://github.com/fedden/poker_ai?screenshot=true#prerequisites)

This repository assumes Python 3.7 or newer is used.

Installing
----------

[](https://github.com/fedden/poker_ai?screenshot=true#installing)

Either install from pypi:

Or if you want to dev on our code, install the Python package from source by cloning this repo and `pip -e` installing it:

git clone https://github.com/fedden/poker\_ai.git # Though really we should use ssh here!
cd /path/to/poker\_ai
pip install .

Command Line Interface (CLI)
----------------------------

[](https://github.com/fedden/poker_ai?screenshot=true#command-line-interface-cli)

We have a CLI that will be installed when you pip install the package. To get help on any option, just add the `--help` flag when invoking the CLI.

How to get a list of commands that can be run:

You will need to produce some lookup tables that cluster the various information sets. Here is more information on that:

How to get information on training an agent:

poker\_ai train start --help

How to get information on resuming training:

poker\_ai train resume --help

Once you have an agent, and want to play against it, you can do the following:

Build a Bot
-----------

[](https://github.com/fedden/poker_ai?screenshot=true#build-a-bot)

### Cluster Hero Information

[](https://github.com/fedden/poker_ai?screenshot=true#cluster-hero-information)

In poker, the number of card combinations for one player on the river can exceed 56 billion combinations. In order to make this information tractable, we must group together strategically similar situations. We do this with two types of compression: lossy and lossless compression. Currently we only support a 20 card deck without modification.

You'll save the combinations of public information in a file called card\_info\_lut.joblib located in your project directory.

### Train your bot

[](https://github.com/fedden/poker_ai?screenshot=true#train-your-bot)

We use MCCFR to learn strategies. The MCCFR algorithm uses iterative self-play to adjust strategy based on regret.

You'll create a folder in your project directory with the learned strategy and configuration files, in case you need to resume later.

### Play your bot

[](https://github.com/fedden/poker_ai?screenshot=true#play-your-bot)

Finally, you can play your bot with the following command:

You'll create a results.yaml file in ~/.poker/. So be sure to see how you stack up against your bot.

Running tests
-------------

[](https://github.com/fedden/poker_ai?screenshot=true#running-tests)

We are working hard on testing our components, but contributions here are always welcome. You can run the tests by cloning the code, changing directory to this repositories root directory (i.e `poker_ai/`) and call the python test library `pytest`:

cd /path/to/poker\_ai
pip install pytest
pytest

See below on how to run the tests from the docker image.

Building the docker image
-------------------------

[](https://github.com/fedden/poker_ai?screenshot=true#building-the-docker-image)

We use a custom docker image for our testing suite.

You'll need to have computed the pickled card information lookup tables first (the cluster command for poker\_ai). We build the images like below, in this case the luts are in './research/blueprint\_algo'. First we build the parent image, with all of the dependancies.

docker build --build-arg LUT\_DIR=research/blueprint\_algo -f ParentDockerfile -t pokerai .

Then we build the test image.

docker build -t pokeraitest .

We then can run the tests with:

docker run -it pokeraitest pytest 

This is just a note for the developers, but we can push the parent image to the registry with the following (please ensure the version tag that comes after the colon is correct). We want to do this because we need various dependancies for the remote tests, and travis builds the `pokeraitest` image with the current git commit that has just been pushed.

docker tag pokerai pokerai/pokerai:1.0.0rc1
docker push pokerai/pokerai:1.0.0rc1

Building documentation
----------------------

[](https://github.com/fedden/poker_ai?screenshot=true#building-documentation)

Documentation is hosted, but you can build it yourself if you wish:

# Build the documentation.
cd /path/to/poker\_ai/docs
make html
cd ./\_build/html 
# Run a webserver and navigate to localhost and the port (usually 8000) in your browser.
python -m http.server 

Repository Structure
--------------------

[](https://github.com/fedden/poker_ai?screenshot=true#repository-structure)

Below is a rough structure of the codebase.

```
├── applications   # Larger applications like the state visualiser sever.
├── paper          # Main source of info and documentation :)
├── poker_ai       # Main Python library.
│   ├── ai         # Stub functions for ai algorithms.
│   ├── games      # Implementations of poker games as node based objects that
│   │              # can be traversed in a depth-first recursive manner.
│   ├── poker      # WIP general code for managing a hand of poker.
│   ├── terminal   # Code to play against the AI from your console.
│   └── utils      # Utility code like seed setting.
├── research       # A directory for research/development scripts 
│                  # to help formulate understanding and ideas.
└── test           # Python tests.
    ├── functional # Functional tests that test multiple components 
    │              # together.
    └── unit       # Individual tests for functions and objects.
```

Code Examples
-------------

[](https://github.com/fedden/poker_ai?screenshot=true#code-examples)

Here are some assorted examples of things that are being built in this repo.

### State based poker traversal

[](https://github.com/fedden/poker_ai?screenshot=true#state-based-poker-traversal)

To perform MCCFR, the core algorithm of poker\_ai, we need a class that encodes all of the poker rules, that we can apply an action to which then creates a new game state.

pot \= Pot()
players \= \[
    ShortDeckPokerPlayer(player\_i\=player\_i, initial\_chips\=10000, pot\=pot)
    for player\_i in range(n\_players)
\]
state \= ShortDeckPokerState(players\=players)
for action in state.legal\_actions:
    new\_state: ShortDeckPokerState \= state.apply\_action(action)

### Playing against AI in your terminal

[](https://github.com/fedden/poker_ai?screenshot=true#playing-against-ai-in-your-terminal)

We also have some code to play a round of poker against the AI agents, inside your terminal.

The characters are a little broken when captured in `asciinema`, but you'll get the idea by watching this video below. Results should be better in your actual terminal!

[![Image 32](https://camo.githubusercontent.com/76b90f9a6e8e4526ba95477c77ec367dc69bdd45e301be51adba8bb2506c5406/68747470733a2f2f61736369696e656d612e6f72672f612f3333313233342e737667)](https://asciinema.org/a/331234)

To invoke the code, either call the \`run\_terminal\_app\` method directly from the \`poker\_ai.terminal.runner\` module, or call from python like so:

cd /path/to/poker\_ai/dir
python -m poker\_ai.terminal.runner       \\
  --agent offline                        \\ 
  --pickle\_dir ./research/blueprint\_algo \\
  --strategy\_path ./research/blueprint\_algo/offline\_strategy\_285800.gz 

### Web visualisation code

[](https://github.com/fedden/poker_ai?screenshot=true#web-visualisation-code)

We are also working on code to visualise a given instance of the `ShortDeckPokerState`, which looks like this:

[![Image 33](https://github.com/fedden/poker_ai-poker-AI/raw/develop/assets/visualisation.png)](https://github.com/fedden/poker_ai-poker-AI/blob/develop/assets/visualisation.png)

It is so we can visualise the AI as it plays, and also debug particular situations visually. The idea as it stands, is a live web-visualisation server like TensorBoard, so you'll just push your current poker game state, and this will be reflected in the visualisations, so you can see what the agents are doing.

[_The frontend code is based on this codepen._](https://codepen.io/Rovak/pen/ExYeQar)

Here is an example of how you could plot the poker game state:

from plot import PokerPlot
from poker\_ai.games.short\_deck.player import ShortDeckPokerPlayer
from poker\_ai.games.short\_deck.state import ShortDeckPokerState
from poker\_ai.poker.pot import Pot

def get\_state() \-\> ShortDeckPokerState:
    """Gets a state to visualise"""
    n\_players \= 6
    pot \= Pot()
    players \= \[
        ShortDeckPokerPlayer(player\_i\=player\_i, initial\_chips\=10000, pot\=pot)
        for player\_i in range(n\_players)
    \]
    return ShortDeckPokerState(
        players\=players, 
        pickle\_dir\="../../research/blueprint\_algo/"
    )

pp: PokerPlot \= PokerPlot()
\# If you visit http://localhost:5000/ now you will see an empty table.

\# ... later on in the code, as proxy for some code that obtains a new state ...
\# Obtain a new state.
state: ShortDeckPokerState \= get\_state()
\# Update the state to be plotted, this is sent via websockets to the frontend.
pp.update\_state(state)
\# http://localhost:5000/ will now display a table with 6 players.

### Playing a game of poker

[](https://github.com/fedden/poker_ai?screenshot=true#playing-a-game-of-poker)

There are two parts to this repository, the code to manage a game of poker, and the code to train an AI algorithm to play the game of poker. A low level thing to first to is to implement a poker engine class that can manage a game of poker.

The reason the poker engine is implemented is because it is useful to have a well-integrated poker environment available during the development of the AI algorithm, incase there are tweaks that must be made to accomadate things like the history of state or the replay of a scenario during Monte Carlo Counterfactual Regret Minimisation.

The following code is how one might program a round of poker that is deterministic using the engine. This engine is now the first pass that will be used support self play.

from poker\_ai import utils
from poker\_ai.ai.dummy import RandomPlayer
from poker\_ai.poker.table import PokerTable
from poker\_ai.poker.engine import PokerEngine
from poker\_ai.poker.pot import Pot

\# Seed so things are deterministic.
utils.random.seed(42)

\# Some settings for the amount of chips.
initial\_chips\_amount \= 10000
small\_blind\_amount \= 50
big\_blind\_amount \= 100

\# Create the pot.
pot \= Pot()
\# Instanciate six players that will make random moves, make sure 
\# they can reference the pot so they can add chips to it.
players \= \[
    RandomPlayer(
        name\=f'player {player\_i}',
        initial\_chips\=initial\_chips\_amount,
        pot\=pot)
    for player\_i in range(6)
\]
\# Create the table with the players on it.
table \= PokerTable(players\=players, pot\=pot)
\# Create the engine that will manage the poker game lifecycle.
engine \= PokerEngine(
    table\=table,
    small\_blind\=small\_blind\_amount,
    big\_blind\=big\_blind\_amount)
\# Play a round of Texas Hold'em Poker!
engine.play\_one\_round()

Roadmap
-------

[](https://github.com/fedden/poker_ai?screenshot=true#roadmap)

The following todo will change dynamically as my understanding of the algorithms and the poker\_ai project evolves.

At first, the goal is to prototype in Python as iteration will be much easier and quicker. Once there is a working prototype, write in a systems level language like C++ and optimise for performance.

### 1\. Game engine iteration.

[](https://github.com/fedden/poker_ai?screenshot=true#1-game-engine-iteration)

_Implement a multiplayer working heads up no limit poker game engine to support the self-play._

*   Lay down the foundation of game objects (player, card etc).
*   Add poker hand evaluation code to the engine.
*   Support a player going all in during betting.
*   Support a player going all in during payouts.
*   Lots of testing for various scenarios to ensure logic is working as expected.

### 2\. AI iteration.

[](https://github.com/fedden/poker_ai?screenshot=true#2-ai-iteration)

_Iterate on the AI algorithms and the integration into the poker engine._

*   Integrate the AI strategy to support self-play in the multiplayer poker game engine.
*   In the game-engine, allow the replay of any round the current hand to support MCCFR.
*   Implement the creation of the blueprint strategy using Monte Carlo CFR miminisation.
*   Add the real-time search for better strategies during the game.

### 3\. Game engine iteration.

[](https://github.com/fedden/poker_ai?screenshot=true#3-game-engine-iteration)

_Strengthen the game engine with more tests and allow users to see live visualisation of game state._

*   Start work on a visualisation server to allow a game state to be displayed.
*   Triple check that the rules are implemented in the poker engine as described in the supplimentary material.
*   Work through the coverage, adding more tests, can never have enough.

[![Image 34](https://github.com/fedden/poker_ai/raw/develop/assets/regret.jpeg)](https://github.com/fedden/poker_ai/blob/develop/assets/regret.jpeg)

Contributing
------------

[](https://github.com/fedden/poker_ai?screenshot=true#contributing)

This is an open effort and help, criticisms and ideas are all welcome.

First of all, please check out the [CONTRIBUTING](https://github.com/fedden/poker_ai/blob/develop/CONTRIBUTING.md) guide.

Feel free to start a discussion on the github issues or to reach out to me at leonfedden at gmail dot com.

License
-------

[](https://github.com/fedden/poker_ai?screenshot=true#license)

The code is provided under the copy-left GPL licence. If you need it under a more permissive license then please contact me at leonfedden at gmail dot com.

Stargazers over time
--------------------

[](https://github.com/fedden/poker_ai?screenshot=true#stargazers-over-time)

We appreciate you getting this far in the README file! If you like what we are doing, please give us a star and share with your friends!

[![Image 35: Stargazers over time](https://camo.githubusercontent.com/c26994023d46a1351ba47fa25bfd313c6a2b5aa625b7fa55a319e879e8ad9cbd/68747470733a2f2f7374617263686172742e63632f66656464656e2f706f6b65725f61692e737667)](https://starchart.cc/fedden/poker_ai)

## Metadata

```json
{
  "title": "GitHub - fedden/poker_ai: 🤖 An Open Source Texas Hold'em AI",
  "description": "🤖 An Open Source Texas Hold'em AI. Contribute to fedden/poker_ai development by creating an account on GitHub.",
  "url": "https://github.com/fedden/poker_ai?screenshot=true",
  "content": "| code-thing | status |\n| --- | --- |\n| master | [![Image 26: Build Status](https://camo.githubusercontent.com/1aab2c0e0eb1cfb751c5b6941b6570bffc1fc5b685f247008eac68e5556868b4/68747470733a2f2f7472617669732d63692e6f72672f66656464656e2f706f6b65725f61692e7376673f6272616e63683d6d6173746572)](https://travis-ci.org/fedden/poker_ai) |\n| develop | [![Image 27: Build Status](https://camo.githubusercontent.com/0a9fb074d8cc44e3196c0af2c6c76be4d5e364fae552ee7c816d8a0c10abc648/68747470733a2f2f7472617669732d63692e6f72672f66656464656e2f706f6b65725f61692e7376673f6272616e63683d646576656c6f70)](https://travis-ci.org/fedden/poker_ai) |\n| maintainability | [![Image 28: Maintainability](https://camo.githubusercontent.com/9000f7351d9478175bc4e62920219d6a8aaf3bb69309cdc0674d14bbbb8f8790/68747470733a2f2f6170692e636f6465636c696d6174652e636f6d2f76312f6261646765732f63356135353664616530393762383039623464392f6d61696e7461696e6162696c697479)](https://codeclimate.com/github/fedden/poker_ai/maintainability) |\n| coverage | [![Image 29: Test Coverage](https://camo.githubusercontent.com/f00890caccc5e5a54b356435c815b7252e519e2c59b33f7246c4c66ebc85f74f/68747470733a2f2f6170692e636f6465636c696d6174652e636f6d2f76312f6261646765732f63356135353664616530393762383039623464392f746573745f636f766572616765)](https://codeclimate.com/github/fedden/poker_ai/test_coverage) |\n| license | [![Image 30: License: GPL v3](https://camo.githubusercontent.com/8a398fc9fbf479a323d2d91b9fcb6fb9c6b4d08e96dbb544488ccbed312115fc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d47504c76332d626c75652e737667)](https://www.gnu.org/licenses/gpl-3.0) |\n\n[Read the documentation](https://github.com/fedden/poker_ai/blob/develop)\n\n🤖 Poker AI\n-----------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#-poker-ai)\n\nThis repository will contain a best effort open source implementation of a poker AI using the ideas of Counterfactual Regret.\n\n[![Image 31](https://github.com/fedden/poker_ai/raw/develop/assets/poker.jpg)](https://github.com/fedden/poker_ai/blob/develop/assets/poker.jpg)\n\n_Made with love from the developers [Leon](https://www.leonfedden.co.uk/) and [Colin](http://www.colinmanko.com/)._\n\n_A special thank you to [worldveil](https://github.com/worldveil) for originally writing [this awesome hand evaluator python2 module](https://github.com/worldveil/deuces), which was ported to python3 and [maintained here](https://github.com/fedden/poker_ai/tree/master/poker_ai/poker/evaluation)._\n\nJoin the Community\n------------------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#join-the-community)\n\n[https://thepoker.ai](https://thepoker.ai/)\n\nPrerequisites\n-------------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#prerequisites)\n\nThis repository assumes Python 3.7 or newer is used.\n\nInstalling\n----------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#installing)\n\nEither install from pypi:\n\nOr if you want to dev on our code, install the Python package from source by cloning this repo and `pip -e` installing it:\n\ngit clone https://github.com/fedden/poker\\_ai.git # Though really we should use ssh here!\ncd /path/to/poker\\_ai\npip install .\n\nCommand Line Interface (CLI)\n----------------------------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#command-line-interface-cli)\n\nWe have a CLI that will be installed when you pip install the package. To get help on any option, just add the `--help` flag when invoking the CLI.\n\nHow to get a list of commands that can be run:\n\nYou will need to produce some lookup tables that cluster the various information sets. Here is more information on that:\n\nHow to get information on training an agent:\n\npoker\\_ai train start --help\n\nHow to get information on resuming training:\n\npoker\\_ai train resume --help\n\nOnce you have an agent, and want to play against it, you can do the following:\n\nBuild a Bot\n-----------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#build-a-bot)\n\n### Cluster Hero Information\n\n[](https://github.com/fedden/poker_ai?screenshot=true#cluster-hero-information)\n\nIn poker, the number of card combinations for one player on the river can exceed 56 billion combinations. In order to make this information tractable, we must group together strategically similar situations. We do this with two types of compression: lossy and lossless compression. Currently we only support a 20 card deck without modification.\n\nYou'll save the combinations of public information in a file called card\\_info\\_lut.joblib located in your project directory.\n\n### Train your bot\n\n[](https://github.com/fedden/poker_ai?screenshot=true#train-your-bot)\n\nWe use MCCFR to learn strategies. The MCCFR algorithm uses iterative self-play to adjust strategy based on regret.\n\nYou'll create a folder in your project directory with the learned strategy and configuration files, in case you need to resume later.\n\n### Play your bot\n\n[](https://github.com/fedden/poker_ai?screenshot=true#play-your-bot)\n\nFinally, you can play your bot with the following command:\n\nYou'll create a results.yaml file in ~/.poker/. So be sure to see how you stack up against your bot.\n\nRunning tests\n-------------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#running-tests)\n\nWe are working hard on testing our components, but contributions here are always welcome. You can run the tests by cloning the code, changing directory to this repositories root directory (i.e `poker_ai/`) and call the python test library `pytest`:\n\ncd /path/to/poker\\_ai\npip install pytest\npytest\n\nSee below on how to run the tests from the docker image.\n\nBuilding the docker image\n-------------------------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#building-the-docker-image)\n\nWe use a custom docker image for our testing suite.\n\nYou'll need to have computed the pickled card information lookup tables first (the cluster command for poker\\_ai). We build the images like below, in this case the luts are in './research/blueprint\\_algo'. First we build the parent image, with all of the dependancies.\n\ndocker build --build-arg LUT\\_DIR=research/blueprint\\_algo -f ParentDockerfile -t pokerai .\n\nThen we build the test image.\n\ndocker build -t pokeraitest .\n\nWe then can run the tests with:\n\ndocker run -it pokeraitest pytest \n\nThis is just a note for the developers, but we can push the parent image to the registry with the following (please ensure the version tag that comes after the colon is correct). We want to do this because we need various dependancies for the remote tests, and travis builds the `pokeraitest` image with the current git commit that has just been pushed.\n\ndocker tag pokerai pokerai/pokerai:1.0.0rc1\ndocker push pokerai/pokerai:1.0.0rc1\n\nBuilding documentation\n----------------------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#building-documentation)\n\nDocumentation is hosted, but you can build it yourself if you wish:\n\n# Build the documentation.\ncd /path/to/poker\\_ai/docs\nmake html\ncd ./\\_build/html \n# Run a webserver and navigate to localhost and the port (usually 8000) in your browser.\npython -m http.server \n\nRepository Structure\n--------------------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#repository-structure)\n\nBelow is a rough structure of the codebase.\n\n```\n├── applications   # Larger applications like the state visualiser sever.\n├── paper          # Main source of info and documentation :)\n├── poker_ai       # Main Python library.\n│   ├── ai         # Stub functions for ai algorithms.\n│   ├── games      # Implementations of poker games as node based objects that\n│   │              # can be traversed in a depth-first recursive manner.\n│   ├── poker      # WIP general code for managing a hand of poker.\n│   ├── terminal   # Code to play against the AI from your console.\n│   └── utils      # Utility code like seed setting.\n├── research       # A directory for research/development scripts \n│                  # to help formulate understanding and ideas.\n└── test           # Python tests.\n    ├── functional # Functional tests that test multiple components \n    │              # together.\n    └── unit       # Individual tests for functions and objects.\n```\n\nCode Examples\n-------------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#code-examples)\n\nHere are some assorted examples of things that are being built in this repo.\n\n### State based poker traversal\n\n[](https://github.com/fedden/poker_ai?screenshot=true#state-based-poker-traversal)\n\nTo perform MCCFR, the core algorithm of poker\\_ai, we need a class that encodes all of the poker rules, that we can apply an action to which then creates a new game state.\n\npot \\= Pot()\nplayers \\= \\[\n    ShortDeckPokerPlayer(player\\_i\\=player\\_i, initial\\_chips\\=10000, pot\\=pot)\n    for player\\_i in range(n\\_players)\n\\]\nstate \\= ShortDeckPokerState(players\\=players)\nfor action in state.legal\\_actions:\n    new\\_state: ShortDeckPokerState \\= state.apply\\_action(action)\n\n### Playing against AI in your terminal\n\n[](https://github.com/fedden/poker_ai?screenshot=true#playing-against-ai-in-your-terminal)\n\nWe also have some code to play a round of poker against the AI agents, inside your terminal.\n\nThe characters are a little broken when captured in `asciinema`, but you'll get the idea by watching this video below. Results should be better in your actual terminal!\n\n[![Image 32](https://camo.githubusercontent.com/76b90f9a6e8e4526ba95477c77ec367dc69bdd45e301be51adba8bb2506c5406/68747470733a2f2f61736369696e656d612e6f72672f612f3333313233342e737667)](https://asciinema.org/a/331234)\n\nTo invoke the code, either call the \\`run\\_terminal\\_app\\` method directly from the \\`poker\\_ai.terminal.runner\\` module, or call from python like so:\n\ncd /path/to/poker\\_ai/dir\npython -m poker\\_ai.terminal.runner       \\\\\n  --agent offline                        \\\\ \n  --pickle\\_dir ./research/blueprint\\_algo \\\\\n  --strategy\\_path ./research/blueprint\\_algo/offline\\_strategy\\_285800.gz \n\n### Web visualisation code\n\n[](https://github.com/fedden/poker_ai?screenshot=true#web-visualisation-code)\n\nWe are also working on code to visualise a given instance of the `ShortDeckPokerState`, which looks like this:\n\n[![Image 33](https://github.com/fedden/poker_ai-poker-AI/raw/develop/assets/visualisation.png)](https://github.com/fedden/poker_ai-poker-AI/blob/develop/assets/visualisation.png)\n\nIt is so we can visualise the AI as it plays, and also debug particular situations visually. The idea as it stands, is a live web-visualisation server like TensorBoard, so you'll just push your current poker game state, and this will be reflected in the visualisations, so you can see what the agents are doing.\n\n[_The frontend code is based on this codepen._](https://codepen.io/Rovak/pen/ExYeQar)\n\nHere is an example of how you could plot the poker game state:\n\nfrom plot import PokerPlot\nfrom poker\\_ai.games.short\\_deck.player import ShortDeckPokerPlayer\nfrom poker\\_ai.games.short\\_deck.state import ShortDeckPokerState\nfrom poker\\_ai.poker.pot import Pot\n\ndef get\\_state() \\-\\> ShortDeckPokerState:\n    \"\"\"Gets a state to visualise\"\"\"\n    n\\_players \\= 6\n    pot \\= Pot()\n    players \\= \\[\n        ShortDeckPokerPlayer(player\\_i\\=player\\_i, initial\\_chips\\=10000, pot\\=pot)\n        for player\\_i in range(n\\_players)\n    \\]\n    return ShortDeckPokerState(\n        players\\=players, \n        pickle\\_dir\\=\"../../research/blueprint\\_algo/\"\n    )\n\npp: PokerPlot \\= PokerPlot()\n\\# If you visit http://localhost:5000/ now you will see an empty table.\n\n\\# ... later on in the code, as proxy for some code that obtains a new state ...\n\\# Obtain a new state.\nstate: ShortDeckPokerState \\= get\\_state()\n\\# Update the state to be plotted, this is sent via websockets to the frontend.\npp.update\\_state(state)\n\\# http://localhost:5000/ will now display a table with 6 players.\n\n### Playing a game of poker\n\n[](https://github.com/fedden/poker_ai?screenshot=true#playing-a-game-of-poker)\n\nThere are two parts to this repository, the code to manage a game of poker, and the code to train an AI algorithm to play the game of poker. A low level thing to first to is to implement a poker engine class that can manage a game of poker.\n\nThe reason the poker engine is implemented is because it is useful to have a well-integrated poker environment available during the development of the AI algorithm, incase there are tweaks that must be made to accomadate things like the history of state or the replay of a scenario during Monte Carlo Counterfactual Regret Minimisation.\n\nThe following code is how one might program a round of poker that is deterministic using the engine. This engine is now the first pass that will be used support self play.\n\nfrom poker\\_ai import utils\nfrom poker\\_ai.ai.dummy import RandomPlayer\nfrom poker\\_ai.poker.table import PokerTable\nfrom poker\\_ai.poker.engine import PokerEngine\nfrom poker\\_ai.poker.pot import Pot\n\n\\# Seed so things are deterministic.\nutils.random.seed(42)\n\n\\# Some settings for the amount of chips.\ninitial\\_chips\\_amount \\= 10000\nsmall\\_blind\\_amount \\= 50\nbig\\_blind\\_amount \\= 100\n\n\\# Create the pot.\npot \\= Pot()\n\\# Instanciate six players that will make random moves, make sure \n\\# they can reference the pot so they can add chips to it.\nplayers \\= \\[\n    RandomPlayer(\n        name\\=f'player {player\\_i}',\n        initial\\_chips\\=initial\\_chips\\_amount,\n        pot\\=pot)\n    for player\\_i in range(6)\n\\]\n\\# Create the table with the players on it.\ntable \\= PokerTable(players\\=players, pot\\=pot)\n\\# Create the engine that will manage the poker game lifecycle.\nengine \\= PokerEngine(\n    table\\=table,\n    small\\_blind\\=small\\_blind\\_amount,\n    big\\_blind\\=big\\_blind\\_amount)\n\\# Play a round of Texas Hold'em Poker!\nengine.play\\_one\\_round()\n\nRoadmap\n-------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#roadmap)\n\nThe following todo will change dynamically as my understanding of the algorithms and the poker\\_ai project evolves.\n\nAt first, the goal is to prototype in Python as iteration will be much easier and quicker. Once there is a working prototype, write in a systems level language like C++ and optimise for performance.\n\n### 1\\. Game engine iteration.\n\n[](https://github.com/fedden/poker_ai?screenshot=true#1-game-engine-iteration)\n\n_Implement a multiplayer working heads up no limit poker game engine to support the self-play._\n\n*   Lay down the foundation of game objects (player, card etc).\n*   Add poker hand evaluation code to the engine.\n*   Support a player going all in during betting.\n*   Support a player going all in during payouts.\n*   Lots of testing for various scenarios to ensure logic is working as expected.\n\n### 2\\. AI iteration.\n\n[](https://github.com/fedden/poker_ai?screenshot=true#2-ai-iteration)\n\n_Iterate on the AI algorithms and the integration into the poker engine._\n\n*   Integrate the AI strategy to support self-play in the multiplayer poker game engine.\n*   In the game-engine, allow the replay of any round the current hand to support MCCFR.\n*   Implement the creation of the blueprint strategy using Monte Carlo CFR miminisation.\n*   Add the real-time search for better strategies during the game.\n\n### 3\\. Game engine iteration.\n\n[](https://github.com/fedden/poker_ai?screenshot=true#3-game-engine-iteration)\n\n_Strengthen the game engine with more tests and allow users to see live visualisation of game state._\n\n*   Start work on a visualisation server to allow a game state to be displayed.\n*   Triple check that the rules are implemented in the poker engine as described in the supplimentary material.\n*   Work through the coverage, adding more tests, can never have enough.\n\n[![Image 34](https://github.com/fedden/poker_ai/raw/develop/assets/regret.jpeg)](https://github.com/fedden/poker_ai/blob/develop/assets/regret.jpeg)\n\nContributing\n------------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#contributing)\n\nThis is an open effort and help, criticisms and ideas are all welcome.\n\nFirst of all, please check out the [CONTRIBUTING](https://github.com/fedden/poker_ai/blob/develop/CONTRIBUTING.md) guide.\n\nFeel free to start a discussion on the github issues or to reach out to me at leonfedden at gmail dot com.\n\nLicense\n-------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#license)\n\nThe code is provided under the copy-left GPL licence. If you need it under a more permissive license then please contact me at leonfedden at gmail dot com.\n\nStargazers over time\n--------------------\n\n[](https://github.com/fedden/poker_ai?screenshot=true#stargazers-over-time)\n\nWe appreciate you getting this far in the README file! If you like what we are doing, please give us a star and share with your friends!\n\n[![Image 35: Stargazers over time](https://camo.githubusercontent.com/c26994023d46a1351ba47fa25bfd313c6a2b5aa625b7fa55a319e879e8ad9cbd/68747470733a2f2f7374617263686172742e63632f66656464656e2f706f6b65725f61692e737667)](https://starchart.cc/fedden/poker_ai)",
  "usage": {
    "tokens": 4434
  }
}
```
