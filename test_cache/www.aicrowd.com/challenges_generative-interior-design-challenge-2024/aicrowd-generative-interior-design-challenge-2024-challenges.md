---
title: AIcrowd | Generative Interior Design Challenge 2024 | Challenges
description: Revolutionising Interior Design with AI
url: https://www.aicrowd.com/challenges/generative-interior-design-challenge-2024
timestamp: 2025-01-20T16:01:50.998Z
domain: www.aicrowd.com
path: challenges_generative-interior-design-challenge-2024
---

# AIcrowd | Generative Interior Design Challenge 2024 | Challenges


Revolutionising Interior Design with AI


## Content

> Make your first submission using the [baseline starter kit](https://gitlab.aicrowd.com/aicrowd/challenges/generative-interior-design-challenge-2024/generative-interior-design-challenge-2024-starter-kit).
> 
> 🔈 [The final sprint in the Generative Interior Design Challenge - New Dev Data Released](https://discourse.aicrowd.com/t/announcement-the-final-sprint-in-the-generative-interior-design-challenge-new-dev-data-released)

🕵️ Introduction
----------------

### Revolutionising Interior Design with AI

Join the Generative Interior Design 2024, a pioneering challenge at the intersection of Computer Vision, Generative AI and Design. This new competition aims to leverage the power of AI and to supply innovative and creative tools to designers, where your algorithms will turn images of empty rooms into fully furnished spaces guided by text descriptions. Use your skills and imagination to bring life into empty rooms, transforming them into visions of beauty and functionality. Participate to revolutionize the way we will envision and design living spaces in the future.

📑 The Task
-----------

Participants are required to develop an algorithm capable of interpreting a text prompt and an image of an empty room, and generating a new image depicting the **same** room being furnished and designed according to the prompt. The key objective is to assist interior designers, architects, and homeowners in visualizing potential designs for spaces, whether it be for new constructions, renovations, or rental properties.

![Image 75](https://images.aicrowd.com/uploads/ckeditor/pictures/1253/content_vis.png)

Your mission, should you choose to accept it, involves harnessing AI to transform empty spaces into visually stunning interiors, guided only by text prompts. This challenge isn’t just about coding; it’s a blend of art and technology, where your skills bring to life unique, AI-crafted spaces from bare canvases. Dive deep into the complexities of LLMs, explore the nuances of image generation neural networks, and unleash a wave of creativity in interior design.

**Objectives:**

*   Technological Innovation: Push the limits of generative networks in computer vision for realistic and functional interior designs.
    
*   Practical Application: Create a tool to aid in visualizing and planning interior designs.
    
*   Industry Impact: Open new possibilities in interior design, enhancing client-designer interactions.
    

💾 Dataset
----------

**Test Set:**  
Engage with a variety of empty rooms, each awaiting transformation through your algorithms, inspired by their corresponding prompts.

You’ll find _‘input\_images’_ - a gallery of empty rooms, each linked with a text prompt in _‘input\_list.tsv’._ It’s your canvas for innovation.

**Training Set:**  
No predefined dataset. You’re free to use any resources, complemented by our baseline model.

Participants are invited to use publicly available data under common-use license or other public research datasets. Make sure to following these guidelines:

*   Always be transparent when using external data. Document your methods clearly and ethically.
    
*   Ensure external datasets are for non-commercial use and comply with their terms.
    
*   Justify your dataset choice and its relevance to transforming room images, ensuring it adheres to the dataset’s terms of use.
    

🚀 Submission Guideline
-----------------------

Generate images of the furnished rooms by modifying the style and adding appropriate furniture, while keeping original room geometry for the walls, windows and doors. Make your first submission with ease using our starter kit.

👨‍🎓 Evaluation
----------------

Generated images will be manually evaluated by a panel of trained experts according to the following four criteria: Room layout, Realism, Functionality and Consistency with text prompt: The final selection of prize winners will also score solutions according to their artistic qualities evaluated by the team of professional designers.

1.  **Room layout (Voting)**: The room layout criterion is crucial for maintaining the integrity of the original empty room, making it the utmost requirement for solutions in this competition. It is imperative that the generated room preserves the exact positioning and shapes of windows, doors, wall forms, and other elements that cannot be easily altered through basic renovation. If the evaluators detect substantial deviations in the room's shape, indicating that the walls, windows or doors no longer correspond to the original empty room, the assessment will be terminated resulting in the 0 score for the examined image.
    
2.  **Realism (Mean Opinion Score)**: This metric assesses the authenticity and credibility of the generated designs. It evaluates adherence to physical laws and the logical arrangement of objects within the design. Submissions will be assessed as: Fully Realistic, Mostly Realistic, Mostly Not Realistic, and Not Realistic at All.
    
3.  **Functionality (Mean Opinion Score)**: This criterion is about the practical application and utility of the generated designs in real-world scenarios. The evaluative spectrum ranges from Fully Functional, through Partially Functional, to Not Functional.
    
4.  **Consistency with text prompt**: This parameter measures the precision with which the generated design replicates the elements outlined in the text prompt, with special emphasis on the enumerated furniture items. Evaluators will employ a detailed checklist, derived from the text prompt, to verify the presence and fidelity of the specified elements in the generated image.
    

The final score will be calculated as an average three assessments: Realism, Functionality, and Consistency with text prompt. Human assessment is inherently subjective, resulting in potential variations in evaluations between different evaluators. To mitigate this, each metric is evaluated by a group of N experts for each image. If a new submission generates exactly the same image as its previous version, previous evaluation scores will be recycled for that image, i.e. a new copy of the previous image won’t undergo the evaluation.

![Image 76](https://images.aicrowd.com/uploads/ckeditor/pictures/1258/content_exampletwo.png)

![Image 77](https://images.aicrowd.com/uploads/ckeditor/pictures/1260/content_exampletwo.png)

📅 Timeline
-----------

*   Challenge Start: January 30, 2024
*   Submission Closure: April 1, 2024 UTC: 23:55
*   Announcement of teams passing the first evaluation round: April 5, 2024
*   Public assessment and selection of winners by the expert jury at [MCS](https://machinescansee.com/): April 17, 2024
*   Prize awards and presentations of solutions by the winners: April 17, 2024

💰 Prizes
---------

This challenge gathers a prize pool of USD 15,000. The top three teams or participants will be rewarded as follows:

*   🥇 1st on the leaderboard: USD 7000
*   🥈 2nd on the leaderboard: USD 5000
*   🥉 3rd on the leaderboard: USD 3000

Teams passing the first evaluation round will be awarded a travel grant to participate in Machines Can See Summit 2024) in Dubai. The winners of the challenge will be invited to present their solutions at the Challenge session of MCS.

📚 Baseline
-----------

The baseline for this challenge originates from the following project: [ControlNet Interior Design on Hugging Face](https://huggingface.co/spaces/ml6team/controlnet-interior-design).

**Key Points:**

*   The runtime per image should not exceed 45sec. on a A10G GPU.
    
*   Each team is allowed to make at most one submission per day.
    

📱 Community Engagement
-----------------------

Join a [thriving community](https://discourse.aicrowd.com/c/machines-can-design-2024-6254dd/2819) eager to exchange ideas, team up, and enrich each other’s experience in this captivating challenge. Be [part of a group of thinkers](https://discord.gg/AxVVdvz7vj) and innovators. [Exchange resources](https://discourse.aicrowd.com/c/machines-can-design-2024-6254dd/2819), [engage in thought-provoking discussions](https://discord.gg/AxVVdvz7vj), and [create winning teams](https://discourse.aicrowd.com/c/machines-can-design-2024-6254dd/2819).

## Metadata

```json
{
  "title": "AIcrowd | Generative Interior Design Challenge 2024 | Challenges",
  "description": "Revolutionising Interior Design with AI",
  "url": "https://www.aicrowd.com/challenges/generative-interior-design-challenge-2024",
  "content": "> Make your first submission using the [baseline starter kit](https://gitlab.aicrowd.com/aicrowd/challenges/generative-interior-design-challenge-2024/generative-interior-design-challenge-2024-starter-kit).\n> \n> 🔈 [The final sprint in the Generative Interior Design Challenge - New Dev Data Released](https://discourse.aicrowd.com/t/announcement-the-final-sprint-in-the-generative-interior-design-challenge-new-dev-data-released)\n\n🕵️ Introduction\n----------------\n\n### Revolutionising Interior Design with AI\n\nJoin the Generative Interior Design 2024, a pioneering challenge at the intersection of Computer Vision, Generative AI and Design. This new competition aims to leverage the power of AI and to supply innovative and creative tools to designers, where your algorithms will turn images of empty rooms into fully furnished spaces guided by text descriptions. Use your skills and imagination to bring life into empty rooms, transforming them into visions of beauty and functionality. Participate to revolutionize the way we will envision and design living spaces in the future.\n\n📑 The Task\n-----------\n\nParticipants are required to develop an algorithm capable of interpreting a text prompt and an image of an empty room, and generating a new image depicting the **same** room being furnished and designed according to the prompt. The key objective is to assist interior designers, architects, and homeowners in visualizing potential designs for spaces, whether it be for new constructions, renovations, or rental properties.\n\n![Image 75](https://images.aicrowd.com/uploads/ckeditor/pictures/1253/content_vis.png)\n\nYour mission, should you choose to accept it, involves harnessing AI to transform empty spaces into visually stunning interiors, guided only by text prompts. This challenge isn’t just about coding; it’s a blend of art and technology, where your skills bring to life unique, AI-crafted spaces from bare canvases. Dive deep into the complexities of LLMs, explore the nuances of image generation neural networks, and unleash a wave of creativity in interior design.\n\n**Objectives:**\n\n*   Technological Innovation: Push the limits of generative networks in computer vision for realistic and functional interior designs.\n    \n*   Practical Application: Create a tool to aid in visualizing and planning interior designs.\n    \n*   Industry Impact: Open new possibilities in interior design, enhancing client-designer interactions.\n    \n\n💾 Dataset\n----------\n\n**Test Set:**  \nEngage with a variety of empty rooms, each awaiting transformation through your algorithms, inspired by their corresponding prompts.\n\nYou’ll find _‘input\\_images’_ - a gallery of empty rooms, each linked with a text prompt in _‘input\\_list.tsv’._ It’s your canvas for innovation.\n\n**Training Set:**  \nNo predefined dataset. You’re free to use any resources, complemented by our baseline model.\n\nParticipants are invited to use publicly available data under common-use license or other public research datasets. Make sure to following these guidelines:\n\n*   Always be transparent when using external data. Document your methods clearly and ethically.\n    \n*   Ensure external datasets are for non-commercial use and comply with their terms.\n    \n*   Justify your dataset choice and its relevance to transforming room images, ensuring it adheres to the dataset’s terms of use.\n    \n\n🚀 Submission Guideline\n-----------------------\n\nGenerate images of the furnished rooms by modifying the style and adding appropriate furniture, while keeping original room geometry for the walls, windows and doors. Make your first submission with ease using our starter kit.\n\n👨‍🎓 Evaluation\n----------------\n\nGenerated images will be manually evaluated by a panel of trained experts according to the following four criteria: Room layout, Realism, Functionality and Consistency with text prompt: The final selection of prize winners will also score solutions according to their artistic qualities evaluated by the team of professional designers.\n\n1.  **Room layout (Voting)**: The room layout criterion is crucial for maintaining the integrity of the original empty room, making it the utmost requirement for solutions in this competition. It is imperative that the generated room preserves the exact positioning and shapes of windows, doors, wall forms, and other elements that cannot be easily altered through basic renovation. If the evaluators detect substantial deviations in the room's shape, indicating that the walls, windows or doors no longer correspond to the original empty room, the assessment will be terminated resulting in the 0 score for the examined image.\n    \n2.  **Realism (Mean Opinion Score)**: This metric assesses the authenticity and credibility of the generated designs. It evaluates adherence to physical laws and the logical arrangement of objects within the design. Submissions will be assessed as: Fully Realistic, Mostly Realistic, Mostly Not Realistic, and Not Realistic at All.\n    \n3.  **Functionality (Mean Opinion Score)**: This criterion is about the practical application and utility of the generated designs in real-world scenarios. The evaluative spectrum ranges from Fully Functional, through Partially Functional, to Not Functional.\n    \n4.  **Consistency with text prompt**: This parameter measures the precision with which the generated design replicates the elements outlined in the text prompt, with special emphasis on the enumerated furniture items. Evaluators will employ a detailed checklist, derived from the text prompt, to verify the presence and fidelity of the specified elements in the generated image.\n    \n\nThe final score will be calculated as an average three assessments: Realism, Functionality, and Consistency with text prompt. Human assessment is inherently subjective, resulting in potential variations in evaluations between different evaluators. To mitigate this, each metric is evaluated by a group of N experts for each image. If a new submission generates exactly the same image as its previous version, previous evaluation scores will be recycled for that image, i.e. a new copy of the previous image won’t undergo the evaluation.\n\n![Image 76](https://images.aicrowd.com/uploads/ckeditor/pictures/1258/content_exampletwo.png)\n\n![Image 77](https://images.aicrowd.com/uploads/ckeditor/pictures/1260/content_exampletwo.png)\n\n📅 Timeline\n-----------\n\n*   Challenge Start: January 30, 2024\n*   Submission Closure: April 1, 2024 UTC: 23:55\n*   Announcement of teams passing the first evaluation round: April 5, 2024\n*   Public assessment and selection of winners by the expert jury at [MCS](https://machinescansee.com/): April 17, 2024\n*   Prize awards and presentations of solutions by the winners: April 17, 2024\n\n💰 Prizes\n---------\n\nThis challenge gathers a prize pool of USD 15,000. The top three teams or participants will be rewarded as follows:\n\n*   🥇 1st on the leaderboard: USD 7000\n*   🥈 2nd on the leaderboard: USD 5000\n*   🥉 3rd on the leaderboard: USD 3000\n\nTeams passing the first evaluation round will be awarded a travel grant to participate in Machines Can See Summit 2024) in Dubai. The winners of the challenge will be invited to present their solutions at the Challenge session of MCS.\n\n📚 Baseline\n-----------\n\nThe baseline for this challenge originates from the following project: [ControlNet Interior Design on Hugging Face](https://huggingface.co/spaces/ml6team/controlnet-interior-design).\n\n**Key Points:**\n\n*   The runtime per image should not exceed 45sec. on a A10G GPU.\n    \n*   Each team is allowed to make at most one submission per day.\n    \n\n📱 Community Engagement\n-----------------------\n\nJoin a [thriving community](https://discourse.aicrowd.com/c/machines-can-design-2024-6254dd/2819) eager to exchange ideas, team up, and enrich each other’s experience in this captivating challenge. Be [part of a group of thinkers](https://discord.gg/AxVVdvz7vj) and innovators. [Exchange resources](https://discourse.aicrowd.com/c/machines-can-design-2024-6254dd/2819), [engage in thought-provoking discussions](https://discord.gg/AxVVdvz7vj), and [create winning teams](https://discourse.aicrowd.com/c/machines-can-design-2024-6254dd/2819).",
  "usage": {
    "tokens": 1737
  }
}
```
