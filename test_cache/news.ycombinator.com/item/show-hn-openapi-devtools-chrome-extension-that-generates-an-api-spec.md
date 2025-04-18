---
title: Show HN: OpenAPI DevTools – Chrome extension that generates an API spec
description: 
url: https://news.ycombinator.com/item?id=38012032
timestamp: 2025-01-20T15:50:06.414Z
domain: news.ycombinator.com
path: item
---

# Show HN: OpenAPI DevTools – Chrome extension that generates an API spec



## Content

	Hacker News new | past | comments | ask | show | jobs | submit	login



	
	Show HN: OpenAPI DevTools – Chrome extension that generates an API spec (github.com/andrewwalsh)
	811 points by mrmagoo2 on Oct 25, 2023 | hide | past | favorite | 102 comments

	
Effortlessly discover API behaviour with a Chrome extension that automatically generates OpenAPI specifications in real time for any app or website.



	
	
the_absurdist on Oct 25, 2023 | next [–]


I wish this would document the auth headers.

What would be particularly useful is if it saved token values and then (through search) joined them on the response of the auth call to get the initial token.

That way you could easily determine what auth call was needed to get you a token to use the endpoint.



	
	
mrmagoo2 on Oct 25, 2023 | parent | next [–]


Great suggestion, I will look into this.



	
	
hoerzu on Oct 26, 2023 | root | parent | next [–]


I have used llama to figure out the duplications / pathparamters :)



	
	
truemotive on Oct 28, 2023 | root | parent | prev | next [–]


You… you built the thing I’ve been spending 3 days looking for… oh man



	
	
ttul on Oct 25, 2023 | prev | next [–]


This is super cool. Writing code to drop into the JavaScript console lets you do insane things. I’ve found great success using ChatGPT to help me write the code, which I then just cut and paste into the console. Asking it to “make it all run in parallel using async/await” will massively speed up execution of serial tasks.

For instance, I had GPT help me write browser JS that groks literally thousands of IP addresses in an open security tool that shall not be named. I can vacuum much of their entire database in seconds by making hundreds of async calls. While they do have bot protection on the website, they appear to have no protection at all on their browser APIs once the user has been given a cookie… I suspect this is common.



	
	
jhardy54 on Oct 26, 2023 | parent | next [–]


This is about OpenAPI (Swagger), not OpenAI (ChatGPT).



	
	
cxr on Oct 31, 2023 | root | parent | next [–]


This is an extension for Chrome, not Safari.



	
	
ttul on Oct 28, 2023 | root | parent | prev | next [–]


I know.



	
	
a_c on Oct 25, 2023 | prev | next [–]


Love it!

I used https://vite-plugin-web-extension.aklinker1.io/guide/ before to have cross browser extension support. If you don't mind I could take a look to add firefox support (no guarantee)



	
	
mrmagoo2 on Oct 25, 2023 | parent | next [–]


As a follow up, the algorithm that powers this makes use of the chrome.devtools.network API. Specifically it passes the Request object that is in the HAR 1.2 archive format.

So if you can pass the equivalent of that in Firefox/other browsers to the insert method and switch things up a bit, it should be relatively straightforward. I will think about pulling out the core logic into its own lib.

https://developer.chrome.com/docs/extensions/reference/devto...

https://developer.chrome.com/docs/extensions/reference/devto...

https://github.com/AndrewWalsh/openapi-devtools/blob/main/sr...



	
	
a_c on Oct 26, 2023 | root | parent | next [–]


Indeed I have issue here. Firefox maintain a library for unified extension API https://github.com/mozilla/webextension-polyfill

Their type definition for HAR request isn't exported https://github.com/DefinitelyTyped/DefinitelyTyped/blob/mast...

So I can't drop in replace the type on https://github.com/AndrewWalsh/openapi-devtools/blob/main/sr...



	
	
a_c on Oct 26, 2023 | root | parent | next [–]


Also the polyfill has a promise based API rather than a callback, which I don't yet know if there is a workaround



	
	
mrmagoo2 on Oct 25, 2023 | parent | prev | next [–]


Hey absolutely please do, thank you!



	
	
lucasyvas on Oct 25, 2023 | parent | prev | next [–]


This would be excellent



	
	
civilitty on Oct 25, 2023 | parent | prev | next [–]


There's also Plasmo which provides some abstractions over the browsers: https://github.com/PlasmoHQ/plasmo



	
	
parhamn on Oct 25, 2023 | parent | prev | next [–]


Are devtools extensions/panels standardized?



	
	
a_c on Oct 25, 2023 | root | parent | next [–]


Do you mean the devtool protocol[1]? I didn't follow the space so have no knowledge on it. On the other hand there seem to be a polyfilled API on chrome.devtools.network.Request which OP's extension uses extensively https://github.com/DefinitelyTyped/DefinitelyTyped/blob/mast...

[1] https://chromedevtools.github.io/devtools-protocol/



	
	
distortedsignal on Oct 25, 2023 | parent | prev | next [–]


I'd love to see FF support on this.



	
	
archiewood on Oct 25, 2023 | prev | next [–]


My most common use case here is to then want to hit the API from python, and adjust the params / url etc.

Would love a "copy to python requests" button that

grabs the headers

