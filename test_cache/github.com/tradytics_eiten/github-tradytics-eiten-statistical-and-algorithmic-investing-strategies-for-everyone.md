---
title: GitHub - tradytics/eiten: Statistical and Algorithmic Investing Strategies for Everyone
description: Statistical and Algorithmic Investing Strategies for Everyone - tradytics/eiten
url: https://github.com/tradytics/eiten
timestamp: 2025-01-20T15:32:01.993Z
domain: github.com
path: tradytics_eiten
---

# GitHub - tradytics/eiten: Statistical and Algorithmic Investing Strategies for Everyone


Statistical and Algorithmic Investing Strategies for Everyone - tradytics/eiten


## Content

[![Image 17](https://github.com/tradytics/eiten/raw/master/figures/normal-512x512.png)](https://github.com/tradytics/eiten/blob/master/figures/normal-512x512.png)

Eiten - Algorithmic Investing Strategies for Everyone
-----------------------------------------------------

[](https://github.com/tradytics/eiten?screenshot=true#eiten---algorithmic-investing-strategies-for-everyone)

Eiten is an open source toolkit by [Tradytics](https://www.tradytics.com/) that implements various statistical and algorithmic investing strategies such as **Eigen Portfolios**, **Minimum Variance Portfolios**, **Maximum Sharpe Ratio Portfolios**, and **Genetic Algorithms** based Portfolios. It allows you to build your own portfolios with your own set of stocks that can beat the market. The rigorous testing framework included in Eiten enables you to have confidence in your portfolios.

If you are looking to discuss these tools in depth and talk about more tools that we are working on, please feel free to join our [Discord](https://discord.gg/QuvE2Z8) channel where we have a bunch of more tools too.

### Files Description

[](https://github.com/tradytics/eiten?screenshot=true#files-description)

| Path | Description |
| --- | --- |
| eiten | Main folder. |
| └  figures | Figures for this github repositories. |
| └  stocks | Folder to keep your stock lists that you want to use to create your portfolios. |
| └  strategies | A bunch of strategies implemented in python. |
| backtester.py | Backtesting module that both backtests and forward tests all portfolios. |
| data\_loader.py | Module for loading data from yahoo finance. |
| portfolio\_manager.py | Main file that takes in a bunch of arguments and generates several portfolios for you. |
| simulator.py | Simulator that uses historical returns and monte carlo to simulate future prices for the portfolios. |
| strategy\_manager.py | Manages the strategies implemented in the 'strategies' folder. |

Required Packages
-----------------

[](https://github.com/tradytics/eiten?screenshot=true#required-packages)

You will need to install the following package to train and test the models.

*   [Scikit-learn](https://scikit-learn.org/)
*   [Numpy](https://numpy.org/)
*   [Tqdm](https://github.com/tqdm/tqdm)
*   [Yfinance](https://github.com/ranaroussi/yfinance)
*   [Pandas](https://pandas.pydata.org/)
*   [Scipy](https://www.scipy.org/install.html)

You can install all packages using the following command. Please note that the script was written using python3.

```
pip install -r requirements.txt
```

Build your portfolios
---------------------

[](https://github.com/tradytics/eiten?screenshot=true#build-your-portfolios)

Let us see how we can use all the strategies given in the toolkit to build our portfolios. The first thing you need to do is modify the **stocks.txt** file in the **stocks** folder and add the stocks of your choice. It is recommended to keep the list small i.e anywhere between **5 to 50** stocks should be fine. We have already put a small stocks list containing a bunch of tech stocks like AAPL, MSFT, TSLA etc. Let us build our portfolios now. This is the main command that you need to run.

```
python portfolio_manager.py --is_test 1 --future_bars 90 --data_granularity_minutes 3600 --history_to_use all --apply_noise_filtering 1 --market_index QQQ --only_long 1 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt
```

This command will use last 5 years of daily data excluding the last 90 days and build several portfolios for you. Based on those portfolios, it will then test them on the out of sample data of 90 days and show you the performance of each portfolio. Finally, it will also compare the performance with your choice of market index which is **QQQ** here. Let's dive into each of the parameters in detail.

*   **is\_test**: The value determined if the program is going to keep some separate data for future testing. When this is enabled, the value of **future\_bars** should be larger than 5.
*   **future\_bars**: These are the bars that the tool will exclude during portfolio building and will forward test the portfolios on the excluded set. This is also called out of sample data.
*   **data\_granularity\_minutes**: How much granular data do you want to use to build your portfolios. For long term portfolios, you should use daily data but for short term, you can use hourly or minute level data. The possible values here are **3600, 60, 30, 15, 5, 1.** 3600 means daily.
*   **history\_to\_use**: Whether to use a specific number of historical bars or use everything that we receive from yahoo finance. For minute level data, we only receive up to one month of historical data. For daily, we receive 5 years worth of historical data. If you want to use all available data, the value should be **all** but if you want to use smaller history, you can set it to an integer value e.g **100** which will only use the last 100 bars to build the portfolios.
*   **apply\_noise\_filtering**: This uses [random matrix theory](http://faculty.baruch.cuny.edu/jgatheral/randommatrixcovariance2008.pdf) to filter out the covariance matrix from randomness thus yielding better portfolios. A value of 1 will enable it and 0 will disable it.
*   **market\_index**: Which index do you want to use to compare your portfolios. This should mostly be **SPY** but since we analyzed tech stocks, we used **QQQ**.
*   **only\_long**: Whether to use long only portfolio or enable short selling as well. Long only portfolios have shown to have better performance using algorithmic techniques.
*   **eigen\_portfolio\_number**: Which eigen portfolio to use. Any value between 1-5 should work. The first eigen portfolio (1) represents the market portfolio and should act just like the underlying index such as SPY or QQQ. The second one is orthogonal and uncorrelated to the market and poses the greatest risk and reward. The following ones have reduced risk and reward. Read more on [eigen-portfolios](https://srome.github.io/Eigenvesting-I-Linear-Algebra-Can-Help-You-Choose-Your-Stock-Portfolio/).
*   **stocks\_file\_path**: File that contains the list of stocks that you want to use to build your portfolio.

### Some Portfolio Building Examples

[](https://github.com/tradytics/eiten?screenshot=true#some-portfolio-building-examples)

Here are a few examples for building different types of portfolios.

*   Both **long and short** portfolios by analyzing last **90 days** data and keeping the **last 30 days** as testing data. This will give us 60 days of portfolio construction data and 30 days of testing.

```
python portfolio_manager.py --is_test 1 --future_bars 30 --data_granularity_minutes 3600 --history_to_use 90 --apply_noise_filtering 1 --market_index QQQ --only_long 0 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt
```

*   Only **long portfolio** on **60 minute bars** of the last **30 days**. **No future testing**. Compare the results with **SPY** index instead of QQQ.

```
python portfolio_manager.py --is_test 0 --future_bars 0 --data_granularity_minutes 60 --history_to_use all --apply_noise_filtering 1 --market_index SPY --only_long 1 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt
```

*   **Do not apply noise filtering** on the covariance matrix. Use the **first eigen portfolio** (market portfolio) and compare with SQQQ,

```
python portfolio_manager.py --is_test 1 --future_bars 90 --data_granularity_minutes 3600 --history_to_use all --apply_noise_filtering 0 --market_index SQQQ --only_long 1 --eigen_portfolio_number 1 --stocks_file_path stocks/stocks.txt
```

Portfolio Strategies
--------------------

[](https://github.com/tradytics/eiten?screenshot=true#portfolio-strategies)

Four different portfolio strategies are currently supported by the toolkit.

1.  **Eigen Portfolios**
    1.  These portfolios are orthogonal and uncorrelated to the market in general thus yielding high reward and alpha. However, since they are uncorrelated to the market, they can also provide great risk. The first eigen portfolio is considered to be a market portfolio which is often ignored. The second one is uncorrelated to the others and provides the highest risk and reward. As we go down the numbering, the risk as well as the reward are reduced.
2.  **Minimum Variance Portfolio (MVP)**
    1.  MVP tries to minimize the variance of the portfolio. These portfolios are lowest risk and reward.
3.  **Maximum Sharpe Ratio Portfolio (MSR)**
    1.  MSR solves an optimization problem that tries to maximize the sharpe ratio of the portfolio. It uses past returns during the optimization process which means if past returns are not the same as future returns, the results can vary in future.
4.  **Genetic Algorithm (GA) based Portfolio**
    1.  This is our own implementation of a GA based portfolio that again tries to maximize the sharpe ratio but in a slightly more robust way. This usually provides more robust portfolios than the others.

When you run the command above, our tool will generate portfolios from all these strategies and give them to you. Let us look at some resulting portfolios.

Resulting Portfolios
--------------------

[](https://github.com/tradytics/eiten?screenshot=true#resulting-portfolios)

For the purpose these results, we will use the 9 stocks in the stocks/stocks.txt file. When we run the above command, we first get the portfolio weights for all four strategies. For testing purposes, the above command used last five years of daily data up till April 29th. The remaining data for this year was used for forward testing i.e the portfolio strategies had no access to it when building the portfolios.

**What if my portfolio needs different stocks?**: All you need to do is change the stocks in the stocks.txt file and run the tool again. Here is the final command again that we run in order to get our portfolios:

```
python portfolio_manager.py --is_test 1 --future_bars 90 --data_granularity_minutes 3600 --history_to_use all --apply_noise_filtering 1 --market_index QQQ --only_long 1 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt
```

### Portfolio Weights

[](https://github.com/tradytics/eiten?screenshot=true#portfolio-weights)

[![Image 18](https://github.com/tradytics/eiten/raw/master/figures/portfolio_weights.png)](https://github.com/tradytics/eiten/blob/master/figures/portfolio_weights.png)

We can see that the eigen portfolio is giving a large weight to TSLA while the others are dividing their weights more uniformly. An interesting phenomena happening here is the hedging with **SQQQ** that all the strategies have learned automatically. Every tool is assigning some positive weight to SQQQ while also assigning positive weights to other stocks which indicates that the strategies are automatically trying to hedge the portfolios from risk. Obviously this is not perfect, but just the fact that it's happening is fascinating. Let us look at the backtest results on the last five years prior to April 29, 2020.

### Backtest Results

[](https://github.com/tradytics/eiten?screenshot=true#backtest-results)

[![Image 19](https://github.com/tradytics/eiten/raw/master/figures/backtest_results.png)](https://github.com/tradytics/eiten/blob/master/figures/backtest_results.png)

The backtests look pretty encouraging. The black dotted line is the market index i.e **QQQ**. Other lines are the strategies. Our custom genetic algorithm implementation seems to have the best backtest results because it's an advanced version of other strategies. The eigen portfolio that weighed TSLA the most have the most volatility but its profits are also very high. Finally, as expected, the MVP has the minimum variance and ultimately the least profits. However, since the variance is extremely low, it is a good portfolio for those who want to stay safe. The most interesting part comes next, let us look at the forward or future test results for these portfolios.

### Forward Test Results

[](https://github.com/tradytics/eiten?screenshot=true#forward-test-results)

[![Image 20](https://github.com/tradytics/eiten/raw/master/figures/future_test_results.png)](https://github.com/tradytics/eiten/blob/master/figures/future_test_results.png)

These results are from April 29th, 2020 to September 4th, 2020. The eigen portfolio performed the best but it also had a lot of volatility. Moreover, most of those returns are due to TSLA rocketing in the last few months. After that, our GA algorithm worked quite effectively as it beat the market index. Again, as expected, the MVP had the lowest risk and reward and slowly went up in 4-5 months. This shows the effectiveness and power of these algorithmic portfolio optimization strategies where we've developed different portfolios for different kinds of risk and reward profiles.

Conclusion and Discussion
-------------------------

[](https://github.com/tradytics/eiten?screenshot=true#conclusion-and-discussion)

We are happy to share this toolkit with the trading community and hope that people will like and contribute to it. As is the case with everything in trading, these strategies are not perfect but they are based on rigorous theory and some great empirical results. Please take care when trading with these strategies and always manage your risk. The above results were not cherry picked but the market has been highly bullish in the last few months which has led to the strong results shown above. We would love for the community to try out different strategies and share them with us.

#### Special Thanks

[](https://github.com/tradytics/eiten?screenshot=true#special-thanks)

Special thanks to [Scott Rome's](https://srome.github.io/) blog. The eigen portfolios and minimum variance portfolio concepts came from his blog posts. The code for filtering eigen values of the covariance matrix was also mostly obtained from one of his posts.

License
-------

[](https://github.com/tradytics/eiten?screenshot=true#license)

[![Image 21: License: GPL v3](https://camo.githubusercontent.com/8a398fc9fbf479a323d2d91b9fcb6fb9c6b4d08e96dbb544488ccbed312115fc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d47504c76332d626c75652e737667)](https://www.gnu.org/licenses/gpl-3.0)

A product by [Tradytics](https://www.tradytics.com/)

Copyright (c) 2020-present, Tradytics.com

## Metadata

```json
{
  "title": "GitHub - tradytics/eiten: Statistical and Algorithmic Investing Strategies for Everyone",
  "description": "Statistical and Algorithmic Investing Strategies for Everyone - tradytics/eiten",
  "url": "https://github.com/tradytics/eiten?screenshot=true",
  "content": "[![Image 17](https://github.com/tradytics/eiten/raw/master/figures/normal-512x512.png)](https://github.com/tradytics/eiten/blob/master/figures/normal-512x512.png)\n\nEiten - Algorithmic Investing Strategies for Everyone\n-----------------------------------------------------\n\n[](https://github.com/tradytics/eiten?screenshot=true#eiten---algorithmic-investing-strategies-for-everyone)\n\nEiten is an open source toolkit by [Tradytics](https://www.tradytics.com/) that implements various statistical and algorithmic investing strategies such as **Eigen Portfolios**, **Minimum Variance Portfolios**, **Maximum Sharpe Ratio Portfolios**, and **Genetic Algorithms** based Portfolios. It allows you to build your own portfolios with your own set of stocks that can beat the market. The rigorous testing framework included in Eiten enables you to have confidence in your portfolios.\n\nIf you are looking to discuss these tools in depth and talk about more tools that we are working on, please feel free to join our [Discord](https://discord.gg/QuvE2Z8) channel where we have a bunch of more tools too.\n\n### Files Description\n\n[](https://github.com/tradytics/eiten?screenshot=true#files-description)\n\n| Path | Description |\n| --- | --- |\n| eiten | Main folder. |\n| └  figures | Figures for this github repositories. |\n| └  stocks | Folder to keep your stock lists that you want to use to create your portfolios. |\n| └  strategies | A bunch of strategies implemented in python. |\n| backtester.py | Backtesting module that both backtests and forward tests all portfolios. |\n| data\\_loader.py | Module for loading data from yahoo finance. |\n| portfolio\\_manager.py | Main file that takes in a bunch of arguments and generates several portfolios for you. |\n| simulator.py | Simulator that uses historical returns and monte carlo to simulate future prices for the portfolios. |\n| strategy\\_manager.py | Manages the strategies implemented in the 'strategies' folder. |\n\nRequired Packages\n-----------------\n\n[](https://github.com/tradytics/eiten?screenshot=true#required-packages)\n\nYou will need to install the following package to train and test the models.\n\n*   [Scikit-learn](https://scikit-learn.org/)\n*   [Numpy](https://numpy.org/)\n*   [Tqdm](https://github.com/tqdm/tqdm)\n*   [Yfinance](https://github.com/ranaroussi/yfinance)\n*   [Pandas](https://pandas.pydata.org/)\n*   [Scipy](https://www.scipy.org/install.html)\n\nYou can install all packages using the following command. Please note that the script was written using python3.\n\n```\npip install -r requirements.txt\n```\n\nBuild your portfolios\n---------------------\n\n[](https://github.com/tradytics/eiten?screenshot=true#build-your-portfolios)\n\nLet us see how we can use all the strategies given in the toolkit to build our portfolios. The first thing you need to do is modify the **stocks.txt** file in the **stocks** folder and add the stocks of your choice. It is recommended to keep the list small i.e anywhere between **5 to 50** stocks should be fine. We have already put a small stocks list containing a bunch of tech stocks like AAPL, MSFT, TSLA etc. Let us build our portfolios now. This is the main command that you need to run.\n\n```\npython portfolio_manager.py --is_test 1 --future_bars 90 --data_granularity_minutes 3600 --history_to_use all --apply_noise_filtering 1 --market_index QQQ --only_long 1 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt\n```\n\nThis command will use last 5 years of daily data excluding the last 90 days and build several portfolios for you. Based on those portfolios, it will then test them on the out of sample data of 90 days and show you the performance of each portfolio. Finally, it will also compare the performance with your choice of market index which is **QQQ** here. Let's dive into each of the parameters in detail.\n\n*   **is\\_test**: The value determined if the program is going to keep some separate data for future testing. When this is enabled, the value of **future\\_bars** should be larger than 5.\n*   **future\\_bars**: These are the bars that the tool will exclude during portfolio building and will forward test the portfolios on the excluded set. This is also called out of sample data.\n*   **data\\_granularity\\_minutes**: How much granular data do you want to use to build your portfolios. For long term portfolios, you should use daily data but for short term, you can use hourly or minute level data. The possible values here are **3600, 60, 30, 15, 5, 1.** 3600 means daily.\n*   **history\\_to\\_use**: Whether to use a specific number of historical bars or use everything that we receive from yahoo finance. For minute level data, we only receive up to one month of historical data. For daily, we receive 5 years worth of historical data. If you want to use all available data, the value should be **all** but if you want to use smaller history, you can set it to an integer value e.g **100** which will only use the last 100 bars to build the portfolios.\n*   **apply\\_noise\\_filtering**: This uses [random matrix theory](http://faculty.baruch.cuny.edu/jgatheral/randommatrixcovariance2008.pdf) to filter out the covariance matrix from randomness thus yielding better portfolios. A value of 1 will enable it and 0 will disable it.\n*   **market\\_index**: Which index do you want to use to compare your portfolios. This should mostly be **SPY** but since we analyzed tech stocks, we used **QQQ**.\n*   **only\\_long**: Whether to use long only portfolio or enable short selling as well. Long only portfolios have shown to have better performance using algorithmic techniques.\n*   **eigen\\_portfolio\\_number**: Which eigen portfolio to use. Any value between 1-5 should work. The first eigen portfolio (1) represents the market portfolio and should act just like the underlying index such as SPY or QQQ. The second one is orthogonal and uncorrelated to the market and poses the greatest risk and reward. The following ones have reduced risk and reward. Read more on [eigen-portfolios](https://srome.github.io/Eigenvesting-I-Linear-Algebra-Can-Help-You-Choose-Your-Stock-Portfolio/).\n*   **stocks\\_file\\_path**: File that contains the list of stocks that you want to use to build your portfolio.\n\n### Some Portfolio Building Examples\n\n[](https://github.com/tradytics/eiten?screenshot=true#some-portfolio-building-examples)\n\nHere are a few examples for building different types of portfolios.\n\n*   Both **long and short** portfolios by analyzing last **90 days** data and keeping the **last 30 days** as testing data. This will give us 60 days of portfolio construction data and 30 days of testing.\n\n```\npython portfolio_manager.py --is_test 1 --future_bars 30 --data_granularity_minutes 3600 --history_to_use 90 --apply_noise_filtering 1 --market_index QQQ --only_long 0 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt\n```\n\n*   Only **long portfolio** on **60 minute bars** of the last **30 days**. **No future testing**. Compare the results with **SPY** index instead of QQQ.\n\n```\npython portfolio_manager.py --is_test 0 --future_bars 0 --data_granularity_minutes 60 --history_to_use all --apply_noise_filtering 1 --market_index SPY --only_long 1 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt\n```\n\n*   **Do not apply noise filtering** on the covariance matrix. Use the **first eigen portfolio** (market portfolio) and compare with SQQQ,\n\n```\npython portfolio_manager.py --is_test 1 --future_bars 90 --data_granularity_minutes 3600 --history_to_use all --apply_noise_filtering 0 --market_index SQQQ --only_long 1 --eigen_portfolio_number 1 --stocks_file_path stocks/stocks.txt\n```\n\nPortfolio Strategies\n--------------------\n\n[](https://github.com/tradytics/eiten?screenshot=true#portfolio-strategies)\n\nFour different portfolio strategies are currently supported by the toolkit.\n\n1.  **Eigen Portfolios**\n    1.  These portfolios are orthogonal and uncorrelated to the market in general thus yielding high reward and alpha. However, since they are uncorrelated to the market, they can also provide great risk. The first eigen portfolio is considered to be a market portfolio which is often ignored. The second one is uncorrelated to the others and provides the highest risk and reward. As we go down the numbering, the risk as well as the reward are reduced.\n2.  **Minimum Variance Portfolio (MVP)**\n    1.  MVP tries to minimize the variance of the portfolio. These portfolios are lowest risk and reward.\n3.  **Maximum Sharpe Ratio Portfolio (MSR)**\n    1.  MSR solves an optimization problem that tries to maximize the sharpe ratio of the portfolio. It uses past returns during the optimization process which means if past returns are not the same as future returns, the results can vary in future.\n4.  **Genetic Algorithm (GA) based Portfolio**\n    1.  This is our own implementation of a GA based portfolio that again tries to maximize the sharpe ratio but in a slightly more robust way. This usually provides more robust portfolios than the others.\n\nWhen you run the command above, our tool will generate portfolios from all these strategies and give them to you. Let us look at some resulting portfolios.\n\nResulting Portfolios\n--------------------\n\n[](https://github.com/tradytics/eiten?screenshot=true#resulting-portfolios)\n\nFor the purpose these results, we will use the 9 stocks in the stocks/stocks.txt file. When we run the above command, we first get the portfolio weights for all four strategies. For testing purposes, the above command used last five years of daily data up till April 29th. The remaining data for this year was used for forward testing i.e the portfolio strategies had no access to it when building the portfolios.\n\n**What if my portfolio needs different stocks?**: All you need to do is change the stocks in the stocks.txt file and run the tool again. Here is the final command again that we run in order to get our portfolios:\n\n```\npython portfolio_manager.py --is_test 1 --future_bars 90 --data_granularity_minutes 3600 --history_to_use all --apply_noise_filtering 1 --market_index QQQ --only_long 1 --eigen_portfolio_number 3 --stocks_file_path stocks/stocks.txt\n```\n\n### Portfolio Weights\n\n[](https://github.com/tradytics/eiten?screenshot=true#portfolio-weights)\n\n[![Image 18](https://github.com/tradytics/eiten/raw/master/figures/portfolio_weights.png)](https://github.com/tradytics/eiten/blob/master/figures/portfolio_weights.png)\n\nWe can see that the eigen portfolio is giving a large weight to TSLA while the others are dividing their weights more uniformly. An interesting phenomena happening here is the hedging with **SQQQ** that all the strategies have learned automatically. Every tool is assigning some positive weight to SQQQ while also assigning positive weights to other stocks which indicates that the strategies are automatically trying to hedge the portfolios from risk. Obviously this is not perfect, but just the fact that it's happening is fascinating. Let us look at the backtest results on the last five years prior to April 29, 2020.\n\n### Backtest Results\n\n[](https://github.com/tradytics/eiten?screenshot=true#backtest-results)\n\n[![Image 19](https://github.com/tradytics/eiten/raw/master/figures/backtest_results.png)](https://github.com/tradytics/eiten/blob/master/figures/backtest_results.png)\n\nThe backtests look pretty encouraging. The black dotted line is the market index i.e **QQQ**. Other lines are the strategies. Our custom genetic algorithm implementation seems to have the best backtest results because it's an advanced version of other strategies. The eigen portfolio that weighed TSLA the most have the most volatility but its profits are also very high. Finally, as expected, the MVP has the minimum variance and ultimately the least profits. However, since the variance is extremely low, it is a good portfolio for those who want to stay safe. The most interesting part comes next, let us look at the forward or future test results for these portfolios.\n\n### Forward Test Results\n\n[](https://github.com/tradytics/eiten?screenshot=true#forward-test-results)\n\n[![Image 20](https://github.com/tradytics/eiten/raw/master/figures/future_test_results.png)](https://github.com/tradytics/eiten/blob/master/figures/future_test_results.png)\n\nThese results are from April 29th, 2020 to September 4th, 2020. The eigen portfolio performed the best but it also had a lot of volatility. Moreover, most of those returns are due to TSLA rocketing in the last few months. After that, our GA algorithm worked quite effectively as it beat the market index. Again, as expected, the MVP had the lowest risk and reward and slowly went up in 4-5 months. This shows the effectiveness and power of these algorithmic portfolio optimization strategies where we've developed different portfolios for different kinds of risk and reward profiles.\n\nConclusion and Discussion\n-------------------------\n\n[](https://github.com/tradytics/eiten?screenshot=true#conclusion-and-discussion)\n\nWe are happy to share this toolkit with the trading community and hope that people will like and contribute to it. As is the case with everything in trading, these strategies are not perfect but they are based on rigorous theory and some great empirical results. Please take care when trading with these strategies and always manage your risk. The above results were not cherry picked but the market has been highly bullish in the last few months which has led to the strong results shown above. We would love for the community to try out different strategies and share them with us.\n\n#### Special Thanks\n\n[](https://github.com/tradytics/eiten?screenshot=true#special-thanks)\n\nSpecial thanks to [Scott Rome's](https://srome.github.io/) blog. The eigen portfolios and minimum variance portfolio concepts came from his blog posts. The code for filtering eigen values of the covariance matrix was also mostly obtained from one of his posts.\n\nLicense\n-------\n\n[](https://github.com/tradytics/eiten?screenshot=true#license)\n\n[![Image 21: License: GPL v3](https://camo.githubusercontent.com/8a398fc9fbf479a323d2d91b9fcb6fb9c6b4d08e96dbb544488ccbed312115fc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d47504c76332d626c75652e737667)](https://www.gnu.org/licenses/gpl-3.0)\n\nA product by [Tradytics](https://www.tradytics.com/)\n\nCopyright (c) 2020-present, Tradytics.com",
  "usage": {
    "tokens": 3310
  }
}
```
