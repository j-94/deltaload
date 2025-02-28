---
title: How ChatGPT and GPT-4 Can Be Used for 3D Content Generation
description: See how GPT-4 was combined with Omniverse DeepSearch for a custom generative AI extension that retrieves 3D objects with text prompts and adds them to a  scene.
url: https://medium.com/@nvidiaomniverse/chatgpt-and-gpt-4-for-3d-content-generation-9cbe5d17ec15
timestamp: 2025-01-20T15:43:05.625Z
domain: medium.com
path: @nvidiaomniverse_chatgpt-and-gpt-4-for-3d-content-generation-9cbe5d17ec15
---

# How ChatGPT and GPT-4 Can Be Used for 3D Content Generation


See how GPT-4 was combined with Omniverse DeepSearch for a custom generative AI extension that retrieves 3D objects with text prompts and adds them to a  scene.


## Content

Developing custom AI tools for 3D workflows is easy in NVIDIA Omniverse
-----------------------------------------------------------------------

[![Image 21: NVIDIA Omniverse](https://miro.medium.com/v2/resize:fill:88:88/1*AMdz0Pn1o9ExyoOVxk5pUw@2x.jpeg)](https://medium.com/@nvidiaomniverse?source=post_page---byline--9cbe5d17ec15--------------------------------)

_By: Mario Viviani, Manager, Developer Relations, NVIDIA Omniverse_

![Image 22](https://miro.medium.com/v2/resize:fit:700/0*tjH9QDo5JPKd79sT)

Demand for 3D worlds and virtual environments is growing exponentially across the world’s industries. 3D workflows are core to industrial digitalization, developing real-time simulations to test and validate autonomous vehicles and robots, operating digital twins to optimize industrial manufacturing, and paving new paths for scientific discovery.

Today, 3D design and world building is still highly manual. While 2D artists and designers have been graced with [assistant tools](https://www.nvidia.com/en-us/studio/canvas/), 3D workflows remain filled with repetitive, tedious tasks.

Creating or finding objects for a scene is a time-intensive process that requires specialized 3D skills honed over time like modeling and texturing. Placing objects correctly and art directing a 3D environment to perfection requires hours of fine tuning.

To reduce manual, repetitive tasks and help creators and designers focus on the creative, enjoyable aspects of their work, NVIDIA has launched numerous AI projects like [generative AI tools for virtual worlds](https://developer.nvidia.com/blog/rapidly-generate-3d-assets-for-virtual-worlds-with-generative-ai/).

The iPhone moment of AI
-----------------------

With ChatGPT, we are now experiencing the [iPhone moment of AI](https://stratechery.com/2023/an-interview-with-nvidia-ceo-jensen-huang-about-ais-iphone-moment/), where individuals of all technical levels can interact with an advanced computing platform using everyday language. [Large language models](https://blogs.nvidia.com/blog/2023/01/26/what-are-large-language-models-used-for/) (LLMs) had been growing increasingly sophisticated, and when a user-friendly interface like ChatGPT made them accessible to everyone, it became the [fastest-growing consumer application in history](https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/), surpassing 100 million users just two months after launching. Now, every industry is planning to harness the power of AI for a wide range of applications like drug discovery, autonomous machines, and avatar virtual assistants.

Recently, we experimented with OpenAI’s viral ChatGPT and new GPT-4 large multimodal model to show how easy it is to develop custom tools that can rapidly generate 3D objects for virtual worlds in [NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/). Compared to ChatGPT, GPT-4 marks a “pretty substantial improvement across many dimensions,” said OpenAI co-founder Ilya Sutskever in a [fireside chat](https://blogs.nvidia.com/blog/2023/03/22/sutskever-openai-gtc/) with NVIDIA founder and CEO Jensen Huang at [GTC 2023](https://www.nvidia.com/gtc/).

By combining GPT-4 with [Omniverse DeepSearch](https://docs.omniverse.nvidia.com/prod_nucleus/prod_nucleus/features.html#deepsearch), a smart AI librarian that’s able to search through massive databases of untagged 3D assets, we were able to quickly develop a custom extension that retrieves 3D objects with simple, text-based prompts and automatically add them to a 3D scene.

AI Room Generator Extension
---------------------------

This fun experiment in [NVIDIA Omniverse](https://developer.nvidia.com/omniverse), a development platform for 3D applications, shows developers and technical artists how easy it is to quickly develop custom tools that leverage generative AI to populate realistic environments. End users can simply enter text-based prompts to automatically generate and place high-fidelity objects, saving hours of time that would typically be required to create a complex scene.

Objects generated from the extension are based on [Universal Scene Description](https://www.nvidia.com/en-us/omniverse/usd/) (USD) [SimReady assets](https://developer.nvidia.com/omniverse/simready-assets). SimReady assets are physically-accurate 3D objects that can be used in any simulation and behave as they would in the real world.

**Getting information about the 3D Scene**
------------------------------------------

Everything starts with the USD scene in Omniverse. Users can easily circle an area using the Pencil tool in Omniverse, type in the kind of room/environment they want to generate — for example, a warehouse, or a reception room — and with one click that area is created.

![Image 23](https://miro.medium.com/v2/resize:fit:700/0*lU1j_uiLRmYtf0N4)

**Creating the Prompt for ChatGPT**
-----------------------------------

The ChatGPT prompt is composed of four pieces: system input, user input example, assistant output example, and user prompt.

Let’s start with the aspects of the prompt that tailor to the user’s scenario. This includes text that the user inputs plus data from the scene.

For example, if the user wants to create a reception room, they specify something like “This is the room where we meet our customers. Make sure there is a set of comfortable armchairs, a sofa and a coffee table.” Or, if they want to add a certain number of items they could add “make sure to include a minimum of 10 items.”

This text is combined with scene information like the size and name of the area where we will place items as the **User Prompt.**

“Reception room, 7x10m, origin at (0.0,0.0,0.0). This is the room where we meet   
our customers. Make sure there is a set of comfortable armchairs, a sofa and a   
coffee table”

This notion of combining the user’s text with details from the scene is powerful. It’s much simpler to select an object in the scene and programatically access its details than requiring the user to write a prompt to describe all these details. I suspect we’ll see a lot of Omniverse extensions that make use of this Text + Scene to Scene pattern.

Beyond the user prompt, we also need to prime ChatGPT with a system prompt and a shot or two for training.

In order to create predictable, deterministic results, the AI is instructed by the system prompt and examples to **specifically return a JSON with all the information formatted in a well-defined way**, so it can then be used in Omniverse.

Here are the four pieces of the prompt that we will send.

**System Prompt**
-----------------

This sets the constraints and instructions for the AI

You are an area generator expert. Given an area of a certain size, you can generate a list of items that are appropriate to that area, in the right place.You operate in a 3D Space. You work in a X,Y,Z coordinate system. X denotes width, Y denotes height, Z denotes depth. 0.0,0.0,0.0 is the default space origin.

You receive from the user the name of the area, the size of the area on X and Z axis in centimeters, the origin point of the area (which is at the center of the area).

You answer by only generating JSON files that contain the following information:

\- area\_name: name of the area  
\- X: coordinate of the area on X axis  
\- Y: coordinate of the area on Y axis  
\- Z: coordinate of the area on Z axis  
\- area\_size\_X: dimension in cm of the area on X axis  
\- area\_size\_Z: dimension in cm of the area on Z axis  
\- area\_objects\_list: list of all the objects in the area

For each object you need to store:  
\- object\_name: name of the object  
\- X: coordinate of the object on X axis  
\- Y: coordinate of the object on Y axis  
\- Z: coordinate of the object on Z axis

Each object name should include an appropriate adjective.

Keep in mind, objects should be placed in the area to create the most meaningful layout possible, and they shouldn't overlap.  
All objects must be within the bounds of the area size; Never place objects further than 1/2 the length or 1/2 the depth of the area from the origin.  
Also keep in mind that the objects should be disposed all over the area in respect to the origin point of the area, and you can use negative values as well to display items correctly, since the origin of the area is always at the center of the area.

Remember, you only generate JSON code, nothing else. It's very important.

**User Input Example**
----------------------

This is an example of what a user might submit. Notice that it’s a combination of data from the scene and text prompt.

"Reception room, 7x10m, origin at (0.0,0.0,0.0). This is the room where we meet   
our customers. Make sure there is a set of comfortable armchairs, a sofa and a   
coffee table"

**Assistant Output Example**
----------------------------

This provides a template that the AI must use. Notice how we’re describing the exact JSON we expect.

{  
    "area\_name": "Reception",  
    "X": 0.0,  
    "Y": 0.0,  
    "Z": 0.0,  
    "area\_size\_X": 700,  
    "area\_size\_Z": 1000,  
    "area\_objects\_list": \[  
        {  
            "object\_name": "White\_Round\_Coffee\_Table",  
            "X": -120,  
            "Y": 0.0,  
            "Z": 130  
        },  
        {  
            "object\_name": "Leather\_Sofa",  
            "X": 250,  
            "Y": 0.0,  
            "Z": -90  
        },  
        {  
            "object\_name": "Comfortable\_Armchair\_1",  
            "X": -150,  
            "Y": 0.0,  
            "Z": 50  
        },  
        {  
            "object\_name": "Comfortable\_Armchair\_2",  
            "X": -150,  
            "Y": 0.0,  
            "Z": -50  
        }  \]  
}

**Connecting to OpenAI**
------------------------

This prompt is sent to the AI from the Extension via Python code. This is quite easy in Omniverse Kit and can be done with just a couple commands using the latest [O](https://pypi.org/project/openai/)[penAI Python Library](https://pypi.org/project/openai/). Notice that we are passing to the OpenAI API the system input, the sample user input and the sample expected assistant output we have just outlined. The variable “response” will contain the expected response from ChatGPT.

\# Create a completion using the chatGPT model     
 response = openai.ChatCompletion.create(  
         model="gpt-3.5-turbo",  
         # if you have access, you can swap to model="gpt-4",  
                    messages=\[  
                            {"role": "system", "content": system\_input},  
                            {"role": "user", "content": user\_input},  
                            {"role": "assistant", "content": assistant\_input},  
                            {"role": "user", "content": my\_prompt},  
                             \]  
                    )  
    # parse response and extract text  
    text = response\["choices"\]\[0\]\["message"\]\['content'\]

**Passing the result from ChatGPT to Omniverse DeepSearch API and generating the scene**
----------------------------------------------------------------------------------------

![Image 24](https://miro.medium.com/v2/resize:fit:700/0*K2MrfLg3Cr36E2Ux)

The items from the ChatGPT JSON response are then parsed by the extension and passed to the Omnivere DeepSearch API. DeepSearch allows users to search 3D models stored within an Omniverse Nucleus server using natural language queries.

This means that even if we don’t know the exact file name of a model of a sofa, for example, we can retrieve it just by searching for “Comfortable Sofa” which is exactly what we got from ChatGPT.

DeepSearch understands natural language and by asking it for a “Comfortable Sofa” we get a list of items that our helpful AI librarian has decided are best suited from the selection of assets we have in our current asset library. It is surprisingly good at this and so we often can use the first item it returns, but of course we build in choice in case the user wants to select something from the list.

From there, we simply add the object to the stage.

**Adding items from DeepSearch into Omniverse stage**
-----------------------------------------------------

![Image 25](https://miro.medium.com/v2/resize:fit:700/0*WR5Zbz2EgxQDyvZC)

Now that DeepSearch has returned results, we just need to place the objects in Omniverse. In our extension, we created a function called place\_deepsearch\_results() that processes all the items and places them in the scene.

def place\_deepsearch\_results(gpt\_results, query\_result, root\_prim\_path):  
        index = 0  
        for item in query\_result:  
            # Define Prim            
            stage = omni.usd.get\_context().get\_stage()prim\_parent\_path = root\_prim\_path + item\[‘object\_name’\].replace(" ", "\_")  
            parent\_xForm = UsdGeom.Xform.Define(stage, prim\_parent\_path)

prim\_path = prim\_parent\_path + "/" + item\[‘object\_name’\].replace(" ", "\_")  
            next\_prim = stage.DefinePrim(prim\_path, 'Xform')

# Add reference to USD Asset  
            references: Usd.references = next\_prim.GetReferences()

references.AddReference(  
                assetPath="your\_server://your\_asset\_folder" + item\[‘asset\_path’\])

# Add reference for future search refinement   
            config = next\_prim.CreateAttribute("DeepSearch:Query", Sdf.ValueTypeNames.String)  
            config.Set(item\[‘object\_name’\])

# translate prim  
            next\_object = gpt\_results\[index\]  
            index = index + 1  
            x = next\_object\['X'\]  
            y = next\_object\['Y'\]  
            z = next\_object\['Z'\]

This method to place items, iterates over the query\_result items that we got from GPT, creating and defining new primitives using the USD API, setting their transformations and attributes based on data in gpt\_results. We also save the DeepSearch query in an attribute in the USD, so it can be used afterwards in case we want to run DeepSearch again. Note that the assetPath “your\_server//your\_asset\_folder” is a placeholder and should be substituted with the real path of the folder where DeepSearch is performed.

And voila! We have our AI-generated scene in Omniverse!

**Swapping items using DeepSearch**
-----------------------------------

However, we might not like all the items that are retrieved the first time. So, we built a small companion extension to allow users to browse for similar objects and swap them in with just a click. With Omniverse, it is very easy to build in a modular way so you can easily extend your workflows with additional extensions.

![Image 26](https://miro.medium.com/v2/resize:fit:480/0*xJjOOhsDTLwEiaag)

This companion extension is quite simple. It takes as argument an object generated via DeepSearch, and offers two buttons to get the next or previous object from the related DeepSearch query. For example, if the USD file contained the Attribute “DeepSearch:Query = Modern Sofa”, it would run this search again via DeepSearch and get the next best result. You could of course extend this to be a visual UI with pictures of all the search results similar to the window we use for general DeepSearch queries. To keep this example simple, we just opted for two simple buttons.

See the code below that shows the functions to increment the index, and the function _replace\_reference(self)_ that is actually operating the swap of the object based on the index.

def increment\_prim\_index():  
            if self.\_query\_results is None:  
                return self.\_index = self.\_index + 1

if self.\_index \>\= len(self.\_query\_results.paths):  
                self.\_index = 0

self.replace\_reference()

def replace\_reference(self):  
        references: Usd.references = self.\_selected\_prim.GetReferences()  
        references.ClearReferences()  
        references.AddReference(  
                assetPath="your\_server://your\_asset\_folder" + self.\_query\_results.paths\[self.\_index\].uri)

Note that, as above, the path “your\_server://your\_asset\_folder” is just a placeholder, and you should replace it with the Nucleus folder where your DeepSearch query gets performed.

![Image 27](https://miro.medium.com/v2/resize:fit:700/0*hpXw_C-Wnb9NbUZJ)

A gray couch swapped in for the brown couch using DeepSearch

This shows how by combining the power of LLMs and Omniverse APIs it is possible to create tools that power creativity and speed up processes.

From ChatGPT to GPT-4
---------------------

One of the main advancements in OpenAI’s new GPT-4 is its increased spatial awareness in large language models.

We initially used ChatGPT API, which is based on GPT-3.5-turbo. While it offered good spatial awareness, GPT-4 offers much better results. The version you see in the video above is using GPT-4.

GPT-4 is vastly improved in respect to GPT-3.5 at solving complex tasks and comprehending complex instructions. Therefore we could be much more descriptive and use natural language when engineering the text prompt to “instruct the AI”

We could give the AI very explicit instructions like:

*   “Each object name should include an appropriate adjective.”
*   “Keep in mind, objects should be placed in the area to create the most meaningful layout possible, and they shouldn’t overlap.”
*   “All objects must be within the bounds of the area size; Never place objects further than 1/2 the length or 1/2 the depth of the area from the origin.”
*   “Also keep in mind that the objects should be placed all over the area in respect to the origin point of the area, and you can use negative values as well to display items correctly, since the origin of the area is always at the center of the area.”

The fact that these system prompts are being appropriately followed by the AI when generating the response is particularly impressive, as the AI demonstrates to have a good understanding of spatial awareness and how to properly place items. One of the challenges of using GPT-3.5 for this task is that sometimes objects were spawned outside the room, or at odd placements.

GPT-4 not only places objects within the right boundaries of the room, but also places objects logically: a bedside table will actually show up on the side of a bed, a coffee table will be placed in between two sofas, and so on.

With this, we’re likely just scratching the surface of what LLMs can do in 3D spaces!

Building your own ChatGPT-powered extension
-------------------------------------------

While this is just a small demo of what AI can do once it’s connected to a 3D space, we believe it will open doors to a wide range of tools beyond scene building. Developers can build AI-powered extensions in Omniverse for lighting, cameras, animations, character dialog, and other elements that optimize creator workflows. They can even develop tools to attach physics to scenes and run entire simulations.

You can download and experiment with the [AI Room Generator Extension Sample on GitHub](https://github.com/NVIDIA-Omniverse/kit-extension-sample-airoomgenerator). We encourage other developers to try building on the extension or creating their own generative AI extensions for Omniverse.

Using Omniverse Kit, you can start integrating AI into your extensions today. [Download Omniverse](https://www.nvidia.com/en-us/omniverse/download/) to get started.

_Get started with NVIDIA Omniverse by downloading the standard license_ [_free_](https://www.nvidia.com/en-us/omniverse/download/)_, or learn how_ [_Omniverse Enterprise can connect your team_](https://www.nvidia.com/en-us/omniverse/enterprise/)_. If you are a developer,_ [_get started with Omniverse_](https://developer.nvidia.com/omniverse/get-started/) _resources. Stay up to date on the platform by subscribing to the_ [_newsletter_](https://nvda.ws/3u5KPv1)_, and following NVIDIA Omniverse on_ [_Instagram_](https://www.instagram.com/nvidiaomniverse/)_,_ [_Medium_](https://medium.com/@nvidiaomniverse)_, and_ [_Twitter_](https://twitter.com/nvidiaomniverse)_. For resources, check out our_ [_forums_](https://forums.developer.nvidia.com/c/omniverse/300)_,_ [_Discord server_](https://discord.com/invite/XWQNJDNuaC)_,_ [_Twitch_](https://www.twitch.tv/nvidiaomniverse)_, and_ [_YouTube_](https://www.youtube.com/channel/UCSKUoczbGAcMld7HjpCR8OA) _channels._

**About the Author**

![Image 28](https://miro.medium.com/v2/resize:fit:700/0*gr95rGPhN5chTAkC)

Mario Viviani is Manager of Developer Relations for Omniverse at NVIDIA, based in London, UK. His team focuses on helping developers and partners get familiar and onboard on NVIDIA Omniverse. Passionate technologist and hands on-developer, he’s ex-Amazon, where he led the global Apps and Games Tech Evangelism team; previously was co-founder of startups and led his own consulting company in mobile apps development. He is always projected into the future and into what is the next “big thing”!

## Metadata

```json
{
  "title": "How ChatGPT and GPT-4 Can Be Used for 3D Content Generation",
  "description": "See how GPT-4 was combined with Omniverse DeepSearch for a custom generative AI extension that retrieves 3D objects with text prompts and adds them to a  scene.",
  "url": "https://medium.com/@nvidiaomniverse/chatgpt-and-gpt-4-for-3d-content-generation-9cbe5d17ec15",
  "content": "Developing custom AI tools for 3D workflows is easy in NVIDIA Omniverse\n-----------------------------------------------------------------------\n\n[![Image 21: NVIDIA Omniverse](https://miro.medium.com/v2/resize:fill:88:88/1*AMdz0Pn1o9ExyoOVxk5pUw@2x.jpeg)](https://medium.com/@nvidiaomniverse?source=post_page---byline--9cbe5d17ec15--------------------------------)\n\n_By: Mario Viviani, Manager, Developer Relations, NVIDIA Omniverse_\n\n![Image 22](https://miro.medium.com/v2/resize:fit:700/0*tjH9QDo5JPKd79sT)\n\nDemand for 3D worlds and virtual environments is growing exponentially across the world’s industries. 3D workflows are core to industrial digitalization, developing real-time simulations to test and validate autonomous vehicles and robots, operating digital twins to optimize industrial manufacturing, and paving new paths for scientific discovery.\n\nToday, 3D design and world building is still highly manual. While 2D artists and designers have been graced with [assistant tools](https://www.nvidia.com/en-us/studio/canvas/), 3D workflows remain filled with repetitive, tedious tasks.\n\nCreating or finding objects for a scene is a time-intensive process that requires specialized 3D skills honed over time like modeling and texturing. Placing objects correctly and art directing a 3D environment to perfection requires hours of fine tuning.\n\nTo reduce manual, repetitive tasks and help creators and designers focus on the creative, enjoyable aspects of their work, NVIDIA has launched numerous AI projects like [generative AI tools for virtual worlds](https://developer.nvidia.com/blog/rapidly-generate-3d-assets-for-virtual-worlds-with-generative-ai/).\n\nThe iPhone moment of AI\n-----------------------\n\nWith ChatGPT, we are now experiencing the [iPhone moment of AI](https://stratechery.com/2023/an-interview-with-nvidia-ceo-jensen-huang-about-ais-iphone-moment/), where individuals of all technical levels can interact with an advanced computing platform using everyday language. [Large language models](https://blogs.nvidia.com/blog/2023/01/26/what-are-large-language-models-used-for/) (LLMs) had been growing increasingly sophisticated, and when a user-friendly interface like ChatGPT made them accessible to everyone, it became the [fastest-growing consumer application in history](https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/), surpassing 100 million users just two months after launching. Now, every industry is planning to harness the power of AI for a wide range of applications like drug discovery, autonomous machines, and avatar virtual assistants.\n\nRecently, we experimented with OpenAI’s viral ChatGPT and new GPT-4 large multimodal model to show how easy it is to develop custom tools that can rapidly generate 3D objects for virtual worlds in [NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/). Compared to ChatGPT, GPT-4 marks a “pretty substantial improvement across many dimensions,” said OpenAI co-founder Ilya Sutskever in a [fireside chat](https://blogs.nvidia.com/blog/2023/03/22/sutskever-openai-gtc/) with NVIDIA founder and CEO Jensen Huang at [GTC 2023](https://www.nvidia.com/gtc/).\n\nBy combining GPT-4 with [Omniverse DeepSearch](https://docs.omniverse.nvidia.com/prod_nucleus/prod_nucleus/features.html#deepsearch), a smart AI librarian that’s able to search through massive databases of untagged 3D assets, we were able to quickly develop a custom extension that retrieves 3D objects with simple, text-based prompts and automatically add them to a 3D scene.\n\nAI Room Generator Extension\n---------------------------\n\nThis fun experiment in [NVIDIA Omniverse](https://developer.nvidia.com/omniverse), a development platform for 3D applications, shows developers and technical artists how easy it is to quickly develop custom tools that leverage generative AI to populate realistic environments. End users can simply enter text-based prompts to automatically generate and place high-fidelity objects, saving hours of time that would typically be required to create a complex scene.\n\nObjects generated from the extension are based on [Universal Scene Description](https://www.nvidia.com/en-us/omniverse/usd/) (USD) [SimReady assets](https://developer.nvidia.com/omniverse/simready-assets). SimReady assets are physically-accurate 3D objects that can be used in any simulation and behave as they would in the real world.\n\n**Getting information about the 3D Scene**\n------------------------------------------\n\nEverything starts with the USD scene in Omniverse. Users can easily circle an area using the Pencil tool in Omniverse, type in the kind of room/environment they want to generate — for example, a warehouse, or a reception room — and with one click that area is created.\n\n![Image 23](https://miro.medium.com/v2/resize:fit:700/0*lU1j_uiLRmYtf0N4)\n\n**Creating the Prompt for ChatGPT**\n-----------------------------------\n\nThe ChatGPT prompt is composed of four pieces: system input, user input example, assistant output example, and user prompt.\n\nLet’s start with the aspects of the prompt that tailor to the user’s scenario. This includes text that the user inputs plus data from the scene.\n\nFor example, if the user wants to create a reception room, they specify something like “This is the room where we meet our customers. Make sure there is a set of comfortable armchairs, a sofa and a coffee table.” Or, if they want to add a certain number of items they could add “make sure to include a minimum of 10 items.”\n\nThis text is combined with scene information like the size and name of the area where we will place items as the **User Prompt.**\n\n“Reception room, 7x10m, origin at (0.0,0.0,0.0). This is the room where we meet   \nour customers. Make sure there is a set of comfortable armchairs, a sofa and a   \ncoffee table”\n\nThis notion of combining the user’s text with details from the scene is powerful. It’s much simpler to select an object in the scene and programatically access its details than requiring the user to write a prompt to describe all these details. I suspect we’ll see a lot of Omniverse extensions that make use of this Text + Scene to Scene pattern.\n\nBeyond the user prompt, we also need to prime ChatGPT with a system prompt and a shot or two for training.\n\nIn order to create predictable, deterministic results, the AI is instructed by the system prompt and examples to **specifically return a JSON with all the information formatted in a well-defined way**, so it can then be used in Omniverse.\n\nHere are the four pieces of the prompt that we will send.\n\n**System Prompt**\n-----------------\n\nThis sets the constraints and instructions for the AI\n\nYou are an area generator expert. Given an area of a certain size, you can generate a list of items that are appropriate to that area, in the right place.You operate in a 3D Space. You work in a X,Y,Z coordinate system. X denotes width, Y denotes height, Z denotes depth. 0.0,0.0,0.0 is the default space origin.\n\nYou receive from the user the name of the area, the size of the area on X and Z axis in centimeters, the origin point of the area (which is at the center of the area).\n\nYou answer by only generating JSON files that contain the following information:\n\n\\- area\\_name: name of the area  \n\\- X: coordinate of the area on X axis  \n\\- Y: coordinate of the area on Y axis  \n\\- Z: coordinate of the area on Z axis  \n\\- area\\_size\\_X: dimension in cm of the area on X axis  \n\\- area\\_size\\_Z: dimension in cm of the area on Z axis  \n\\- area\\_objects\\_list: list of all the objects in the area\n\nFor each object you need to store:  \n\\- object\\_name: name of the object  \n\\- X: coordinate of the object on X axis  \n\\- Y: coordinate of the object on Y axis  \n\\- Z: coordinate of the object on Z axis\n\nEach object name should include an appropriate adjective.\n\nKeep in mind, objects should be placed in the area to create the most meaningful layout possible, and they shouldn't overlap.  \nAll objects must be within the bounds of the area size; Never place objects further than 1/2 the length or 1/2 the depth of the area from the origin.  \nAlso keep in mind that the objects should be disposed all over the area in respect to the origin point of the area, and you can use negative values as well to display items correctly, since the origin of the area is always at the center of the area.\n\nRemember, you only generate JSON code, nothing else. It's very important.\n\n**User Input Example**\n----------------------\n\nThis is an example of what a user might submit. Notice that it’s a combination of data from the scene and text prompt.\n\n\"Reception room, 7x10m, origin at (0.0,0.0,0.0). This is the room where we meet   \nour customers. Make sure there is a set of comfortable armchairs, a sofa and a   \ncoffee table\"\n\n**Assistant Output Example**\n----------------------------\n\nThis provides a template that the AI must use. Notice how we’re describing the exact JSON we expect.\n\n{  \n    \"area\\_name\": \"Reception\",  \n    \"X\": 0.0,  \n    \"Y\": 0.0,  \n    \"Z\": 0.0,  \n    \"area\\_size\\_X\": 700,  \n    \"area\\_size\\_Z\": 1000,  \n    \"area\\_objects\\_list\": \\[  \n        {  \n            \"object\\_name\": \"White\\_Round\\_Coffee\\_Table\",  \n            \"X\": -120,  \n            \"Y\": 0.0,  \n            \"Z\": 130  \n        },  \n        {  \n            \"object\\_name\": \"Leather\\_Sofa\",  \n            \"X\": 250,  \n            \"Y\": 0.0,  \n            \"Z\": -90  \n        },  \n        {  \n            \"object\\_name\": \"Comfortable\\_Armchair\\_1\",  \n            \"X\": -150,  \n            \"Y\": 0.0,  \n            \"Z\": 50  \n        },  \n        {  \n            \"object\\_name\": \"Comfortable\\_Armchair\\_2\",  \n            \"X\": -150,  \n            \"Y\": 0.0,  \n            \"Z\": -50  \n        }  \\]  \n}\n\n**Connecting to OpenAI**\n------------------------\n\nThis prompt is sent to the AI from the Extension via Python code. This is quite easy in Omniverse Kit and can be done with just a couple commands using the latest [O](https://pypi.org/project/openai/)[penAI Python Library](https://pypi.org/project/openai/). Notice that we are passing to the OpenAI API the system input, the sample user input and the sample expected assistant output we have just outlined. The variable “response” will contain the expected response from ChatGPT.\n\n\\# Create a completion using the chatGPT model     \n response = openai.ChatCompletion.create(  \n         model=\"gpt-3.5-turbo\",  \n         # if you have access, you can swap to model=\"gpt-4\",  \n                    messages=\\[  \n                            {\"role\": \"system\", \"content\": system\\_input},  \n                            {\"role\": \"user\", \"content\": user\\_input},  \n                            {\"role\": \"assistant\", \"content\": assistant\\_input},  \n                            {\"role\": \"user\", \"content\": my\\_prompt},  \n                             \\]  \n                    )  \n    # parse response and extract text  \n    text = response\\[\"choices\"\\]\\[0\\]\\[\"message\"\\]\\['content'\\]\n\n**Passing the result from ChatGPT to Omniverse DeepSearch API and generating the scene**\n----------------------------------------------------------------------------------------\n\n![Image 24](https://miro.medium.com/v2/resize:fit:700/0*K2MrfLg3Cr36E2Ux)\n\nThe items from the ChatGPT JSON response are then parsed by the extension and passed to the Omnivere DeepSearch API. DeepSearch allows users to search 3D models stored within an Omniverse Nucleus server using natural language queries.\n\nThis means that even if we don’t know the exact file name of a model of a sofa, for example, we can retrieve it just by searching for “Comfortable Sofa” which is exactly what we got from ChatGPT.\n\nDeepSearch understands natural language and by asking it for a “Comfortable Sofa” we get a list of items that our helpful AI librarian has decided are best suited from the selection of assets we have in our current asset library. It is surprisingly good at this and so we often can use the first item it returns, but of course we build in choice in case the user wants to select something from the list.\n\nFrom there, we simply add the object to the stage.\n\n**Adding items from DeepSearch into Omniverse stage**\n-----------------------------------------------------\n\n![Image 25](https://miro.medium.com/v2/resize:fit:700/0*WR5Zbz2EgxQDyvZC)\n\nNow that DeepSearch has returned results, we just need to place the objects in Omniverse. In our extension, we created a function called place\\_deepsearch\\_results() that processes all the items and places them in the scene.\n\ndef place\\_deepsearch\\_results(gpt\\_results, query\\_result, root\\_prim\\_path):  \n        index = 0  \n        for item in query\\_result:  \n            # Define Prim            \n            stage = omni.usd.get\\_context().get\\_stage()prim\\_parent\\_path = root\\_prim\\_path + item\\[‘object\\_name’\\].replace(\" \", \"\\_\")  \n            parent\\_xForm = UsdGeom.Xform.Define(stage, prim\\_parent\\_path)\n\nprim\\_path = prim\\_parent\\_path + \"/\" + item\\[‘object\\_name’\\].replace(\" \", \"\\_\")  \n            next\\_prim = stage.DefinePrim(prim\\_path, 'Xform')\n\n# Add reference to USD Asset  \n            references: Usd.references = next\\_prim.GetReferences()\n\nreferences.AddReference(  \n                assetPath=\"your\\_server://your\\_asset\\_folder\" + item\\[‘asset\\_path’\\])\n\n# Add reference for future search refinement   \n            config = next\\_prim.CreateAttribute(\"DeepSearch:Query\", Sdf.ValueTypeNames.String)  \n            config.Set(item\\[‘object\\_name’\\])\n\n# translate prim  \n            next\\_object = gpt\\_results\\[index\\]  \n            index = index + 1  \n            x = next\\_object\\['X'\\]  \n            y = next\\_object\\['Y'\\]  \n            z = next\\_object\\['Z'\\]\n\nThis method to place items, iterates over the query\\_result items that we got from GPT, creating and defining new primitives using the USD API, setting their transformations and attributes based on data in gpt\\_results. We also save the DeepSearch query in an attribute in the USD, so it can be used afterwards in case we want to run DeepSearch again. Note that the assetPath “your\\_server//your\\_asset\\_folder” is a placeholder and should be substituted with the real path of the folder where DeepSearch is performed.\n\nAnd voila! We have our AI-generated scene in Omniverse!\n\n**Swapping items using DeepSearch**\n-----------------------------------\n\nHowever, we might not like all the items that are retrieved the first time. So, we built a small companion extension to allow users to browse for similar objects and swap them in with just a click. With Omniverse, it is very easy to build in a modular way so you can easily extend your workflows with additional extensions.\n\n![Image 26](https://miro.medium.com/v2/resize:fit:480/0*xJjOOhsDTLwEiaag)\n\nThis companion extension is quite simple. It takes as argument an object generated via DeepSearch, and offers two buttons to get the next or previous object from the related DeepSearch query. For example, if the USD file contained the Attribute “DeepSearch:Query = Modern Sofa”, it would run this search again via DeepSearch and get the next best result. You could of course extend this to be a visual UI with pictures of all the search results similar to the window we use for general DeepSearch queries. To keep this example simple, we just opted for two simple buttons.\n\nSee the code below that shows the functions to increment the index, and the function _replace\\_reference(self)_ that is actually operating the swap of the object based on the index.\n\ndef increment\\_prim\\_index():  \n            if self.\\_query\\_results is None:  \n                return self.\\_index = self.\\_index + 1\n\nif self.\\_index \\>\\= len(self.\\_query\\_results.paths):  \n                self.\\_index = 0\n\nself.replace\\_reference()\n\ndef replace\\_reference(self):  \n        references: Usd.references = self.\\_selected\\_prim.GetReferences()  \n        references.ClearReferences()  \n        references.AddReference(  \n                assetPath=\"your\\_server://your\\_asset\\_folder\" + self.\\_query\\_results.paths\\[self.\\_index\\].uri)\n\nNote that, as above, the path “your\\_server://your\\_asset\\_folder” is just a placeholder, and you should replace it with the Nucleus folder where your DeepSearch query gets performed.\n\n![Image 27](https://miro.medium.com/v2/resize:fit:700/0*hpXw_C-Wnb9NbUZJ)\n\nA gray couch swapped in for the brown couch using DeepSearch\n\nThis shows how by combining the power of LLMs and Omniverse APIs it is possible to create tools that power creativity and speed up processes.\n\nFrom ChatGPT to GPT-4\n---------------------\n\nOne of the main advancements in OpenAI’s new GPT-4 is its increased spatial awareness in large language models.\n\nWe initially used ChatGPT API, which is based on GPT-3.5-turbo. While it offered good spatial awareness, GPT-4 offers much better results. The version you see in the video above is using GPT-4.\n\nGPT-4 is vastly improved in respect to GPT-3.5 at solving complex tasks and comprehending complex instructions. Therefore we could be much more descriptive and use natural language when engineering the text prompt to “instruct the AI”\n\nWe could give the AI very explicit instructions like:\n\n*   “Each object name should include an appropriate adjective.”\n*   “Keep in mind, objects should be placed in the area to create the most meaningful layout possible, and they shouldn’t overlap.”\n*   “All objects must be within the bounds of the area size; Never place objects further than 1/2 the length or 1/2 the depth of the area from the origin.”\n*   “Also keep in mind that the objects should be placed all over the area in respect to the origin point of the area, and you can use negative values as well to display items correctly, since the origin of the area is always at the center of the area.”\n\nThe fact that these system prompts are being appropriately followed by the AI when generating the response is particularly impressive, as the AI demonstrates to have a good understanding of spatial awareness and how to properly place items. One of the challenges of using GPT-3.5 for this task is that sometimes objects were spawned outside the room, or at odd placements.\n\nGPT-4 not only places objects within the right boundaries of the room, but also places objects logically: a bedside table will actually show up on the side of a bed, a coffee table will be placed in between two sofas, and so on.\n\nWith this, we’re likely just scratching the surface of what LLMs can do in 3D spaces!\n\nBuilding your own ChatGPT-powered extension\n-------------------------------------------\n\nWhile this is just a small demo of what AI can do once it’s connected to a 3D space, we believe it will open doors to a wide range of tools beyond scene building. Developers can build AI-powered extensions in Omniverse for lighting, cameras, animations, character dialog, and other elements that optimize creator workflows. They can even develop tools to attach physics to scenes and run entire simulations.\n\nYou can download and experiment with the [AI Room Generator Extension Sample on GitHub](https://github.com/NVIDIA-Omniverse/kit-extension-sample-airoomgenerator). We encourage other developers to try building on the extension or creating their own generative AI extensions for Omniverse.\n\nUsing Omniverse Kit, you can start integrating AI into your extensions today. [Download Omniverse](https://www.nvidia.com/en-us/omniverse/download/) to get started.\n\n_Get started with NVIDIA Omniverse by downloading the standard license_ [_free_](https://www.nvidia.com/en-us/omniverse/download/)_, or learn how_ [_Omniverse Enterprise can connect your team_](https://www.nvidia.com/en-us/omniverse/enterprise/)_. If you are a developer,_ [_get started with Omniverse_](https://developer.nvidia.com/omniverse/get-started/) _resources. Stay up to date on the platform by subscribing to the_ [_newsletter_](https://nvda.ws/3u5KPv1)_, and following NVIDIA Omniverse on_ [_Instagram_](https://www.instagram.com/nvidiaomniverse/)_,_ [_Medium_](https://medium.com/@nvidiaomniverse)_, and_ [_Twitter_](https://twitter.com/nvidiaomniverse)_. For resources, check out our_ [_forums_](https://forums.developer.nvidia.com/c/omniverse/300)_,_ [_Discord server_](https://discord.com/invite/XWQNJDNuaC)_,_ [_Twitch_](https://www.twitch.tv/nvidiaomniverse)_, and_ [_YouTube_](https://www.youtube.com/channel/UCSKUoczbGAcMld7HjpCR8OA) _channels._\n\n**About the Author**\n\n![Image 28](https://miro.medium.com/v2/resize:fit:700/0*gr95rGPhN5chTAkC)\n\nMario Viviani is Manager of Developer Relations for Omniverse at NVIDIA, based in London, UK. His team focuses on helping developers and partners get familiar and onboard on NVIDIA Omniverse. Passionate technologist and hands on-developer, he’s ex-Amazon, where he led the global Apps and Games Tech Evangelism team; previously was co-founder of startups and led his own consulting company in mobile apps development. He is always projected into the future and into what is the next “big thing”!",
  "publishedTime": "2023-03-30T15:59:53.910Z",
  "usage": {
    "tokens": 4904
  }
}
```