generates a boilerplate python snippet including the headers and the URL:

    import requests
    import json

    url = '<endpoint>'

    headers = {
        'User-Agent': 'Mozilla/5.0 ...',
        ...
    }

    data = {
        "page": 5,
        "size": 28
        ...
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")



	
	
ea016 on Oct 25, 2023 | parent | next [–]


Steps to do so:

- open the network console

- right click on the request

- click "copy as curl"

- visit https://curlconverter.com/ to convert to Python/Node/any language



	
	
tech234a on Oct 25, 2023 | root | parent | next [–]


Also available as a VSCode extension that automatically matches the pasted content to the programming language used in the current file: https://marketplace.visualstudio.com/items?itemName=curlconv...



	
	
verhovsky on Oct 25, 2023 | root | parent | next [–]


I made a fork of the Chrome DevTools that adds "Copy as Python" to the right click menu of each request in the Network tab. You can tell Chrome to use a different version of the DevTools if you start it from the command line

https://github.com/curlconverter/curlconverter/issues/64#iss...



	
	
tilne on Oct 25, 2023 | root | parent | prev | next [–]


Thank you for this. I didn’t know curlconverter existed.



	
	
archiewood on Oct 25, 2023 | root | parent | prev | next [–]


This is my current workflow, though with ChatGPT.

I was just trying to save a few clicks



	
	
novia on Oct 25, 2023 | root | parent | next [–]


You made your request sound important to implement when you already have a workaround that doesn't take very much time...

This is why feature bloat is a thing



	
	
MurageKabui on Oct 25, 2023 | root | parent | prev | next [–]


I was to say this lol



	
	
knowsuchagency on Oct 25, 2023 | parent | prev | next [–]


You could take the OpenAPI json generated from this project and feed it to https://docs.scalar.com/swagger-editor which generates boilerplate in several formats, including Python



	
	
gabrielsroka on Oct 25, 2023 | parent | prev | next [–]


1. You should almost always use requests.Session() instead of requests. It's faster, and can make the code shorter.

2. requests can dump to JSON for you by using json=, so you don't need a separate module. It'll even set the content-type header to application/json for you.

  import requests
  
  url = '<endpoint>'
  
  headers = {
      'User-Agent': 'Mozilla/5.0 ...',
      ...
  }
  
  session = requests.Session()
  session.headers.update(headers)
 
  data = {
      "page": 5,
      "size": 28
      ...
  }
  
  response = session.post(url, json=data)
  
  if response.status_code == 200:
      print(response.json())
  else:
      print(f"Error {response.status_code}: {response.text}")



	
	
westurner on Oct 26, 2023 | parent | prev | next [–]


SeleniumIDE can record and save browser test cases to Python: https://github.com/SeleniumHQ/selenium-ide

awesome-test-automation/python-test-automation.md lists a number of ways to wrap selenium/webdriver and also playwright: https://github.com/atinfo/awesome-test-automation/blob/maste...

vcr.py, playback, and rr do [HTTP,] test recording and playback. httprunner can record and replay HAR. DevTools can save http requests and responses to HAR files.

awesome-web-archiving lists a number of tools that work with WARC; but only har2warc: https://github.com/iipc/awesome-web-archiving/blob/main/READ...



	
	
prometheon1 on Oct 25, 2023 | parent | prev | next [–]


You could potentially go one step further and make Python classes that wrap the whole API automatically from the OpenAPI file: https://github.com/mom1/apiclient-pydantic-generator



	
	
kej on Oct 25, 2023 | parent | prev | next [–]


It seems like you could combine this extension with some of the OpenAPI -> Python projects to get your desired result. (e.g. https://github.com/wy-z/requests-openapi )



	
	
yread on Oct 25, 2023 | parent | prev | next [–]


wow what a perfect service to steal session cookies



	
	
lucasyvas on Oct 25, 2023 | prev | next [–]


This reminds me a lot of:

https://github.com/alufers/mitmproxy2swagger

However, having the capability delivered in a browser extension is extremely handy!



	
	
aeontech on Oct 25, 2023 | parent | next [–]


this comment section is a goldmine :)

Thanks for sharing this, I suspect this is going to be super useful for my work



	
	
jimmySixDOF on Oct 25, 2023 | prev | next [–]


Nice this made me go back and check up on the Gorilla LLM project [1] to see whats they are doing with API and if they have applied their fine tuning to any of the newer foundation models but looks like things have slowed down since they launched (?) or maybe development is happening elsewhere on some invisible discord channel but I hope the intersection of API calling and LLM as a logic processing function keep getting focus it's an important direction for interop across the web.

[1] https://github.com/ShishirPatil/gorilla



	
	
quan on Oct 25, 2023 | parent | next [–]


I open sourced this tool that takes OpenAPI spec and let you control API using natural language https://github.com/mquan/api2ai

Let me know if you have any questions or feature request



	
	
ushakov on Oct 25, 2023 | root | parent | next [–]


How is this different from what LangChain already offers with their OpenAPI chain?

https://python.langchain.com/docs/use_cases/apis



	
	
quan on Oct 26, 2023 | root | parent | next [–]


afaik, the langchain solution loads entire openAPI spec which consumes a lot of token and won't work for many large API. For efficient token usage, api2ai divides the task into two steps: api planning and params parsing. First step takes a summarization of all the endpoints. Once the endpoint is known, we parse params using the schema of the selected endpoint.



	
	
user3939382 on Oct 25, 2023 | prev | next [–]


There's a similar, more powerful tool if you're into this

https://www.akitasoftware.com/



	
	
thesurlydev on Oct 25, 2023 | parent | next [–]


FYI, Akita was just bought by Postman: https://www.akitasoftware.com/blog-posts/announcing-akita-ha...



	
	
rattray on Oct 25, 2023 | parent | prev | next [–]


https://www.useoptic.com/ is another one, which is a little more tailored to building & updating OpenAPI specs. Works well on live traffic and/or tests.



	
	
misnome on Oct 25, 2023 | parent | prev | next [–]


Crikey, if you hadn't directly connected this as similar, I would have no idea what their product would even vaguely do from that landing page.



	
	
user3939382 on Oct 25, 2023 | root | parent | next [–]


Agree.

> Akita makes monitoring and observing system behavior accessible for every developer. Quickly discover all your endpoints, see which are slowest, and learn which have errors

Translation: Install a Docker extension that intercepts and inspects your network requests to infer the shape of your API.

I feel like when you're targeting developers, you should quickly explain what it is you actually do.



	
	
karaterobot on Oct 25, 2023 | root | parent | next [–]


Companies in general should do this, not just ones targeting developers! Instead they have a bunch of vague marketing copy that means nothing. It's a pet peeve.

My favorite is when they think they're keeping it short and to the point, with no bull. So, they'll have a hero section with copy like "Sharpen capacity. Scale across segments. Nuff said." No, not enough said, say more!



	
	
Aeolun on Oct 25, 2023 | root | parent | next [–]


> Companies in general should do this, not just ones targeting developers! Instead they have a bunch of vague marketing copy that means nothing. It's a pet peeve.

This seems to appeal to purchasing teams. When you write what the app actually does suddenly it’s technical and the team doesn’t understand what is written any more.



	
	
aeontech on Oct 25, 2023 | parent | prev | next [–]


The important distinction that this is entirely client-side, while Akita requires an agent running server-side.



	
	
ushakov on Oct 25, 2023 | parent | prev | next [–]


There's actually a whole lot of them! Keploy comes to mind and Pixie (eBPF-based)



	
	
adrianbr on Oct 25, 2023 | prev | next [–]


This is amazing! to figure out the website apis has always been a huge pita. With our dlt library project we can turn the openapi spec into pipelines and have the data pushed somewhere https://www.loom.com/share/2806b873ba1c4e0ea382eb3b4fbaf808?...



	
	
ricberw on Oct 25, 2023 | prev | next [–]


This is awesome!

I'll second/third the feature request for auto-including auth headers/calls (as many of the sites I'm trying to understand/use APIs from use persistent keys, and scraping these separately is just unnecessary extra time).

On that same note, I'd greatly appreciate keeping the initial request as a "sample request" within the spec.

I'd also greatly appreciate an option to attempt to automatically scrape for required fields (e.g. try removing each query variable one at a time, look for errors, document them).

Thanks for this :)



	
	
autonomousErwin on Oct 25, 2023 | prev | next [–]


