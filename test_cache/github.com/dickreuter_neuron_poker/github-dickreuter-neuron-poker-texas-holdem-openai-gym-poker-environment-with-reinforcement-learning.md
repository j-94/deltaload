---
title: GitHub - dickreuter/neuron_poker: Texas holdem OpenAi gym poker environment with reinforcement learning based on keras-rl. Includes virtual rendering and montecarlo for equity calculation.
description: Texas holdem OpenAi gym poker environment with reinforcement learning based on keras-rl. Includes virtual rendering and montecarlo for equity calculation. - dickreuter/neuron_poker
url: https://github.com/dickreuter/neuron_poker
timestamp: 2025-01-20T15:31:13.257Z
domain: github.com
path: dickreuter_neuron_poker
---

# GitHub - dickreuter/neuron_poker: Texas holdem OpenAi gym poker environment with reinforcement learning based on keras-rl. Includes virtual rendering and montecarlo for equity calculation.


Texas holdem OpenAi gym poker environment with reinforcement learning based on keras-rl. Includes virtual rendering and montecarlo for equity calculation. - dickreuter/neuron_poker


## Content

Neuron Poker: OpenAi gym environment for texas holdem poker
-----------------------------------------------------------

[](https://github.com/dickreuter/neuron_poker?screenshot=true#neuron-poker-openai-gym-environment-for-texas-holdem-poker)

This is an environment for training neural networks to play texas holdem. Please try to model your own players and create a pull request so we can collaborate and create the best possible player.

Usage:
------

[](https://github.com/dickreuter/neuron_poker?screenshot=true#usage)

Run:

*   Install Python 3.11, I would also recommend to install PyCharm.
*   Install Poetry with `curl -sSL https://install.python-poetry.org | python3 -`
*   Create a virtual environment with `poetry env use python3.11`
*   Activate it with `poetry shell`
*   Install all required packages with `poetry install --no-root`
*   Run 6 random players playing against each other: `poetry run python main.py selfplay random --render` or
*   To manually control the players:`poetry run python main.py selfplay keypress --render`
*   Example of genetic algorithm with self improvement: `poetry run python main.py selfplay equity_improvement --improvement_rounds=20 --episodes=10`
*   In order to use the C++ version of the equity calculator, you will also need to install Visual Studio 2019 (or GCC over Cygwin may work as well). To use it, use the -c option when running main.py.
*   For more advanced users: `poetry run python main.py selfplay dqn_train -c` will start training the deep Q agent with C++ Monte Carlo for faster calculation

[![Image 23](https://github.com/dickreuter/neuron_poker/raw/master/doc/table.gif)](https://github.com/dickreuter/neuron_poker/blob/master/doc/table.gif)

### Analysis of the run

[](https://github.com/dickreuter/neuron_poker?screenshot=true#analysis-of-the-run)

At the end of an episode, the performance of the players can be observed via the summary plot. [![Image 24: image0](https://github.com/dickreuter/neuron_poker/raw/master/doc/pots.png)](https://github.com/dickreuter/neuron_poker/blob/master/doc/pots.png)

### Packages and modules:

[](https://github.com/dickreuter/neuron_poker?screenshot=true#packages-and-modules)

main.py: entry point and command line interpreter. Runs agents with the gym. The docstring at the top of the file describes the command line options. They are interpreted by docopt.

### gym\_env

[](https://github.com/dickreuter/neuron_poker?screenshot=true#gym_env)

*   `env.py`: Texas Hold’em unlimited openai gym environment & `rendering.py`: rendering graphics while playing

### agents

[](https://github.com/dickreuter/neuron_poker?screenshot=true#agents)

Please add your model based agents here.

*   `agent_random.py`: an agent making random decisions
*   `agent_keypress.py`: an agent taking decision via keypress
*   `agent_consider_equity.py`: an agent considering equity information
*   `agent_keras_rl_dqn.py`: Deep Q learning agent, using keras-rl for deep reinforcement learning
*   `agent_custom_q1.py`: Custom implementation of deep q learning

Note that the observation property is a dictionary that contains all the information about the players and table that can be used to make a decision.

### Custom implementation of q learning

[](https://github.com/dickreuter/neuron_poker?screenshot=true#custom-implementation-of-q-learning)

Custom impelemtation of reinforcement learning. This package is now in a separate repo: [www.github.com/dickreuter/tf\_rl](http://www.github.com/dickreuter/tf_rl)

### tools

[](https://github.com/dickreuter/neuron_poker?screenshot=true#tools)

*   `hand_evaluator.py`: evaluate the best hand of multiple players
*   `helper.py`: helper functions
*   `montecarlo_numpy2.py`: fast numpy based montecarlo simulation to calculate equity. Not yet working correctly. Some tests are failing. Feel free to fix them.
*   `montecarlo_python.py`: relatively slow python based montecarlo for equity calculation. Supports preflight ranges for other players.
*   `montecarlo_cpp`: c++ implementation of equity calculator. Around 500x faster than python version

#### tests

[](https://github.com/dickreuter/neuron_poker?screenshot=true#tests)

*   `test_gym_env.py`: tests for the end.
*   `test_montecarlo.py`: tests for the hands evaluator and python based equity calculator.
*   `test_montecarlo_numpy.py`: tests for the numpy montecarlo
*   `test_pylint.py`: pylint and pydoc tests to ensure pep8 standards and static code analysis

Roadmap
-------

[](https://github.com/dickreuter/neuron_poker?screenshot=true#roadmap)

### Agents

[](https://github.com/dickreuter/neuron_poker?screenshot=true#agents-1)

*   \[x\] Agent based on user interaction (keypress)
*   \[x\] Random agent
*   \[x\] Equity based strategy (i.e. call and bet above threshold)
*   \[x\] Equity based strategy with genetic algorithm, adjusting the treshold based on winning agent.
*   \[x\] C++ implementation of equity calculator to significantly speed up runs
*   \[x\] Agent based on reinforcement learning with experience replay (Deep Q learning, based on keras-rl)
*   \[/\] Custom agents (see above section for more details)

### Reinforcement learning: Deep Q agent

[](https://github.com/dickreuter/neuron_poker?screenshot=true#reinforcement-learning-deep-q-agent)

`neuron_poker.agents.agent_dqn` implements a deep q agent with help of keras-rl. A number of parameters can be se:

*   nb\_max\_start\_steps = 20 # maximum of random actions at the beginning
*   nb\_steps\_warmup = 75 # before training starts, should be higher than start steps
*   nb\_steps = 10000 # total number of steps
*   memory\_limit = int(nb\_steps / 3) # limiting the memory of experience replay
*   batch\_size = 500 # number of items sampled from memory to train

Training can be observed via tensorboard (run `tensorboard --logdir=./Graph` from command line) [![Image 25: image2](https://github.com/dickreuter/neuron_poker/raw/master/doc/tensorboard-example.png)](https://github.com/dickreuter/neuron_poker/blob/master/doc/tensorboard-example.png)

How to contribute
-----------------

[](https://github.com/dickreuter/neuron_poker?screenshot=true#how-to-contribute)

### Launching from main.py

[](https://github.com/dickreuter/neuron_poker?screenshot=true#launching-from-mainpy)

In `main.py` an agent is launched as follows (here adding 6 random agents to the table). To edit what is accepted to main.py via command line, simply add another line in the docstring at the top of main.py.

def random\_action(render):
    """Create an environment with 6 random players"""
    env\_name \= 'neuron\_poker-v0'
    stack \= 500
    self.env \= gym.make(env\_name, num\_of\_players\=6, initial\_stacks\=stack)
    for \_ in range(num\_of\_plrs):
        player \= RandomPlayer(500)
        self.env.add\_player(player)

    self.env.reset()

As you can see, as a first step, the environment needs to be created. As a second step, different agents need to be added to the table. As a third step the game is kicked off with a reset. Agents with autoplay set to True will automatically play, by having the action method called of their class. Alternatively you can use the PlayerShell class and the environment will require you call call the step function manually and loop over it. This may be helpful when using other packages which are designed to interface with the gym, such as keras-rl.

#### Adding a new model / agent

[](https://github.com/dickreuter/neuron_poker?screenshot=true#adding-a-new-model--agent)

An example agent can be seen in random\_agent.py

To build a new agent, an agent needs to be created, where the follwing function is modified. You will need to use the observation parameter, which contains the current state of the table, the players and and the agent itself, as a parameter to determine the best action.

def action(self, action\_space, observation):  \# pylint: disable=no-self-use
    """Mandatory method that calculates the move based on the observation array and the action space."""
    \_ \= observation  \# not using the observation for random decision
    this\_player\_action\_space \= {Action.FOLD, Action.CHECK, Action.CALL, Action.RAISE\_POT, Action.RAISE\_HAlF\_POT}
    possible\_moves \= this\_player\_action\_space.intersection(set(action\_space))
    action \= random.choice(list(possible\_moves))
    return action

### Observing the state

[](https://github.com/dickreuter/neuron_poker?screenshot=true#observing-the-state)

The state is represented as a numpy array that contains the following information:

class CommunityData:
    def \_\_init\_\_(self, num\_players):
        self.current\_player\_position \= \[False\] \* num\_players  \# ix\[0\] = dealer
        self.stage \= \[False\] \* 4  \# one hot: preflop, flop, turn, river
        self.community\_pot: float: the full pot of this hand
        self.current\_round\_pot: float: the pot of funds added in this round
        self.active\_players \= \[False\] \* num\_players  \# one hot encoded, 0 = dealer
        self.big\_blind
        self.small\_blind

class StageData:  \# as a list, 8 times:
    """Preflop, flop, turn and river, 2 rounds each"""

    def \_\_init\_\_(self, num\_players):
        self.calls \= \[False\] \* num\_players  \# ix\[0\] = dealer
        self.raises \= \[False\] \* num\_players  \# ix\[0\] = dealer
        self.min\_call\_at\_action \= \[0\] \* num\_players  \# ix\[0\] = dealer
        self.contribution \= \[0\] \* num\_players  \# ix\[0\] = dealer
        self.stack\_at\_action \= \[0\] \* num\_players  \# ix\[0\] = dealer
        self.community\_pot\_at\_action \= \[0\] \* num\_players  \# ix\[0\] = dealer

class PlayerData:
    "Player specific information"

    def \_\_init\_\_(self):
        self.position: one hot encoded, 0\=dealer
        self.equity\_to\_river: montecarlo
        self.equity\_to\_river\_2plr: montecarlo
        self.equity\_to\_river\_3plr: montecarlo
        self.stack: current player stack

### How to integrate your code on Github

[](https://github.com/dickreuter/neuron_poker?screenshot=true#how-to-integrate-your-code-on-github)

It will be hard for one person alone to beat the world at poker. That's why this repo aims to have a collaborative environment, where models can be added and evaluated.

To contribute do the following:

*   Get Pycharm and build the virtual python environment. Use can do: `pip install -r requirements.txt`
*   If you want to use the 500x faster c++ based equity calculator, also install visual studio, but this is not necessary
*   Clone your fork to your local machine. You can do this directly from pycharm: VCS --\> check out from version control --\> git
*   Add as remote the original repository where you created the fork from and call it upstream (the connection to your fork should be called origin). This can be done with vcs --\> git --\> remotes
*   Create a new branch: click on master at the bottom right, and then click on 'new branch'
*   Make your edits.
*   Ensure all tests pass. Under file --\> settings --\> python integrated tools switch to pytest (see screenshot). [![Image 26: image1](https://github.com/dickreuter/neuron_poker/raw/master/doc/pytest.png)](https://github.com/dickreuter/neuron_poker/blob/master/doc/pytest.png) You can then just right click on the tests folder and run all tests. All tests need to pass. Make sure to add your own tests by simply naming the funtion test\_...
*   Make sure all the tests are passing. Best run pytest as described above (in pycharm just right click on the tests folder and run it). If a test fails, you can debug the test, by right clicking on it and put breakpoints, or even open a console at the breakpoint: [https://stackoverflow.com/questions/19329601/interactive-shell-debugging-with-pycharm](https://stackoverflow.com/questions/19329601/interactive-shell-debugging-with-pycharm)
*   Commit your changes (CTRL+K}
*   Push your changes to your origin (your fork) (CTRL+SHIFT+K)
*   To bring your branch up to date with upstream master, if it has moved on: rebase onto upstream master: click on your branch name at the bottom right of pycharm, then click on upstream/master, then rebase onto. You may need to resolve soe conflicts. Once this is done, make sure to always force-push (ctrl+shift+k), (not just push). This can be done by selecting the dropdown next to push and choose force-push (important: don't push and merge a rebased branch with your remote)
*   Create a pull request on your github.com to merge your branch with the upstream master.
*   When your pull request is approved, it will be merged into the upstream/master.

## Metadata

```json
{
  "title": "GitHub - dickreuter/neuron_poker: Texas holdem OpenAi gym poker environment with reinforcement learning based on keras-rl. Includes virtual rendering and montecarlo for equity calculation.",
  "description": "Texas holdem OpenAi gym poker environment with reinforcement learning based on keras-rl. Includes virtual rendering and montecarlo for equity calculation. - dickreuter/neuron_poker",
  "url": "https://github.com/dickreuter/neuron_poker?screenshot=true",
  "content": "Neuron Poker: OpenAi gym environment for texas holdem poker\n-----------------------------------------------------------\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#neuron-poker-openai-gym-environment-for-texas-holdem-poker)\n\nThis is an environment for training neural networks to play texas holdem. Please try to model your own players and create a pull request so we can collaborate and create the best possible player.\n\nUsage:\n------\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#usage)\n\nRun:\n\n*   Install Python 3.11, I would also recommend to install PyCharm.\n*   Install Poetry with `curl -sSL https://install.python-poetry.org | python3 -`\n*   Create a virtual environment with `poetry env use python3.11`\n*   Activate it with `poetry shell`\n*   Install all required packages with `poetry install --no-root`\n*   Run 6 random players playing against each other: `poetry run python main.py selfplay random --render` or\n*   To manually control the players:`poetry run python main.py selfplay keypress --render`\n*   Example of genetic algorithm with self improvement: `poetry run python main.py selfplay equity_improvement --improvement_rounds=20 --episodes=10`\n*   In order to use the C++ version of the equity calculator, you will also need to install Visual Studio 2019 (or GCC over Cygwin may work as well). To use it, use the -c option when running main.py.\n*   For more advanced users: `poetry run python main.py selfplay dqn_train -c` will start training the deep Q agent with C++ Monte Carlo for faster calculation\n\n[![Image 23](https://github.com/dickreuter/neuron_poker/raw/master/doc/table.gif)](https://github.com/dickreuter/neuron_poker/blob/master/doc/table.gif)\n\n### Analysis of the run\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#analysis-of-the-run)\n\nAt the end of an episode, the performance of the players can be observed via the summary plot. [![Image 24: image0](https://github.com/dickreuter/neuron_poker/raw/master/doc/pots.png)](https://github.com/dickreuter/neuron_poker/blob/master/doc/pots.png)\n\n### Packages and modules:\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#packages-and-modules)\n\nmain.py: entry point and command line interpreter. Runs agents with the gym. The docstring at the top of the file describes the command line options. They are interpreted by docopt.\n\n### gym\\_env\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#gym_env)\n\n*   `env.py`: Texas Hold’em unlimited openai gym environment & `rendering.py`: rendering graphics while playing\n\n### agents\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#agents)\n\nPlease add your model based agents here.\n\n*   `agent_random.py`: an agent making random decisions\n*   `agent_keypress.py`: an agent taking decision via keypress\n*   `agent_consider_equity.py`: an agent considering equity information\n*   `agent_keras_rl_dqn.py`: Deep Q learning agent, using keras-rl for deep reinforcement learning\n*   `agent_custom_q1.py`: Custom implementation of deep q learning\n\nNote that the observation property is a dictionary that contains all the information about the players and table that can be used to make a decision.\n\n### Custom implementation of q learning\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#custom-implementation-of-q-learning)\n\nCustom impelemtation of reinforcement learning. This package is now in a separate repo: [www.github.com/dickreuter/tf\\_rl](http://www.github.com/dickreuter/tf_rl)\n\n### tools\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#tools)\n\n*   `hand_evaluator.py`: evaluate the best hand of multiple players\n*   `helper.py`: helper functions\n*   `montecarlo_numpy2.py`: fast numpy based montecarlo simulation to calculate equity. Not yet working correctly. Some tests are failing. Feel free to fix them.\n*   `montecarlo_python.py`: relatively slow python based montecarlo for equity calculation. Supports preflight ranges for other players.\n*   `montecarlo_cpp`: c++ implementation of equity calculator. Around 500x faster than python version\n\n#### tests\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#tests)\n\n*   `test_gym_env.py`: tests for the end.\n*   `test_montecarlo.py`: tests for the hands evaluator and python based equity calculator.\n*   `test_montecarlo_numpy.py`: tests for the numpy montecarlo\n*   `test_pylint.py`: pylint and pydoc tests to ensure pep8 standards and static code analysis\n\nRoadmap\n-------\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#roadmap)\n\n### Agents\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#agents-1)\n\n*   \\[x\\] Agent based on user interaction (keypress)\n*   \\[x\\] Random agent\n*   \\[x\\] Equity based strategy (i.e. call and bet above threshold)\n*   \\[x\\] Equity based strategy with genetic algorithm, adjusting the treshold based on winning agent.\n*   \\[x\\] C++ implementation of equity calculator to significantly speed up runs\n*   \\[x\\] Agent based on reinforcement learning with experience replay (Deep Q learning, based on keras-rl)\n*   \\[/\\] Custom agents (see above section for more details)\n\n### Reinforcement learning: Deep Q agent\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#reinforcement-learning-deep-q-agent)\n\n`neuron_poker.agents.agent_dqn` implements a deep q agent with help of keras-rl. A number of parameters can be se:\n\n*   nb\\_max\\_start\\_steps = 20 # maximum of random actions at the beginning\n*   nb\\_steps\\_warmup = 75 # before training starts, should be higher than start steps\n*   nb\\_steps = 10000 # total number of steps\n*   memory\\_limit = int(nb\\_steps / 3) # limiting the memory of experience replay\n*   batch\\_size = 500 # number of items sampled from memory to train\n\nTraining can be observed via tensorboard (run `tensorboard --logdir=./Graph` from command line) [![Image 25: image2](https://github.com/dickreuter/neuron_poker/raw/master/doc/tensorboard-example.png)](https://github.com/dickreuter/neuron_poker/blob/master/doc/tensorboard-example.png)\n\nHow to contribute\n-----------------\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#how-to-contribute)\n\n### Launching from main.py\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#launching-from-mainpy)\n\nIn `main.py` an agent is launched as follows (here adding 6 random agents to the table). To edit what is accepted to main.py via command line, simply add another line in the docstring at the top of main.py.\n\ndef random\\_action(render):\n    \"\"\"Create an environment with 6 random players\"\"\"\n    env\\_name \\= 'neuron\\_poker-v0'\n    stack \\= 500\n    self.env \\= gym.make(env\\_name, num\\_of\\_players\\=6, initial\\_stacks\\=stack)\n    for \\_ in range(num\\_of\\_plrs):\n        player \\= RandomPlayer(500)\n        self.env.add\\_player(player)\n\n    self.env.reset()\n\nAs you can see, as a first step, the environment needs to be created. As a second step, different agents need to be added to the table. As a third step the game is kicked off with a reset. Agents with autoplay set to True will automatically play, by having the action method called of their class. Alternatively you can use the PlayerShell class and the environment will require you call call the step function manually and loop over it. This may be helpful when using other packages which are designed to interface with the gym, such as keras-rl.\n\n#### Adding a new model / agent\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#adding-a-new-model--agent)\n\nAn example agent can be seen in random\\_agent.py\n\nTo build a new agent, an agent needs to be created, where the follwing function is modified. You will need to use the observation parameter, which contains the current state of the table, the players and and the agent itself, as a parameter to determine the best action.\n\ndef action(self, action\\_space, observation):  \\# pylint: disable=no-self-use\n    \"\"\"Mandatory method that calculates the move based on the observation array and the action space.\"\"\"\n    \\_ \\= observation  \\# not using the observation for random decision\n    this\\_player\\_action\\_space \\= {Action.FOLD, Action.CHECK, Action.CALL, Action.RAISE\\_POT, Action.RAISE\\_HAlF\\_POT}\n    possible\\_moves \\= this\\_player\\_action\\_space.intersection(set(action\\_space))\n    action \\= random.choice(list(possible\\_moves))\n    return action\n\n### Observing the state\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#observing-the-state)\n\nThe state is represented as a numpy array that contains the following information:\n\nclass CommunityData:\n    def \\_\\_init\\_\\_(self, num\\_players):\n        self.current\\_player\\_position \\= \\[False\\] \\* num\\_players  \\# ix\\[0\\] = dealer\n        self.stage \\= \\[False\\] \\* 4  \\# one hot: preflop, flop, turn, river\n        self.community\\_pot: float: the full pot of this hand\n        self.current\\_round\\_pot: float: the pot of funds added in this round\n        self.active\\_players \\= \\[False\\] \\* num\\_players  \\# one hot encoded, 0 = dealer\n        self.big\\_blind\n        self.small\\_blind\n\nclass StageData:  \\# as a list, 8 times:\n    \"\"\"Preflop, flop, turn and river, 2 rounds each\"\"\"\n\n    def \\_\\_init\\_\\_(self, num\\_players):\n        self.calls \\= \\[False\\] \\* num\\_players  \\# ix\\[0\\] = dealer\n        self.raises \\= \\[False\\] \\* num\\_players  \\# ix\\[0\\] = dealer\n        self.min\\_call\\_at\\_action \\= \\[0\\] \\* num\\_players  \\# ix\\[0\\] = dealer\n        self.contribution \\= \\[0\\] \\* num\\_players  \\# ix\\[0\\] = dealer\n        self.stack\\_at\\_action \\= \\[0\\] \\* num\\_players  \\# ix\\[0\\] = dealer\n        self.community\\_pot\\_at\\_action \\= \\[0\\] \\* num\\_players  \\# ix\\[0\\] = dealer\n\nclass PlayerData:\n    \"Player specific information\"\n\n    def \\_\\_init\\_\\_(self):\n        self.position: one hot encoded, 0\\=dealer\n        self.equity\\_to\\_river: montecarlo\n        self.equity\\_to\\_river\\_2plr: montecarlo\n        self.equity\\_to\\_river\\_3plr: montecarlo\n        self.stack: current player stack\n\n### How to integrate your code on Github\n\n[](https://github.com/dickreuter/neuron_poker?screenshot=true#how-to-integrate-your-code-on-github)\n\nIt will be hard for one person alone to beat the world at poker. That's why this repo aims to have a collaborative environment, where models can be added and evaluated.\n\nTo contribute do the following:\n\n*   Get Pycharm and build the virtual python environment. Use can do: `pip install -r requirements.txt`\n*   If you want to use the 500x faster c++ based equity calculator, also install visual studio, but this is not necessary\n*   Clone your fork to your local machine. You can do this directly from pycharm: VCS --\\> check out from version control --\\> git\n*   Add as remote the original repository where you created the fork from and call it upstream (the connection to your fork should be called origin). This can be done with vcs --\\> git --\\> remotes\n*   Create a new branch: click on master at the bottom right, and then click on 'new branch'\n*   Make your edits.\n*   Ensure all tests pass. Under file --\\> settings --\\> python integrated tools switch to pytest (see screenshot). [![Image 26: image1](https://github.com/dickreuter/neuron_poker/raw/master/doc/pytest.png)](https://github.com/dickreuter/neuron_poker/blob/master/doc/pytest.png) You can then just right click on the tests folder and run all tests. All tests need to pass. Make sure to add your own tests by simply naming the funtion test\\_...\n*   Make sure all the tests are passing. Best run pytest as described above (in pycharm just right click on the tests folder and run it). If a test fails, you can debug the test, by right clicking on it and put breakpoints, or even open a console at the breakpoint: [https://stackoverflow.com/questions/19329601/interactive-shell-debugging-with-pycharm](https://stackoverflow.com/questions/19329601/interactive-shell-debugging-with-pycharm)\n*   Commit your changes (CTRL+K}\n*   Push your changes to your origin (your fork) (CTRL+SHIFT+K)\n*   To bring your branch up to date with upstream master, if it has moved on: rebase onto upstream master: click on your branch name at the bottom right of pycharm, then click on upstream/master, then rebase onto. You may need to resolve soe conflicts. Once this is done, make sure to always force-push (ctrl+shift+k), (not just push). This can be done by selecting the dropdown next to push and choose force-push (important: don't push and merge a rebased branch with your remote)\n*   Create a pull request on your github.com to merge your branch with the upstream master.\n*   When your pull request is approved, it will be merged into the upstream/master.",
  "usage": {
    "tokens": 3178
  }
}
```
