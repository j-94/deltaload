---
title: Tool use (function calling) - Anthropic
description: 
url: https://docs.anthropic.com/claude/docs/tool-use-examples#specifying-tools
timestamp: 2025-01-20T16:02:40.340Z
domain: docs.anthropic.com
path: claude_docs_tool-use-examples
---

# Tool use (function calling) - Anthropic



## Content

Tool use (function calling) - Anthropic
===============
  

   

[Anthropic home page![Image 3: light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![Image 4: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](https://docs.anthropic.com/)

English

Search...

*   [Research](https://www.anthropic.com/research)
*   [News](https://www.anthropic.com/news)
*   [Go to claude.ai](https://claude.ai/)
*   [Go to claude.ai](https://claude.ai/)

Search...

Navigation

Build with Claude

Tool use (function calling)

[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)

*   [Developer Console](https://console.anthropic.com/)
*   [Developer Discord](https://www.anthropic.com/discord)
*   [Support](https://support.anthropic.com/)

##### Get started

*   [Overview](https://docs.anthropic.com/en/docs/welcome)
*   [Initial setup](https://docs.anthropic.com/en/docs/initial-setup)
*   [Intro to Claude](https://docs.anthropic.com/en/docs/intro-to-claude)

##### Learn about Claude

*   Use cases
    
*   [Models](https://docs.anthropic.com/en/docs/about-claude/models)
*   [Security and compliance](https://trust.anthropic.com/)

##### Build with Claude

*   [Define success criteria](https://docs.anthropic.com/en/docs/build-with-claude/define-success)
*   [Develop test cases](https://docs.anthropic.com/en/docs/build-with-claude/develop-tests)
*   Prompt engineering
    
*   [Text generation](https://docs.anthropic.com/en/docs/build-with-claude/text-generation)
*   [Embeddings](https://docs.anthropic.com/en/docs/build-with-claude/embeddings)
*   [Google Sheets add-on](https://docs.anthropic.com/en/docs/build-with-claude/claude-for-sheets)
*   [Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)
*   [Tool use (function calling)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
*   [Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/build-with-claude/mcp)
*   [Computer use (beta)](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
*   [Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
*   [Message Batches](https://docs.anthropic.com/en/docs/build-with-claude/message-batches)
*   [PDF support](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support)
*   [Token counting](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)
*   [Multilingual support](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support)

##### Test and evaluate

*   Strengthen guardrails
    
*   [Using the Evaluation Tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool)

##### Administration

*   [Admin API](https://docs.anthropic.com/en/docs/administration/administration-api)

##### Resources

*   [Glossary](https://docs.anthropic.com/en/docs/resources/glossary)
*   [Model Deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations)
*   [System status](https://status.anthropic.com/)
*   [Claude 3 model card](https://assets.anthropic.com/m/61e7d27f8c8f5919/original/Claude-3-Model-Card.pdf)
*   [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
*   [Anthropic Courses](https://github.com/anthropics/courses)

##### Legal center

*   [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)

Build with Claude

Tool use (function calling)
===========================

Claude is capable of interacting with external client-side tools and functions, allowing you to equip Claude with your own custom tools to perform a wider variety of tasks.

Learn everything you need to master tool use with Claude via our new comprehensive [tool use course](https://github.com/anthropics/courses/tree/master/tool_use)! Please continue to share your ideas and suggestions using this [form](https://forms.gle/BFnYc6iCkWoRzFgk7).

Here’s an example of how to provide tools to Claude using the Messages API:

* * *

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#how-tool-use-works)

How tool use works
------------------------------------------------------------------------------------------------------

Integrate external tools with Claude in these steps:

1

Provide Claude with tools and a user prompt

*   Define tools with names, descriptions, and input schemas in your API request.
*   Include a user prompt that might require these tools, e.g., “What’s the weather in San Francisco?”

2

Claude decides to use a tool

*   Claude assesses if any tools can help with the user’s query.
*   If yes, Claude constructs a properly formatted tool use request.
*   The API response has a `stop_reason` of `tool_use`, signaling Claude’s intent.

3

Extract tool input, run code, and return results

*   On your end, extract the tool name and input from Claude’s request.
*   Execute the actual tool code client-side.
*   Continue the conversation with a new `user` message containing a `tool_result` content block.

4

Claude uses tool result to formulate a response

*   Claude analyzes the tool results to craft its final response to the original user prompt.

Note: Steps 3 and 4 are optional. For some workflows, Claude’s tool use request (step 2) might be all you need, without sending results back to Claude.

**Tools are user-provided**

It’s important to note that Claude does not have access to any built-in server-side tools. All tools must be explicitly provided by you, the user, in each API request. This gives you full control and flexibility over the tools Claude can use.

The [computer use (beta)](https://docs.anthropic.com/en/docs/computer-use) functionality is an exception - it introduces tools that are provided by Anthropic but implemented by you, the user.

* * *

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#how-to-implement-tool-use)

How to implement tool use
--------------------------------------------------------------------------------------------------------------------

### 

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#choosing-a-model)

Choosing a model

Generally, use Claude 3.5 Sonnet or Claude 3 Opus for complex tools and ambiguous queries; they handle multiple tools better and seek clarification when needed.

Use Claude 3.5 Haiku or Claude 3 Haiku for straightforward tools, but note they may infer missing parameters.

### 

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#specifying-tools)

Specifying tools

Tools are specified in the `tools` top-level parameter of the API request. Each tool definition includes:

| Parameter | Description |
| --- | --- |
| `name` | The name of the tool. Must match the regex `^[a-zA-Z0-9_-]{1,64}$`. |
| `description` | A detailed plaintext description of what the tool does, when it should be used, and how it behaves. |
| `input_schema` | A [JSON Schema](https://json-schema.org/) object defining the expected parameters for the tool. |

Example simple tool definition

JSON

```JSON
{
  "name": "get_weather",
  "description": "Get the current weather in a given location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The city and state, e.g. San Francisco, CA"
      },
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "The unit of temperature, either 'celsius' or 'fahrenheit'"
      }
    },
    "required": ["location"]
  }
}
```

This tool, named `get_weather`, expects an input object with a required `location` string and an optional `unit` string that must be either “celsius” or “fahrenheit”.

#### 

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#tool-use-system-prompt)

Tool use system prompt

When you call the Anthropic API with the `tools` parameter, we construct a special system prompt from the tool definitions, tool configuration, and any user-specified system prompt. The constructed prompt is designed to instruct the model to use the specified tool(s) and provide the necessary context for the tool to operate properly:

```
In this environment you have access to a set of tools you can use to answer the user's question.
{{ FORMATTING INSTRUCTIONS }}
String and scalar parameters should be specified as is, while lists and objects should use JSON format. Note that spaces for string values are not stripped. The output is not expected to be valid XML and is parsed with regular expressions.
Here are the functions available in JSONSchema format:
{{ TOOL DEFINITIONS IN JSON SCHEMA }}
{{ USER SYSTEM PROMPT }}
{{ TOOL CONFIGURATION }}
```

#### 

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#best-practices-for-tool-definitions)

Best practices for tool definitions

To get the best performance out of Claude when using tools, follow these guidelines:

*   **Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain every detail about the tool, including:
    *   What the tool does
    *   When it should be used (and when it shouldn’t)
    *   What each parameter means and how it affects the tool’s behavior
    *   Any important caveats or limitations, such as what information the tool does not return if the tool name is unclear. The more context you can give Claude about your tools, the better it will be at deciding when and how to use them. Aim for at least 3-4 sentences per tool description, more if the tool is complex.
*   **Prioritize descriptions over examples.** While you can include examples of how to use a tool in its description or in the accompanying prompt, this is less important than having a clear and comprehensive explanation of the tool’s purpose and parameters. Only add examples after you’ve fully fleshed out the description.

Example of a good tool description

JSON

```JSON
{
  "name": "get_stock_price",
  "description": "Retrieves the current stock price for a given ticker symbol. The ticker symbol must be a valid symbol for a publicly traded company on a major US stock exchange like NYSE or NASDAQ. The tool will return the latest trade price in USD. It should be used when the user asks about the current or most recent price of a specific stock. It will not provide any other information about the stock or company.",
  "input_schema": {
    "type": "object",
    "properties": {
      "ticker": {
        "type": "string",
        "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
      }
    },
    "required": ["ticker"]
  }
}
```

Example poor tool description

JSON

```JSON
{
  "name": "get_stock_price",
  "description": "Gets the stock price for a ticker.",
  "input_schema": {
    "type": "object",
    "properties": {
      "ticker": {
        "type": "string"
      }
    },
    "required": ["ticker"]
  }
}
```

The good description clearly explains what the tool does, when to use it, what data it returns, and what the `ticker` parameter means. The poor description is too brief and leaves Claude with many open questions about the tool’s behavior and usage.

### 

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#controlling-claudes-output)

Controlling Claude’s output

#### 

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#forcing-tool-use)

Forcing tool use

In some cases, you may want Claude to use a specific tool to answer the user’s question, even if Claude thinks it can provide an answer without using a tool. You can do this by specifying the tool in the `tool_choice` field like so:

```
tool_choice = {"type": "tool", "name": "get_weather"}
```

When working with the tool\_choice parameter, we have three possible options:

*   `auto` allows Claude to decide whether to call any provided tools or not. This is the default value.
*   `any` tells Claude that it must use one of the provided tools, but doesn’t force a particular tool.
*   `tool` allows us to force Claude to always use a particular tool.

This diagram illustrates how each option works:

Note that when you have `tool_choice` as `any` or `tool`, we will prefill the assistant message to force a tool to be used. This means that the models will not emit a chain-of-thought `text` content block before `tool_use` content blocks, even if explicitly asked to do so.

Our testing has shown that this should not reduce performance. If you would like to keep chain-of-thought (particularly with Opus) while still requesting that the model use a specific tool, you can use `{"type": "auto"}` for `tool_choice` (the default) and add explicit instructions in a `user` message. For example: `What's the weather like in London? Use the get_weather tool in your response.`

#### 

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#json-output)

JSON output

Tools do not necessarily need to be client-side functions — you can use tools anytime you want the model to return JSON output that follows a provided schema. For example, you might use a `record_summary` tool with a particular schema. See [tool use examples](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#json-mode) for a full working example.

#### 

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#chain-of-thought)

Chain of thought

When using tools, Claude will often show its “chain of thought”, i.e. the step-by-step reasoning it uses to break down the problem and decide which tools to use. The Claude 3 Opus model will do this if `tool_choice` is set to `auto` (this is the default value, see [Forcing tool use](https://docs.anthropic.com/_sites/docs.anthropic.com/en/docs/build-with-claude/tool-use#forcing-tool-use)), and Sonnet and Haiku can be prompted into doing it.

For example, given the prompt “What’s the weather like in San Francisco right now, and what time is it there?”, Claude might respond with:

JSON

```JSON
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "<thinking>To answer this question, I will: 1. Use the get_weather tool to get the current weather in San Francisco. 2. Use the get_time tool to get the current time in the America/Los_Angeles timezone, which covers San Francisco, CA.</thinking>"
    },
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": {"location": "San Francisco, CA"}
    }
  ]
}
```

This chain of thought gives insight into Claude’s reasoning process and can help you debug unexpected behavior.

With the Claude 3 Sonnet model, chain of thought is less common by default, but you can prompt Claude to show its reasoning by adding something like `"Before answering, explain your reasoning step-by-step in tags."` to the user message or system prompt.

It’s important to note that while the `<thinking>` tags are a common convention Claude uses to denote its chain of thought, the exact format (such as what this XML tag is named) may change over time. Your code should treat the chain of thought like any other assistant-generated text, and not rely on the presence or specific formatting of the `<thinking>` tags.

#### 

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#disabling-parallel-tool-use)

Disabling parallel tool use

By default, Claude may use multiple tools to answer a user query. You can disable this behavior by setting `disable_parallel_tool_use=true` in the `tool_choice` field.

*   When `tool_choice` type is `auto`, this ensures that Claude uses **at most one** tool
*   When `tool_choice` type is `any` or `tool`, this ensures that Claude uses **exactly one** tool

### 

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#handling-tool-use-and-tool-result-content-blocks)

Handling tool use and tool result content blocks

When Claude decides to use one of the tools you’ve provided, it will return a response with a `stop_reason` of `tool_use` and one or more `tool_use` content blocks in the API response that include:

*   `id`: A unique identifier for this particular tool use block. This will be used to match up the tool results later.
*   `name`: The name of the tool being used.
*   `input`: An object containing the input being passed to the tool, conforming to the tool’s `input_schema`.

Example API response with a \`tool\_use\` content block

JSON

```JSON
{
  "id": "msg_01Aq9w938a90dw8q",
  "model": "claude-3-5-sonnet-20241022",
  "stop_reason": "tool_use",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "<thinking>I need to use the get_weather, and the user wants SF, which is likely San Francisco, CA.</thinking>"
    },
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": {"location": "San Francisco, CA", "unit": "celsius"}
    }
  ]
}
```

When you receive a tool use response, you should:

1.  Extract the `name`, `id`, and `input` from the `tool_use` block.
2.  Run the actual tool in your codebase corresponding to that tool name, passing in the tool `input`.
3.  Continue the conversation by sending a new message with the `role` of `user`, and a `content` block containing the `tool_result` type and the following information:
    *   `tool_use_id`: The `id` of the tool use request this is a result for.
    *   `content`: The result of the tool, as a string (e.g. `"content": "15 degrees"`) or list of nested content blocks (e.g. `"content": [{"type": "text", "text": "15 degrees"}]`). These content blocks can use the `text` or `image` types.
    *   `is_error` (optional): Set to `true` if the tool execution resulted in an error.

Example of successful tool result

JSON

```JSON
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "15 degrees"
    }
  ]
}
```

Example of tool result with images

JSON

```JSON
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": [
        {"type": "text", "text": "15 degrees"},
        {
          "type": "image",
          "source": {
            "type": "base64",
            "media_type": "image/jpeg",
            "data": "/9j/4AAQSkZJRg...",
          }
        }
      ]
    }
  ]
}
```

Example of empty tool result

JSON

```JSON
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
    }
  ]
}
```

After receiving the tool result, Claude will use that information to continue generating a response to the original user prompt.

**Differences from other APIs**

Unlike APIs that separate tool use or use special roles like `tool` or `function`, Anthropic’s API integrates tools directly into the `user` and `assistant` message structure.

Messages contain arrays of `text`, `image`, `tool_use`, and `tool_result` blocks. `user` messages include client-side content and `tool_result`, while `assistant` messages contain AI-generated content and `tool_use`.

### 

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#troubleshooting-errors)

Troubleshooting errors

There are a few different types of errors that can occur when using tools with Claude:

Tool execution error

If the tool itself throws an error during execution (e.g. a network error when fetching weather data), you can return the error message in the `content` along with `"is_error": true`:

JSON

```JSON
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "ConnectionError: the weather service API is not available (HTTP 500)",
      "is_error": true
    }
  ]
}
```

Claude will then incorporate this error into its response to the user, e.g. “I’m sorry, I was unable to retrieve the current weather because the weather service API is not available. Please try again later.”

Max tokens exceeded

If Claude’s response is cut off due to hitting the `max_tokens` limit, and the truncated response contains an incomplete tool use block, you’ll need to retry the request with a higher `max_tokens` value to get the full tool use.

Invalid tool name

If Claude’s attempted use of a tool is invalid (e.g. missing required parameters), it usually means that the there wasn’t enough information for Claude to use the tool correctly. Your best bet during development is to try the request again with more-detailed `description` values in your tool definitions.

However, you can also continue the conversation forward with a `tool_result` that indicates the error, and Claude will try to use the tool again with the missing information filled in:

JSON

```JSON
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "Error: Missing required 'location' parameter",
      "is_error": true
    }
  ]
}
```

If a tool request is invalid or missing parameters, Claude will retry 2-3 times with corrections before apologizing to the user.

<search\_quality\_reflection\> tags

To prevent Claude from reflecting on search quality with <search\_quality\_reflection\> tags, add “Do not reflect on the quality of the returned search results in your response” to your prompt.

* * *

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#tool-use-examples)

Tool use examples
----------------------------------------------------------------------------------------------------

Here are a few code examples demonstrating various tool use patterns and techniques. For brevity’s sake, the tools are simple tools, and the tool descriptions are shorter than would be ideal to ensure best performance.

Single tool example

Claude will return a response similar to:

JSON

```JSON
{
  "id": "msg_01Aq9w938a90dw8q",
  "model": "claude-3-5-sonnet-20241022",
  "stop_reason": "tool_use",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "<thinking>I need to call the get_weather function, and the user wants SF, which is likely San Francisco, CA.</thinking>"
    },
    {
      "type": "tool_use",
      "id": "toolu_01A09q90qw90lq917835lq9",
      "name": "get_weather",
      "input": {"location": "San Francisco, CA", "unit": "celsius"}
    }
  ]
}
```

You would then need to execute the `get_weather` function with the provided input, and return the result in a new `user` message:

This will print Claude’s final response, incorporating the weather data:

JSON

```JSON
{
  "id": "msg_01Aq9w938a90dw8q",
  "model": "claude-3-5-sonnet-20241022",
  "stop_reason": "stop_sequence",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "The current weather in San Francisco is 15 degrees Celsius (59 degrees Fahrenheit). It's a cool day in the city by the bay!"
    }
  ]
}
```

Multiple tool example

You can provide Claude with multiple tools to choose from in a single request. Here’s an example with both a `get_weather` and a `get_time` tool, along with a user query that asks for both.

In this case, Claude will most likely try to use two separate tools, one at a time — `get_weather` and then `get_time` — in order to fully answer the user’s question. However, it will also occasionally output two `tool_use` blocks at once, particularly if they are not dependent on each other. You would need to execute each tool and return their results in separate `tool_result` blocks within a single `user` message.

Missing information

If the user’s prompt doesn’t include enough information to fill all the required parameters for a tool, Claude 3 Opus is much more likely to recognize that a parameter is missing and ask for it. Claude 3 Sonnet may ask, especially when prompted to think before outputting a tool request. But it may also do its best to infer a reasonable value.

For example, using the `get_weather` tool above, if you ask Claude “What’s the weather?” without specifying a location, Claude, particularly Claude 3 Sonnet, may make a guess about tools inputs:

JSON

```JSON
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "get_weather",
  "input": {"location": "New York, NY", "unit": "fahrenheit"}
}
```

This behavior is not guaranteed, especially for more ambiguous prompts and for models less intelligent than Claude 3 Opus. If Claude 3 Opus doesn’t have enough context to fill in the required parameters, it is far more likely respond with a clarifying question instead of making a tool call.

Sequential tools

Some tasks may require calling multiple tools in sequence, using the output of one tool as the input to another. In such a case, Claude will call one tool at a time. If prompted to call the tools all at once, Claude is likely to guess parameters for tools further downstream if they are dependent on tool results for tools further upstream.

Here’s an example of using a `get_location` tool to get the user’s location, then passing that location to the `get_weather` tool:

In this case, Claude would first call the `get_location` tool to get the user’s location. After you return the location in a `tool_result`, Claude would then call `get_weather` with that location to get the final answer.

The full conversation might look like:

| Role | Content |
| --- | --- |
| User | What’s the weather like where I am? |
| Assistant | <thinking\>To answer this, I first need to determine the user’s location using the get\_location tool. Then I can pass that location to the get\_weather tool to find the current weather there.</thinking\>\[Tool use for get\_location\] |
| User | \[Tool result for get\_location with matching id and result of San Francisco, CA\] |
| Assistant | \[Tool use for get\_weather with the following input\]{ “location”: “San Francisco, CA”, “unit”: “fahrenheit” } |
| User | \[Tool result for get\_weather with matching id and result of “59°F (15°C), mostly cloudy”\] |
| Assistant | Based on your current location in San Francisco, CA, the weather right now is 59°F (15°C) and mostly cloudy. It’s a fairly cool and overcast day in the city. You may want to bring a light jacket if you’re heading outside. |

This example demonstrates how Claude can chain together multiple tool calls to answer a question that requires gathering data from different sources. The key steps are:

1.  Claude first realizes it needs the user’s location to answer the weather question, so it calls the `get_location` tool.
2.  The user (i.e. the client code) executes the actual `get_location` function and returns the result “San Francisco, CA” in a `tool_result` block.
3.  With the location now known, Claude proceeds to call the `get_weather` tool, passing in “San Francisco, CA” as the `location` parameter (as well as a guessed `unit` parameter, as `unit` is not a required parameter).
4.  The user again executes the actual `get_weather` function with the provided arguments and returns the weather data in another `tool_result` block.
5.  Finally, Claude incorporates the weather data into a natural language response to the original question.

Chain of thought tool use

By default, Claude 3 Opus is prompted to think before it answers a tool use query to best determine whether a tool is necessary, which tool to use, and the appropriate parameters. Claude 3 Sonnet and Claude 3 Haiku are prompted to try to use tools as much as possible and are more likely to call an unnecessary tool or infer missing parameters. To prompt Sonnet or Haiku to better assess the user query before making tool calls, the following prompt can be used:

Chain of thought prompt

`Answer the user's request using relevant tools (if they are available). Before calling a tool, do some analysis within \<thinking>\</thinking> tags. First, think about which of the provided tools is the relevant tool to answer the user's request. Second, go through each of the required parameters of the relevant tool and determine if the user has directly provided or given enough information to infer a value. When deciding if the parameter can be inferred, carefully consider all the context to see if it supports a specific value. If all of the required parameters are present or can be reasonably inferred, close the thinking tag and proceed with the tool call. BUT, if one of the values for a required parameter is missing, DO NOT invoke the function (not even with fillers for the missing params) and instead, ask the user to provide the missing parameters. DO NOT ask for more information on optional parameters if it is not provided.     `

JSON mode

You can use tools to get Claude produce JSON output that follows a schema, even if you don’t have any intention of running that output through a tool or function.

When using tools in this way:

*   You usually want to provide a **single** tool
*   You should set `tool_choice` (see [Forcing tool use](https://docs.anthropic.com/en/docs/tool-use#forcing-tool-use)) to instruct the model to explicitly use that tool
*   Remember that the model will pass the `input` to the tool, so the name of the tool and description should be from the model’s perspective.

The following uses a `record_summary` tool to describe an image following a particular format.

* * *

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#pricing)

Pricing
--------------------------------------------------------------------------------

Tool use requests are priced the same as any other Claude API request, based on the total number of input tokens sent to the model (including in the `tools` parameter) and the number of output tokens generated.”

The additional tokens from tool use come from:

*   The `tools` parameter in API requests (tool names, descriptions, and schemas)
*   `tool_use` content blocks in API requests and responses
*   `tool_result` content blocks in API requests

When you use `tools`, we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above):

| Model | Tool choice | Tool use system prompt token count |
| --- | --- | --- |
| Claude 3.5 Sonnet (Oct) | `auto`
* * *

`any`, `tool` | 346 tokens

* * *

313 tokens |
| Claude 3 Opus | `auto`

* * *

`any`, `tool` | 530 tokens

* * *

281 tokens |
| Claude 3 Sonnet | `auto`

* * *

`any`, `tool` | 159 tokens

* * *

235 tokens |
| Claude 3 Haiku | `auto`

* * *

`any`, `tool` | 264 tokens

* * *

340 tokens |
| Claude 3.5 Sonnet (June) | `auto`

* * *

`any`, `tool` | 294 tokens

* * *

261 tokens |

These token counts are added to your normal input and output tokens to calculate the total cost of a request. Refer to our [models overview table](https://docs.anthropic.com/en/docs/models-overview#model-comparison) for current per-model prices.

When you send a tool use prompt, just like any other API request, the response will output both input and output token counts as part of the reported `usage` metrics.

* * *

[​](https://docs.anthropic.com/claude/docs/tool-use-examples#next-steps)

Next Steps
--------------------------------------------------------------------------------------

Explore our repository of ready-to-implement tool use code examples in our cookbooks:

[Calculator Tool --------------- Learn how to integrate a simple calculator tool with Claude for precise numerical computations.](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/calculator_tool.ipynb)[Customer Service Agent ---------------------- Build a responsive customer service bot that leverages client-side tools to enhance support.](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/customer_service_agent.ipynb)[JSON Extractor -------------- See how Claude and tool use can extract structured data from unstructured text.](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/extracting_structured_json.ipynb)

Was this page helpful?

YesNo

[Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)[Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/build-with-claude/mcp)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

On this page

*   [How tool use works](https://docs.anthropic.com/claude/docs/tool-use-examples#how-tool-use-works)
*   [How to implement tool use](https://docs.anthropic.com/claude/docs/tool-use-examples#how-to-implement-tool-use)
*   [Choosing a model](https://docs.anthropic.com/claude/docs/tool-use-examples#choosing-a-model)
*   [Specifying tools](https://docs.anthropic.com/claude/docs/tool-use-examples#specifying-tools)
*   [Tool use system prompt](https://docs.anthropic.com/claude/docs/tool-use-examples#tool-use-system-prompt)
*   [Best practices for tool definitions](https://docs.anthropic.com/claude/docs/tool-use-examples#best-practices-for-tool-definitions)
*   [Controlling Claude’s output](https://docs.anthropic.com/claude/docs/tool-use-examples#controlling-claudes-output)
*   [Forcing tool use](https://docs.anthropic.com/claude/docs/tool-use-examples#forcing-tool-use)
*   [JSON output](https://docs.anthropic.com/claude/docs/tool-use-examples#json-output)
*   [Chain of thought](https://docs.anthropic.com/claude/docs/tool-use-examples#chain-of-thought)
*   [Disabling parallel tool use](https://docs.anthropic.com/claude/docs/tool-use-examples#disabling-parallel-tool-use)
*   [Handling tool use and tool result content blocks](https://docs.anthropic.com/claude/docs/tool-use-examples#handling-tool-use-and-tool-result-content-blocks)
*   [Troubleshooting errors](https://docs.anthropic.com/claude/docs/tool-use-examples#troubleshooting-errors)
*   [Tool use examples](https://docs.anthropic.com/claude/docs/tool-use-examples#tool-use-examples)
*   [Pricing](https://docs.anthropic.com/claude/docs/tool-use-examples#pricing)
*   [Next Steps](https://docs.anthropic.com/claude/docs/tool-use-examples#next-steps)

## Metadata

```json
{
  "title": "Tool use (function calling) - Anthropic",
  "description": "",
  "url": "https://docs.anthropic.com/claude/docs/tool-use-examples#specifying-tools",
  "content": "Tool use (function calling) - Anthropic\n===============\n  \n\n   \n\n[Anthropic home page![Image 3: light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![Image 4: dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](https://docs.anthropic.com/)\n\nEnglish\n\nSearch...\n\n*   [Research](https://www.anthropic.com/research)\n*   [News](https://www.anthropic.com/news)\n*   [Go to claude.ai](https://claude.ai/)\n*   [Go to claude.ai](https://claude.ai/)\n\nSearch...\n\nNavigation\n\nBuild with Claude\n\nTool use (function calling)\n\n[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)\n\n*   [Developer Console](https://console.anthropic.com/)\n*   [Developer Discord](https://www.anthropic.com/discord)\n*   [Support](https://support.anthropic.com/)\n\n##### Get started\n\n*   [Overview](https://docs.anthropic.com/en/docs/welcome)\n*   [Initial setup](https://docs.anthropic.com/en/docs/initial-setup)\n*   [Intro to Claude](https://docs.anthropic.com/en/docs/intro-to-claude)\n\n##### Learn about Claude\n\n*   Use cases\n    \n*   [Models](https://docs.anthropic.com/en/docs/about-claude/models)\n*   [Security and compliance](https://trust.anthropic.com/)\n\n##### Build with Claude\n\n*   [Define success criteria](https://docs.anthropic.com/en/docs/build-with-claude/define-success)\n*   [Develop test cases](https://docs.anthropic.com/en/docs/build-with-claude/develop-tests)\n*   Prompt engineering\n    \n*   [Text generation](https://docs.anthropic.com/en/docs/build-with-claude/text-generation)\n*   [Embeddings](https://docs.anthropic.com/en/docs/build-with-claude/embeddings)\n*   [Google Sheets add-on](https://docs.anthropic.com/en/docs/build-with-claude/claude-for-sheets)\n*   [Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)\n*   [Tool use (function calling)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)\n*   [Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/build-with-claude/mcp)\n*   [Computer use (beta)](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)\n*   [Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)\n*   [Message Batches](https://docs.anthropic.com/en/docs/build-with-claude/message-batches)\n*   [PDF support](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support)\n*   [Token counting](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)\n*   [Multilingual support](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support)\n\n##### Test and evaluate\n\n*   Strengthen guardrails\n    \n*   [Using the Evaluation Tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool)\n\n##### Administration\n\n*   [Admin API](https://docs.anthropic.com/en/docs/administration/administration-api)\n\n##### Resources\n\n*   [Glossary](https://docs.anthropic.com/en/docs/resources/glossary)\n*   [Model Deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations)\n*   [System status](https://status.anthropic.com/)\n*   [Claude 3 model card](https://assets.anthropic.com/m/61e7d27f8c8f5919/original/Claude-3-Model-Card.pdf)\n*   [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)\n*   [Anthropic Courses](https://github.com/anthropics/courses)\n\n##### Legal center\n\n*   [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)\n\nBuild with Claude\n\nTool use (function calling)\n===========================\n\nClaude is capable of interacting with external client-side tools and functions, allowing you to equip Claude with your own custom tools to perform a wider variety of tasks.\n\nLearn everything you need to master tool use with Claude via our new comprehensive [tool use course](https://github.com/anthropics/courses/tree/master/tool_use)! Please continue to share your ideas and suggestions using this [form](https://forms.gle/BFnYc6iCkWoRzFgk7).\n\nHere’s an example of how to provide tools to Claude using the Messages API:\n\n* * *\n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#how-tool-use-works)\n\nHow tool use works\n------------------------------------------------------------------------------------------------------\n\nIntegrate external tools with Claude in these steps:\n\n1\n\nProvide Claude with tools and a user prompt\n\n*   Define tools with names, descriptions, and input schemas in your API request.\n*   Include a user prompt that might require these tools, e.g., “What’s the weather in San Francisco?”\n\n2\n\nClaude decides to use a tool\n\n*   Claude assesses if any tools can help with the user’s query.\n*   If yes, Claude constructs a properly formatted tool use request.\n*   The API response has a `stop_reason` of `tool_use`, signaling Claude’s intent.\n\n3\n\nExtract tool input, run code, and return results\n\n*   On your end, extract the tool name and input from Claude’s request.\n*   Execute the actual tool code client-side.\n*   Continue the conversation with a new `user` message containing a `tool_result` content block.\n\n4\n\nClaude uses tool result to formulate a response\n\n*   Claude analyzes the tool results to craft its final response to the original user prompt.\n\nNote: Steps 3 and 4 are optional. For some workflows, Claude’s tool use request (step 2) might be all you need, without sending results back to Claude.\n\n**Tools are user-provided**\n\nIt’s important to note that Claude does not have access to any built-in server-side tools. All tools must be explicitly provided by you, the user, in each API request. This gives you full control and flexibility over the tools Claude can use.\n\nThe [computer use (beta)](https://docs.anthropic.com/en/docs/computer-use) functionality is an exception - it introduces tools that are provided by Anthropic but implemented by you, the user.\n\n* * *\n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#how-to-implement-tool-use)\n\nHow to implement tool use\n--------------------------------------------------------------------------------------------------------------------\n\n### \n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#choosing-a-model)\n\nChoosing a model\n\nGenerally, use Claude 3.5 Sonnet or Claude 3 Opus for complex tools and ambiguous queries; they handle multiple tools better and seek clarification when needed.\n\nUse Claude 3.5 Haiku or Claude 3 Haiku for straightforward tools, but note they may infer missing parameters.\n\n### \n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#specifying-tools)\n\nSpecifying tools\n\nTools are specified in the `tools` top-level parameter of the API request. Each tool definition includes:\n\n| Parameter | Description |\n| --- | --- |\n| `name` | The name of the tool. Must match the regex `^[a-zA-Z0-9_-]{1,64}$`. |\n| `description` | A detailed plaintext description of what the tool does, when it should be used, and how it behaves. |\n| `input_schema` | A [JSON Schema](https://json-schema.org/) object defining the expected parameters for the tool. |\n\nExample simple tool definition\n\nJSON\n\n```JSON\n{\n  \"name\": \"get_weather\",\n  \"description\": \"Get the current weather in a given location\",\n  \"input_schema\": {\n    \"type\": \"object\",\n    \"properties\": {\n      \"location\": {\n        \"type\": \"string\",\n        \"description\": \"The city and state, e.g. San Francisco, CA\"\n      },\n      \"unit\": {\n        \"type\": \"string\",\n        \"enum\": [\"celsius\", \"fahrenheit\"],\n        \"description\": \"The unit of temperature, either 'celsius' or 'fahrenheit'\"\n      }\n    },\n    \"required\": [\"location\"]\n  }\n}\n```\n\nThis tool, named `get_weather`, expects an input object with a required `location` string and an optional `unit` string that must be either “celsius” or “fahrenheit”.\n\n#### \n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#tool-use-system-prompt)\n\nTool use system prompt\n\nWhen you call the Anthropic API with the `tools` parameter, we construct a special system prompt from the tool definitions, tool configuration, and any user-specified system prompt. The constructed prompt is designed to instruct the model to use the specified tool(s) and provide the necessary context for the tool to operate properly:\n\n```\nIn this environment you have access to a set of tools you can use to answer the user's question.\n{{ FORMATTING INSTRUCTIONS }}\nString and scalar parameters should be specified as is, while lists and objects should use JSON format. Note that spaces for string values are not stripped. The output is not expected to be valid XML and is parsed with regular expressions.\nHere are the functions available in JSONSchema format:\n{{ TOOL DEFINITIONS IN JSON SCHEMA }}\n{{ USER SYSTEM PROMPT }}\n{{ TOOL CONFIGURATION }}\n```\n\n#### \n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#best-practices-for-tool-definitions)\n\nBest practices for tool definitions\n\nTo get the best performance out of Claude when using tools, follow these guidelines:\n\n*   **Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain every detail about the tool, including:\n    *   What the tool does\n    *   When it should be used (and when it shouldn’t)\n    *   What each parameter means and how it affects the tool’s behavior\n    *   Any important caveats or limitations, such as what information the tool does not return if the tool name is unclear. The more context you can give Claude about your tools, the better it will be at deciding when and how to use them. Aim for at least 3-4 sentences per tool description, more if the tool is complex.\n*   **Prioritize descriptions over examples.** While you can include examples of how to use a tool in its description or in the accompanying prompt, this is less important than having a clear and comprehensive explanation of the tool’s purpose and parameters. Only add examples after you’ve fully fleshed out the description.\n\nExample of a good tool description\n\nJSON\n\n```JSON\n{\n  \"name\": \"get_stock_price\",\n  \"description\": \"Retrieves the current stock price for a given ticker symbol. The ticker symbol must be a valid symbol for a publicly traded company on a major US stock exchange like NYSE or NASDAQ. The tool will return the latest trade price in USD. It should be used when the user asks about the current or most recent price of a specific stock. It will not provide any other information about the stock or company.\",\n  \"input_schema\": {\n    \"type\": \"object\",\n    \"properties\": {\n      \"ticker\": {\n        \"type\": \"string\",\n        \"description\": \"The stock ticker symbol, e.g. AAPL for Apple Inc.\"\n      }\n    },\n    \"required\": [\"ticker\"]\n  }\n}\n```\n\nExample poor tool description\n\nJSON\n\n```JSON\n{\n  \"name\": \"get_stock_price\",\n  \"description\": \"Gets the stock price for a ticker.\",\n  \"input_schema\": {\n    \"type\": \"object\",\n    \"properties\": {\n      \"ticker\": {\n        \"type\": \"string\"\n      }\n    },\n    \"required\": [\"ticker\"]\n  }\n}\n```\n\nThe good description clearly explains what the tool does, when to use it, what data it returns, and what the `ticker` parameter means. The poor description is too brief and leaves Claude with many open questions about the tool’s behavior and usage.\n\n### \n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#controlling-claudes-output)\n\nControlling Claude’s output\n\n#### \n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#forcing-tool-use)\n\nForcing tool use\n\nIn some cases, you may want Claude to use a specific tool to answer the user’s question, even if Claude thinks it can provide an answer without using a tool. You can do this by specifying the tool in the `tool_choice` field like so:\n\n```\ntool_choice = {\"type\": \"tool\", \"name\": \"get_weather\"}\n```\n\nWhen working with the tool\\_choice parameter, we have three possible options:\n\n*   `auto` allows Claude to decide whether to call any provided tools or not. This is the default value.\n*   `any` tells Claude that it must use one of the provided tools, but doesn’t force a particular tool.\n*   `tool` allows us to force Claude to always use a particular tool.\n\nThis diagram illustrates how each option works:\n\nNote that when you have `tool_choice` as `any` or `tool`, we will prefill the assistant message to force a tool to be used. This means that the models will not emit a chain-of-thought `text` content block before `tool_use` content blocks, even if explicitly asked to do so.\n\nOur testing has shown that this should not reduce performance. If you would like to keep chain-of-thought (particularly with Opus) while still requesting that the model use a specific tool, you can use `{\"type\": \"auto\"}` for `tool_choice` (the default) and add explicit instructions in a `user` message. For example: `What's the weather like in London? Use the get_weather tool in your response.`\n\n#### \n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#json-output)\n\nJSON output\n\nTools do not necessarily need to be client-side functions — you can use tools anytime you want the model to return JSON output that follows a provided schema. For example, you might use a `record_summary` tool with a particular schema. See [tool use examples](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#json-mode) for a full working example.\n\n#### \n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#chain-of-thought)\n\nChain of thought\n\nWhen using tools, Claude will often show its “chain of thought”, i.e. the step-by-step reasoning it uses to break down the problem and decide which tools to use. The Claude 3 Opus model will do this if `tool_choice` is set to `auto` (this is the default value, see [Forcing tool use](https://docs.anthropic.com/_sites/docs.anthropic.com/en/docs/build-with-claude/tool-use#forcing-tool-use)), and Sonnet and Haiku can be prompted into doing it.\n\nFor example, given the prompt “What’s the weather like in San Francisco right now, and what time is it there?”, Claude might respond with:\n\nJSON\n\n```JSON\n{\n  \"role\": \"assistant\",\n  \"content\": [\n    {\n      \"type\": \"text\",\n      \"text\": \"<thinking>To answer this question, I will: 1. Use the get_weather tool to get the current weather in San Francisco. 2. Use the get_time tool to get the current time in the America/Los_Angeles timezone, which covers San Francisco, CA.</thinking>\"\n    },\n    {\n      \"type\": \"tool_use\",\n      \"id\": \"toolu_01A09q90qw90lq917835lq9\",\n      \"name\": \"get_weather\",\n      \"input\": {\"location\": \"San Francisco, CA\"}\n    }\n  ]\n}\n```\n\nThis chain of thought gives insight into Claude’s reasoning process and can help you debug unexpected behavior.\n\nWith the Claude 3 Sonnet model, chain of thought is less common by default, but you can prompt Claude to show its reasoning by adding something like `\"Before answering, explain your reasoning step-by-step in tags.\"` to the user message or system prompt.\n\nIt’s important to note that while the `<thinking>` tags are a common convention Claude uses to denote its chain of thought, the exact format (such as what this XML tag is named) may change over time. Your code should treat the chain of thought like any other assistant-generated text, and not rely on the presence or specific formatting of the `<thinking>` tags.\n\n#### \n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#disabling-parallel-tool-use)\n\nDisabling parallel tool use\n\nBy default, Claude may use multiple tools to answer a user query. You can disable this behavior by setting `disable_parallel_tool_use=true` in the `tool_choice` field.\n\n*   When `tool_choice` type is `auto`, this ensures that Claude uses **at most one** tool\n*   When `tool_choice` type is `any` or `tool`, this ensures that Claude uses **exactly one** tool\n\n### \n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#handling-tool-use-and-tool-result-content-blocks)\n\nHandling tool use and tool result content blocks\n\nWhen Claude decides to use one of the tools you’ve provided, it will return a response with a `stop_reason` of `tool_use` and one or more `tool_use` content blocks in the API response that include:\n\n*   `id`: A unique identifier for this particular tool use block. This will be used to match up the tool results later.\n*   `name`: The name of the tool being used.\n*   `input`: An object containing the input being passed to the tool, conforming to the tool’s `input_schema`.\n\nExample API response with a \\`tool\\_use\\` content block\n\nJSON\n\n```JSON\n{\n  \"id\": \"msg_01Aq9w938a90dw8q\",\n  \"model\": \"claude-3-5-sonnet-20241022\",\n  \"stop_reason\": \"tool_use\",\n  \"role\": \"assistant\",\n  \"content\": [\n    {\n      \"type\": \"text\",\n      \"text\": \"<thinking>I need to use the get_weather, and the user wants SF, which is likely San Francisco, CA.</thinking>\"\n    },\n    {\n      \"type\": \"tool_use\",\n      \"id\": \"toolu_01A09q90qw90lq917835lq9\",\n      \"name\": \"get_weather\",\n      \"input\": {\"location\": \"San Francisco, CA\", \"unit\": \"celsius\"}\n    }\n  ]\n}\n```\n\nWhen you receive a tool use response, you should:\n\n1.  Extract the `name`, `id`, and `input` from the `tool_use` block.\n2.  Run the actual tool in your codebase corresponding to that tool name, passing in the tool `input`.\n3.  Continue the conversation by sending a new message with the `role` of `user`, and a `content` block containing the `tool_result` type and the following information:\n    *   `tool_use_id`: The `id` of the tool use request this is a result for.\n    *   `content`: The result of the tool, as a string (e.g. `\"content\": \"15 degrees\"`) or list of nested content blocks (e.g. `\"content\": [{\"type\": \"text\", \"text\": \"15 degrees\"}]`). These content blocks can use the `text` or `image` types.\n    *   `is_error` (optional): Set to `true` if the tool execution resulted in an error.\n\nExample of successful tool result\n\nJSON\n\n```JSON\n{\n  \"role\": \"user\",\n  \"content\": [\n    {\n      \"type\": \"tool_result\",\n      \"tool_use_id\": \"toolu_01A09q90qw90lq917835lq9\",\n      \"content\": \"15 degrees\"\n    }\n  ]\n}\n```\n\nExample of tool result with images\n\nJSON\n\n```JSON\n{\n  \"role\": \"user\",\n  \"content\": [\n    {\n      \"type\": \"tool_result\",\n      \"tool_use_id\": \"toolu_01A09q90qw90lq917835lq9\",\n      \"content\": [\n        {\"type\": \"text\", \"text\": \"15 degrees\"},\n        {\n          \"type\": \"image\",\n          \"source\": {\n            \"type\": \"base64\",\n            \"media_type\": \"image/jpeg\",\n            \"data\": \"/9j/4AAQSkZJRg...\",\n          }\n        }\n      ]\n    }\n  ]\n}\n```\n\nExample of empty tool result\n\nJSON\n\n```JSON\n{\n  \"role\": \"user\",\n  \"content\": [\n    {\n      \"type\": \"tool_result\",\n      \"tool_use_id\": \"toolu_01A09q90qw90lq917835lq9\",\n    }\n  ]\n}\n```\n\nAfter receiving the tool result, Claude will use that information to continue generating a response to the original user prompt.\n\n**Differences from other APIs**\n\nUnlike APIs that separate tool use or use special roles like `tool` or `function`, Anthropic’s API integrates tools directly into the `user` and `assistant` message structure.\n\nMessages contain arrays of `text`, `image`, `tool_use`, and `tool_result` blocks. `user` messages include client-side content and `tool_result`, while `assistant` messages contain AI-generated content and `tool_use`.\n\n### \n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#troubleshooting-errors)\n\nTroubleshooting errors\n\nThere are a few different types of errors that can occur when using tools with Claude:\n\nTool execution error\n\nIf the tool itself throws an error during execution (e.g. a network error when fetching weather data), you can return the error message in the `content` along with `\"is_error\": true`:\n\nJSON\n\n```JSON\n{\n  \"role\": \"user\",\n  \"content\": [\n    {\n      \"type\": \"tool_result\",\n      \"tool_use_id\": \"toolu_01A09q90qw90lq917835lq9\",\n      \"content\": \"ConnectionError: the weather service API is not available (HTTP 500)\",\n      \"is_error\": true\n    }\n  ]\n}\n```\n\nClaude will then incorporate this error into its response to the user, e.g. “I’m sorry, I was unable to retrieve the current weather because the weather service API is not available. Please try again later.”\n\nMax tokens exceeded\n\nIf Claude’s response is cut off due to hitting the `max_tokens` limit, and the truncated response contains an incomplete tool use block, you’ll need to retry the request with a higher `max_tokens` value to get the full tool use.\n\nInvalid tool name\n\nIf Claude’s attempted use of a tool is invalid (e.g. missing required parameters), it usually means that the there wasn’t enough information for Claude to use the tool correctly. Your best bet during development is to try the request again with more-detailed `description` values in your tool definitions.\n\nHowever, you can also continue the conversation forward with a `tool_result` that indicates the error, and Claude will try to use the tool again with the missing information filled in:\n\nJSON\n\n```JSON\n{\n  \"role\": \"user\",\n  \"content\": [\n    {\n      \"type\": \"tool_result\",\n      \"tool_use_id\": \"toolu_01A09q90qw90lq917835lq9\",\n      \"content\": \"Error: Missing required 'location' parameter\",\n      \"is_error\": true\n    }\n  ]\n}\n```\n\nIf a tool request is invalid or missing parameters, Claude will retry 2-3 times with corrections before apologizing to the user.\n\n<search\\_quality\\_reflection\\> tags\n\nTo prevent Claude from reflecting on search quality with <search\\_quality\\_reflection\\> tags, add “Do not reflect on the quality of the returned search results in your response” to your prompt.\n\n* * *\n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#tool-use-examples)\n\nTool use examples\n----------------------------------------------------------------------------------------------------\n\nHere are a few code examples demonstrating various tool use patterns and techniques. For brevity’s sake, the tools are simple tools, and the tool descriptions are shorter than would be ideal to ensure best performance.\n\nSingle tool example\n\nClaude will return a response similar to:\n\nJSON\n\n```JSON\n{\n  \"id\": \"msg_01Aq9w938a90dw8q\",\n  \"model\": \"claude-3-5-sonnet-20241022\",\n  \"stop_reason\": \"tool_use\",\n  \"role\": \"assistant\",\n  \"content\": [\n    {\n      \"type\": \"text\",\n      \"text\": \"<thinking>I need to call the get_weather function, and the user wants SF, which is likely San Francisco, CA.</thinking>\"\n    },\n    {\n      \"type\": \"tool_use\",\n      \"id\": \"toolu_01A09q90qw90lq917835lq9\",\n      \"name\": \"get_weather\",\n      \"input\": {\"location\": \"San Francisco, CA\", \"unit\": \"celsius\"}\n    }\n  ]\n}\n```\n\nYou would then need to execute the `get_weather` function with the provided input, and return the result in a new `user` message:\n\nThis will print Claude’s final response, incorporating the weather data:\n\nJSON\n\n```JSON\n{\n  \"id\": \"msg_01Aq9w938a90dw8q\",\n  \"model\": \"claude-3-5-sonnet-20241022\",\n  \"stop_reason\": \"stop_sequence\",\n  \"role\": \"assistant\",\n  \"content\": [\n    {\n      \"type\": \"text\",\n      \"text\": \"The current weather in San Francisco is 15 degrees Celsius (59 degrees Fahrenheit). It's a cool day in the city by the bay!\"\n    }\n  ]\n}\n```\n\nMultiple tool example\n\nYou can provide Claude with multiple tools to choose from in a single request. Here’s an example with both a `get_weather` and a `get_time` tool, along with a user query that asks for both.\n\nIn this case, Claude will most likely try to use two separate tools, one at a time — `get_weather` and then `get_time` — in order to fully answer the user’s question. However, it will also occasionally output two `tool_use` blocks at once, particularly if they are not dependent on each other. You would need to execute each tool and return their results in separate `tool_result` blocks within a single `user` message.\n\nMissing information\n\nIf the user’s prompt doesn’t include enough information to fill all the required parameters for a tool, Claude 3 Opus is much more likely to recognize that a parameter is missing and ask for it. Claude 3 Sonnet may ask, especially when prompted to think before outputting a tool request. But it may also do its best to infer a reasonable value.\n\nFor example, using the `get_weather` tool above, if you ask Claude “What’s the weather?” without specifying a location, Claude, particularly Claude 3 Sonnet, may make a guess about tools inputs:\n\nJSON\n\n```JSON\n{\n  \"type\": \"tool_use\",\n  \"id\": \"toolu_01A09q90qw90lq917835lq9\",\n  \"name\": \"get_weather\",\n  \"input\": {\"location\": \"New York, NY\", \"unit\": \"fahrenheit\"}\n}\n```\n\nThis behavior is not guaranteed, especially for more ambiguous prompts and for models less intelligent than Claude 3 Opus. If Claude 3 Opus doesn’t have enough context to fill in the required parameters, it is far more likely respond with a clarifying question instead of making a tool call.\n\nSequential tools\n\nSome tasks may require calling multiple tools in sequence, using the output of one tool as the input to another. In such a case, Claude will call one tool at a time. If prompted to call the tools all at once, Claude is likely to guess parameters for tools further downstream if they are dependent on tool results for tools further upstream.\n\nHere’s an example of using a `get_location` tool to get the user’s location, then passing that location to the `get_weather` tool:\n\nIn this case, Claude would first call the `get_location` tool to get the user’s location. After you return the location in a `tool_result`, Claude would then call `get_weather` with that location to get the final answer.\n\nThe full conversation might look like:\n\n| Role | Content |\n| --- | --- |\n| User | What’s the weather like where I am? |\n| Assistant | <thinking\\>To answer this, I first need to determine the user’s location using the get\\_location tool. Then I can pass that location to the get\\_weather tool to find the current weather there.</thinking\\>\\[Tool use for get\\_location\\] |\n| User | \\[Tool result for get\\_location with matching id and result of San Francisco, CA\\] |\n| Assistant | \\[Tool use for get\\_weather with the following input\\]{ “location”: “San Francisco, CA”, “unit”: “fahrenheit” } |\n| User | \\[Tool result for get\\_weather with matching id and result of “59°F (15°C), mostly cloudy”\\] |\n| Assistant | Based on your current location in San Francisco, CA, the weather right now is 59°F (15°C) and mostly cloudy. It’s a fairly cool and overcast day in the city. You may want to bring a light jacket if you’re heading outside. |\n\nThis example demonstrates how Claude can chain together multiple tool calls to answer a question that requires gathering data from different sources. The key steps are:\n\n1.  Claude first realizes it needs the user’s location to answer the weather question, so it calls the `get_location` tool.\n2.  The user (i.e. the client code) executes the actual `get_location` function and returns the result “San Francisco, CA” in a `tool_result` block.\n3.  With the location now known, Claude proceeds to call the `get_weather` tool, passing in “San Francisco, CA” as the `location` parameter (as well as a guessed `unit` parameter, as `unit` is not a required parameter).\n4.  The user again executes the actual `get_weather` function with the provided arguments and returns the weather data in another `tool_result` block.\n5.  Finally, Claude incorporates the weather data into a natural language response to the original question.\n\nChain of thought tool use\n\nBy default, Claude 3 Opus is prompted to think before it answers a tool use query to best determine whether a tool is necessary, which tool to use, and the appropriate parameters. Claude 3 Sonnet and Claude 3 Haiku are prompted to try to use tools as much as possible and are more likely to call an unnecessary tool or infer missing parameters. To prompt Sonnet or Haiku to better assess the user query before making tool calls, the following prompt can be used:\n\nChain of thought prompt\n\n`Answer the user's request using relevant tools (if they are available). Before calling a tool, do some analysis within \\<thinking>\\</thinking> tags. First, think about which of the provided tools is the relevant tool to answer the user's request. Second, go through each of the required parameters of the relevant tool and determine if the user has directly provided or given enough information to infer a value. When deciding if the parameter can be inferred, carefully consider all the context to see if it supports a specific value. If all of the required parameters are present or can be reasonably inferred, close the thinking tag and proceed with the tool call. BUT, if one of the values for a required parameter is missing, DO NOT invoke the function (not even with fillers for the missing params) and instead, ask the user to provide the missing parameters. DO NOT ask for more information on optional parameters if it is not provided.     `\n\nJSON mode\n\nYou can use tools to get Claude produce JSON output that follows a schema, even if you don’t have any intention of running that output through a tool or function.\n\nWhen using tools in this way:\n\n*   You usually want to provide a **single** tool\n*   You should set `tool_choice` (see [Forcing tool use](https://docs.anthropic.com/en/docs/tool-use#forcing-tool-use)) to instruct the model to explicitly use that tool\n*   Remember that the model will pass the `input` to the tool, so the name of the tool and description should be from the model’s perspective.\n\nThe following uses a `record_summary` tool to describe an image following a particular format.\n\n* * *\n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#pricing)\n\nPricing\n--------------------------------------------------------------------------------\n\nTool use requests are priced the same as any other Claude API request, based on the total number of input tokens sent to the model (including in the `tools` parameter) and the number of output tokens generated.”\n\nThe additional tokens from tool use come from:\n\n*   The `tools` parameter in API requests (tool names, descriptions, and schemas)\n*   `tool_use` content blocks in API requests and responses\n*   `tool_result` content blocks in API requests\n\nWhen you use `tools`, we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above):\n\n| Model | Tool choice | Tool use system prompt token count |\n| --- | --- | --- |\n| Claude 3.5 Sonnet (Oct) | `auto`\n* * *\n\n`any`, `tool` | 346 tokens\n\n* * *\n\n313 tokens |\n| Claude 3 Opus | `auto`\n\n* * *\n\n`any`, `tool` | 530 tokens\n\n* * *\n\n281 tokens |\n| Claude 3 Sonnet | `auto`\n\n* * *\n\n`any`, `tool` | 159 tokens\n\n* * *\n\n235 tokens |\n| Claude 3 Haiku | `auto`\n\n* * *\n\n`any`, `tool` | 264 tokens\n\n* * *\n\n340 tokens |\n| Claude 3.5 Sonnet (June) | `auto`\n\n* * *\n\n`any`, `tool` | 294 tokens\n\n* * *\n\n261 tokens |\n\nThese token counts are added to your normal input and output tokens to calculate the total cost of a request. Refer to our [models overview table](https://docs.anthropic.com/en/docs/models-overview#model-comparison) for current per-model prices.\n\nWhen you send a tool use prompt, just like any other API request, the response will output both input and output token counts as part of the reported `usage` metrics.\n\n* * *\n\n[​](https://docs.anthropic.com/claude/docs/tool-use-examples#next-steps)\n\nNext Steps\n--------------------------------------------------------------------------------------\n\nExplore our repository of ready-to-implement tool use code examples in our cookbooks:\n\n[Calculator Tool --------------- Learn how to integrate a simple calculator tool with Claude for precise numerical computations.](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/calculator_tool.ipynb)[Customer Service Agent ---------------------- Build a responsive customer service bot that leverages client-side tools to enhance support.](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/customer_service_agent.ipynb)[JSON Extractor -------------- See how Claude and tool use can extract structured data from unstructured text.](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/extracting_structured_json.ipynb)\n\nWas this page helpful?\n\nYesNo\n\n[Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)[Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/build-with-claude/mcp)\n\n[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)\n\nOn this page\n\n*   [How tool use works](https://docs.anthropic.com/claude/docs/tool-use-examples#how-tool-use-works)\n*   [How to implement tool use](https://docs.anthropic.com/claude/docs/tool-use-examples#how-to-implement-tool-use)\n*   [Choosing a model](https://docs.anthropic.com/claude/docs/tool-use-examples#choosing-a-model)\n*   [Specifying tools](https://docs.anthropic.com/claude/docs/tool-use-examples#specifying-tools)\n*   [Tool use system prompt](https://docs.anthropic.com/claude/docs/tool-use-examples#tool-use-system-prompt)\n*   [Best practices for tool definitions](https://docs.anthropic.com/claude/docs/tool-use-examples#best-practices-for-tool-definitions)\n*   [Controlling Claude’s output](https://docs.anthropic.com/claude/docs/tool-use-examples#controlling-claudes-output)\n*   [Forcing tool use](https://docs.anthropic.com/claude/docs/tool-use-examples#forcing-tool-use)\n*   [JSON output](https://docs.anthropic.com/claude/docs/tool-use-examples#json-output)\n*   [Chain of thought](https://docs.anthropic.com/claude/docs/tool-use-examples#chain-of-thought)\n*   [Disabling parallel tool use](https://docs.anthropic.com/claude/docs/tool-use-examples#disabling-parallel-tool-use)\n*   [Handling tool use and tool result content blocks](https://docs.anthropic.com/claude/docs/tool-use-examples#handling-tool-use-and-tool-result-content-blocks)\n*   [Troubleshooting errors](https://docs.anthropic.com/claude/docs/tool-use-examples#troubleshooting-errors)\n*   [Tool use examples](https://docs.anthropic.com/claude/docs/tool-use-examples#tool-use-examples)\n*   [Pricing](https://docs.anthropic.com/claude/docs/tool-use-examples#pricing)\n*   [Next Steps](https://docs.anthropic.com/claude/docs/tool-use-examples#next-steps)",
  "usage": {
    "tokens": 8317
  }
}
```
