---
title: GitHub - Yvictor/TradingGym: Trading and Backtesting environment for training reinforcement learning agent or simple rule base algo.
description: Trading and Backtesting environment for training reinforcement learning agent or simple rule base algo. - Yvictor/TradingGym
url: https://github.com/Yvictor/TradingGym
timestamp: 2025-01-20T15:30:29.997Z
domain: github.com
path: Yvictor_TradingGym
---

# GitHub - Yvictor/TradingGym: Trading and Backtesting environment for training reinforcement learning agent or simple rule base algo.


Trading and Backtesting environment for training reinforcement learning agent or simple rule base algo. - Yvictor/TradingGym


## Content

TradingGym
----------

[](https://github.com/Yvictor/TradingGym?screenshot=true#tradinggym)

[![Image 10: Build Status](https://camo.githubusercontent.com/9e6e7de999b850460311c6c5acfe337e1330a67cc20adb0d04f29c11a0abb0d3/68747470733a2f2f7472617669732d63692e6f72672f59766963746f722f54726164696e6747796d2e7376673f6272616e63683d6d6173746572)](https://travis-ci.org/Yvictor/TradingGym)

TradingGym is a toolkit for training and backtesting the reinforcement learning algorithms. This was inspired by OpenAI Gym and imitated the framework form. Not only traning env but also has backtesting and in the future will implement realtime trading env with Interactivate Broker API and so on.

This training env originally design for tickdata, but also support for ohlc data format. WIP.

### Installation

[](https://github.com/Yvictor/TradingGym?screenshot=true#installation)

```
git clone https://github.com/Yvictor/TradingGym.git
cd TradingGym
python setup.py install
```

### Getting Started

[](https://github.com/Yvictor/TradingGym?screenshot=true#getting-started)

import random
import numpy as np
import pandas as pd
import trading\_env

df \= pd.read\_hdf('dataset/SGXTW.h5', 'STW')

env \= trading\_env.make(env\_id\='training\_v1', obs\_data\_len\=256, step\_len\=128,
                       df\=df, fee\=0.1, max\_position\=5, deal\_col\_name\='Price', 
                       feature\_names\=\['Price', 'Volume', 
                                      'Ask\_price','Bid\_price', 
                                      'Ask\_deal\_vol','Bid\_deal\_vol',
                                      'Bid/Ask\_deal', 'Updown'\])

env.reset()
env.render()

state, reward, done, info \= env.step(random.randrange(3))

\### randow choice action and show the transaction detail
for i in range(500):
    print(i)
    state, reward, done, info \= env.step(random.randrange(3))
    print(state, reward)
    env.render()
    if done:
        break
env.transaction\_details

*   obs\_data\_len: observation data length
*   step\_len: when call step rolling windows will + step\_len
*   df exmaple

> | index | datetime | bid | ask | price | volume | serial\_number | dealin |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | 0 | 2010-05-25 08:45:00 | 7188.0 | 7188.0 | 7188.0 | 527.0 | 0.0 | 0.0 |
> | 1 | 2010-05-25 08:45:00 | 7188.0 | 7189.0 | 7189.0 | 1.0 | 1.0 | 1.0 |
> | 2 | 2010-05-25 08:45:00 | 7188.0 | 7189.0 | 7188.0 | 1.0 | 2.0 | \-1.0 |
> | 3 | 2010-05-25 08:45:00 | 7188.0 | 7189.0 | 7188.0 | 4.0 | 3.0 | \-1.0 |
> | 4 | 2010-05-25 08:45:00 | 7188.0 | 7189.0 | 7188.0 | 2.0 | 4.0 | \-1.0 |

*   df: dataframe that contain data for trading

> serial\_number -\> serial num of deal at each day recalculating

*   fee: when each deal will pay the fee, set with your product.
*   max\_position: the max market position for you trading share.
*   deal\_col\_name: the column name for cucalate reward used.
*   feature\_names: list contain the feature columns to use in trading status.

[![Image 11: gif](https://github.com/Yvictor/TradingGym/raw/master/fig/render.gif)](https://github.com/Yvictor/TradingGym/blob/master/fig/render.gif)

### Training

[](https://github.com/Yvictor/TradingGym?screenshot=true#training)

#### simple dqn

[](https://github.com/Yvictor/TradingGym?screenshot=true#simple-dqn)

*   WIP

#### policy gradient

[](https://github.com/Yvictor/TradingGym?screenshot=true#policy-gradient)

*   WIP

#### actor-critic

[](https://github.com/Yvictor/TradingGym?screenshot=true#actor-critic)

*   WIP

#### A3C with RNN

[](https://github.com/Yvictor/TradingGym?screenshot=true#a3c-with-rnn)

*   WIP

### Backtesting

[](https://github.com/Yvictor/TradingGym?screenshot=true#backtesting)

*   loading env just like training

env \= trading\_env.make(env\_id\='backtest\_v1', obs\_data\_len\=1024, step\_len\=512,
                       df\=df, fee\=0.1, max\_position\=5, deal\_col\_name\='Price', 
                        feature\_names\=\['Price', 'Volume', 
                                       'Ask\_price','Bid\_price', 
                                       'Ask\_deal\_vol','Bid\_deal\_vol',
                                       'Bid/Ask\_deal', 'Updown'\])

*   load your own agent

class YourAgent:
    def \_\_init\_\_(self):
        \# build your network and so on
        pass
    def choice\_action(self, state):
        \## your rule base conditon or your max Qvalue action or Policy Gradient action
         \# action=0 -\> do nothing
         \# action=1 -\> buy 1 share
         \# action=2 -\> sell 1 share
        \## in this testing case we just build a simple random policy 
        return np.random.randint(3)

*   start to backtest

agent \= YourAgent()

transactions \= \[\]
while not env.backtest\_done:
    state \= env.backtest()
    done \= False
    while not done:
        state, reward, done, info \= env.step(agent.choice\_action(state))
        #print(state, reward)
        #env.render()
        if done:
            transactions.append(info)
            break
transaction \= pd.concate(transactions)
transaction

|  | step | datetime | transact | transact\_type | price | share | price\_mean | position | reward\_fluc | reward | reward\_sum | color | rotation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1537 | 2013-04-09 10:58:45 | Buy | new | 277.1 | 1.0 | 277.100000 | 1.0 | 0.000000e+00 | 0.000000e+00 | 0.000000 | 1 | 1 |
| 5 | 3073 | 2013-04-09 11:47:26 | Sell | cover | 276.8 | \-1.0 | 277.100000 | 0.0 | \-4.000000e-01 | \-4.000000e-01 | \-0.400000 | 2 | 2 |
| 10 | 5633 | 2013-04-09 13:23:40 | Sell | new | 276.9 | \-1.0 | 276.900000 | \-1.0 | 0.000000e+00 | 0.000000e+00 | \-0.400000 | 2 | 1 |
| 11 | 6145 | 2013-04-09 13:30:36 | Sell | new | 276.7 | \-1.0 | 276.800000 | \-2.0 | 1.000000e-01 | 0.000000e+00 | \-0.400000 | 2 | 1 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 211 | 108545 | 2013-04-19 13:18:32 | Sell | new | 286.7 | \-1.0 | 286.525000 | \-2.0 | \-4.500000e-01 | 0.000000e+00 | 30.650000 | 2 | 1 |
| 216 | 111105 | 2013-04-19 16:02:01 | Sell | new | 289.2 | \-1.0 | 287.416667 | \-3.0 | \-5.550000e+00 | 0.000000e+00 | 30.650000 | 2 | 1 |
| 217 | 111617 | 2013-04-19 17:54:29 | Sell | new | 289.2 | \-1.0 | 287.862500 | \-4.0 | \-5.650000e+00 | 0.000000e+00 | 30.650000 | 2 | 1 |
| 218 | 112129 | 2013-04-19 21:36:21 | Sell | new | 288.0 | \-1.0 | 287.890000 | \-5.0 | \-9.500000e-01 | 0.000000e+00 | 30.650000 | 2 | 1 |
| 219 | 112129 | 2013-04-19 21:36:21 | Buy | cover | 288.0 | 5.0 | 287.890000 | 0.0 | 0.000000e+00 | \-1.050000e+00 | 29.600000 | 1 | 2 |

128 rows × 13 columns

#### exmaple of rule base usage

[](https://github.com/Yvictor/TradingGym?screenshot=true#exmaple-of-rule-base-usage)

*   ma crossover and crossunder

env \= trading\_env.make(env\_id\='backtest\_v1', obs\_data\_len\=10, step\_len\=1,
                       df\=df, fee\=0.1, max\_position\=5, deal\_col\_name\='Price', 
                       feature\_names\=\['Price', 'MA'\])
class MaAgent:
    def \_\_init\_\_(self):
        pass
        
    def choice\_action(self, state):
        if state\[\-1\]\[0\] \> state\[\-1\]\[1\] and state\[\-2\]\[0\] <\= state\[\-2\]\[1\]:
            return 1
        elif state\[\-1\]\[0\] < state\[\-1\]\[1\] and state\[\-2\]\[0\] \>\= state\[\-2\]\[1\]:
            return 2
        else:
            return 0
\# then same as above

## Metadata

```json
{
  "title": "GitHub - Yvictor/TradingGym: Trading and Backtesting environment for training reinforcement learning agent or simple rule base algo.",
  "description": "Trading and Backtesting environment for training reinforcement learning agent or simple rule base algo. - Yvictor/TradingGym",
  "url": "https://github.com/Yvictor/TradingGym?screenshot=true",
  "content": "TradingGym\n----------\n\n[](https://github.com/Yvictor/TradingGym?screenshot=true#tradinggym)\n\n[![Image 10: Build Status](https://camo.githubusercontent.com/9e6e7de999b850460311c6c5acfe337e1330a67cc20adb0d04f29c11a0abb0d3/68747470733a2f2f7472617669732d63692e6f72672f59766963746f722f54726164696e6747796d2e7376673f6272616e63683d6d6173746572)](https://travis-ci.org/Yvictor/TradingGym)\n\nTradingGym is a toolkit for training and backtesting the reinforcement learning algorithms. This was inspired by OpenAI Gym and imitated the framework form. Not only traning env but also has backtesting and in the future will implement realtime trading env with Interactivate Broker API and so on.\n\nThis training env originally design for tickdata, but also support for ohlc data format. WIP.\n\n### Installation\n\n[](https://github.com/Yvictor/TradingGym?screenshot=true#installation)\n\n```\ngit clone https://github.com/Yvictor/TradingGym.git\ncd TradingGym\npython setup.py install\n```\n\n### Getting Started\n\n[](https://github.com/Yvictor/TradingGym?screenshot=true#getting-started)\n\nimport random\nimport numpy as np\nimport pandas as pd\nimport trading\\_env\n\ndf \\= pd.read\\_hdf('dataset/SGXTW.h5', 'STW')\n\nenv \\= trading\\_env.make(env\\_id\\='training\\_v1', obs\\_data\\_len\\=256, step\\_len\\=128,\n                       df\\=df, fee\\=0.1, max\\_position\\=5, deal\\_col\\_name\\='Price', \n                       feature\\_names\\=\\['Price', 'Volume', \n                                      'Ask\\_price','Bid\\_price', \n                                      'Ask\\_deal\\_vol','Bid\\_deal\\_vol',\n                                      'Bid/Ask\\_deal', 'Updown'\\])\n\nenv.reset()\nenv.render()\n\nstate, reward, done, info \\= env.step(random.randrange(3))\n\n\\### randow choice action and show the transaction detail\nfor i in range(500):\n    print(i)\n    state, reward, done, info \\= env.step(random.randrange(3))\n    print(state, reward)\n    env.render()\n    if done:\n        break\nenv.transaction\\_details\n\n*   obs\\_data\\_len: observation data length\n*   step\\_len: when call step rolling windows will + step\\_len\n*   df exmaple\n\n> | index | datetime | bid | ask | price | volume | serial\\_number | dealin |\n> | --- | --- | --- | --- | --- | --- | --- | --- |\n> | 0 | 2010-05-25 08:45:00 | 7188.0 | 7188.0 | 7188.0 | 527.0 | 0.0 | 0.0 |\n> | 1 | 2010-05-25 08:45:00 | 7188.0 | 7189.0 | 7189.0 | 1.0 | 1.0 | 1.0 |\n> | 2 | 2010-05-25 08:45:00 | 7188.0 | 7189.0 | 7188.0 | 1.0 | 2.0 | \\-1.0 |\n> | 3 | 2010-05-25 08:45:00 | 7188.0 | 7189.0 | 7188.0 | 4.0 | 3.0 | \\-1.0 |\n> | 4 | 2010-05-25 08:45:00 | 7188.0 | 7189.0 | 7188.0 | 2.0 | 4.0 | \\-1.0 |\n\n*   df: dataframe that contain data for trading\n\n> serial\\_number -\\> serial num of deal at each day recalculating\n\n*   fee: when each deal will pay the fee, set with your product.\n*   max\\_position: the max market position for you trading share.\n*   deal\\_col\\_name: the column name for cucalate reward used.\n*   feature\\_names: list contain the feature columns to use in trading status.\n\n[![Image 11: gif](https://github.com/Yvictor/TradingGym/raw/master/fig/render.gif)](https://github.com/Yvictor/TradingGym/blob/master/fig/render.gif)\n\n### Training\n\n[](https://github.com/Yvictor/TradingGym?screenshot=true#training)\n\n#### simple dqn\n\n[](https://github.com/Yvictor/TradingGym?screenshot=true#simple-dqn)\n\n*   WIP\n\n#### policy gradient\n\n[](https://github.com/Yvictor/TradingGym?screenshot=true#policy-gradient)\n\n*   WIP\n\n#### actor-critic\n\n[](https://github.com/Yvictor/TradingGym?screenshot=true#actor-critic)\n\n*   WIP\n\n#### A3C with RNN\n\n[](https://github.com/Yvictor/TradingGym?screenshot=true#a3c-with-rnn)\n\n*   WIP\n\n### Backtesting\n\n[](https://github.com/Yvictor/TradingGym?screenshot=true#backtesting)\n\n*   loading env just like training\n\nenv \\= trading\\_env.make(env\\_id\\='backtest\\_v1', obs\\_data\\_len\\=1024, step\\_len\\=512,\n                       df\\=df, fee\\=0.1, max\\_position\\=5, deal\\_col\\_name\\='Price', \n                        feature\\_names\\=\\['Price', 'Volume', \n                                       'Ask\\_price','Bid\\_price', \n                                       'Ask\\_deal\\_vol','Bid\\_deal\\_vol',\n                                       'Bid/Ask\\_deal', 'Updown'\\])\n\n*   load your own agent\n\nclass YourAgent:\n    def \\_\\_init\\_\\_(self):\n        \\# build your network and so on\n        pass\n    def choice\\_action(self, state):\n        \\## your rule base conditon or your max Qvalue action or Policy Gradient action\n         \\# action=0 -\\> do nothing\n         \\# action=1 -\\> buy 1 share\n         \\# action=2 -\\> sell 1 share\n        \\## in this testing case we just build a simple random policy \n        return np.random.randint(3)\n\n*   start to backtest\n\nagent \\= YourAgent()\n\ntransactions \\= \\[\\]\nwhile not env.backtest\\_done:\n    state \\= env.backtest()\n    done \\= False\n    while not done:\n        state, reward, done, info \\= env.step(agent.choice\\_action(state))\n        #print(state, reward)\n        #env.render()\n        if done:\n            transactions.append(info)\n            break\ntransaction \\= pd.concate(transactions)\ntransaction\n\n|  | step | datetime | transact | transact\\_type | price | share | price\\_mean | position | reward\\_fluc | reward | reward\\_sum | color | rotation |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| 2 | 1537 | 2013-04-09 10:58:45 | Buy | new | 277.1 | 1.0 | 277.100000 | 1.0 | 0.000000e+00 | 0.000000e+00 | 0.000000 | 1 | 1 |\n| 5 | 3073 | 2013-04-09 11:47:26 | Sell | cover | 276.8 | \\-1.0 | 277.100000 | 0.0 | \\-4.000000e-01 | \\-4.000000e-01 | \\-0.400000 | 2 | 2 |\n| 10 | 5633 | 2013-04-09 13:23:40 | Sell | new | 276.9 | \\-1.0 | 276.900000 | \\-1.0 | 0.000000e+00 | 0.000000e+00 | \\-0.400000 | 2 | 1 |\n| 11 | 6145 | 2013-04-09 13:30:36 | Sell | new | 276.7 | \\-1.0 | 276.800000 | \\-2.0 | 1.000000e-01 | 0.000000e+00 | \\-0.400000 | 2 | 1 |\n| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |\n| 211 | 108545 | 2013-04-19 13:18:32 | Sell | new | 286.7 | \\-1.0 | 286.525000 | \\-2.0 | \\-4.500000e-01 | 0.000000e+00 | 30.650000 | 2 | 1 |\n| 216 | 111105 | 2013-04-19 16:02:01 | Sell | new | 289.2 | \\-1.0 | 287.416667 | \\-3.0 | \\-5.550000e+00 | 0.000000e+00 | 30.650000 | 2 | 1 |\n| 217 | 111617 | 2013-04-19 17:54:29 | Sell | new | 289.2 | \\-1.0 | 287.862500 | \\-4.0 | \\-5.650000e+00 | 0.000000e+00 | 30.650000 | 2 | 1 |\n| 218 | 112129 | 2013-04-19 21:36:21 | Sell | new | 288.0 | \\-1.0 | 287.890000 | \\-5.0 | \\-9.500000e-01 | 0.000000e+00 | 30.650000 | 2 | 1 |\n| 219 | 112129 | 2013-04-19 21:36:21 | Buy | cover | 288.0 | 5.0 | 287.890000 | 0.0 | 0.000000e+00 | \\-1.050000e+00 | 29.600000 | 1 | 2 |\n\n128 rows × 13 columns\n\n#### exmaple of rule base usage\n\n[](https://github.com/Yvictor/TradingGym?screenshot=true#exmaple-of-rule-base-usage)\n\n*   ma crossover and crossunder\n\nenv \\= trading\\_env.make(env\\_id\\='backtest\\_v1', obs\\_data\\_len\\=10, step\\_len\\=1,\n                       df\\=df, fee\\=0.1, max\\_position\\=5, deal\\_col\\_name\\='Price', \n                       feature\\_names\\=\\['Price', 'MA'\\])\nclass MaAgent:\n    def \\_\\_init\\_\\_(self):\n        pass\n        \n    def choice\\_action(self, state):\n        if state\\[\\-1\\]\\[0\\] \\> state\\[\\-1\\]\\[1\\] and state\\[\\-2\\]\\[0\\] <\\= state\\[\\-2\\]\\[1\\]:\n            return 1\n        elif state\\[\\-1\\]\\[0\\] < state\\[\\-1\\]\\[1\\] and state\\[\\-2\\]\\[0\\] \\>\\= state\\[\\-2\\]\\[1\\]:\n            return 2\n        else:\n            return 0\n\\# then same as above",
  "usage": {
    "tokens": 2649
  }
}
```
