---
title: TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation | Proceedings of the 17th ACM Conference on Recommender Systems
description: 
url: https://dl.acm.org/doi/10.1145/3604915.3608857#sec-cit
timestamp: 2025-01-20T15:46:51.186Z
domain: dl.acm.org
path: doi_10.1145_3604915.3608857
---

# TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation | Proceedings of the 17th ACM Conference on Recommender Systems



## Content

[Authors Info & Claims](https://dl.acm.org/doi/10.1145/3604915.3608857#tab-contributors)

Published: 14 September 2023 [Publication History](https://dl.acm.org/doi/10.1145/3604915.3608857#core-history)

[](https://dl.acm.org/doi/10.1145/3604915.3608857# "Check for updates on crossmark")

Abstract
--------

Large Language Models (LLMs) have demonstrated remarkable performance across diverse domains, thereby prompting researchers to explore their potential for use in recommendation systems. Initial attempts have leveraged the exceptional capabilities of LLMs, such as rich knowledge and strong generalization through In-context Learning, which involves phrasing the recommendation task as prompts. Nevertheless, the performance of LLMs in recommendation tasks remains suboptimal due to a substantial disparity between the training tasks for LLMs and recommendation tasks, as well as inadequate recommendation data during pre-training. To bridge the gap, we consider building a Large Recommendation Language Model by tunning LLMs with recommendation data. To this end, we propose an efficient and effective Tuning framework for Aligning LLMs with Recommendations, namely TALLRec. We have demonstrated that the proposed TALLRec framework can significantly enhance the recommendation capabilities of LLMs in the movie and book domains, even with a limited dataset of fewer than 100 samples. Additionally, the proposed framework is highly efficient and can be executed on a single RTX 3090 with LLaMA-7B. Furthermore, the fine-tuned LLM exhibits robust cross-domain generalization. Our code and data are available at https://github.com/SAI990323/TALLRec.

Supplemental Material
---------------------

ZIP File

Recsys 2023 short paper

*   [Download](https://dl.acm.org/doi/suppl/10.1145/3604915.3608857/suppl_file/recsys23-110.zip)
*   1.76 MB

References
----------

\[1\]

Qingyao Ai, Ting Bai, Zhao Cao, Yi Chang, Jiawei Chen, Zhumin Chen, Zhiyong Cheng, Shoubin Dong, Zhicheng Dou, Fuli Feng, 2023. Information Retrieval Meets Large Language Models: A Strategic Report from Chinese IR Community. arXiv preprint arXiv:2307.09751 (2023).

\[2\]

Greg Brockman, Mira Murati, Peter Welinder, and OpenAI. 2022. OpenAI API.

\[3\]

Tom Brown, Benjamin Mann, Nick Ryder, 2020. Language models are few-shot learners. NeurIPS 33 (2020), 1877–1901.

\[4\]

Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, 2022. Palm: Scaling language modeling with pathways. arXiv preprint arXiv:2204.02311 (2022).

\[5\]

Qiang Cui, Shu Wu, Qiang Liu, Wen Zhong, and Liang Wang. 2020. MV-RNN: A Multi-View Recurrent Neural Network for Sequential Recommendation. IEEE Trans. Knowl. Data Eng. 32, 2 (2020), 317–331.

\[6\]

Zeyu Cui, Jianxin Ma, Chang Zhou, Jingren Zhou, and Hongxia Yang. 2022. M6-Rec: Generative Pretrained Language Models are Open-Ended Recommender Systems. arXiv preprint arXiv:2205.08084 (2022).

\[7\]

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In NAACL. Association for Computational Linguistics, 4171–4186.

\[8\]

Sihao Ding, Fuli Feng, Xiangnan He, Jinqiu Jin, Wenjie Wang, Yong Liao, and Yongdong Zhang. 2022. Interpolative Distillation for Unifying Biased and Debiased Recommendation. In SIGIR ’22, July 11 - 15, 2022. ACM, 40–49.

\[9\]

Tim Donkers, Benedikt Loepp, and Jürgen Ziegler. 2017. Sequential user-based recurrent neural network recommendations. In Proceedings of the eleventh ACM conference on recommender systems. 152–160.

\[10\]

Danny Driess, Fei Xia, Mehdi S. M. Sajjadi, 2023. PaLM-E: An Embodied Multimodal Language Model. abs/2303.03378 (2023). arXiv:2303.03378

\[11\]

Hui Fang, Danning Zhang, Yiheng Shu, and Guibing Guo. 2020. Deep Learning for Sequential Recommendation: Algorithms, Influential Factors, and Evaluations. ACM Trans. Inf. Syst. 39, 1 (2020), 10:1–10:42.

\[12\]

F.Maxwell and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. In ACM Transactions on Interactive Intelligent Systems (TiiS).

\[13\]

Yunfan Gao 2023. Chat-REC: Towards Interactive and Explainable LLMs-Augmented Recommender System. arXiv preprint:2303.14524 (2023).

\[14\]

Shijie Geng, Shuchang Liu, Zuohui Fu, Yingqiang Ge, and Yongfeng Zhang. 2022. Recommendation as language processing (rlp): A unified pretrain, personalized prompt & predict paradigm (p5). In Proceedings of the 16th ACM Conference on Recommender Systems. 299–315.

\[15\]

Ruining He and Julian McAuley. 2016. Fusing similarity models with markov chains for sparse sequential recommendation. In 2016 IEEE 16th international conference on data mining (ICDM). IEEE, 191–200.

\[16\]

Xiangnan He, Kuan Deng, Xiang Wang, Yan Li, Yongdong Zhang, and Meng Wang. 2020. Lightgcn: Simplifying and powering graph convolution network for recommendation. In SIGIR’20. 639–648.

\[17\]

Balázs Hidasi 2016. Session-based Recommendations with Recurrent Neural Networks. In ICLR.

\[18\]

Jordan Hoffmann 2022. Training compute-optimal large language models. arXiv preprint arXiv:2203.15556 (2022).

\[19\]

Yupeng Hou, Shanlei Mu, Wayne Xin Zhao, Yaliang Li, Bolin Ding, and Ji-Rong Wen. 2022. Towards Universal Sequence Representation Learning for Recommender Systems. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 585–593.

\[20\]

Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, 2019. Parameter-Efficient Transfer Learning for NLP. In Proceedings of the 36th International Conference on Machine Learning, ICML 2019, 9-15 June 2019, Vol. 97\. 2790–2799.

\[21\]

Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. 2022. LoRA: Low-Rank Adaptation of Large Language Models. In The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022.

\[22\]

Srinivasan Iyer, Xi Victoria Lin, Ramakanth Pasunuru, 2022. OPT-IML: Scaling Language Model Instruction Meta Learning through the Lens of Generalization. arXiv preprint arXiv:2212.12017 (2022).

\[23\]

Joel Jang, Seungone Kim, Seonghyeon Ye, Doyoung Kim, Lajanugen Logeswaran, Moontae Lee, Kyungjae Lee, and Minjoon Seo. 2023. Exploring the Benefits of Training Expert Language Models over Instruction Tuning. (2023). arXiv:2302.03202

\[24\]

Vitor Jeronymo, Luiz Henrique Bonifacio, Hugo Abonizio, Marzieh Fadaee, Roberto de Alencar Lotufo, Jakub Zavrel, and Rodrigo Frassetto Nogueira. 2023. InPars-v2: Large Language Models as Efficient Dataset Generators for Information Retrieval. abs/2301.01820 (2023). arXiv:2301.01820

\[25\]

Matthew Jin, Syed Shahriar, Michele Tufano, Xin Shi, Shuai Lu, Neel Sundaresan, and Alexey Svyatkovskiy. 2023. InferFix: End-to-End Program Repair with LLMs. (2023). arXiv:2303.07263

\[26\]

Wang-Cheng Kang and Julian McAuley. 2018. Self-attentive sequential recommendation. In ICDM. 197–206.

\[27\]

Yehuda Koren, Robert Bell, and Chris Volinsky. 2009. Matrix factorization techniques for recommender systems. Computer 42, 8 (2009), 30–37.

\[28\]

Brian Lester, Rami Al-Rfou, and Noah Constant. 2021. The Power of Scale for Parameter-Efficient Prompt Tuning. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, EMNLP,7-11 November, 2021. Association for Computational Linguistics, 3045–3059.

\[29\]

Lei Li, Yongfeng Zhang, and Li Chen. 2023. Personalized prompt learning for explainable recommendation. ACM Transactions on Information Systems 41, 4 (2023), 1–26.

\[30\]

Ruyu Li, Wenhao Deng, Yu Cheng, Zheng Yuan, Jiaqi Zhang, and Fajie Yuan. 2023. Exploring the Upper Limits of Text-Based Collaborative Filtering Using Large Language Models: Discoveries and Insights. arXiv preprint arXiv:2305.11700 (2023).

\[31\]

Xiang Lisa Li and Percy Liang. 2021. Prefix-Tuning: Optimizing Continuous Prompts for Generation. In ACL/IJCNLP 2021, August 1-6, 2021. Association for Computational Linguistics, 4582–4597.

\[32\]

Percy Liang, Rishi Bommasani, Tony Lee, 2022. Holistic evaluation of language models. arXiv preprint arXiv:2211.09110 (2022).

\[33\]

Xi Victoria Lin, Todor Mihaylov, 2021. Few-shot learning with multilingual language models. arXiv preprint arXiv:2112.10668 (2021).

\[34\]

Tariq Mahmood and Francesco Ricci. 2007. Learning and adaptivity in interactive recommender systems. In Proceedings of the ninth international conference on Electronic commerce. 75–84.

\[35\]

Yabo Ni, Dan Ou, Shichen Liu, 2018. Perceive Your Users in Depth: Learning Universal User Representations from Multiple E-commerce Tasks. In KDD 2018, August 19-23, 2018. ACM, 596–605.

\[36\]

Long Ouyang 2022. Training language models to follow instructions with human feedback. NeurIPS 35 (2022), 27730–27744.

\[37\]

Baolin Peng 2023. Instruction Tuning with GPT-4. (2023). arXiv:2304.03277

\[38\]

Ruihong Qiu, Zi Huang, Hongzhi Yin, and Zijian Wang. 2021. Contrastive Learning for Representation Degeneration Problem in Sequential Recommendation. (2021). arXiv:2110.05730

\[39\]

Ruihong Qiu, Zi Huang, Hongzhi Yin, and Zijian Wang. 2022. Contrastive Learning for Representation Degeneration Problem in Sequential Recommendation. In WSDM ’22: The Fifteenth ACM International Conference on Web Search and Data Mining, February 21 - 25, 2022. ACM, 813–823.

\[40\]

Steffen Rendle, Christoph Freudenthaler, and Lars Schmidt-Thieme. 2010. Factorizing personalized markov chains for next-basket recommendation. In Proceedings of the 19th international conference on World wide web. 811–820.

\[41\]

Victor Sanh, Albert Webson, Colin Raffel, 2021. Multitask prompted training enables zero-shot task generalization. arXiv:2110.08207 (2021).

\[42\]

Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. 2023. Toolformer: Language models can teach themselves to use tools. arXiv preprint arXiv:2302.04761 (2023).

\[43\]

Dhruv Shah, Blazej Osinski, Brian Ichter, and Sergey Levine. 2022. LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action. In CoRL 2022, 14-18 December 2022(Proceedings of Machine Learning Research, Vol. 205). PMLR, 492–504.

\[44\]

Jiaxi Tang and Ke Wang. 2018. Personalized top-n sequential recommendation via convolutional sequence embedding. In WSDM. 565–573.

\[45\]

Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and Tatsunori B. Hashimoto. 2023. Stanford Alpaca: An Instruction-following LLaMA model.

\[46\]

Hugo Touvron 2023. LlaMA: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971 (2023).

\[47\]

Lei Wang 2023. Zero-Shot Next-Item Recommendation using Large Pretrained Language Models. arXiv preprint arXiv:2304.03153 (2023).

\[48\]

Liang Wang, Nan Yang, and Furu Wei. 2023. Query2doc: Query Expansion with Large Language Models. (2023). arXiv:2303.07678

\[49\]

Pengfei Wang, Jiafeng Guo, Yanyan Lan, Jun Xu, Shengxian Wan, and Xueqi Cheng. 2015. Learning hierarchical representation model for nextbasket recommendation. In Proceedings of the 38th International ACM SIGIR conference on Research and Development in Information Retrieval. 403–412.

\[50\]

Shoujin Wang, Liang Hu, Yan Wang, Longbing Cao, Quan Z. Sheng, and Mehmet A. Orgun. 2019. Sequential Recommender Systems: Challenges, Progress and Prospects. In IJCAI 2019, Macao, China, August 10-16, 2019. ijcai.org, 6332–6338.

\[51\]

Ziyang Wang, Huoyu Liu, Wei Wei, Yue Hu, Xian-Ling Mao, Shaojian He, Rui Fang, and Dangyang Chen. 2022. Multi-level Contrastive Learning Framework for Sequential Recommendation. (2022). arXiv:2208.13007

\[52\]

Zhenlei Wang, Shiqi Shen, Zhipeng Wang, Bo Chen, Xu Chen, and Ji-Rong Wen. 2022. Unbiased Sequential Recommendation with Latent Confounders. In WWW ’22: The ACM Web Conference 2022, Virtual Event, Lyon, France, April 25 - 29, 2022. ACM, 2195–2204.

\[53\]

Jason Wei, Maarten Bosma, Vincent Y Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M Dai, and Quoc V Le. 2021. Finetuned language models are zero-shot learners. arXiv preprint arXiv:2109.01652 (2021).

\[54\]

Jason Wei, Yi Tay, Rishi Bommasani, 2022. Emergent abilities of large language models. arXiv preprint arXiv:2206.07682 (2022).

\[55\]

Hongyi Wen, Xinyang Yi, Tiansheng Yao, Jiaxi Tang, Lichan Hong, and Ed H. Chi. 2022. Distributionally-robust Recommendations for Improving Worst-case User Experience. In WWW ’22: The ACM Web Conference 2022, Virtual Event, Lyon, France, April 25 - 29, 2022. ACM, 3606–3610.

\[56\]

Ted Xiao, Harris Chan, Pierre Sermanet, Ayzaan Wahid, Anthony Brohan, Karol Hausman, Sergey Levine, and Jonathan Tompson. 2022. Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models. abs/2211.11736 (2022). arXiv:2211.11736

\[57\]

Xu Xie, Fei Sun, Zhaoyang Liu, Shiwen Wu, Jinyang Gao, Jiandong Zhang, Bolin Ding, and Bin Cui. 2022. Contrastive Learning for Sequential Recommendation. In 38th IEEE International Conference on Data Engineering, ICDE 2022, Kuala Lumpur, Malaysia, May 9-12, 2022. IEEE, 1259–1273.

\[58\]

Chengfeng Xu, Jian Feng, Pengpeng Zhao, Fuzhen Zhuang, Deqing Wang, Yanchi Liu, and Victor S. Sheng. 2021. Long- and short-term self-attention network for sequential recommendation. Neurocomputing 423 (2021), 580–589.

\[59\]

An Yan, Shuo Cheng, Wang-Cheng Kang, Mengting Wan, and Julian J. McAuley. 2019. CosRec: 2D Convolutional Neural Networks for Sequential Recommendation. In CIKM 2019, November 3-7, 2019. ACM, 2173–2176.

\[60\]

Zhengyi Yang 2023. A Generic Learning Framework for Sequential Recommendation with Distribution Shifts. (2023).

\[61\]

Fajie Yuan, Xiangnan He, Alexandros Karatzoglou, and Liguang Zhang. 2020. Parameter-Efficient Transfer from Sequential Behaviors for User Modeling and Recommendation. In SIGIR 2020, July 25-30, 2020. ACM, 1469–1478.

\[62\]

Fajie Yuan, Alexandros Karatzoglou, Ioannis Arapakis, Joemon M. Jose, and Xiangnan He. 2019. A Simple Convolutional Generative Network for Next Item Recommendation. In WSDM 2019, February 11-15, 2019. ACM, 582–590.

\[63\]

Zheng Yuan, Fajie Yuan, Yu Song, Youhua Li, Junchen Fu, Fei Yang, Yunzhu Pan, and Yongxin Ni. 2023. Where to Go Next for Recommender Systems? ID- vs. Modality-based Recommender Models Revisited. In Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR 2023, Taipei, Taiwan, July 23-27, 2023, Hsin-Hsi Chen, Wei-Jou (Edward) Duh, Hen-Hsen Huang, Makoto P. Kato, Josiane Mothe, and Barbara Poblete (Eds.). ACM, 2639–2649. https://doi.org/10.1145/3539618.3591932

\[64\]

Jizhi Zhang, Keqin Bao, Yang Zhang, Wenjie Wang, Fuli Feng, and Xiangnan He. 2023. Is chatgpt fair for recommendation? evaluating fairness in large language model recommendation. In Proceedings of the 17th ACM Conference on Recommender Systems(RecSys ’23). Association for Computing Machinery.

\[65\]

Tingting Zhang, Pengpeng Zhao, Yanchi Liu, 2019. Feature-level Deeper Self-Attention Network for Sequential Recommendation. In Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, IJCAI 2019, August 10-16, 2019. ijcai.org, 4320–4326.

\[66\]

Yang Zhang 2023. Reformulating CTR Prediction: Learning Invariant Feature Interactions for Recommendation. (2023).

\[67\]

Yang Zhang, Fuli Feng, Xiangnan He, Tianxin Wei, Chonggang Song, Guohui Ling, and Yongdong Zhang. 2021. Causal Intervention for Leveraging Popularity Bias in Recommendation. In SIGIR ’21, July 11-15, 2021. ACM, 11–20.

\[68\]

Zizhuo Zhang and Bang Wang. 2023. Prompt Learning for News Recommendation. arXiv preprint arXiv:2304.05263 (2023).

\[69\]

Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, Yifan Du, Chen Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, Peiyu Liu, Jian-Yun Nie, and Ji-Rong Wen. 2023. A Survey of Large Language Models. CoRR abs/2303.18223 (2023). https://doi.org/10.48550/arXiv.2303.18223 arXiv:2303.18223

\[70\]

Yu Zheng 2021. Disentangling User Interest and Conformity for Recommendation with Causal Embedding. In WWW ’21. 2980–2991.

\[71\]

Cai-Nicolas Ziegler, Sean M. McNee, Joseph A. Konstan, and Georg Lausen. 2005. Improving Recommendation Lists through Topic Diversification. In Proceedings of the 14th International Conference on World Wide Web(WWW ’05). Association for Computing Machinery, 22–32.

Information & Contributors
--------------------------

### Information

#### Published In

![Image 30: cover image ACM Conferences](https://dl.acm.org/cms/asset/c62a0a4a-67ca-4d0f-a82d-3b2199595c63/3604915.cover.jpg)

RecSys '23: Proceedings of the 17th ACM Conference on Recommender Systems

September 2023

1406 pages

Copyright © 2023 ACM.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from [\[email protected\]](https://dl.acm.org/cdn-cgi/l/email-protection).

#### Publisher

Association for Computing Machinery

New York, NY, United States

#### Publication History

**Published**: 14 September 2023

#### Permissions

Request permissions for this article.

#### Check for updates

[](https://dl.acm.org/doi/10.1145/3604915.3608857# "Check for updates on crossmark")

#### Author Tags

1.  [Instruction Tuning](https://dl.acm.org/keyword/Instruction+Tuning?expand=all)
2.  [Large Language Models](https://dl.acm.org/keyword/Large+Language+Models?expand=all)
3.  [Recommendation](https://dl.acm.org/keyword/Recommendation?expand=all)

#### Qualifiers

*   Short-paper
*   Research
*   Refereed limited

#### Conference

#### Acceptance Rates

Overall Acceptance Rate 254 of 1,295 submissions, 20%

### Contributors

![Image 31](https://dl.acm.org/specs/products/acm/releasedAssets/images/loader-7e60691fbe777356dc81ff6d223a82a6.gif)

#### Other Metrics

Bibliometrics & Citations
-------------------------

### Bibliometrics

#### Article Metrics

*   [View Citations](https://dl.acm.org/doi/10.1145/3604915.3608857#tab-citations)

*   Downloads (Last 12 months)1,661
*   Downloads (Last 6 weeks)190

Reflects downloads up to 17 Jan 2025

#### Other Metrics

### Citations

*   Kim WLim SKim GChoi S(2025)Extracting Implicit User Preferences in Conversational Recommender Systems Using Large Language ModelsMathematics10.3390/math13020221**13**:2(221)Online publication date: 10-Jan-2025
*   Xu TLi B(2025)KELLM: Knowledge-Enhanced Label-Wise Large Language Model for Safe and Interpretable Drug RecommendationElectronics10.3390/electronics14010154**14**:1(154)Online publication date: 2-Jan-2025
*   Wang XChen HPan ZZhou YGuan CSun LZhu W(2025)Automated Disentangled Sequential Recommendation with Large Language ModelsACM Transactions on Information Systems10.1145/3675164**43**:2(1-29)Online publication date: 17-Jan-2025
*   Cheema ASarfraz MHabib UZaman QBoonchieng E(2025)CD-LLMCARS: Cross Domain Fine-Tuned Large Language Model for Context-Aware Recommender SystemsIEEE Open Journal of the Computer Society10.1109/OJCS.2024.3509221**6**(49-59)Online publication date: 2025
*   Jiang MLi MCao WYang MZhou L(2025)Multi-task convolutional deep neural network for recommendation based on knowledge graphsNeurocomputing10.1016/j.neucom.2024.129136**619**(129136)Online publication date: Feb-2025
*   Tang MCui SJin ZLiang SLi CZou L(2025)Sequential recommendation by reprogramming pretrained transformerInformation Processing & Management10.1016/j.ipm.2024.103938**62**:1(103938)Online publication date: Jan-2025
*   Zhai JLiao LLiu XWang YLi RCao XGao LGong ZGu FHe JLu YShi YSalakhutdinov RKolter ZHeller KWeller AOliver NScarlett JBerkenkamp F(2024)Actions speak louder than wordsProceedings of the 41st International Conference on Machine Learning10.5555/3692070.3694484(58484-58509)Online publication date: 21-Jul-2024
*   Qu ZXie RXiao CYao YLiu ZLian FKang ZZhou J(2024)Thoroughly Modeling Multi-domain Pre-trained Recommendation as LanguageACM Transactions on Information Systems10.1145/3708883Online publication date: 19-Dec-2024
*   Chen LGao CDu XLuo HJin DLi YWang M(2024)Enhancing ID-based Recommendation with Large Language ModelsACM Transactions on Information Systems10.1145/3704263Online publication date: 13-Nov-2024
*   Zhang YHu ZBai YWu JWang QFeng F(2024)Recommendation Unlearning via Influence FunctionACM Transactions on Recommender Systems10.1145/3701763**3**:2(1-23)Online publication date: 29-Oct-2024
*   Show More Cited By

View Options
------------

#### Login options

Check if you have access through your login credentials or your institution to get full access on this article.

[Sign in](https://dl.acm.org/action/showLogin?redirectUri=%2Fdoi%2F10.1145%2F3604915.3608857 "Sign in")

#### Full Access

### View options

#### PDF

View or Download as a PDF file.

[PDF](https://dl.acm.org/doi/pdf/10.1145/3604915.3608857 "View PDF")

#### eReader

View online with eReader.

[eReader](https://dl.acm.org/doi/epdf/10.1145/3604915.3608857 "View online with eReader")

#### HTML Format

View this article in HTML Format.

[HTML Format](https://dl.acm.org/doi/fullHtml/10.1145/3604915.3608857 "View this article in HTML Format")

Media
-----

### Figures

### Other

Tables
------

## Metadata

```json
{
  "title": "TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation | Proceedings of the 17th ACM Conference on Recommender Systems",
  "description": "",
  "url": "https://dl.acm.org/doi/10.1145/3604915.3608857#sec-cit",
  "content": "[Authors Info & Claims](https://dl.acm.org/doi/10.1145/3604915.3608857#tab-contributors)\n\nPublished: 14 September 2023 [Publication History](https://dl.acm.org/doi/10.1145/3604915.3608857#core-history)\n\n[](https://dl.acm.org/doi/10.1145/3604915.3608857# \"Check for updates on crossmark\")\n\nAbstract\n--------\n\nLarge Language Models (LLMs) have demonstrated remarkable performance across diverse domains, thereby prompting researchers to explore their potential for use in recommendation systems. Initial attempts have leveraged the exceptional capabilities of LLMs, such as rich knowledge and strong generalization through In-context Learning, which involves phrasing the recommendation task as prompts. Nevertheless, the performance of LLMs in recommendation tasks remains suboptimal due to a substantial disparity between the training tasks for LLMs and recommendation tasks, as well as inadequate recommendation data during pre-training. To bridge the gap, we consider building a Large Recommendation Language Model by tunning LLMs with recommendation data. To this end, we propose an efficient and effective Tuning framework for Aligning LLMs with Recommendations, namely TALLRec. We have demonstrated that the proposed TALLRec framework can significantly enhance the recommendation capabilities of LLMs in the movie and book domains, even with a limited dataset of fewer than 100 samples. Additionally, the proposed framework is highly efficient and can be executed on a single RTX 3090 with LLaMA-7B. Furthermore, the fine-tuned LLM exhibits robust cross-domain generalization. Our code and data are available at https://github.com/SAI990323/TALLRec.\n\nSupplemental Material\n---------------------\n\nZIP File\n\nRecsys 2023 short paper\n\n*   [Download](https://dl.acm.org/doi/suppl/10.1145/3604915.3608857/suppl_file/recsys23-110.zip)\n*   1.76 MB\n\nReferences\n----------\n\n\\[1\\]\n\nQingyao Ai, Ting Bai, Zhao Cao, Yi Chang, Jiawei Chen, Zhumin Chen, Zhiyong Cheng, Shoubin Dong, Zhicheng Dou, Fuli Feng, 2023. Information Retrieval Meets Large Language Models: A Strategic Report from Chinese IR Community. arXiv preprint arXiv:2307.09751 (2023).\n\n\\[2\\]\n\nGreg Brockman, Mira Murati, Peter Welinder, and OpenAI. 2022. OpenAI API.\n\n\\[3\\]\n\nTom Brown, Benjamin Mann, Nick Ryder, 2020. Language models are few-shot learners. NeurIPS 33 (2020), 1877–1901.\n\n\\[4\\]\n\nAakanksha Chowdhery, Sharan Narang, Jacob Devlin, 2022. Palm: Scaling language modeling with pathways. arXiv preprint arXiv:2204.02311 (2022).\n\n\\[5\\]\n\nQiang Cui, Shu Wu, Qiang Liu, Wen Zhong, and Liang Wang. 2020. MV-RNN: A Multi-View Recurrent Neural Network for Sequential Recommendation. IEEE Trans. Knowl. Data Eng. 32, 2 (2020), 317–331.\n\n\\[6\\]\n\nZeyu Cui, Jianxin Ma, Chang Zhou, Jingren Zhou, and Hongxia Yang. 2022. M6-Rec: Generative Pretrained Language Models are Open-Ended Recommender Systems. arXiv preprint arXiv:2205.08084 (2022).\n\n\\[7\\]\n\nJacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In NAACL. Association for Computational Linguistics, 4171–4186.\n\n\\[8\\]\n\nSihao Ding, Fuli Feng, Xiangnan He, Jinqiu Jin, Wenjie Wang, Yong Liao, and Yongdong Zhang. 2022. Interpolative Distillation for Unifying Biased and Debiased Recommendation. In SIGIR ’22, July 11 - 15, 2022. ACM, 40–49.\n\n\\[9\\]\n\nTim Donkers, Benedikt Loepp, and Jürgen Ziegler. 2017. Sequential user-based recurrent neural network recommendations. In Proceedings of the eleventh ACM conference on recommender systems. 152–160.\n\n\\[10\\]\n\nDanny Driess, Fei Xia, Mehdi S. M. Sajjadi, 2023. PaLM-E: An Embodied Multimodal Language Model. abs/2303.03378 (2023). arXiv:2303.03378\n\n\\[11\\]\n\nHui Fang, Danning Zhang, Yiheng Shu, and Guibing Guo. 2020. Deep Learning for Sequential Recommendation: Algorithms, Influential Factors, and Evaluations. ACM Trans. Inf. Syst. 39, 1 (2020), 10:1–10:42.\n\n\\[12\\]\n\nF.Maxwell and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. In ACM Transactions on Interactive Intelligent Systems (TiiS).\n\n\\[13\\]\n\nYunfan Gao 2023. Chat-REC: Towards Interactive and Explainable LLMs-Augmented Recommender System. arXiv preprint:2303.14524 (2023).\n\n\\[14\\]\n\nShijie Geng, Shuchang Liu, Zuohui Fu, Yingqiang Ge, and Yongfeng Zhang. 2022. Recommendation as language processing (rlp): A unified pretrain, personalized prompt & predict paradigm (p5). In Proceedings of the 16th ACM Conference on Recommender Systems. 299–315.\n\n\\[15\\]\n\nRuining He and Julian McAuley. 2016. Fusing similarity models with markov chains for sparse sequential recommendation. In 2016 IEEE 16th international conference on data mining (ICDM). IEEE, 191–200.\n\n\\[16\\]\n\nXiangnan He, Kuan Deng, Xiang Wang, Yan Li, Yongdong Zhang, and Meng Wang. 2020. Lightgcn: Simplifying and powering graph convolution network for recommendation. In SIGIR’20. 639–648.\n\n\\[17\\]\n\nBalázs Hidasi 2016. Session-based Recommendations with Recurrent Neural Networks. In ICLR.\n\n\\[18\\]\n\nJordan Hoffmann 2022. Training compute-optimal large language models. arXiv preprint arXiv:2203.15556 (2022).\n\n\\[19\\]\n\nYupeng Hou, Shanlei Mu, Wayne Xin Zhao, Yaliang Li, Bolin Ding, and Ji-Rong Wen. 2022. Towards Universal Sequence Representation Learning for Recommender Systems. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 585–593.\n\n\\[20\\]\n\nNeil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, 2019. Parameter-Efficient Transfer Learning for NLP. In Proceedings of the 36th International Conference on Machine Learning, ICML 2019, 9-15 June 2019, Vol. 97\\. 2790–2799.\n\n\\[21\\]\n\nEdward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. 2022. LoRA: Low-Rank Adaptation of Large Language Models. In The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022.\n\n\\[22\\]\n\nSrinivasan Iyer, Xi Victoria Lin, Ramakanth Pasunuru, 2022. OPT-IML: Scaling Language Model Instruction Meta Learning through the Lens of Generalization. arXiv preprint arXiv:2212.12017 (2022).\n\n\\[23\\]\n\nJoel Jang, Seungone Kim, Seonghyeon Ye, Doyoung Kim, Lajanugen Logeswaran, Moontae Lee, Kyungjae Lee, and Minjoon Seo. 2023. Exploring the Benefits of Training Expert Language Models over Instruction Tuning. (2023). arXiv:2302.03202\n\n\\[24\\]\n\nVitor Jeronymo, Luiz Henrique Bonifacio, Hugo Abonizio, Marzieh Fadaee, Roberto de Alencar Lotufo, Jakub Zavrel, and Rodrigo Frassetto Nogueira. 2023. InPars-v2: Large Language Models as Efficient Dataset Generators for Information Retrieval. abs/2301.01820 (2023). arXiv:2301.01820\n\n\\[25\\]\n\nMatthew Jin, Syed Shahriar, Michele Tufano, Xin Shi, Shuai Lu, Neel Sundaresan, and Alexey Svyatkovskiy. 2023. InferFix: End-to-End Program Repair with LLMs. (2023). arXiv:2303.07263\n\n\\[26\\]\n\nWang-Cheng Kang and Julian McAuley. 2018. Self-attentive sequential recommendation. In ICDM. 197–206.\n\n\\[27\\]\n\nYehuda Koren, Robert Bell, and Chris Volinsky. 2009. Matrix factorization techniques for recommender systems. Computer 42, 8 (2009), 30–37.\n\n\\[28\\]\n\nBrian Lester, Rami Al-Rfou, and Noah Constant. 2021. The Power of Scale for Parameter-Efficient Prompt Tuning. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, EMNLP,7-11 November, 2021. Association for Computational Linguistics, 3045–3059.\n\n\\[29\\]\n\nLei Li, Yongfeng Zhang, and Li Chen. 2023. Personalized prompt learning for explainable recommendation. ACM Transactions on Information Systems 41, 4 (2023), 1–26.\n\n\\[30\\]\n\nRuyu Li, Wenhao Deng, Yu Cheng, Zheng Yuan, Jiaqi Zhang, and Fajie Yuan. 2023. Exploring the Upper Limits of Text-Based Collaborative Filtering Using Large Language Models: Discoveries and Insights. arXiv preprint arXiv:2305.11700 (2023).\n\n\\[31\\]\n\nXiang Lisa Li and Percy Liang. 2021. Prefix-Tuning: Optimizing Continuous Prompts for Generation. In ACL/IJCNLP 2021, August 1-6, 2021. Association for Computational Linguistics, 4582–4597.\n\n\\[32\\]\n\nPercy Liang, Rishi Bommasani, Tony Lee, 2022. Holistic evaluation of language models. arXiv preprint arXiv:2211.09110 (2022).\n\n\\[33\\]\n\nXi Victoria Lin, Todor Mihaylov, 2021. Few-shot learning with multilingual language models. arXiv preprint arXiv:2112.10668 (2021).\n\n\\[34\\]\n\nTariq Mahmood and Francesco Ricci. 2007. Learning and adaptivity in interactive recommender systems. In Proceedings of the ninth international conference on Electronic commerce. 75–84.\n\n\\[35\\]\n\nYabo Ni, Dan Ou, Shichen Liu, 2018. Perceive Your Users in Depth: Learning Universal User Representations from Multiple E-commerce Tasks. In KDD 2018, August 19-23, 2018. ACM, 596–605.\n\n\\[36\\]\n\nLong Ouyang 2022. Training language models to follow instructions with human feedback. NeurIPS 35 (2022), 27730–27744.\n\n\\[37\\]\n\nBaolin Peng 2023. Instruction Tuning with GPT-4. (2023). arXiv:2304.03277\n\n\\[38\\]\n\nRuihong Qiu, Zi Huang, Hongzhi Yin, and Zijian Wang. 2021. Contrastive Learning for Representation Degeneration Problem in Sequential Recommendation. (2021). arXiv:2110.05730\n\n\\[39\\]\n\nRuihong Qiu, Zi Huang, Hongzhi Yin, and Zijian Wang. 2022. Contrastive Learning for Representation Degeneration Problem in Sequential Recommendation. In WSDM ’22: The Fifteenth ACM International Conference on Web Search and Data Mining, February 21 - 25, 2022. ACM, 813–823.\n\n\\[40\\]\n\nSteffen Rendle, Christoph Freudenthaler, and Lars Schmidt-Thieme. 2010. Factorizing personalized markov chains for next-basket recommendation. In Proceedings of the 19th international conference on World wide web. 811–820.\n\n\\[41\\]\n\nVictor Sanh, Albert Webson, Colin Raffel, 2021. Multitask prompted training enables zero-shot task generalization. arXiv:2110.08207 (2021).\n\n\\[42\\]\n\nTimo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. 2023. Toolformer: Language models can teach themselves to use tools. arXiv preprint arXiv:2302.04761 (2023).\n\n\\[43\\]\n\nDhruv Shah, Blazej Osinski, Brian Ichter, and Sergey Levine. 2022. LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action. In CoRL 2022, 14-18 December 2022(Proceedings of Machine Learning Research, Vol. 205). PMLR, 492–504.\n\n\\[44\\]\n\nJiaxi Tang and Ke Wang. 2018. Personalized top-n sequential recommendation via convolutional sequence embedding. In WSDM. 565–573.\n\n\\[45\\]\n\nRohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and Tatsunori B. Hashimoto. 2023. Stanford Alpaca: An Instruction-following LLaMA model.\n\n\\[46\\]\n\nHugo Touvron 2023. LlaMA: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971 (2023).\n\n\\[47\\]\n\nLei Wang 2023. Zero-Shot Next-Item Recommendation using Large Pretrained Language Models. arXiv preprint arXiv:2304.03153 (2023).\n\n\\[48\\]\n\nLiang Wang, Nan Yang, and Furu Wei. 2023. Query2doc: Query Expansion with Large Language Models. (2023). arXiv:2303.07678\n\n\\[49\\]\n\nPengfei Wang, Jiafeng Guo, Yanyan Lan, Jun Xu, Shengxian Wan, and Xueqi Cheng. 2015. Learning hierarchical representation model for nextbasket recommendation. In Proceedings of the 38th International ACM SIGIR conference on Research and Development in Information Retrieval. 403–412.\n\n\\[50\\]\n\nShoujin Wang, Liang Hu, Yan Wang, Longbing Cao, Quan Z. Sheng, and Mehmet A. Orgun. 2019. Sequential Recommender Systems: Challenges, Progress and Prospects. In IJCAI 2019, Macao, China, August 10-16, 2019. ijcai.org, 6332–6338.\n\n\\[51\\]\n\nZiyang Wang, Huoyu Liu, Wei Wei, Yue Hu, Xian-Ling Mao, Shaojian He, Rui Fang, and Dangyang Chen. 2022. Multi-level Contrastive Learning Framework for Sequential Recommendation. (2022). arXiv:2208.13007\n\n\\[52\\]\n\nZhenlei Wang, Shiqi Shen, Zhipeng Wang, Bo Chen, Xu Chen, and Ji-Rong Wen. 2022. Unbiased Sequential Recommendation with Latent Confounders. In WWW ’22: The ACM Web Conference 2022, Virtual Event, Lyon, France, April 25 - 29, 2022. ACM, 2195–2204.\n\n\\[53\\]\n\nJason Wei, Maarten Bosma, Vincent Y Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M Dai, and Quoc V Le. 2021. Finetuned language models are zero-shot learners. arXiv preprint arXiv:2109.01652 (2021).\n\n\\[54\\]\n\nJason Wei, Yi Tay, Rishi Bommasani, 2022. Emergent abilities of large language models. arXiv preprint arXiv:2206.07682 (2022).\n\n\\[55\\]\n\nHongyi Wen, Xinyang Yi, Tiansheng Yao, Jiaxi Tang, Lichan Hong, and Ed H. Chi. 2022. Distributionally-robust Recommendations for Improving Worst-case User Experience. In WWW ’22: The ACM Web Conference 2022, Virtual Event, Lyon, France, April 25 - 29, 2022. ACM, 3606–3610.\n\n\\[56\\]\n\nTed Xiao, Harris Chan, Pierre Sermanet, Ayzaan Wahid, Anthony Brohan, Karol Hausman, Sergey Levine, and Jonathan Tompson. 2022. Robotic Skill Acquisition via Instruction Augmentation with Vision-Language Models. abs/2211.11736 (2022). arXiv:2211.11736\n\n\\[57\\]\n\nXu Xie, Fei Sun, Zhaoyang Liu, Shiwen Wu, Jinyang Gao, Jiandong Zhang, Bolin Ding, and Bin Cui. 2022. Contrastive Learning for Sequential Recommendation. In 38th IEEE International Conference on Data Engineering, ICDE 2022, Kuala Lumpur, Malaysia, May 9-12, 2022. IEEE, 1259–1273.\n\n\\[58\\]\n\nChengfeng Xu, Jian Feng, Pengpeng Zhao, Fuzhen Zhuang, Deqing Wang, Yanchi Liu, and Victor S. Sheng. 2021. Long- and short-term self-attention network for sequential recommendation. Neurocomputing 423 (2021), 580–589.\n\n\\[59\\]\n\nAn Yan, Shuo Cheng, Wang-Cheng Kang, Mengting Wan, and Julian J. McAuley. 2019. CosRec: 2D Convolutional Neural Networks for Sequential Recommendation. In CIKM 2019, November 3-7, 2019. ACM, 2173–2176.\n\n\\[60\\]\n\nZhengyi Yang 2023. A Generic Learning Framework for Sequential Recommendation with Distribution Shifts. (2023).\n\n\\[61\\]\n\nFajie Yuan, Xiangnan He, Alexandros Karatzoglou, and Liguang Zhang. 2020. Parameter-Efficient Transfer from Sequential Behaviors for User Modeling and Recommendation. In SIGIR 2020, July 25-30, 2020. ACM, 1469–1478.\n\n\\[62\\]\n\nFajie Yuan, Alexandros Karatzoglou, Ioannis Arapakis, Joemon M. Jose, and Xiangnan He. 2019. A Simple Convolutional Generative Network for Next Item Recommendation. In WSDM 2019, February 11-15, 2019. ACM, 582–590.\n\n\\[63\\]\n\nZheng Yuan, Fajie Yuan, Yu Song, Youhua Li, Junchen Fu, Fei Yang, Yunzhu Pan, and Yongxin Ni. 2023. Where to Go Next for Recommender Systems? ID- vs. Modality-based Recommender Models Revisited. In Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR 2023, Taipei, Taiwan, July 23-27, 2023, Hsin-Hsi Chen, Wei-Jou (Edward) Duh, Hen-Hsen Huang, Makoto P. Kato, Josiane Mothe, and Barbara Poblete (Eds.). ACM, 2639–2649. https://doi.org/10.1145/3539618.3591932\n\n\\[64\\]\n\nJizhi Zhang, Keqin Bao, Yang Zhang, Wenjie Wang, Fuli Feng, and Xiangnan He. 2023. Is chatgpt fair for recommendation? evaluating fairness in large language model recommendation. In Proceedings of the 17th ACM Conference on Recommender Systems(RecSys ’23). Association for Computing Machinery.\n\n\\[65\\]\n\nTingting Zhang, Pengpeng Zhao, Yanchi Liu, 2019. Feature-level Deeper Self-Attention Network for Sequential Recommendation. In Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, IJCAI 2019, August 10-16, 2019. ijcai.org, 4320–4326.\n\n\\[66\\]\n\nYang Zhang 2023. Reformulating CTR Prediction: Learning Invariant Feature Interactions for Recommendation. (2023).\n\n\\[67\\]\n\nYang Zhang, Fuli Feng, Xiangnan He, Tianxin Wei, Chonggang Song, Guohui Ling, and Yongdong Zhang. 2021. Causal Intervention for Leveraging Popularity Bias in Recommendation. In SIGIR ’21, July 11-15, 2021. ACM, 11–20.\n\n\\[68\\]\n\nZizhuo Zhang and Bang Wang. 2023. Prompt Learning for News Recommendation. arXiv preprint arXiv:2304.05263 (2023).\n\n\\[69\\]\n\nWayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, Yifan Du, Chen Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, Peiyu Liu, Jian-Yun Nie, and Ji-Rong Wen. 2023. A Survey of Large Language Models. CoRR abs/2303.18223 (2023). https://doi.org/10.48550/arXiv.2303.18223 arXiv:2303.18223\n\n\\[70\\]\n\nYu Zheng 2021. Disentangling User Interest and Conformity for Recommendation with Causal Embedding. In WWW ’21. 2980–2991.\n\n\\[71\\]\n\nCai-Nicolas Ziegler, Sean M. McNee, Joseph A. Konstan, and Georg Lausen. 2005. Improving Recommendation Lists through Topic Diversification. In Proceedings of the 14th International Conference on World Wide Web(WWW ’05). Association for Computing Machinery, 22–32.\n\nInformation & Contributors\n--------------------------\n\n### Information\n\n#### Published In\n\n![Image 30: cover image ACM Conferences](https://dl.acm.org/cms/asset/c62a0a4a-67ca-4d0f-a82d-3b2199595c63/3604915.cover.jpg)\n\nRecSys '23: Proceedings of the 17th ACM Conference on Recommender Systems\n\nSeptember 2023\n\n1406 pages\n\nCopyright © 2023 ACM.\n\nPermission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from [\\[email protected\\]](https://dl.acm.org/cdn-cgi/l/email-protection).\n\n#### Publisher\n\nAssociation for Computing Machinery\n\nNew York, NY, United States\n\n#### Publication History\n\n**Published**: 14 September 2023\n\n#### Permissions\n\nRequest permissions for this article.\n\n#### Check for updates\n\n[](https://dl.acm.org/doi/10.1145/3604915.3608857# \"Check for updates on crossmark\")\n\n#### Author Tags\n\n1.  [Instruction Tuning](https://dl.acm.org/keyword/Instruction+Tuning?expand=all)\n2.  [Large Language Models](https://dl.acm.org/keyword/Large+Language+Models?expand=all)\n3.  [Recommendation](https://dl.acm.org/keyword/Recommendation?expand=all)\n\n#### Qualifiers\n\n*   Short-paper\n*   Research\n*   Refereed limited\n\n#### Conference\n\n#### Acceptance Rates\n\nOverall Acceptance Rate 254 of 1,295 submissions, 20%\n\n### Contributors\n\n![Image 31](https://dl.acm.org/specs/products/acm/releasedAssets/images/loader-7e60691fbe777356dc81ff6d223a82a6.gif)\n\n#### Other Metrics\n\nBibliometrics & Citations\n-------------------------\n\n### Bibliometrics\n\n#### Article Metrics\n\n*   [View Citations](https://dl.acm.org/doi/10.1145/3604915.3608857#tab-citations)\n\n*   Downloads (Last 12 months)1,661\n*   Downloads (Last 6 weeks)190\n\nReflects downloads up to 17 Jan 2025\n\n#### Other Metrics\n\n### Citations\n\n*   Kim WLim SKim GChoi S(2025)Extracting Implicit User Preferences in Conversational Recommender Systems Using Large Language ModelsMathematics10.3390/math13020221**13**:2(221)Online publication date: 10-Jan-2025\n*   Xu TLi B(2025)KELLM: Knowledge-Enhanced Label-Wise Large Language Model for Safe and Interpretable Drug RecommendationElectronics10.3390/electronics14010154**14**:1(154)Online publication date: 2-Jan-2025\n*   Wang XChen HPan ZZhou YGuan CSun LZhu W(2025)Automated Disentangled Sequential Recommendation with Large Language ModelsACM Transactions on Information Systems10.1145/3675164**43**:2(1-29)Online publication date: 17-Jan-2025\n*   Cheema ASarfraz MHabib UZaman QBoonchieng E(2025)CD-LLMCARS: Cross Domain Fine-Tuned Large Language Model for Context-Aware Recommender SystemsIEEE Open Journal of the Computer Society10.1109/OJCS.2024.3509221**6**(49-59)Online publication date: 2025\n*   Jiang MLi MCao WYang MZhou L(2025)Multi-task convolutional deep neural network for recommendation based on knowledge graphsNeurocomputing10.1016/j.neucom.2024.129136**619**(129136)Online publication date: Feb-2025\n*   Tang MCui SJin ZLiang SLi CZou L(2025)Sequential recommendation by reprogramming pretrained transformerInformation Processing & Management10.1016/j.ipm.2024.103938**62**:1(103938)Online publication date: Jan-2025\n*   Zhai JLiao LLiu XWang YLi RCao XGao LGong ZGu FHe JLu YShi YSalakhutdinov RKolter ZHeller KWeller AOliver NScarlett JBerkenkamp F(2024)Actions speak louder than wordsProceedings of the 41st International Conference on Machine Learning10.5555/3692070.3694484(58484-58509)Online publication date: 21-Jul-2024\n*   Qu ZXie RXiao CYao YLiu ZLian FKang ZZhou J(2024)Thoroughly Modeling Multi-domain Pre-trained Recommendation as LanguageACM Transactions on Information Systems10.1145/3708883Online publication date: 19-Dec-2024\n*   Chen LGao CDu XLuo HJin DLi YWang M(2024)Enhancing ID-based Recommendation with Large Language ModelsACM Transactions on Information Systems10.1145/3704263Online publication date: 13-Nov-2024\n*   Zhang YHu ZBai YWu JWang QFeng F(2024)Recommendation Unlearning via Influence FunctionACM Transactions on Recommender Systems10.1145/3701763**3**:2(1-23)Online publication date: 29-Oct-2024\n*   Show More Cited By\n\nView Options\n------------\n\n#### Login options\n\nCheck if you have access through your login credentials or your institution to get full access on this article.\n\n[Sign in](https://dl.acm.org/action/showLogin?redirectUri=%2Fdoi%2F10.1145%2F3604915.3608857 \"Sign in\")\n\n#### Full Access\n\n### View options\n\n#### PDF\n\nView or Download as a PDF file.\n\n[PDF](https://dl.acm.org/doi/pdf/10.1145/3604915.3608857 \"View PDF\")\n\n#### eReader\n\nView online with eReader.\n\n[eReader](https://dl.acm.org/doi/epdf/10.1145/3604915.3608857 \"View online with eReader\")\n\n#### HTML Format\n\nView this article in HTML Format.\n\n[HTML Format](https://dl.acm.org/doi/fullHtml/10.1145/3604915.3608857 \"View this article in HTML Format\")\n\nMedia\n-----\n\n### Figures\n\n### Other\n\nTables\n------",
  "usage": {
    "tokens": 6500
  }
}
```
