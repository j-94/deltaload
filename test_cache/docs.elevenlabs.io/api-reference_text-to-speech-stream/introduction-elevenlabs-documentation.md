---
title: Introduction — ElevenLabs Documentation
description: Explore our Guides and API Reference to get the most out of ElevenLabs.
url: https://docs.elevenlabs.io/api-reference/text-to-speech-stream
timestamp: 2025-01-20T15:49:16.978Z
domain: docs.elevenlabs.io
path: api-reference_text-to-speech-stream
---

# Introduction — ElevenLabs Documentation


Explore our Guides and API Reference to get the most out of ElevenLabs.


## Content

Welcome
-------

In this documentation we will help you get started with [ElevenLabs](https://elevenlabs.io/). Before we get started, we would like to mention that we also offer a [Help Center](https://help.elevenlabs.io/hc/en-us) which is more of an FAQ. Here, you can find answers to individual questions and interact with our chatbot. Additionally, you can submit tickets directly to our support team if you have any inquiries.

### Create

We will cover everything, beginning with Text to Speech and Speech to Speech, where you will generate your first audio using our Default Voices.

We also provide several features that extend beyond the realm of speech, including our Sound Effects Generator and our upcoming [Music Generator](https://www.youtube.com/watch?v=d8k4Pit4_ZU) (release date and name to be determined).

###### Text to Speech (Speech Synthesis)

Our Text-to-Speech technology, also known as Speech Synthesis, is the core of ElevenLabs. It serves as the foundation for many of the features we offer and powers many services worldwide. This technology transforms text into incredibly realistic speech.

To ensure you get the most out of this feature, it is important to use an appropriate voice for what you are trying to achieve and to familiarize yourself with the different models we offer, as both of these factors have a tremendous effect on the delivery and quality of the output.

###### Speech to Speech (Voice Changer)

Our Speech-to-Speech technology, also known as Voice Changer, converts a source voice (audio input) into a different voice while retaining the source voice’s accent, cadence, and overall delivery, but with the timbre and vocal quality of the selected voice.

This feature is great for standalone usage, as it provides your voice acting with a wider range of tonalities. Additionally, when used in conjunction with Text-to-Speech, it allows for easy correction of pronunciations and adds specific performances or characteristics, emulating subtle vocal nuances for a more human touch. You can make the AI whisper, sigh, laugh, or cry by simply acting it out and then using the voice changer.

###### Sound Effects

Our Sound Effects generator allows you to create a wide range of audio effects by inputting descriptive prompts. This feature is great across variety of uses, such as film sound design, video game audio, music production, and much more. Users can generate sounds by typing a description into a text box, and the AI will produce multiple variations based on the given prompt.

The tool offers settings to control the duration of the sound and how closely the output adheres to the prompt.

###### Music (in development)

### Voices

Once you have created your first audio output, we will proceed to cloning or designing your first voice on the My Voices page. After setting up your voices, you will be able to use your own voices to generate audio.

###### Voice Design

Voice Design allows for the creation of unique voices from text prompts, filling gaps when specific voices aren’t available in the Voice Library or where you might even prefer a synthetically generated voice. You can create both realistic voices, which focus on attributes like age, accent, and emotion, and character voices, which allow you to create more creative voices by using more creative language.

###### Instant Voice Cloning

Instant Voice Cloning enables you to create voice clones quickly from short audio samples, without the need for training. It uses a technology to create voice instantaneously, capturing its tone and inflections. While effective for many voices, it may struggle with unique accents or voices not encountered during training. High-quality, consistent audio samples are crucial for optimal results.

###### Professional Voice Cloning

Professional Voice Cloning creates hyper-realistic voice models by training on larger datasets of a speaker’s voice. Available from the Creator tier and above, it offers extremely higher accuracy and can capture intricate details, such as accents and tonal nuances. This method requires more audio data, between 1 - 3 hours, and a few hours to train the model but results in a voice clone that closely resembles the original.

[](https://elevenlabs.io/docs/product/voices/voice-lab/professional-voice-cloning)

###### Voice Library

The Voice Library is a marketplace where users can share and discover a wide variety of voices, including professional voice clones from real people who have cloned their voices and decided to share them with the rest of the community.

It offers filters and search options to help users find specific voice styles, languages, and accents. Users can add voices to “My Voices” for use across ElevenLabs features, and shared voices can earn either credits or monetary rewards based on usage.

### Workflows

Moving on, we will also go through our workflow-specific section, where we offer a variety of tools and workflows for different needs.

First, we will start with Projects, which is our end-to-end solution for creating voiceovers for long-form content, such as articles or audiobooks, with just a few clicks.

We will cover Dubbing, our solution for making content more accessible in all languages while preserving the original voice and striving to maintain the same performance across languages. This service comes in two flavors: automatic and studio.

Our automatic solution allows users to create dubs in any language supported by the AI with just a few clicks. Meanwhile, the Dubbing Studio provides an end-to-end workflow with great controllability for producing perfect dubs.

Finally, we will cover our Conversation AI platform, which provides an easy setup process for quickly and easily deploying conversational AI, as well as API endpoints and SDKs, to allow for seamless integration into your existing applications or flows.

###### Projects

Projects is a comprehensive tool for creating long-form audio content, such as audiobooks. It allows users to upload documents or web pages and generate voiceover narrations. It is easy to manage and keep track of all of your projects, select voices, and adjust settings for quality and download options. Projects is available on paid tiers, offering an efficient workflow for producing lengthy audio content.

###### Dubbing

Dubbing allows you to create high-quality dubs in various languages while preserving the original performance. You can upload or import video/audio files and select the original and target languages. The tool supports multiple formats and offers options for modifying specific parts of the dub. It’s available on all plans, with advanced features in the Dubbing Studio.

[](https://elevenlabs.io/docs/product/dubbing/overview)

###### Automatic

Automatic Dubbing quickly translates and replaces the original audio of a video with a dub in a new language, maintaining the original speaker’s voice characteristics. It provides a final output without the option for edits, making it ideal for fast and straightforward dubbing needs. You can upload files or import them via URL to start the process.

[](https://elevenlabs.io/docs/api-reference/create-dub)

###### Studio

Dubbing Studio offers an advanced dubbing experience, allowing you to edit and customize dubs extensively. It supports manual transcription adjustments, voice selection, and precise timing edits. You can manage speaker tracks, regenerate audio, and export the final output in various formats. This feature provides full control over the dubbing process, ideal for detailed and tailored projects.

[](https://elevenlabs.io/docs/product/dubbing/studio)

###### Voiceover Studio

Voiceover Studio allows you to create interactive audio content with flexibility. It combines an audio timeline with text-to-speech, speech-to-speech, and sound effects, enabling the creation of dialogues between multiple speakers. You can upload videos or start projects from scratch, adding voiceover and sound effects tracks. Available on the Creator plan and above, it offers tools for crafting detailed and dynamic voiceover projects.

[](https://elevenlabs.io/docs/product/voiceover-studio/overview)

###### Audio Native

Audio Native is an embedded audio player that automatically voices web page content using ElevenLabs’ text-to-speech service. It allows embedding pre-generated audio from projects into web pages with a simple HTML snippet. Available on the Creator plan and above, it includes metrics for tracking audience engagement through a listener dashboard.

###### Conversational AI

Conversational AI is a platform for deploying interactive voice agents that can interact with you or your users in natural conversations. It integrates Speech to Text, Language Models, and Text to Speech, along with features like interruption handling and turn-taking logic. Users can customize agents with different voices and system prompts, making it suitable for applications like customer service, virtual assistants, and interactive characters.

Signing up
----------

You can sign up using the traditional method of email plus password or using Google OAuth.

If you choose to sign up with your email, you will be asked to verify your email address before you can start using the service. Once you have verified your email, you will be taken to the Speech Synthesis page, where you can immediately start using the service. Simply type anything into the box and press “generate” to convert the text into voiceover narration. Please note that each time you press “generate” anywhere on the website, it will deduct credits from your quota.

If you sign up using Google OAuth, your account will be intrinsically linked to your Google account, meaning you will not be able to change your email address, as it will always be linked to your Google email.

Subscriptions
-------------

Once you sign up, you will be automatically assigned to the free tier. To view your subscription, click on “My Account” in the bottom left corner and select [“Subscription”](https://elevenlabs.io/app/subscription). You can read more about the different plans [here](https://elevenlabs.io/pricing). If you scroll down, you will find a comparison table that can be quite helpful in highlighting the differences between the various plans.

We offer five public plans: Free, Starter, Creator, Pro, Scale, and Business. In addition, we also offer a sixth option - Enterprise - tailored to the unique needs and usage of our clients.

You can see details of all our plans on the subscription page. This includes information about the total monthly credit quota, the number of custom voices you can have saved simultaneously, and the quality of audio produced.

Cloning is only available on the Starter tier and above. However, the free plan offers three custom voices that you can create using our Voice Design tool, or you can add voices from the Voice Library if they are not limited to paid tiers only.

You can upgrade your subscription at any time, and any unused quota from your previous plan will roll over to the new one. As long as you don’t cancel or downgrade, unused credits at the end of the month will carry over to the next month, up to a maximum of two months’ worth of credits. For more information, please visit our Help Center articles:

*   [“How does credit rollover work?"](https://help.elevenlabs.io/hc/en-us/articles/27561768104081-How-does-credit-rollover-work)
*   ["What happens to my subscription and quota at the end of the month?”](https://help.elevenlabs.io/hc/en-us/articles/13514114771857-What-happens-to-my-subscription-and-quota-at-the-end-of-the-month)

From the subscription page, you can also downgrade your subscription at any point in time if you would like. When downgrading, it won’t take effect until the current cycle ends, ensuring that you won’t lose any of the monthly quota before your month is up.

When generating content on our paid plans, you get commercial rights to use that content. If you are on the free plan, you can use the content non-commercially with attribution. Read more about the license in our [Terms of Service](https://elevenlabs.io/terms) and in our Help Center [here](https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform-).

For more information on payment methods, please refer to the [Help Center](https://help.elevenlabs.io/).

## Metadata

```json
{
  "title": "Introduction — ElevenLabs Documentation",
  "description": "Explore our Guides and API Reference to get the most out of ElevenLabs.",
  "url": "https://docs.elevenlabs.io/api-reference/text-to-speech-stream",
  "content": "Welcome\n-------\n\nIn this documentation we will help you get started with [ElevenLabs](https://elevenlabs.io/). Before we get started, we would like to mention that we also offer a [Help Center](https://help.elevenlabs.io/hc/en-us) which is more of an FAQ. Here, you can find answers to individual questions and interact with our chatbot. Additionally, you can submit tickets directly to our support team if you have any inquiries.\n\n### Create\n\nWe will cover everything, beginning with Text to Speech and Speech to Speech, where you will generate your first audio using our Default Voices.\n\nWe also provide several features that extend beyond the realm of speech, including our Sound Effects Generator and our upcoming [Music Generator](https://www.youtube.com/watch?v=d8k4Pit4_ZU) (release date and name to be determined).\n\n###### Text to Speech (Speech Synthesis)\n\nOur Text-to-Speech technology, also known as Speech Synthesis, is the core of ElevenLabs. It serves as the foundation for many of the features we offer and powers many services worldwide. This technology transforms text into incredibly realistic speech.\n\nTo ensure you get the most out of this feature, it is important to use an appropriate voice for what you are trying to achieve and to familiarize yourself with the different models we offer, as both of these factors have a tremendous effect on the delivery and quality of the output.\n\n###### Speech to Speech (Voice Changer)\n\nOur Speech-to-Speech technology, also known as Voice Changer, converts a source voice (audio input) into a different voice while retaining the source voice’s accent, cadence, and overall delivery, but with the timbre and vocal quality of the selected voice.\n\nThis feature is great for standalone usage, as it provides your voice acting with a wider range of tonalities. Additionally, when used in conjunction with Text-to-Speech, it allows for easy correction of pronunciations and adds specific performances or characteristics, emulating subtle vocal nuances for a more human touch. You can make the AI whisper, sigh, laugh, or cry by simply acting it out and then using the voice changer.\n\n###### Sound Effects\n\nOur Sound Effects generator allows you to create a wide range of audio effects by inputting descriptive prompts. This feature is great across variety of uses, such as film sound design, video game audio, music production, and much more. Users can generate sounds by typing a description into a text box, and the AI will produce multiple variations based on the given prompt.\n\nThe tool offers settings to control the duration of the sound and how closely the output adheres to the prompt.\n\n###### Music (in development)\n\n### Voices\n\nOnce you have created your first audio output, we will proceed to cloning or designing your first voice on the My Voices page. After setting up your voices, you will be able to use your own voices to generate audio.\n\n###### Voice Design\n\nVoice Design allows for the creation of unique voices from text prompts, filling gaps when specific voices aren’t available in the Voice Library or where you might even prefer a synthetically generated voice. You can create both realistic voices, which focus on attributes like age, accent, and emotion, and character voices, which allow you to create more creative voices by using more creative language.\n\n###### Instant Voice Cloning\n\nInstant Voice Cloning enables you to create voice clones quickly from short audio samples, without the need for training. It uses a technology to create voice instantaneously, capturing its tone and inflections. While effective for many voices, it may struggle with unique accents or voices not encountered during training. High-quality, consistent audio samples are crucial for optimal results.\n\n###### Professional Voice Cloning\n\nProfessional Voice Cloning creates hyper-realistic voice models by training on larger datasets of a speaker’s voice. Available from the Creator tier and above, it offers extremely higher accuracy and can capture intricate details, such as accents and tonal nuances. This method requires more audio data, between 1 - 3 hours, and a few hours to train the model but results in a voice clone that closely resembles the original.\n\n[](https://elevenlabs.io/docs/product/voices/voice-lab/professional-voice-cloning)\n\n###### Voice Library\n\nThe Voice Library is a marketplace where users can share and discover a wide variety of voices, including professional voice clones from real people who have cloned their voices and decided to share them with the rest of the community.\n\nIt offers filters and search options to help users find specific voice styles, languages, and accents. Users can add voices to “My Voices” for use across ElevenLabs features, and shared voices can earn either credits or monetary rewards based on usage.\n\n### Workflows\n\nMoving on, we will also go through our workflow-specific section, where we offer a variety of tools and workflows for different needs.\n\nFirst, we will start with Projects, which is our end-to-end solution for creating voiceovers for long-form content, such as articles or audiobooks, with just a few clicks.\n\nWe will cover Dubbing, our solution for making content more accessible in all languages while preserving the original voice and striving to maintain the same performance across languages. This service comes in two flavors: automatic and studio.\n\nOur automatic solution allows users to create dubs in any language supported by the AI with just a few clicks. Meanwhile, the Dubbing Studio provides an end-to-end workflow with great controllability for producing perfect dubs.\n\nFinally, we will cover our Conversation AI platform, which provides an easy setup process for quickly and easily deploying conversational AI, as well as API endpoints and SDKs, to allow for seamless integration into your existing applications or flows.\n\n###### Projects\n\nProjects is a comprehensive tool for creating long-form audio content, such as audiobooks. It allows users to upload documents or web pages and generate voiceover narrations. It is easy to manage and keep track of all of your projects, select voices, and adjust settings for quality and download options. Projects is available on paid tiers, offering an efficient workflow for producing lengthy audio content.\n\n###### Dubbing\n\nDubbing allows you to create high-quality dubs in various languages while preserving the original performance. You can upload or import video/audio files and select the original and target languages. The tool supports multiple formats and offers options for modifying specific parts of the dub. It’s available on all plans, with advanced features in the Dubbing Studio.\n\n[](https://elevenlabs.io/docs/product/dubbing/overview)\n\n###### Automatic\n\nAutomatic Dubbing quickly translates and replaces the original audio of a video with a dub in a new language, maintaining the original speaker’s voice characteristics. It provides a final output without the option for edits, making it ideal for fast and straightforward dubbing needs. You can upload files or import them via URL to start the process.\n\n[](https://elevenlabs.io/docs/api-reference/create-dub)\n\n###### Studio\n\nDubbing Studio offers an advanced dubbing experience, allowing you to edit and customize dubs extensively. It supports manual transcription adjustments, voice selection, and precise timing edits. You can manage speaker tracks, regenerate audio, and export the final output in various formats. This feature provides full control over the dubbing process, ideal for detailed and tailored projects.\n\n[](https://elevenlabs.io/docs/product/dubbing/studio)\n\n###### Voiceover Studio\n\nVoiceover Studio allows you to create interactive audio content with flexibility. It combines an audio timeline with text-to-speech, speech-to-speech, and sound effects, enabling the creation of dialogues between multiple speakers. You can upload videos or start projects from scratch, adding voiceover and sound effects tracks. Available on the Creator plan and above, it offers tools for crafting detailed and dynamic voiceover projects.\n\n[](https://elevenlabs.io/docs/product/voiceover-studio/overview)\n\n###### Audio Native\n\nAudio Native is an embedded audio player that automatically voices web page content using ElevenLabs’ text-to-speech service. It allows embedding pre-generated audio from projects into web pages with a simple HTML snippet. Available on the Creator plan and above, it includes metrics for tracking audience engagement through a listener dashboard.\n\n###### Conversational AI\n\nConversational AI is a platform for deploying interactive voice agents that can interact with you or your users in natural conversations. It integrates Speech to Text, Language Models, and Text to Speech, along with features like interruption handling and turn-taking logic. Users can customize agents with different voices and system prompts, making it suitable for applications like customer service, virtual assistants, and interactive characters.\n\nSigning up\n----------\n\nYou can sign up using the traditional method of email plus password or using Google OAuth.\n\nIf you choose to sign up with your email, you will be asked to verify your email address before you can start using the service. Once you have verified your email, you will be taken to the Speech Synthesis page, where you can immediately start using the service. Simply type anything into the box and press “generate” to convert the text into voiceover narration. Please note that each time you press “generate” anywhere on the website, it will deduct credits from your quota.\n\nIf you sign up using Google OAuth, your account will be intrinsically linked to your Google account, meaning you will not be able to change your email address, as it will always be linked to your Google email.\n\nSubscriptions\n-------------\n\nOnce you sign up, you will be automatically assigned to the free tier. To view your subscription, click on “My Account” in the bottom left corner and select [“Subscription”](https://elevenlabs.io/app/subscription). You can read more about the different plans [here](https://elevenlabs.io/pricing). If you scroll down, you will find a comparison table that can be quite helpful in highlighting the differences between the various plans.\n\nWe offer five public plans: Free, Starter, Creator, Pro, Scale, and Business. In addition, we also offer a sixth option - Enterprise - tailored to the unique needs and usage of our clients.\n\nYou can see details of all our plans on the subscription page. This includes information about the total monthly credit quota, the number of custom voices you can have saved simultaneously, and the quality of audio produced.\n\nCloning is only available on the Starter tier and above. However, the free plan offers three custom voices that you can create using our Voice Design tool, or you can add voices from the Voice Library if they are not limited to paid tiers only.\n\nYou can upgrade your subscription at any time, and any unused quota from your previous plan will roll over to the new one. As long as you don’t cancel or downgrade, unused credits at the end of the month will carry over to the next month, up to a maximum of two months’ worth of credits. For more information, please visit our Help Center articles:\n\n*   [“How does credit rollover work?\"](https://help.elevenlabs.io/hc/en-us/articles/27561768104081-How-does-credit-rollover-work)\n*   [\"What happens to my subscription and quota at the end of the month?”](https://help.elevenlabs.io/hc/en-us/articles/13514114771857-What-happens-to-my-subscription-and-quota-at-the-end-of-the-month)\n\nFrom the subscription page, you can also downgrade your subscription at any point in time if you would like. When downgrading, it won’t take effect until the current cycle ends, ensuring that you won’t lose any of the monthly quota before your month is up.\n\nWhen generating content on our paid plans, you get commercial rights to use that content. If you are on the free plan, you can use the content non-commercially with attribution. Read more about the license in our [Terms of Service](https://elevenlabs.io/terms) and in our Help Center [here](https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform-).\n\nFor more information on payment methods, please refer to the [Help Center](https://help.elevenlabs.io/).",
  "usage": {
    "tokens": 2483
  }
}
```
