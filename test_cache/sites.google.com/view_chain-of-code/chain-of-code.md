---
title: Chain of Code
description: 
url: https://sites.google.com/view/chain-of-code
timestamp: 2025-01-20T15:50:29.582Z
domain: sites.google.com
path: view_chain-of-code
---

# Chain of Code



## Content

Reasoning with a Language Model-Augmented Code Emulator

Chengshu Li\*,1,2, Jacky Liang1, Andy Zeng1, Xinyun Chen1, Karol Hausman1,2,

Dorsa Sadigh1,2, Sergey Levine1,3, Li Fei-Fei2, Fei Xia†,1, Brian Ichter†,1

1Google DeepMind, 2Stanford University, 3University of California, Berkeley

\*Work done as a student researcher at Google DeepMind. †Equal advising.

[\[Paper\]](https://arxiv.org/pdf/2312.04474.pdf)\[Code (coming soon)\]

![Image 44](https://lh4.googleusercontent.com/vAYylbqRUHvKPDveRgMsuF5XY4EfmHJs0VHMOHAX-8nxMwN9kHZMnSW4J1HSqGihlMemhVraZNmjJS984r-h-YTgSq1A57Qf-vMimPbSw9pPFAgrzsJOydAhK3zedTvEjg=w1280)

Video
-----

![Image 45](https://www.google.com/images/icons/product/drive-32.png)Chain of Code v6.m4v

We propose Chain of Code (CoC), a simple yet surprisingly effective extension that improves Language Model (LM) code-driven reasoning. It broadens the scope of reasoning questions that LMs can correctly answer by "thinking in code".

The key idea is to encourage LMs to format semantic sub-tasks in a program as flexible pseudocode that the interpreter can explicitly catch undefined behaviors and hand off to simulate with an LM (as an "LMulator").

![Image 46](https://lh3.googleusercontent.com/B0VU8vnGQjL4fy2vdPKUvRwZ-3sRFjMzY1LNIDSelsOZ5AmfBBGhvDGeYsgzMS_HQSlFIBi-60ncbyIr29gM78NdlOjrPlivdMAfeudKDFX-lFEeZ7OJFQDgvGZWbVrvxQ=w1280)

![Image 47](https://lh3.googleusercontent.com/x7eOvJ5Yh0C2eILD52UGcpIetvyZfSuUviXGJsqL5AqqljmQuA3_IfB0ZqBarCbdTJUQj47V_DiluB8JA8BsHwGlGkSD4uya8ra164FGDKPJBoXqreS6lgjN7zeHCnQ96w=w1280)

Compared to previous reasoning methods, Chain of Code first (d) generates code or pseudocode to solve the question and then (e) executes the code with a code interpreter if possible, and with an LMulator (language model emulating code) otherwise.

Blue highlight indicates LM generation.

Red highlight indicates LM generated code being executed by an interpreter.

Purple highlight indicates an LMulator simulating the code via a program state in green.

![Image 48](https://lh5.googleusercontent.com/LnbLmgTRMu3AXUSpC5iKpjD6tz5DHGJ5XC87cTzsilYIv0woI7Ds4hkGCbbq2o1hUAOApYqrmx9bdrrCfggX4ZA3_9Kbck9BoBsMbo-s2KDuuJ3PcEdL8eApxGQ2hf3wOA=w1280)

Results on Language Reasoning




-----------------------------------

On BIG-Bench Hard (BBH), Chain of Code achieves 84%, a gain of 12% over Chain of Thought and a new state of the art.  It further, outperforms the average human raters in 18 out of 23 tasks.

![Image 49](https://lh4.googleusercontent.com/yPShMH3kAnlaDZPKKHhbIP7KcznJYquTcAP7OVc1bMW3pkKI39lNEWJDKHUX7LUw0TSiMEnROJB5jOWkbm4WbRTJwxwwYTwiuL_a7YCdyMqGTgOGY-DM_DKcAQcYH49m3w=w1280)

Chain of Code performs on par with Chain of Thought for the NLP subset of BBH, and outperforms even the best human raters for the algorithmic subset of BBH.

![Image 50](https://lh4.googleusercontent.com/CC2gwGKYBvGBfalEW-XyxrqSLAyyVzsyLOrAtZcv2xeFlygHqa2MHCa1t6ZFcb-6Gee-_Xl_uJ0YZHYeUJdr-hapAN7xbsp85w0FwPen7DqvtolwQRuY7WjlNpyDKlh7AQ=w1280)

Chain of Code (Interweave) based on text-davinci-003 even outperforms a much larger instruction tuned model gpt-4, which is instructed to write code to solve the reasoning problems, if it's helpful to do so.

![Image 51](https://lh6.googleusercontent.com/uoiGH2cLyDpD3MuYGwpkA30jlmDplJ87XZj9xxRBT6tdOt0PMN0WGCeYQwvqfOTMSi_E_lLtiby20uiQgQIowAzgB_Vot8mu5vkY9mOxtikh8X3Tic8IkNkfI0xkXYN3FA=w1280)

Chain of Code is well fit for solving robotics tasks because they require both semantic and algorithmic reasoning.

They also involve interfacing with other APIs through code (e.g., control or perception APIs) and with users through natural language.

Red highlight indicates LM generated code being executed by an interpreter.

Purple highlight indicates an LMulator simulating the code.

![Image 52](https://lh6.googleusercontent.com/mL8rT2XUB59Hsg-rLVhixin3K1-Hz-A8fKdzKgDxUmGjI_8RmnaIaKUG1GJy3qPcxK-tXgV3QGdfDig5QuGuztiaAfVKw0v9MzV3akD4C5LUctsoUo22a9HA-t7LXZIP=w1280)

![Image 53](https://www.google.com/images/icons/product/drive-32.png)sorting\_trash\_cropped.mp4

![Image 54](https://lh4.googleusercontent.com/15UXpzZFT0X1HIhR8I1UZKt3Gp6TgRGbh8-UhTzRujTPL1OZDGEA_Hk3RsPgiGk-qOM8KUpBu1spY_YjSP_NOXWv2t95bMInoJbDcj8eClxUbvFIrfqRnV7AQnkipx1xqw=w1280)

![Image 55](https://www.google.com/images/icons/product/drive-32.png)cook\_tomato\_egg\_Chinese\_cropped.mp4

![Image 56](https://lh4.googleusercontent.com/w8RPff8sR-I30QgxwwAw_y4JTUn7e6OOnvQip0xAodFrNioMg0yy0-b-C0TUjl_AJL_NxRhzsper-vzYvAYZraEPfK3qd4KFgLp90L3WxID3s65CJERFE18s-DhEAq1qqQ=w1280)

![Image 57](https://www.google.com/images/icons/product/drive-32.png)season\_steak\_cropped.mp4

Example Model Outputs for Language Reasoning




--------------------------------------------------

Example model outputs for some of the most challenging BBH tasks that require both semantic and algorithm reasoning.

Red highlight indicates LM generated code being executed by an interpreter.

Purple highlight indicates an LMulator simulating the code via a program state in green.

![Image 58](https://lh5.googleusercontent.com/dxBaV-57Kw9EwHzSY83_QbCD21JRuh2koENaJPsO419xs59zOXofGQZrW7eiXX22abv8pdloZTqjNgGXBzdYegEqcdH7Mb5KbDfpdSw38PlKgFCvAX72Az8XPFDx5QtV6g=w1280)

![Image 59](https://lh6.googleusercontent.com/dOuhCzbXONr5fnG8E11AFkHzOLrMMCB_vLC0pw_vA7btDsscCO67-zOGa_0PgcdmwYNeIXpeSyJET0KRmchXijWbooQ6rv0DlMUQvwehpiVWNXXlSIIR-vfnuYtxbwMdxw=w1280)

![Image 60](https://lh5.googleusercontent.com/EZy-E6-Zkng7oofHLcpnV_uNsYILKI9-CiF2zVMANI5iUuhABmZYaw45prNs1OKgw0iSrRVl4YTXl8jqy_sKuOyJMNPYZJGjsQ4FcnlLuCl2rXdp1GiCF21M8WLEIO4s3Q=w1280)

![Image 61](https://lh3.googleusercontent.com/mqDI8lONd4AEZwuqui34U-KdZ85-jDBumEaD_kv4tttm49Jj5B2tBzn3CaOTC_fZ39uNF2y0lZOnTYmkws_aYmIEixQZdaUDugAC2BGW4hvw75GPrPxwBSVLqvxSjYe3Yg=w1280)

With careful ablation studies, we confirm all design choices of Chain of Code is essential for its good performance.

![Image 62](https://lh5.googleusercontent.com/ynQI74DhRHzVymd4Q8Hbx9HtwKqSUvPQW1tt5jcCdLoZZ82ul5MsVEGofGfzhHN3lyPipwdRTl5hu_sNR_9Dvm9y4TnXGUp8n4KHvZcGn0O2U697s6WGiehwFUeZLjJ38w=w1280)

![Image 63](https://lh6.googleusercontent.com/MAtbEWADBP0aOz42lPrp8uC8ALoszgsM8GehCDte81_FOCQ_euRP9SbjjHazaFTjwMjZa_9uu4k9nOYzezo1If_2Eir1yHAhp8O8jHi7SxNSrEWw089CDoQLFcgXHhpF6w=w1280)

Unlike Chain of Thought, which only emerges for large models, Chain of Code scales well with large and small models alike.

![Image 64](https://lh4.googleusercontent.com/AWFj1yRckIF79e9A7l-x71kVwUXKLaxti7yIF52O9GhoA4YJM0146K7Kl7iAqAjnhdHmArPq67pG0fqLQjceh_aZfTS7sLXSjfJr2_NySga2-ATJgOEUeP0okTimfrSQWg=w1280)

@misc{li2023chain,      title={Chain of Code: Reasoning with a Language Model-Augmented Code Emulator},       author={Chengshu Li and Jacky Liang and Andy Zeng and Xinyun Chen and Karol Hausman and Dorsa Sadigh and Sergey Levine and Li Fei-Fei and Fei Xia and Brian Ichter},      year={2023},      eprint={2312.04474},      archivePrefix={arXiv},      primaryClass={cs.CL}}

## Metadata

```json
{
  "title": "Chain of Code",
  "description": "",
  "url": "https://sites.google.com/view/chain-of-code",
  "content": "Reasoning with a Language Model-Augmented Code Emulator\n\nChengshu Li\\*,1,2, Jacky Liang1, Andy Zeng1, Xinyun Chen1, Karol Hausman1,2,\n\nDorsa Sadigh1,2, Sergey Levine1,3, Li Fei-Fei2, Fei Xia†,1, Brian Ichter†,1\n\n1Google DeepMind, 2Stanford University, 3University of California, Berkeley\n\n\\*Work done as a student researcher at Google DeepMind. †Equal advising.\n\n[\\[Paper\\]](https://arxiv.org/pdf/2312.04474.pdf)\\[Code (coming soon)\\]\n\n![Image 44](https://lh4.googleusercontent.com/vAYylbqRUHvKPDveRgMsuF5XY4EfmHJs0VHMOHAX-8nxMwN9kHZMnSW4J1HSqGihlMemhVraZNmjJS984r-h-YTgSq1A57Qf-vMimPbSw9pPFAgrzsJOydAhK3zedTvEjg=w1280)\n\nVideo\n-----\n\n![Image 45](https://www.google.com/images/icons/product/drive-32.png)Chain of Code v6.m4v\n\nWe propose Chain of Code (CoC), a simple yet surprisingly effective extension that improves Language Model (LM) code-driven reasoning. It broadens the scope of reasoning questions that LMs can correctly answer by \"thinking in code\".\n\nThe key idea is to encourage LMs to format semantic sub-tasks in a program as flexible pseudocode that the interpreter can explicitly catch undefined behaviors and hand off to simulate with an LM (as an \"LMulator\").\n\n![Image 46](https://lh3.googleusercontent.com/B0VU8vnGQjL4fy2vdPKUvRwZ-3sRFjMzY1LNIDSelsOZ5AmfBBGhvDGeYsgzMS_HQSlFIBi-60ncbyIr29gM78NdlOjrPlivdMAfeudKDFX-lFEeZ7OJFQDgvGZWbVrvxQ=w1280)\n\n![Image 47](https://lh3.googleusercontent.com/x7eOvJ5Yh0C2eILD52UGcpIetvyZfSuUviXGJsqL5AqqljmQuA3_IfB0ZqBarCbdTJUQj47V_DiluB8JA8BsHwGlGkSD4uya8ra164FGDKPJBoXqreS6lgjN7zeHCnQ96w=w1280)\n\nCompared to previous reasoning methods, Chain of Code first (d) generates code or pseudocode to solve the question and then (e) executes the code with a code interpreter if possible, and with an LMulator (language model emulating code) otherwise.\n\nBlue highlight indicates LM generation.\n\nRed highlight indicates LM generated code being executed by an interpreter.\n\nPurple highlight indicates an LMulator simulating the code via a program state in green.\n\n![Image 48](https://lh5.googleusercontent.com/LnbLmgTRMu3AXUSpC5iKpjD6tz5DHGJ5XC87cTzsilYIv0woI7Ds4hkGCbbq2o1hUAOApYqrmx9bdrrCfggX4ZA3_9Kbck9BoBsMbo-s2KDuuJ3PcEdL8eApxGQ2hf3wOA=w1280)\n\nResults on Language Reasoning\n\n\n\n\n-----------------------------------\n\nOn BIG-Bench Hard (BBH), Chain of Code achieves 84%, a gain of 12% over Chain of Thought and a new state of the art.  It further, outperforms the average human raters in 18 out of 23 tasks.\n\n![Image 49](https://lh4.googleusercontent.com/yPShMH3kAnlaDZPKKHhbIP7KcznJYquTcAP7OVc1bMW3pkKI39lNEWJDKHUX7LUw0TSiMEnROJB5jOWkbm4WbRTJwxwwYTwiuL_a7YCdyMqGTgOGY-DM_DKcAQcYH49m3w=w1280)\n\nChain of Code performs on par with Chain of Thought for the NLP subset of BBH, and outperforms even the best human raters for the algorithmic subset of BBH.\n\n![Image 50](https://lh4.googleusercontent.com/CC2gwGKYBvGBfalEW-XyxrqSLAyyVzsyLOrAtZcv2xeFlygHqa2MHCa1t6ZFcb-6Gee-_Xl_uJ0YZHYeUJdr-hapAN7xbsp85w0FwPen7DqvtolwQRuY7WjlNpyDKlh7AQ=w1280)\n\nChain of Code (Interweave) based on text-davinci-003 even outperforms a much larger instruction tuned model gpt-4, which is instructed to write code to solve the reasoning problems, if it's helpful to do so.\n\n![Image 51](https://lh6.googleusercontent.com/uoiGH2cLyDpD3MuYGwpkA30jlmDplJ87XZj9xxRBT6tdOt0PMN0WGCeYQwvqfOTMSi_E_lLtiby20uiQgQIowAzgB_Vot8mu5vkY9mOxtikh8X3Tic8IkNkfI0xkXYN3FA=w1280)\n\nChain of Code is well fit for solving robotics tasks because they require both semantic and algorithmic reasoning.\n\nThey also involve interfacing with other APIs through code (e.g., control or perception APIs) and with users through natural language.\n\nRed highlight indicates LM generated code being executed by an interpreter.\n\nPurple highlight indicates an LMulator simulating the code.\n\n![Image 52](https://lh6.googleusercontent.com/mL8rT2XUB59Hsg-rLVhixin3K1-Hz-A8fKdzKgDxUmGjI_8RmnaIaKUG1GJy3qPcxK-tXgV3QGdfDig5QuGuztiaAfVKw0v9MzV3akD4C5LUctsoUo22a9HA-t7LXZIP=w1280)\n\n![Image 53](https://www.google.com/images/icons/product/drive-32.png)sorting\\_trash\\_cropped.mp4\n\n![Image 54](https://lh4.googleusercontent.com/15UXpzZFT0X1HIhR8I1UZKt3Gp6TgRGbh8-UhTzRujTPL1OZDGEA_Hk3RsPgiGk-qOM8KUpBu1spY_YjSP_NOXWv2t95bMInoJbDcj8eClxUbvFIrfqRnV7AQnkipx1xqw=w1280)\n\n![Image 55](https://www.google.com/images/icons/product/drive-32.png)cook\\_tomato\\_egg\\_Chinese\\_cropped.mp4\n\n![Image 56](https://lh4.googleusercontent.com/w8RPff8sR-I30QgxwwAw_y4JTUn7e6OOnvQip0xAodFrNioMg0yy0-b-C0TUjl_AJL_NxRhzsper-vzYvAYZraEPfK3qd4KFgLp90L3WxID3s65CJERFE18s-DhEAq1qqQ=w1280)\n\n![Image 57](https://www.google.com/images/icons/product/drive-32.png)season\\_steak\\_cropped.mp4\n\nExample Model Outputs for Language Reasoning\n\n\n\n\n--------------------------------------------------\n\nExample model outputs for some of the most challenging BBH tasks that require both semantic and algorithm reasoning.\n\nRed highlight indicates LM generated code being executed by an interpreter.\n\nPurple highlight indicates an LMulator simulating the code via a program state in green.\n\n![Image 58](https://lh5.googleusercontent.com/dxBaV-57Kw9EwHzSY83_QbCD21JRuh2koENaJPsO419xs59zOXofGQZrW7eiXX22abv8pdloZTqjNgGXBzdYegEqcdH7Mb5KbDfpdSw38PlKgFCvAX72Az8XPFDx5QtV6g=w1280)\n\n![Image 59](https://lh6.googleusercontent.com/dOuhCzbXONr5fnG8E11AFkHzOLrMMCB_vLC0pw_vA7btDsscCO67-zOGa_0PgcdmwYNeIXpeSyJET0KRmchXijWbooQ6rv0DlMUQvwehpiVWNXXlSIIR-vfnuYtxbwMdxw=w1280)\n\n![Image 60](https://lh5.googleusercontent.com/EZy-E6-Zkng7oofHLcpnV_uNsYILKI9-CiF2zVMANI5iUuhABmZYaw45prNs1OKgw0iSrRVl4YTXl8jqy_sKuOyJMNPYZJGjsQ4FcnlLuCl2rXdp1GiCF21M8WLEIO4s3Q=w1280)\n\n![Image 61](https://lh3.googleusercontent.com/mqDI8lONd4AEZwuqui34U-KdZ85-jDBumEaD_kv4tttm49Jj5B2tBzn3CaOTC_fZ39uNF2y0lZOnTYmkws_aYmIEixQZdaUDugAC2BGW4hvw75GPrPxwBSVLqvxSjYe3Yg=w1280)\n\nWith careful ablation studies, we confirm all design choices of Chain of Code is essential for its good performance.\n\n![Image 62](https://lh5.googleusercontent.com/ynQI74DhRHzVymd4Q8Hbx9HtwKqSUvPQW1tt5jcCdLoZZ82ul5MsVEGofGfzhHN3lyPipwdRTl5hu_sNR_9Dvm9y4TnXGUp8n4KHvZcGn0O2U697s6WGiehwFUeZLjJ38w=w1280)\n\n![Image 63](https://lh6.googleusercontent.com/MAtbEWADBP0aOz42lPrp8uC8ALoszgsM8GehCDte81_FOCQ_euRP9SbjjHazaFTjwMjZa_9uu4k9nOYzezo1If_2Eir1yHAhp8O8jHi7SxNSrEWw089CDoQLFcgXHhpF6w=w1280)\n\nUnlike Chain of Thought, which only emerges for large models, Chain of Code scales well with large and small models alike.\n\n![Image 64](https://lh4.googleusercontent.com/AWFj1yRckIF79e9A7l-x71kVwUXKLaxti7yIF52O9GhoA4YJM0146K7Kl7iAqAjnhdHmArPq67pG0fqLQjceh_aZfTS7sLXSjfJr2_NySga2-ATJgOEUeP0okTimfrSQWg=w1280)\n\n@misc{li2023chain,      title={Chain of Code: Reasoning with a Language Model-Augmented Code Emulator},       author={Chengshu Li and Jacky Liang and Andy Zeng and Xinyun Chen and Karol Hausman and Dorsa Sadigh and Sergey Levine and Li Fei-Fei and Fei Xia and Brian Ichter},      year={2023},      eprint={2312.04474},      archivePrefix={arXiv},      primaryClass={cs.CL}}",
  "usage": {
    "tokens": 2706
  }
}
```