This is a first step into turning the entire web into an API albeit before we hit the login/signup roadblocks (but then that's where agents come in)



	
	
toyg on Oct 25, 2023 | parent | next [–]


That's used to be called "the semantic web".

Dreams never die and what is old will be new again.



	
	
thesurlydev on Oct 25, 2023 | prev | next [–]


Great project! These features come to mind that would be great additions:

1. Ability to filter response properties.

2. Ability to work with non-JSON (web scraping) by defining a mapping of CSS selectors to response properties.

3. Cross-reference host names of captured requests with publicly documented APIs.

4. If auth headers are found, prompt user for credentials that can then be stored locally.

5. "Repeater" similarly found in Burp Suite.

6. Generate clients on the fly based on the generated OpenAPI spec.



	
	
worldsayshi on Oct 25, 2023 | parent | next [–]


- Allow using it as a library instead of just a browser extension which would in turn allow:

- Integration with some kind of web crawler to allow automatically walking a web site and extract a database of specifications

Edit: Hmm, it seems that genson-js[1] was used to merge schemas.

1 - https://www.npmjs.com/package/genson-js



	
	
mrmagoo2 on Oct 25, 2023 | root | parent | next [–]


Genson-js is used to merge JSON Schema objects. Essentially there are 5 schemas that we care about in each request - request bodies, request headers, response bodies, response headers, and query parameters. Each endpoint (which may or may not be parameterised) has only one schema for each of these values.

The idea for a crawler is a good one. The core logic that handles spec generation is decoupled from everything else, so it can be extracted into its own library.

But there are approaches that exist for this already, such as har-to-openapi.

https://github.com/jonluca/har-to-openapi



	
	
worldsayshi on Oct 25, 2023 | root | parent | next [–]


Interesting! Thanks! Awesome project :)



	
	
thesurlydev on Oct 25, 2023 | parent | prev | next [–]


7. Train a machine learning model to recognize and extract tabular and repeated data based on training data.

8. Optionally publish generated OpenAPI specs to a central site or open PR to a GH repo, "awesome-openapi-devtools"?



	
	
mrmagoo2 on Oct 25, 2023 | parent | prev | next [–]


Some great ideas here, thank you. I do want to keep it small and focused so I'll forego complex functionality like the Repeater, but you've raised some common pain points I'll tackle.



	
	
ch_sm on Oct 25, 2023 | prev | next [–]


Very nice! Auto generating type information from looking at permutations of values is hard though. Q: Does this handle optional values? Also, being able to mark string field as "enums" and then collecting the possible values instead of just typing it as "string" would be mega handy.



	
	
mrmagoo2 on Oct 25, 2023 | parent | next [–]


It doesn't have any way of determining which values are optional, so it doesn't make that distinction. Hear you on the enums, I'll take another look at what's possible without adding overhead.



	
	
RileyJames on Oct 25, 2023 | prev | next [–]


Amazing. I’ve often wished this would exist. Thank you.

It was always my step 1 towards Xxx. Keen to know what directions you were thinking?

I’d love to see more remixing on top of API’s websites typically only expose for their own use.



	
	
mrmagoo2 on Oct 25, 2023 | parent | next [–]


For sure, there are a few tools out there like Requestly to change API behaviour, but it's a frustrating experience. In terms of the direction, planning to keep this simple so I've no plans for additional features.



	
	
saran945 on Oct 25, 2023 | prev | next [–]


Thanks for sharing Chrome extension @mrmagoo2.

It's amazing to see a tool that simplifies the process of generating OpenAPI spec. this is the best showHN this year.



	
	
ushakov on Oct 25, 2023 | parent | next [–]


Agreed! What would be more awesome though is if it could generate OpenAPI spec from existing HAR files



	
	
mrmagoo2 on Oct 25, 2023 | root | parent | next [–]


It could do as it works with the HAR 1.2 format. There is another library that can do this. It isn't suitable for the FE as it uses QuickType & pulls in a ton of dependencies, but it is far more configurable.

https://github.com/jonluca/har-to-openapi



	
	
jtbayly on Oct 25, 2023 | prev | next [–]


This looks very useful, but what do I do with the discovered data?

Suppose I have a site that runs a search that I want to be able to automate. However, instead of sending the search term in the URL, it updates live (presumably via some API call).

Now suppose I need a one-click solution to be able to open that page and run a specific search.

Is there another Chrome plugin that would allow me to use this API data to make that happen?



	
	
jpmonette on Oct 25, 2023 | prev | next [–]


Had in mind to build something like this for quite some time to quickly explore undocumented APIs - looking forward to see your progress!



	
	
mrmagoo2 on Oct 25, 2023 | parent | next [–]


Thank you!



	
	
HanClinto on Oct 25, 2023 | prev | next [–]


Okay, this is wonderful. Love it already!!

Sometimes I click on a path parameter and it doesn't "create" it, even though there are several other examples in the list. Not sure if it's a bug, or something I'm doing wrong.

Overall, this is an absolutely wonderful tool and I've wanted something like this for a long time. Incredibly useful, thank you!!



	
	
mrmagoo2 on Oct 25, 2023 | parent | next [–]


That sound like a bug, I need to test that feature more thoroughly. Thanks for reporting.



	
	
pbnjay on Oct 26, 2023 | prev | next [–]


Damn I literally built a really similar tool myself using HAR files just a couple weeks ago! Yours is way more polished though, nice work.

I have a lot of ideas in this space (some PoCs), and I've been starting to scope out a company around them. Would love to chat to see if there's any shared opportunity for both of us!



	
	
ushakov on Oct 25, 2023 | prev | next [–]


The problem with this type of tools is that they only produce specs based on infos they can get.

The spec produced will be incomplete (missing paths, methods, response variants, statuses). For that you should use a framework like Fastify, NestJS, tsoa, FastAPI, which have built-in OpenAPI support.

Can be very valuable for reverse-engineering though :)



	
	
hubraumhugo on Oct 25, 2023 | prev | next [–]


Really cool, we're using a similar technique at Kadoa to auto-generate scrapers for any website. Analyzing network calls to find the desired data in API responses is one of the frist things we do before starting to process the DOM.



	
	
albertgoeswoof on Oct 25, 2023 | prev | next [–]


Cool! Can you add autocomplete of paths to URLs based on the spec now?

so I can be typing in the URL bar for any website I have landed on in the past and tab through all the available routes?

e.g.

- news.ycombinator.com_

- news.ycombinator.com/new

- news.ycombinator.com/submit

- news.ycombinator.com/show

etc.



	
	
sdmike1 on Oct 25, 2023 | prev | next [–]


A Firefox version of this would be super handy! Does that already exist?



	
	
wackget on Oct 25, 2023 | prev | next [–]


The description doesn't explain exactly what this extension does.

I assume it monitors all XHR requests as you browse a website, and if the request/response matches [some criteria (e.g. is JSON?)] it will assume it's an API request and log it?

Is that correct?

If so, it will only work on websites where the frontend is implemented like a PWA, with lots of AJAX calls to fetch data, etc. For sites whose pages are all generated server-side, the extension won't generate any API schema, right?

Edit: Also how does it differentiate "API requests" with regular AJAX content fetching? If a website fetches some arbitrary content via an AJAX request (e.g. some lazy-loaded HTML), that's not an API request. That's just part of a website's layout.



	
	
iforgotpassword on Oct 25, 2023 | parent | next [–]


How would it, there isn't any API in the first place with classic websites. Your could maybe consider the urlencoded post requests an API, but then the reply is another html website so how do you formally specify the reply format? "The queried data is somewhere right below the third <h3> except when there's a new message for the logged in user, then it's the fourth one"



	
	
jameshart on Oct 25, 2023 | parent | prev | next [–]


Obviously - a browser extension can only monitor API calls from the browser.



	
	
wackget on Oct 25, 2023 | root | parent | next [–]


Not obviously; all it says is it generates a schema "while using" a website.

