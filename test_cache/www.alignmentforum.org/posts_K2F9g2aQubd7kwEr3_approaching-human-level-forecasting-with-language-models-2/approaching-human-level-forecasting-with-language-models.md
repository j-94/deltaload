---
title: Approaching Human-Level Forecasting with Language Models
description: TL;DR: We present a retrieval-augmented LM system that nears the human crowd performance on judgemental forecasting. …
url: https://www.alignmentforum.org/posts/K2F9g2aQubd7kwEr3/approaching-human-level-forecasting-with-language-models-2
timestamp: 2025-01-20T15:59:05.766Z
domain: www.alignmentforum.org
path: posts_K2F9g2aQubd7kwEr3_approaching-human-level-forecasting-with-language-models-2
---

# Approaching Human-Level Forecasting with Language Models


TL;DR: We present a retrieval-augmented LM system that nears the human crowd performance on judgemental forecasting. …


## Content

_TL;DR_: We present a retrieval-augmented LM system that nears the human crowd performance on judgemental forecasting.

_Paper_: [https://arxiv.org/abs/2402.18563](https://arxiv.org/abs/2402.18563) (Danny Halawi\*, Fred Zhang\*, Chen Yueh-Han\*, and Jacob Steinhardt)

Twitter thread: [https://twitter.com/JacobSteinhardt/status/1763243868353622089](https://twitter.com/JacobSteinhardt/status/1763243868353622089)

Abstract
--------

Forecasting future events is important for policy and decision-making. In this work, we study whether language models (LMs) can forecast at the level of competitive human forecasters. Towards this goal, we develop a retrieval-augmented LM system designed to automatically search for relevant information, generate forecasts, and aggregate predictions. To facilitate our study, we collect a large dataset of questions from competitive forecasting platforms. Under a test set published after the knowledge cut-offs of our LMs, we evaluate the end-to-end performance of our system against the aggregates of human forecasts. On average, the system nears the crowd aggregate of competitive forecasters and in some settings, surpasses it. Our work suggests that using LMs to forecast the future could provide accurate predictions at scale and help inform institutional decision-making.

For safety motivations on automated forecasting, see [Unsolved Problems in ML Safety (2021)](https://arxiv.org/abs/2109.13916) for discussions. In the following, we summarize our main research findings.

Current LMs are not naturally good at forecasting
-------------------------------------------------

First, we find that LMs are not naturally good at forecasting when evaluated zero-shot (with no fine-tuning and no retrieval). On 914 test questions that were opened after June 1, 2023 (post the knowledge cut-offs of these models), most LMs get near chance performance.![Image 9](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/K2F9g2aQubd7kwEr3/hd2ld6jw4rmpa7kco2tz)

Here, all questions are binary, so random guessing gives a Brier score of 0.25. Averaging across all community predictions over time, the human crowd gets 0.149. We present the score of the best model of each series. Only GPT-4 and Claude-2 series beat random guessing (by a margin of \>0.3), though still very far from human aggregates.

System building
---------------

Towards better automated forecasting, we build and optimize a retrieval-augmented LM pipeline for this task.

![Image 10](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/K2F9g2aQubd7kwEr3/kt6ockpmcvkqflxwiiwi)

It functions in 3 steps, mimicking the traditional forecasting procedure:

1.  Retrieval, which gathers relevant information from news sources. Here, we use LM to generate search queries given a question, use these queries to query a news corpus for articles, filter out irrelevant articles, and summarize the remaining.
2.  Reasoning, which weighs available data and makes a forecast. Here, we prompt base and fine-tuned GPT-4 models to generate forecasts and (verbal) reasonings. 
3.  Aggregation, which ensembles individual forecasts into an aggregated prediction. We use trimmed mean to aggregate all the predictions. 

We optimize the system’s hyperparameters and apply a self-supervised approach to fine-tune a base GPT-4 to obtain the fine-tuned LM. See Section 5 of [the full paper](https://arxiv.org/abs/2402.18563) for details.

Data and models
---------------

We use GPT-4-1106 and GPT-3.5 in our system, whose knowledge cut-offs are in April 2023 and September 2021.

To optimize and evaluate the system, we collect a dataset of forecasting questions from 5 competitive forecasting platforms, including Metaculus, Good Judgment Open, INFER, Polymarket, and Manifold.

*   The test set consists _only_ of questions published after June 1st, 2023. Crucially, this is after the knowledge cut-off date of GPT-4 and GPT-3.5, preventing leakage from pre-training. 
*   The train and validation set contains questions before June 1st, 2023, used for hyperparameter search and fine-tuning a GPT-4 base model.

Evaluation results
------------------

For each question, we perform information retrieval at up to 5 different dates during the question’s time span and evaluate our system against community aggregates at each date. (This simulates “forecasting” on past, resolved questions with pre-trained models, a methodology first introduced by [Zou et al, 2022](https://arxiv.org/abs/2206.15474).)

### Unconditional setting

Averaging over a test set of 914 questions and all retrieval points, our system gets an average Brier score of 0.179 vs. crowd 0.149 and an accuracy of 71.5% vs the crowd 77.0%. This significantly improves upon the baseline evaluation we had earlier.

### Selective setting

Through a study on the validation set, we find that our system performs best relative to the crowd along several axes, which hold on the test set:

1.  On questions when the crowd prediction falls between .3 and .7 (i.e., when humans are quite uncertain), it gets a Brier score of .238 (crowd aggregate: .240).
2.  On the earlier retrieval dates (1, 2, and 3), it gets a Brier score of .185 (crowd aggregate: .161). 
3.  When the retrieval system provides at least 5 relevant articles, it gets a Brier score of .175 (crowd aggregate: .143).
4.  Under all three conditions, our system attains a Brier score of .240 (crowd aggregate: .247).

In both 1 and 4, our system actually beats the human crowd.

More interestingly, by taking a (weighted) average of our system and the crowd’s prediction, we always get better scores than both of them, even unconditionally! Conceptually, this shows that our system can be used to complement the human forecasters.

**![Image 11](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/K2F9g2aQubd7kwEr3/hjamcgxphc3mtgsz2cox)**

### Calibration

Finally, we compare our system's calibration against the human crowd. On the test set (figure (c) below), our system is nearly as well calibrated, with RMS calibration error .42 (human crowd: .38).

Interestingly, this is not the case in the baseline evaluation, where the base models are not well calibrated under the zero-shot setting (figure (a) below). Our system, through fine-tuning and ensembling, improves the calibration of the base models, without undergoing specific training for calibration.

![Image 12](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/K2F9g2aQubd7kwEr3/ufulbgr2o6ung9gdorbp)

Future work
-----------

Our results suggest that in the near future, LM-based systems may be able to generate accurate forecasts at the level of competitive human forecasters.

In Section 7 of [the paper](https://arxiv.org/abs/2402.18563), we discuss some directions that we find promising towards this goal, including iteratively applying our fine-tuning method, gathering more forecasting data from the wild for better training, and more.

## Metadata

```json
{
  "title": "Approaching Human-Level Forecasting with Language Models",
  "description": "TL;DR: We present a retrieval-augmented LM system that nears the human crowd performance on judgemental forecasting. …",
  "url": "https://www.alignmentforum.org/posts/K2F9g2aQubd7kwEr3/approaching-human-level-forecasting-with-language-models-2",
  "content": "_TL;DR_: We present a retrieval-augmented LM system that nears the human crowd performance on judgemental forecasting.\n\n_Paper_: [https://arxiv.org/abs/2402.18563](https://arxiv.org/abs/2402.18563) (Danny Halawi\\*, Fred Zhang\\*, Chen Yueh-Han\\*, and Jacob Steinhardt)\n\nTwitter thread: [https://twitter.com/JacobSteinhardt/status/1763243868353622089](https://twitter.com/JacobSteinhardt/status/1763243868353622089)\n\nAbstract\n--------\n\nForecasting future events is important for policy and decision-making. In this work, we study whether language models (LMs) can forecast at the level of competitive human forecasters. Towards this goal, we develop a retrieval-augmented LM system designed to automatically search for relevant information, generate forecasts, and aggregate predictions. To facilitate our study, we collect a large dataset of questions from competitive forecasting platforms. Under a test set published after the knowledge cut-offs of our LMs, we evaluate the end-to-end performance of our system against the aggregates of human forecasts. On average, the system nears the crowd aggregate of competitive forecasters and in some settings, surpasses it. Our work suggests that using LMs to forecast the future could provide accurate predictions at scale and help inform institutional decision-making.\n\nFor safety motivations on automated forecasting, see [Unsolved Problems in ML Safety (2021)](https://arxiv.org/abs/2109.13916) for discussions. In the following, we summarize our main research findings.\n\nCurrent LMs are not naturally good at forecasting\n-------------------------------------------------\n\nFirst, we find that LMs are not naturally good at forecasting when evaluated zero-shot (with no fine-tuning and no retrieval). On 914 test questions that were opened after June 1, 2023 (post the knowledge cut-offs of these models), most LMs get near chance performance.![Image 9](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/K2F9g2aQubd7kwEr3/hd2ld6jw4rmpa7kco2tz)\n\nHere, all questions are binary, so random guessing gives a Brier score of 0.25. Averaging across all community predictions over time, the human crowd gets 0.149. We present the score of the best model of each series. Only GPT-4 and Claude-2 series beat random guessing (by a margin of \\>0.3), though still very far from human aggregates.\n\nSystem building\n---------------\n\nTowards better automated forecasting, we build and optimize a retrieval-augmented LM pipeline for this task.\n\n![Image 10](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/K2F9g2aQubd7kwEr3/kt6ockpmcvkqflxwiiwi)\n\nIt functions in 3 steps, mimicking the traditional forecasting procedure:\n\n1.  Retrieval, which gathers relevant information from news sources. Here, we use LM to generate search queries given a question, use these queries to query a news corpus for articles, filter out irrelevant articles, and summarize the remaining.\n2.  Reasoning, which weighs available data and makes a forecast. Here, we prompt base and fine-tuned GPT-4 models to generate forecasts and (verbal) reasonings. \n3.  Aggregation, which ensembles individual forecasts into an aggregated prediction. We use trimmed mean to aggregate all the predictions. \n\nWe optimize the system’s hyperparameters and apply a self-supervised approach to fine-tune a base GPT-4 to obtain the fine-tuned LM. See Section 5 of [the full paper](https://arxiv.org/abs/2402.18563) for details.\n\nData and models\n---------------\n\nWe use GPT-4-1106 and GPT-3.5 in our system, whose knowledge cut-offs are in April 2023 and September 2021.\n\nTo optimize and evaluate the system, we collect a dataset of forecasting questions from 5 competitive forecasting platforms, including Metaculus, Good Judgment Open, INFER, Polymarket, and Manifold.\n\n*   The test set consists _only_ of questions published after June 1st, 2023. Crucially, this is after the knowledge cut-off date of GPT-4 and GPT-3.5, preventing leakage from pre-training. \n*   The train and validation set contains questions before June 1st, 2023, used for hyperparameter search and fine-tuning a GPT-4 base model.\n\nEvaluation results\n------------------\n\nFor each question, we perform information retrieval at up to 5 different dates during the question’s time span and evaluate our system against community aggregates at each date. (This simulates “forecasting” on past, resolved questions with pre-trained models, a methodology first introduced by [Zou et al, 2022](https://arxiv.org/abs/2206.15474).)\n\n### Unconditional setting\n\nAveraging over a test set of 914 questions and all retrieval points, our system gets an average Brier score of 0.179 vs. crowd 0.149 and an accuracy of 71.5% vs the crowd 77.0%. This significantly improves upon the baseline evaluation we had earlier.\n\n### Selective setting\n\nThrough a study on the validation set, we find that our system performs best relative to the crowd along several axes, which hold on the test set:\n\n1.  On questions when the crowd prediction falls between .3 and .7 (i.e., when humans are quite uncertain), it gets a Brier score of .238 (crowd aggregate: .240).\n2.  On the earlier retrieval dates (1, 2, and 3), it gets a Brier score of .185 (crowd aggregate: .161). \n3.  When the retrieval system provides at least 5 relevant articles, it gets a Brier score of .175 (crowd aggregate: .143).\n4.  Under all three conditions, our system attains a Brier score of .240 (crowd aggregate: .247).\n\nIn both 1 and 4, our system actually beats the human crowd.\n\nMore interestingly, by taking a (weighted) average of our system and the crowd’s prediction, we always get better scores than both of them, even unconditionally! Conceptually, this shows that our system can be used to complement the human forecasters.\n\n**![Image 11](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/K2F9g2aQubd7kwEr3/hjamcgxphc3mtgsz2cox)**\n\n### Calibration\n\nFinally, we compare our system's calibration against the human crowd. On the test set (figure (c) below), our system is nearly as well calibrated, with RMS calibration error .42 (human crowd: .38).\n\nInterestingly, this is not the case in the baseline evaluation, where the base models are not well calibrated under the zero-shot setting (figure (a) below). Our system, through fine-tuning and ensembling, improves the calibration of the base models, without undergoing specific training for calibration.\n\n![Image 12](https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/K2F9g2aQubd7kwEr3/ufulbgr2o6ung9gdorbp)\n\nFuture work\n-----------\n\nOur results suggest that in the near future, LM-based systems may be able to generate accurate forecasts at the level of competitive human forecasters.\n\nIn Section 7 of [the paper](https://arxiv.org/abs/2402.18563), we discuss some directions that we find promising towards this goal, including iteratively applying our fine-tuning method, gathering more forecasting data from the wild for better training, and more.",
  "publishedTime": "2024-02-29T22:36:34.012Z",
  "usage": {
    "tokens": 1706
  }
}
```