"Using" could mean navigating between pages, submitting data via forms, etc.



	
	
yencabulator on Oct 25, 2023 | parent | prev | next [–]


Worse, for something like SvelteKit load functions, this will think there's a "real API" where what's actually there is an internal detail and will change often.

https://kit.svelte.dev/docs/load



	
	
a_c on Oct 25, 2023 | parent | prev | next [–]


It does generate schema.

> Instantly generate an OpenAPI 3.1 specification for any website or application just by using it



	
	
wackget on Oct 25, 2023 | root | parent | next [–]


Yeah but my question remains: by what criteria is a request classed as an "API request"? Websites make tons of XHR requests and not all of them are API requests.

I want to know what this extension does that's different than me looking at the browser's Dev Tools > Network tab.



	
	
mrmagoo2 on Oct 25, 2023 | root | parent | next [–]


The criteria can be found below. There are no hard and fast rules, but the goal is to only include requests that you might otherwise find in a spec.

https://github.com/AndrewWalsh/openapi-devtools/blob/main/sr...



	
	
ushakov on Oct 25, 2023 | prev | next [–]


We at Step CI have a similar tool, that acts as a proxy and can generate OpenAPI spec for the request/response pairs.

(You can also use it to generate automated tests)

If you're interested: mish@stepci.com



	
	
voidmain0001 on Oct 25, 2023 | prev | next [–]


The documentation states 'automatically populate based on JSON requests that fire as you browse the web' so does this mean that gRPC protobuf are not captured?



	
	
mrmagoo2 on Oct 25, 2023 | parent | next [–]


Anything that isn't a JSON request is specifically ignored.



	
	
mdaniel on Oct 25, 2023 | root | parent | next [–]


I saw your sibling comment about "keeping it simple," however that is a bit counter to "generates OpenAPI specifications" since those for sure are not limited to just application/json request/response bodies

I wanted to draw your attention to "normal" POST application/x-www-form-urlencoded <https://github.com/OAI/OpenAPI-Specification/blob/3.1.0/vers...> and its multipart/form-data friend <https://github.com/OAI/OpenAPI-Specification/blob/3.1.0/vers...>

The latter is likely problematic, but the former is in wide use still, including, strangely enough, the AWS API, although some of their newer services do have an application/json protocol

I know that's a lot of words, but the tl;dr would be that if you want your extension to be application/json only, then changing the description to say "OpenAPI specifications for application/json handshakes" would help the consumer be on the same page with your goals



	
	
mrmagoo2 on Oct 26, 2023 | root | parent | next [–]


You raise a good point and it would be great to account for this. I will take a look at this. Excellent suggestion.



	
	
jcrites on Oct 25, 2023 | parent | prev | next [–]


Does gRPC /ProtoBuf have support for web browsers? I don't know of a situation where I'd encounter those in a web application.



	
	
voidmain0001 on Oct 25, 2023 | root | parent | next [–]


https://blog.envoyproxy.io/envoy-and-grpc-web-a-fresh-new-al...



	
	
Aarekaz on Oct 25, 2023 | prev | next [–]


This looks super interesting. Works for anything? Damn.



	
	
pihentagy on Oct 26, 2023 | prev | next [–]


Is there a way to filter out headers?

The result contains headers like content-length and similar.

Also it would be nice if it could factor out common schemas.



	
	
corry on Oct 25, 2023 | prev | next [–]


Awesome! Any chance of a Safari extension too?



	
	
lukeplato on Oct 25, 2023 | prev | next [–]


Would be cool if this shared the user found specs to create a database of API specs for the web



	
	
pmkelly4444 on Oct 25, 2023 | prev | next [–]


this is very cool! I just tried using it, unfortunately, my NextJS app dir project makes most requests from the server side, so it was only capturing "posts" made from the client. Is there a way to run it from the server?



	
	
siva7 on Oct 25, 2023 | prev | next [–]


I'm sure many developers wished at some point such magic would exist



	
	
ec109685 on Oct 25, 2023 | prev | next [–]


Would love this for apps.



	
	
chris_nielsen on Oct 25, 2023 | prev | next [–]


This looks super useful, can’t wait to try it at work tomorrow!



	
	
namtab00 on Oct 25, 2023 | parent | next [–]


Care to share what would it be useful for?

I mean, and I'm asking as a backend dev, if you have to integrate with some API, you use the provided docs/swagger ui.

Why/when would you care to rely on an API integration when it's interface is not publicly shared?



	
	
imhoguy on Oct 25, 2023 | root | parent | next [–]


Because this is for these edge cases where docs are crap and Swagger spec is non-existent.



	
	
zoover2020 on Oct 25, 2023 | root | parent | prev | next [–]


Reverse engineering? You just described it



	
	
jasfi on Oct 25, 2023 | prev | next [–]


This could be useful for learning from any site you admire.



	
	
fullofdev on Oct 26, 2023 | prev [–]


looks really cool! congrats!







Guidelines | FAQ | Lists | API | Security | Legal | Apply to YC | Contact


Search:

## Metadata

```json
{
  "title": "Show HN: OpenAPI DevTools – Chrome extension that generates an API spec",
  "description": "",
  "url": "https://news.ycombinator.com/item?id=38012032",
  "content": "\tHacker News new | past | comments | ask | show | jobs | submit\tlogin\n\n\n\n\t\n\tShow HN: OpenAPI DevTools – Chrome extension that generates an API spec (github.com/andrewwalsh)\n\t811 points by mrmagoo2 on Oct 25, 2023 | hide | past | favorite | 102 comments\n\n\t\nEffortlessly discover API behaviour with a Chrome extension that automatically generates OpenAPI specifications in real time for any app or website.\n\n\n\n\t\n\t\nthe_absurdist on Oct 25, 2023 | next [–]\n\n\nI wish this would document the auth headers.\n\nWhat would be particularly useful is if it saved token values and then (through search) joined them on the response of the auth call to get the initial token.\n\nThat way you could easily determine what auth call was needed to get you a token to use the endpoint.\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | parent | next [–]\n\n\nGreat suggestion, I will look into this.\n\n\n\n\t\n\t\nhoerzu on Oct 26, 2023 | root | parent | next [–]\n\n\nI have used llama to figure out the duplications / pathparamters :)\n\n\n\n\t\n\t\ntruemotive on Oct 28, 2023 | root | parent | prev | next [–]\n\n\nYou… you built the thing I’ve been spending 3 days looking for… oh man\n\n\n\n\t\n\t\nttul on Oct 25, 2023 | prev | next [–]\n\n\nThis is super cool. Writing code to drop into the JavaScript console lets you do insane things. I’ve found great success using ChatGPT to help me write the code, which I then just cut and paste into the console. Asking it to “make it all run in parallel using async/await” will massively speed up execution of serial tasks.\n\nFor instance, I had GPT help me write browser JS that groks literally thousands of IP addresses in an open security tool that shall not be named. I can vacuum much of their entire database in seconds by making hundreds of async calls. While they do have bot protection on the website, they appear to have no protection at all on their browser APIs once the user has been given a cookie… I suspect this is common.\n\n\n\n\t\n\t\njhardy54 on Oct 26, 2023 | parent | next [–]\n\n\nThis is about OpenAPI (Swagger), not OpenAI (ChatGPT).\n\n\n\n\t\n\t\ncxr on Oct 31, 2023 | root | parent | next [–]\n\n\nThis is an extension for Chrome, not Safari.\n\n\n\n\t\n\t\nttul on Oct 28, 2023 | root | parent | prev | next [–]\n\n\nI know.\n\n\n\n\t\n\t\na_c on Oct 25, 2023 | prev | next [–]\n\n\nLove it!\n\nI used https://vite-plugin-web-extension.aklinker1.io/guide/ before to have cross browser extension support. If you don't mind I could take a look to add firefox support (no guarantee)\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | parent | next [–]\n\n\nAs a follow up, the algorithm that powers this makes use of the chrome.devtools.network API. Specifically it passes the Request object that is in the HAR 1.2 archive format.\n\nSo if you can pass the equivalent of that in Firefox/other browsers to the insert method and switch things up a bit, it should be relatively straightforward. I will think about pulling out the core logic into its own lib.\n\nhttps://developer.chrome.com/docs/extensions/reference/devto...\n\nhttps://developer.chrome.com/docs/extensions/reference/devto...\n\nhttps://github.com/AndrewWalsh/openapi-devtools/blob/main/sr...\n\n\n\n\t\n\t\na_c on Oct 26, 2023 | root | parent | next [–]\n\n\nIndeed I have issue here. Firefox maintain a library for unified extension API https://github.com/mozilla/webextension-polyfill\n\nTheir type definition for HAR request isn't exported https://github.com/DefinitelyTyped/DefinitelyTyped/blob/mast...\n\nSo I can't drop in replace the type on https://github.com/AndrewWalsh/openapi-devtools/blob/main/sr...\n\n\n\n\t\n\t\na_c on Oct 26, 2023 | root | parent | next [–]\n\n\nAlso the polyfill has a promise based API rather than a callback, which I don't yet know if there is a workaround\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | parent | prev | next [–]\n\n\nHey absolutely please do, thank you!\n\n\n\n\t\n\t\nlucasyvas on Oct 25, 2023 | parent | prev | next [–]\n\n\nThis would be excellent\n\n\n\n\t\n\t\ncivilitty on Oct 25, 2023 | parent | prev | next [–]\n\n\nThere's also Plasmo which provides some abstractions over the browsers: https://github.com/PlasmoHQ/plasmo\n\n\n\n\t\n\t\nparhamn on Oct 25, 2023 | parent | prev | next [–]\n\n\nAre devtools extensions/panels standardized?\n\n\n\n\t\n\t\na_c on Oct 25, 2023 | root | parent | next [–]\n\n\nDo you mean the devtool protocol[1]? I didn't follow the space so have no knowledge on it. On the other hand there seem to be a polyfilled API on chrome.devtools.network.Request which OP's extension uses extensively https://github.com/DefinitelyTyped/DefinitelyTyped/blob/mast...\n\n[1] https://chromedevtools.github.io/devtools-protocol/\n\n\n\n\t\n\t\ndistortedsignal on Oct 25, 2023 | parent | prev | next [–]\n\n\nI'd love to see FF support on this.\n\n\n\n\t\n\t\narchiewood on Oct 25, 2023 | prev | next [–]\n\n\nMy most common use case here is to then want to hit the API from python, and adjust the params / url etc.\n\nWould love a \"copy to python requests\" button that\n\ngrabs the headers\n\ngenerates a boilerplate python snippet including the headers and the URL:\n\n    import requests\n    import json\n\n    url = '<endpoint>'\n\n    headers = {\n        'User-Agent': 'Mozilla/5.0 ...',\n        ...\n    }\n\n    data = {\n        \"page\": 5,\n        \"size\": 28\n        ...\n    }\n\n    response = requests.post(url, headers=headers, data=json.dumps(data))\n\n    if response.status_code == 200:\n        print(response.json())\n    else:\n        print(f\"Error {response.status_code}: {response.text}\")\n\n\n\n\t\n\t\nea016 on Oct 25, 2023 | parent | next [–]\n\n\nSteps to do so:\n\n- open the network console\n\n- right click on the request\n\n- click \"copy as curl\"\n\n- visit https://curlconverter.com/ to convert to Python/Node/any language\n\n\n\n\t\n\t\ntech234a on Oct 25, 2023 | root | parent | next [–]\n\n\nAlso available as a VSCode extension that automatically matches the pasted content to the programming language used in the current file: https://marketplace.visualstudio.com/items?itemName=curlconv...\n\n\n\n\t\n\t\nverhovsky on Oct 25, 2023 | root | parent | next [–]\n\n\nI made a fork of the Chrome DevTools that adds \"Copy as Python\" to the right click menu of each request in the Network tab. You can tell Chrome to use a different version of the DevTools if you start it from the command line\n\nhttps://github.com/curlconverter/curlconverter/issues/64#iss...\n\n\n\n\t\n\t\ntilne on Oct 25, 2023 | root | parent | prev | next [–]\n\n\nThank you for this. I didn’t know curlconverter existed.\n\n\n\n\t\n\t\narchiewood on Oct 25, 2023 | root | parent | prev | next [–]\n\n\nThis is my current workflow, though with ChatGPT.\n\nI was just trying to save a few clicks\n\n\n\n\t\n\t\nnovia on Oct 25, 2023 | root | parent | next [–]\n\n\nYou made your request sound important to implement when you already have a workaround that doesn't take very much time...\n\nThis is why feature bloat is a thing\n\n\n\n\t\n\t\nMurageKabui on Oct 25, 2023 | root | parent | prev | next [–]\n\n\nI was to say this lol\n\n\n\n\t\n\t\nknowsuchagency on Oct 25, 2023 | parent | prev | next [–]\n\n\nYou could take the OpenAPI json generated from this project and feed it to https://docs.scalar.com/swagger-editor which generates boilerplate in several formats, including Python\n\n\n\n\t\n\t\ngabrielsroka on Oct 25, 2023 | parent | prev | next [–]\n\n\n1. You should almost always use requests.Session() instead of requests. It's faster, and can make the code shorter.\n\n2. requests can dump to JSON for you by using json=, so you don't need a separate module. It'll even set the content-type header to application/json for you.\n\n  import requests\n  \n  url = '<endpoint>'\n  \n  headers = {\n      'User-Agent': 'Mozilla/5.0 ...',\n      ...\n  }\n  \n  session = requests.Session()\n  session.headers.update(headers)\n \n  data = {\n      \"page\": 5,\n      \"size\": 28\n      ...\n  }\n  \n  response = session.post(url, json=data)\n  \n  if response.status_code == 200:\n      print(response.json())\n  else:\n      print(f\"Error {response.status_code}: {response.text}\")\n\n\n\n\t\n\t\nwesturner on Oct 26, 2023 | parent | prev | next [–]\n\n\nSeleniumIDE can record and save browser test cases to Python: https://github.com/SeleniumHQ/selenium-ide\n\nawesome-test-automation/python-test-automation.md lists a number of ways to wrap selenium/webdriver and also playwright: https://github.com/atinfo/awesome-test-automation/blob/maste...\n\nvcr.py, playback, and rr do [HTTP,] test recording and playback. httprunner can record and replay HAR. DevTools can save http requests and responses to HAR files.\n\nawesome-web-archiving lists a number of tools that work with WARC; but only har2warc: https://github.com/iipc/awesome-web-archiving/blob/main/READ...\n\n\n\n\t\n\t\nprometheon1 on Oct 25, 2023 | parent | prev | next [–]\n\n\nYou could potentially go one step further and make Python classes that wrap the whole API automatically from the OpenAPI file: https://github.com/mom1/apiclient-pydantic-generator\n\n\n\n\t\n\t\nkej on Oct 25, 2023 | parent | prev | next [–]\n\n\nIt seems like you could combine this extension with some of the OpenAPI -> Python projects to get your desired result. (e.g. https://github.com/wy-z/requests-openapi )\n\n\n\n\t\n\t\nyread on Oct 25, 2023 | parent | prev | next [–]\n\n\nwow what a perfect service to steal session cookies\n\n\n\n\t\n\t\nlucasyvas on Oct 25, 2023 | prev | next [–]\n\n\nThis reminds me a lot of:\n\nhttps://github.com/alufers/mitmproxy2swagger\n\nHowever, having the capability delivered in a browser extension is extremely handy!\n\n\n\n\t\n\t\naeontech on Oct 25, 2023 | parent | next [–]\n\n\nthis comment section is a goldmine :)\n\nThanks for sharing this, I suspect this is going to be super useful for my work\n\n\n\n\t\n\t\njimmySixDOF on Oct 25, 2023 | prev | next [–]\n\n\nNice this made me go back and check up on the Gorilla LLM project [1] to see whats they are doing with API and if they have applied their fine tuning to any of the newer foundation models but looks like things have slowed down since they launched (?) or maybe development is happening elsewhere on some invisible discord channel but I hope the intersection of API calling and LLM as a logic processing function keep getting focus it's an important direction for interop across the web.\n\n[1] https://github.com/ShishirPatil/gorilla\n\n\n\n\t\n\t\nquan on Oct 25, 2023 | parent | next [–]\n\n\nI open sourced this tool that takes OpenAPI spec and let you control API using natural language https://github.com/mquan/api2ai\n\nLet me know if you have any questions or feature request\n\n\n\n\t\n\t\nushakov on Oct 25, 2023 | root | parent | next [–]\n\n\nHow is this different from what LangChain already offers with their OpenAPI chain?\n\nhttps://python.langchain.com/docs/use_cases/apis\n\n\n\n\t\n\t\nquan on Oct 26, 2023 | root | parent | next [–]\n\n\nafaik, the langchain solution loads entire openAPI spec which consumes a lot of token and won't work for many large API. For efficient token usage, api2ai divides the task into two steps: api planning and params parsing. First step takes a summarization of all the endpoints. Once the endpoint is known, we parse params using the schema of the selected endpoint.\n\n\n\n\t\n\t\nuser3939382 on Oct 25, 2023 | prev | next [–]\n\n\nThere's a similar, more powerful tool if you're into this\n\nhttps://www.akitasoftware.com/\n\n\n\n\t\n\t\nthesurlydev on Oct 25, 2023 | parent | next [–]\n\n\nFYI, Akita was just bought by Postman: https://www.akitasoftware.com/blog-posts/announcing-akita-ha...\n\n\n\n\t\n\t\nrattray on Oct 25, 2023 | parent | prev | next [–]\n\n\nhttps://www.useoptic.com/ is another one, which is a little more tailored to building & updating OpenAPI specs. Works well on live traffic and/or tests.\n\n\n\n\t\n\t\nmisnome on Oct 25, 2023 | parent | prev | next [–]\n\n\nCrikey, if you hadn't directly connected this as similar, I would have no idea what their product would even vaguely do from that landing page.\n\n\n\n\t\n\t\nuser3939382 on Oct 25, 2023 | root | parent | next [–]\n\n\nAgree.\n\n> Akita makes monitoring and observing system behavior accessible for every developer. Quickly discover all your endpoints, see which are slowest, and learn which have errors\n\nTranslation: Install a Docker extension that intercepts and inspects your network requests to infer the shape of your API.\n\nI feel like when you're targeting developers, you should quickly explain what it is you actually do.\n\n\n\n\t\n\t\nkaraterobot on Oct 25, 2023 | root | parent | next [–]\n\n\nCompanies in general should do this, not just ones targeting developers! Instead they have a bunch of vague marketing copy that means nothing. It's a pet peeve.\n\nMy favorite is when they think they're keeping it short and to the point, with no bull. So, they'll have a hero section with copy like \"Sharpen capacity. Scale across segments. Nuff said.\" No, not enough said, say more!\n\n\n\n\t\n\t\nAeolun on Oct 25, 2023 | root | parent | next [–]\n\n\n> Companies in general should do this, not just ones targeting developers! Instead they have a bunch of vague marketing copy that means nothing. It's a pet peeve.\n\nThis seems to appeal to purchasing teams. When you write what the app actually does suddenly it’s technical and the team doesn’t understand what is written any more.\n\n\n\n\t\n\t\naeontech on Oct 25, 2023 | parent | prev | next [–]\n\n\nThe important distinction that this is entirely client-side, while Akita requires an agent running server-side.\n\n\n\n\t\n\t\nushakov on Oct 25, 2023 | parent | prev | next [–]\n\n\nThere's actually a whole lot of them! Keploy comes to mind and Pixie (eBPF-based)\n\n\n\n\t\n\t\nadrianbr on Oct 25, 2023 | prev | next [–]\n\n\nThis is amazing! to figure out the website apis has always been a huge pita. With our dlt library project we can turn the openapi spec into pipelines and have the data pushed somewhere https://www.loom.com/share/2806b873ba1c4e0ea382eb3b4fbaf808?...\n\n\n\n\t\n\t\nricberw on Oct 25, 2023 | prev | next [–]\n\n\nThis is awesome!\n\nI'll second/third the feature request for auto-including auth headers/calls (as many of the sites I'm trying to understand/use APIs from use persistent keys, and scraping these separately is just unnecessary extra time).\n\nOn that same note, I'd greatly appreciate keeping the initial request as a \"sample request\" within the spec.\n\nI'd also greatly appreciate an option to attempt to automatically scrape for required fields (e.g. try removing each query variable one at a time, look for errors, document them).\n\nThanks for this :)\n\n\n\n\t\n\t\nautonomousErwin on Oct 25, 2023 | prev | next [–]\n\n\nThis is a first step into turning the entire web into an API albeit before we hit the login/signup roadblocks (but then that's where agents come in)\n\n\n\n\t\n\t\ntoyg on Oct 25, 2023 | parent | next [–]\n\n\nThat's used to be called \"the semantic web\".\n\nDreams never die and what is old will be new again.\n\n\n\n\t\n\t\nthesurlydev on Oct 25, 2023 | prev | next [–]\n\n\nGreat project! These features come to mind that would be great additions:\n\n1. Ability to filter response properties.\n\n2. Ability to work with non-JSON (web scraping) by defining a mapping of CSS selectors to response properties.\n\n3. Cross-reference host names of captured requests with publicly documented APIs.\n\n4. If auth headers are found, prompt user for credentials that can then be stored locally.\n\n5. \"Repeater\" similarly found in Burp Suite.\n\n6. Generate clients on the fly based on the generated OpenAPI spec.\n\n\n\n\t\n\t\nworldsayshi on Oct 25, 2023 | parent | next [–]\n\n\n- Allow using it as a library instead of just a browser extension which would in turn allow:\n\n- Integration with some kind of web crawler to allow automatically walking a web site and extract a database of specifications\n\nEdit: Hmm, it seems that genson-js[1] was used to merge schemas.\n\n1 - https://www.npmjs.com/package/genson-js\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | root | parent | next [–]\n\n\nGenson-js is used to merge JSON Schema objects. Essentially there are 5 schemas that we care about in each request - request bodies, request headers, response bodies, response headers, and query parameters. Each endpoint (which may or may not be parameterised) has only one schema for each of these values.\n\nThe idea for a crawler is a good one. The core logic that handles spec generation is decoupled from everything else, so it can be extracted into its own library.\n\nBut there are approaches that exist for this already, such as har-to-openapi.\n\nhttps://github.com/jonluca/har-to-openapi\n\n\n\n\t\n\t\nworldsayshi on Oct 25, 2023 | root | parent | next [–]\n\n\nInteresting! Thanks! Awesome project :)\n\n\n\n\t\n\t\nthesurlydev on Oct 25, 2023 | parent | prev | next [–]\n\n\n7. Train a machine learning model to recognize and extract tabular and repeated data based on training data.\n\n8. Optionally publish generated OpenAPI specs to a central site or open PR to a GH repo, \"awesome-openapi-devtools\"?\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | parent | prev | next [–]\n\n\nSome great ideas here, thank you. I do want to keep it small and focused so I'll forego complex functionality like the Repeater, but you've raised some common pain points I'll tackle.\n\n\n\n\t\n\t\nch_sm on Oct 25, 2023 | prev | next [–]\n\n\nVery nice! Auto generating type information from looking at permutations of values is hard though. Q: Does this handle optional values? Also, being able to mark string field as \"enums\" and then collecting the possible values instead of just typing it as \"string\" would be mega handy.\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | parent | next [–]\n\n\nIt doesn't have any way of determining which values are optional, so it doesn't make that distinction. Hear you on the enums, I'll take another look at what's possible without adding overhead.\n\n\n\n\t\n\t\nRileyJames on Oct 25, 2023 | prev | next [–]\n\n\nAmazing. I’ve often wished this would exist. Thank you.\n\nIt was always my step 1 towards Xxx. Keen to know what directions you were thinking?\n\nI’d love to see more remixing on top of API’s websites typically only expose for their own use.\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | parent | next [–]\n\n\nFor sure, there are a few tools out there like Requestly to change API behaviour, but it's a frustrating experience. In terms of the direction, planning to keep this simple so I've no plans for additional features.\n\n\n\n\t\n\t\nsaran945 on Oct 25, 2023 | prev | next [–]\n\n\nThanks for sharing Chrome extension @mrmagoo2.\n\nIt's amazing to see a tool that simplifies the process of generating OpenAPI spec. this is the best showHN this year.\n\n\n\n\t\n\t\nushakov on Oct 25, 2023 | parent | next [–]\n\n\nAgreed! What would be more awesome though is if it could generate OpenAPI spec from existing HAR files\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | root | parent | next [–]\n\n\nIt could do as it works with the HAR 1.2 format. There is another library that can do this. It isn't suitable for the FE as it uses QuickType & pulls in a ton of dependencies, but it is far more configurable.\n\nhttps://github.com/jonluca/har-to-openapi\n\n\n\n\t\n\t\njtbayly on Oct 25, 2023 | prev | next [–]\n\n\nThis looks very useful, but what do I do with the discovered data?\n\nSuppose I have a site that runs a search that I want to be able to automate. However, instead of sending the search term in the URL, it updates live (presumably via some API call).\n\nNow suppose I need a one-click solution to be able to open that page and run a specific search.\n\nIs there another Chrome plugin that would allow me to use this API data to make that happen?\n\n\n\n\t\n\t\njpmonette on Oct 25, 2023 | prev | next [–]\n\n\nHad in mind to build something like this for quite some time to quickly explore undocumented APIs - looking forward to see your progress!\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | parent | next [–]\n\n\nThank you!\n\n\n\n\t\n\t\nHanClinto on Oct 25, 2023 | prev | next [–]\n\n\nOkay, this is wonderful. Love it already!!\n\nSometimes I click on a path parameter and it doesn't \"create\" it, even though there are several other examples in the list. Not sure if it's a bug, or something I'm doing wrong.\n\nOverall, this is an absolutely wonderful tool and I've wanted something like this for a long time. Incredibly useful, thank you!!\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | parent | next [–]\n\n\nThat sound like a bug, I need to test that feature more thoroughly. Thanks for reporting.\n\n\n\n\t\n\t\npbnjay on Oct 26, 2023 | prev | next [–]\n\n\nDamn I literally built a really similar tool myself using HAR files just a couple weeks ago! Yours is way more polished though, nice work.\n\nI have a lot of ideas in this space (some PoCs), and I've been starting to scope out a company around them. Would love to chat to see if there's any shared opportunity for both of us!\n\n\n\n\t\n\t\nushakov on Oct 25, 2023 | prev | next [–]\n\n\nThe problem with this type of tools is that they only produce specs based on infos they can get.\n\nThe spec produced will be incomplete (missing paths, methods, response variants, statuses). For that you should use a framework like Fastify, NestJS, tsoa, FastAPI, which have built-in OpenAPI support.\n\nCan be very valuable for reverse-engineering though :)\n\n\n\n\t\n\t\nhubraumhugo on Oct 25, 2023 | prev | next [–]\n\n\nReally cool, we're using a similar technique at Kadoa to auto-generate scrapers for any website. Analyzing network calls to find the desired data in API responses is one of the frist things we do before starting to process the DOM.\n\n\n\n\t\n\t\nalbertgoeswoof on Oct 25, 2023 | prev | next [–]\n\n\nCool! Can you add autocomplete of paths to URLs based on the spec now?\n\nso I can be typing in the URL bar for any website I have landed on in the past and tab through all the available routes?\n\ne.g.\n\n- news.ycombinator.com_\n\n- news.ycombinator.com/new\n\n- news.ycombinator.com/submit\n\n- news.ycombinator.com/show\n\netc.\n\n\n\n\t\n\t\nsdmike1 on Oct 25, 2023 | prev | next [–]\n\n\nA Firefox version of this would be super handy! Does that already exist?\n\n\n\n\t\n\t\nwackget on Oct 25, 2023 | prev | next [–]\n\n\nThe description doesn't explain exactly what this extension does.\n\nI assume it monitors all XHR requests as you browse a website, and if the request/response matches [some criteria (e.g. is JSON?)] it will assume it's an API request and log it?\n\nIs that correct?\n\nIf so, it will only work on websites where the frontend is implemented like a PWA, with lots of AJAX calls to fetch data, etc. For sites whose pages are all generated server-side, the extension won't generate any API schema, right?\n\nEdit: Also how does it differentiate \"API requests\" with regular AJAX content fetching? If a website fetches some arbitrary content via an AJAX request (e.g. some lazy-loaded HTML), that's not an API request. That's just part of a website's layout.\n\n\n\n\t\n\t\niforgotpassword on Oct 25, 2023 | parent | next [–]\n\n\nHow would it, there isn't any API in the first place with classic websites. Your could maybe consider the urlencoded post requests an API, but then the reply is another html website so how do you formally specify the reply format? \"The queried data is somewhere right below the third <h3> except when there's a new message for the logged in user, then it's the fourth one\"\n\n\n\n\t\n\t\njameshart on Oct 25, 2023 | parent | prev | next [–]\n\n\nObviously - a browser extension can only monitor API calls from the browser.\n\n\n\n\t\n\t\nwackget on Oct 25, 2023 | root | parent | next [–]\n\n\nNot obviously; all it says is it generates a schema \"while using\" a website.\n\n\"Using\" could mean navigating between pages, submitting data via forms, etc.\n\n\n\n\t\n\t\nyencabulator on Oct 25, 2023 | parent | prev | next [–]\n\n\nWorse, for something like SvelteKit load functions, this will think there's a \"real API\" where what's actually there is an internal detail and will change often.\n\nhttps://kit.svelte.dev/docs/load\n\n\n\n\t\n\t\na_c on Oct 25, 2023 | parent | prev | next [–]\n\n\nIt does generate schema.\n\n> Instantly generate an OpenAPI 3.1 specification for any website or application just by using it\n\n\n\n\t\n\t\nwackget on Oct 25, 2023 | root | parent | next [–]\n\n\nYeah but my question remains: by what criteria is a request classed as an \"API request\"? Websites make tons of XHR requests and not all of them are API requests.\n\nI want to know what this extension does that's different than me looking at the browser's Dev Tools > Network tab.\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | root | parent | next [–]\n\n\nThe criteria can be found below. There are no hard and fast rules, but the goal is to only include requests that you might otherwise find in a spec.\n\nhttps://github.com/AndrewWalsh/openapi-devtools/blob/main/sr...\n\n\n\n\t\n\t\nushakov on Oct 25, 2023 | prev | next [–]\n\n\nWe at Step CI have a similar tool, that acts as a proxy and can generate OpenAPI spec for the request/response pairs.\n\n(You can also use it to generate automated tests)\n\nIf you're interested: mish@stepci.com\n\n\n\n\t\n\t\nvoidmain0001 on Oct 25, 2023 | prev | next [–]\n\n\nThe documentation states 'automatically populate based on JSON requests that fire as you browse the web' so does this mean that gRPC protobuf are not captured?\n\n\n\n\t\n\t\nmrmagoo2 on Oct 25, 2023 | parent | next [–]\n\n\nAnything that isn't a JSON request is specifically ignored.\n\n\n\n\t\n\t\nmdaniel on Oct 25, 2023 | root | parent | next [–]\n\n\nI saw your sibling comment about \"keeping it simple,\" however that is a bit counter to \"generates OpenAPI specifications\" since those for sure are not limited to just application/json request/response bodies\n\nI wanted to draw your attention to \"normal\" POST application/x-www-form-urlencoded <https://github.com/OAI/OpenAPI-Specification/blob/3.1.0/vers...> and its multipart/form-data friend <https://github.com/OAI/OpenAPI-Specification/blob/3.1.0/vers...>\n\nThe latter is likely problematic, but the former is in wide use still, including, strangely enough, the AWS API, although some of their newer services do have an application/json protocol\n\nI know that's a lot of words, but the tl;dr would be that if you want your extension to be application/json only, then changing the description to say \"OpenAPI specifications for application/json handshakes\" would help the consumer be on the same page with your goals\n\n\n\n\t\n\t\nmrmagoo2 on Oct 26, 2023 | root | parent | next [–]\n\n\nYou raise a good point and it would be great to account for this. I will take a look at this. Excellent suggestion.\n\n\n\n\t\n\t\njcrites on Oct 25, 2023 | parent | prev | next [–]\n\n\nDoes gRPC /ProtoBuf have support for web browsers? I don't know of a situation where I'd encounter those in a web application.\n\n\n\n\t\n\t\nvoidmain0001 on Oct 25, 2023 | root | parent | next [–]\n\n\nhttps://blog.envoyproxy.io/envoy-and-grpc-web-a-fresh-new-al...\n\n\n\n\t\n\t\nAarekaz on Oct 25, 2023 | prev | next [–]\n\n\nThis looks super interesting. Works for anything? Damn.\n\n\n\n\t\n\t\npihentagy on Oct 26, 2023 | prev | next [–]\n\n\nIs there a way to filter out headers?\n\nThe result contains headers like content-length and similar.\n\nAlso it would be nice if it could factor out common schemas.\n\n\n\n\t\n\t\ncorry on Oct 25, 2023 | prev | next [–]\n\n\nAwesome! Any chance of a Safari extension too?\n\n\n\n\t\n\t\nlukeplato on Oct 25, 2023 | prev | next [–]\n\n\nWould be cool if this shared the user found specs to create a database of API specs for the web\n\n\n\n\t\n\t\npmkelly4444 on Oct 25, 2023 | prev | next [–]\n\n\nthis is very cool! I just tried using it, unfortunately, my NextJS app dir project makes most requests from the server side, so it was only capturing \"posts\" made from the client. Is there a way to run it from the server?\n\n\n\n\t\n\t\nsiva7 on Oct 25, 2023 | prev | next [–]\n\n\nI'm sure many developers wished at some point such magic would exist\n\n\n\n\t\n\t\nec109685 on Oct 25, 2023 | prev | next [–]\n\n\nWould love this for apps.\n\n\n\n\t\n\t\nchris_nielsen on Oct 25, 2023 | prev | next [–]\n\n\nThis looks super useful, can’t wait to try it at work tomorrow!\n\n\n\n\t\n\t\nnamtab00 on Oct 25, 2023 | parent | next [–]\n\n\nCare to share what would it be useful for?\n\nI mean, and I'm asking as a backend dev, if you have to integrate with some API, you use the provided docs/swagger ui.\n\nWhy/when would you care to rely on an API integration when it's interface is not publicly shared?\n\n\n\n\t\n\t\nimhoguy on Oct 25, 2023 | root | parent | next [–]\n\n\nBecause this is for these edge cases where docs are crap and Swagger spec is non-existent.\n\n\n\n\t\n\t\nzoover2020 on Oct 25, 2023 | root | parent | prev | next [–]\n\n\nReverse engineering? You just described it\n\n\n\n\t\n\t\njasfi on Oct 25, 2023 | prev | next [–]\n\n\nThis could be useful for learning from any site you admire.\n\n\n\n\t\n\t\nfullofdev on Oct 26, 2023 | prev [–]\n\n\nlooks really cool! congrats!\n\n\n\n\n\n\n\nGuidelines | FAQ | Lists | API | Security | Legal | Apply to YC | Contact\n\n\nSearch:",
  "usage": {
    "tokens": 7026
  }
}
```
