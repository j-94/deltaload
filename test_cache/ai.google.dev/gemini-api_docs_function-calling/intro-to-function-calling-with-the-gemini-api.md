---
title: Intro to function calling with the Gemini API
description: 
url: https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..
timestamp: 2025-01-20T16:18:54.946Z
domain: ai.google.dev
path: gemini-api_docs_function-calling
---

# Intro to function calling with the Gemini API



## Content

*   [Models](https://ai.google.dev/gemini-api/docs)
    *   [Gemini API docs](https://ai.google.dev/gemini-api/docs)
    *   [API Reference](https://ai.google.dev/api)
    *   [SDKs](https://ai.google.dev/gemini-api/docs/sdks)
    *   [Pricing](https://ai.google.dev/pricing)
    *   [Cookbook](https://github.com/google-gemini/cookbook)
*   Solutions
*   Code assistance
*   Showcase
*   Community

*   [Overview](https://ai.google.dev/gemini-api/docs)
*   Get started
    
*   [Quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
*   [API keys](https://ai.google.dev/gemini-api/docs/api-key)
*   [Libraries](https://ai.google.dev/gemini-api/docs/downloads)
*   [Release notes](https://ai.google.dev/gemini-api/docs/changelog)
*   [Developer forum](https://discuss.ai.google.dev/c/gemini-api/)
*   Models
    
*   [Gemini](https://ai.google.dev/gemini-api/docs/models/gemini)

*   [Experimental models](https://ai.google.dev/gemini-api/docs/models/experimental-models)
*   Capabilities
    
*   [Text generation](https://ai.google.dev/gemini-api/docs/text-generation)
*   [Vision](https://ai.google.dev/gemini-api/docs/vision)
*   [Audio understanding](https://ai.google.dev/gemini-api/docs/audio)
*   [Long context](https://ai.google.dev/gemini-api/docs/long-context)
*   [Code execution](https://ai.google.dev/gemini-api/docs/code-execution)
*   [Structured output](https://ai.google.dev/gemini-api/docs/structured-output)

*   [Document understanding](https://ai.google.dev/gemini-api/docs/document-processing)

*   [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings)
*   Guides
    
*   [Context caching](https://ai.google.dev/gemini-api/docs/caching)

*   [Token counting](https://ai.google.dev/gemini-api/docs/tokens)
*   [OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai)
*   [Billing info](https://ai.google.dev/gemini-api/docs/billing)

*   Gemini for Research
    
*   [Gemini Academic Program](https://ai.google.dev/gemini-api/docs/gemini-for-research)
*   Use cases
    

*   Troubleshooting
    
*   [API troubleshooting](https://ai.google.dev/gemini-api/docs/troubleshooting)
*   [AI Studio troubleshooting](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio)
*   [Google Workspace](https://ai.google.dev/gemini-api/docs/workspace)
*   [Request more quota](https://ai.google.dev/gemini-api/docs/quota)
*   Legal
    
*   [Terms of service](https://ai.google.dev/gemini-api/terms)
*   [Available regions](https://ai.google.dev/gemini-api/docs/available-regions)
*   [Abuse monitoring](https://ai.google.dev/gemini-api/docs/abuse-monitoring)

Using the Gemini API function calling feature, you can provide custom function definitions to the model. The model doesn't directly invoke these functions, but instead generates structured output that specifies a function name and suggested arguments. You can then use the function name and arguments to call an external API, and you can incorporate the resulting API output into a further query to the model, enabling the model to provide a more comprehensive response and take additional actions.

Function calling empowers users to interact with real-time information and services like databases, customer relationship management systems, and document repositories. The feature also enhances the model's ability to provide relevant and contextual answers. Function calling is best for interacting with external systems. If your use case requires the model to perform computation but doesn't involve external systems or APIs, you should consider using [code execution](https://ai.google.dev/gemini-api/docs/code-execution) instead.

For a working example of function calling, see the ["light bot" notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Function_calling_config.ipynb).

How function calling works
--------------------------

You use the function calling feature by adding structured query data describing programing interfaces, called _function declarations_, to a model prompt. The function declarations provide the name of the API function, explain its purpose, any parameters it supports, and descriptions of those parameters. After you pass a list of function declarations in a query to the model, it analyzes function declarations and the rest of the query to determine how to use the declared API in response to the request.

The model then returns an object in an [OpenAPI compatible schema](https://spec.openapis.org/oas/v3.0.3#schema) specifying how to call one or more of the declared functions in order to respond to the user's question. You can then take the recommended function call parameters, call the actual API, get a response, and provide that response to the user or take further action. Note that the model doesn't actually call the declared functions. Instead, you use the returned schema object parameters to call the function. The Gemini API also supports parallel function calling, where the model recommends multiple API function calls based on a single request.

Function declarations
---------------------

When you implement function calling in a prompt, you create a `tools` object, which contains one or more _`function declarations`_. You define functions using JSON, specifically with a [select subset](https://ai.google.dev/api/caching#schema) of the [OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schemawr) format. A single function declaration can include the following parameters:

*   **`name`** (string): The unique identifier for the function within the API call.
*   **`description`** (string): A comprehensive explanation of the function's purpose and capabilities.
*   **`parameters`** (object): Defines the input data required by the function.
    *   **`type`** (string): Specifies the overall data type, such as `object`.
    *   **`properties`** (object): Lists individual parameters, each with:
        *   **`type`** (string): The data type of the parameter, such as `string`, `integer`, `boolean`.
        *   **`description`** (string): A clear explanation of the parameter's purpose and expected format.
    *   **`required`** (array): An array of strings listing the parameter names that are mandatory for the function to operate.

For code examples of a function declaration using cURL commands, see the [Function calling examples](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#function-calling-curl-samples). For examples of creating function declarations using the Gemini API SDKs, see the [Function calling tutorial](https://ai.google.dev/gemini-api/docs/function-calling/tutorial).

### Best practices for function declarations

Accurately defining your functions is essential when integrating them into your requests. Each function relies on specific parameters that guide its behavior and interaction with the model. The following listing provides guidance on defining the parameters of an individual function in a `functions_declarations` array.

*   **`name`**: Use clear, descriptive names without space, period (`.`), or dash (`-`) characters. Instead, use underscore (`_`) characters or camel case.
    
*   **`description`**: Provide detailed, clear, and specific function descriptions, providing examples if necessary. For example, instead of `find theaters`, use ```
    find theaters based on location and optionally movie
    title that is currently playing in theaters.
    ``` Avoid overly broad or ambiguous descriptions.
    
*   **`properties` \> `type`**: Use strongly typed parameters to reduce model hallucinations. For example, if the parameter values are from a finite set, use an `enum` field instead of listing the values in the description (e.g., `"type": "enum", "values": ["now_playing", "upcoming"]`). If the parameter value is always an integer, set the type to `integer` rather than `number`.
    
*   **`properties` \> `description`**: Provide concrete examples and constraints. For example, instead of `the location to search`, use ```
    The city and state,
    e.g. San Francisco, CA or a zip code e.g. 95616
    ```.
    

For more best practices when using function calling, see the [Best Practices](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#best-practices) section.

Function calling mode
---------------------

You can use the function calling _`mode`_ parameter to modify the execution behavior of the feature. There are three modes available:

*   **`AUTO`**: The default model behavior. The model decides to predict either a function call or a natural language response.
*   **`ANY`**: The model is constrained to always predict a function call. If `allowed_function_names` is _not_ provided, the model picks from all of the available function declarations. If `allowed_function_names` _is_ provided, the model picks from the set of allowed functions.
*   **`NONE`**: The model won't predict a function call. In this case, the model behavior is the same as if you don't pass any function declarations.

The usage of the `ANY` mode ("forced function calling") is supported for **`Gemini 1.5 Pro`** and **`Gemini 1.5 Flash`** models only.

You can also pass a set of `allowed_function_names` that, when provided, limits the functions that the model will call. You should only include `allowed_function_names` when the mode is `ANY`. Function names should match function declaration names. With the mode set to `ANY` and the `allowed_function_names` set, the model will predict a function call from the set of function names provided.

The following code snippet from an [example request](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#single-turn-using-mode-and-allowed-functions) shows how to set the `mode` to `ANY` and specify a list of allowed functions:

```
"tool_config": {
  "function_calling_config": {
    "mode": "ANY",
    "allowed_function_names": ["find_theaters", "get_showtimes"]
  },
}
```

Function calling examples
-------------------------

This section provides example prompts for function calling using cURL commands. The examples include single turn and multiple-turn scenarios, and enabling different function calling modes.

When using cURL commands with this feature, the function and parameter information is included in the `tools` element. Each function declaration in the `tools` element contains the function name, and you specify the parameters using an [OpenAPI compatible schema](https://spec.openapis.org/oas/v3.0.3#schema), and a function description.

### Single-turn example

Single-turn is when you call the language model one time. With function calling, a single-turn use case might be when you provide the model a natural language query and a list of functions. In this case, the model uses the function declaration, which includes the function name, parameters, and description, to predict which function to call and the arguments to call it with.

The following curl sample is an example of passing in a description of a function that returns information about where a movie is playing. Several function declarations are included in the request, such as `find_movies` and `find_theaters`.

#### Single-turn function calling example request

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\_KEY \\
  -H 'Content-Type: application/json' \\
  -d '{
    "contents": {
      "role": "user",
      "parts": {
        "text": "Which theaters in Mountain View show Barbie movie?"
    }
  },
  "tools": \[
    {
      "function\_declarations": \[
        {
          "name": "find\_movies",
          "description": "find movie titles currently playing in theaters based on any description, genre, title words, etc.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "description": {
                "type": "string",
                "description": "Any kind of description including category or genre, title words, attributes, etc."
              }
            },
            "required": \[
              "description"
            \]
          }
        },
        {
          "name": "find\_theaters",
          "description": "find theaters based on location and optionally movie title which is currently playing in theaters",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              }
            },
            "required": \[
              "location"
            \]
          }
        },
        {
          "name": "get\_showtimes",
          "description": "Find the start times for movies playing in a specific theater",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              },
              "theater": {
                "type": "string",
                "description": "Name of the theater"
              },
              "date": {
                "type": "string",
                "description": "Date for requested showtime"
              }
            },
            "required": \[
              "location",
              "movie",
              "theater",
              "date"
            \]
          }
        }
      \]
    }
  \]
}'
    

The response to this curl example might be similar to the following.

#### Single-turn function calling curl example response

\[{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "functionCall": {
              "name": "find\_theaters",
              "args": {
                "movie": "Barbie",
                "location": "Mountain View, CA"
              }
            }
          }
        \]
      },
      "finishReason": "STOP",
      "safetyRatings": \[
        {
          "category": "HARM\_CATEGORY\_HARASSMENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HATE\_SPEECH",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
          "probability": "NEGLIGIBLE"
        }
      \]
    }
  \],
  "usageMetadata": {
    "promptTokenCount": 9,
    "totalTokenCount": 9
  }
}\]
    

### Single-turn example using ANY mode

The following curl example is similar to the [single-turn example](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#function-calling-single-turn-curl-sample), but it sets the [mode](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#function_calling_mode) to `ANY`:

```
"tool_config": {
  "function_calling_config": {
    "mode": "ANY"
  },
}
```

#### Single-turn function calling using ANY mode (request)

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\_KEY \\
  -H 'Content-Type: application/json' \\
  -d '{
    "contents": {
      "role": "user",
      "parts": {
        "text": "What movies are showing in North Seattle tonight?"
    }
  },
  "tools": \[
    {
      "function\_declarations": \[
        {
          "name": "find\_movies",
          "description": "find movie titles currently playing in theaters based on any description, genre, title words, etc.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "description": {
                "type": "string",
                "description": "Any kind of description including category or genre, title words, attributes, etc."
              }
            },
            "required": \[
              "description"
            \]
          }
        },
        {
          "name": "find\_theaters",
          "description": "find theaters based on location and optionally movie title which is currently playing in theaters",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              }
            },
            "required": \[
              "location"
            \]
          }
        },
        {
          "name": "get\_showtimes",
          "description": "Find the start times for movies playing in a specific theater",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              },
              "theater": {
                "type": "string",
                "description": "Name of the theater"
              },
              "date": {
                "type": "string",
                "description": "Date for requested showtime"
              }
            },
            "required": \[
              "location",
              "movie",
              "theater",
              "date"
            \]
          }
        }
      \]
    }
  \],
  "tool\_config": {
    "function\_calling\_config": {
      "mode": "ANY"
    },
  }
}'
    

The response might be similar to the following:

#### Single-turn function calling using ANY mode (response)

{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "functionCall": {
              "name": "find\_movies",
              "args": {
                "description": "",
                "location": "North Seattle, WA"
              }
            }
          }
        \],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0,
      "safetyRatings": \[
        {
          "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HARASSMENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HATE\_SPEECH",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
          "probability": "NEGLIGIBLE"
        }
      \]
    }
  \],
  "promptFeedback": {
    "safetyRatings": \[
      {
        "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_HATE\_SPEECH",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_HARASSMENT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
        "probability": "NEGLIGIBLE"
      }
    \]
  }
}
    

### Single-turn example using ANY mode and allowed functions

The following curl example is similar to the [single-turn example](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#function-calling-single-turn-curl-sample), but it sets the [mode](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#function_calling_mode) to `ANY` and includes a list of allowed functions:

```
"tool_config": {
  "function_calling_config": {
    "mode": "ANY",
    "allowed_function_names": ["find_theaters", "get_showtimes"]
  },
}
```

#### Single-turn function calling using ANY mode and allowed functions (request)

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\_KEY \\
  -H 'Content-Type: application/json' \\
  -d '{
    "contents": {
      "role": "user",
      "parts": {
        "text": "What movies are showing in North Seattle tonight?"
    }
  },
  "tools": \[
    {
      "function\_declarations": \[
        {
          "name": "find\_movies",
          "description": "find movie titles currently playing in theaters based on any description, genre, title words, etc.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "description": {
                "type": "string",
                "description": "Any kind of description including category or genre, title words, attributes, etc."
              }
            },
            "required": \[
              "description"
            \]
          }
        },
        {
          "name": "find\_theaters",
          "description": "find theaters based on location and optionally movie title which is currently playing in theaters",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              }
            },
            "required": \[
              "location"
            \]
          }
        },
        {
          "name": "get\_showtimes",
          "description": "Find the start times for movies playing in a specific theater",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              },
              "theater": {
                "type": "string",
                "description": "Name of the theater"
              },
              "date": {
                "type": "string",
                "description": "Date for requested showtime"
              }
            },
            "required": \[
              "location",
              "movie",
              "theater",
              "date"
            \]
          }
        }
      \]
    }
  \],
  "tool\_config": {
    "function\_calling\_config": {
      "mode": "ANY",
      "allowed\_function\_names": \["find\_theaters", "get\_showtimes"\]
    },
  }
}'
    

The model can't predict the `find_movies` function, because it's not on the list of allowed functions, so it predicts a different function instead. The response might be similar to the following:

#### Single-turn function calling using ANY mode and allowed functions (response)

{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "functionCall": {
              "name": "find\_theaters",
              "args": {
                "location": "North Seattle, WA",
                "movie": null
              }
            }
          }
        \],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0,
      "safetyRatings": \[
        {
          "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HARASSMENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HATE\_SPEECH",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
          "probability": "NEGLIGIBLE"
        }
      \]
    }
  \],
  "promptFeedback": {
    "safetyRatings": \[
      {
        "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_HATE\_SPEECH",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_HARASSMENT",
        "probability": "NEGLIGIBLE"
      },
      {
        "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
        "probability": "NEGLIGIBLE"
      }
    \]
  }
}
    

### Multi-turn examples

You can implement a multi-turn function calling scenario by doing the following:

1.  Get a function call response by calling the language model. This is the first turn.
2.  Call the language model using the function call response from the first turn and the function response you get from calling that function. This is the second turn.

The response from the second turn either summarizes the results to answer your query in the first turn, or contains a second function call you can use to get more information for your query.

This topic includes two multi-turn curl examples:

*   [Curl example that uses a function response from a previous turn](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#multi-turn-example-1)
*   [Curl example that calls a language model multiple times](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#multi-turn-example-2)

#### Use a response from a previous turn

The following curl sample calls the function and arguments returned by the previous single-turn example to get a response. The method and parameters returned by the single-turn example are in this JSON.

```
"functionCall": {
  "name": "find_theaters",
  "args": {
    "movie": "Barbie",
    "location": "Mountain View, CA"
  }
}
```

#### Multi-turn function calling curl example request

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\_KEY \\
  -H 'Content-Type: application/json' \\
  -d '{
    "contents": \[{
      "role": "user",
      "parts": \[{
        "text": "Which theaters in Mountain View show Barbie movie?"
    }\]
  }, {
    "role": "model",
    "parts": \[{
      "functionCall": {
        "name": "find\_theaters",
        "args": {
          "location": "Mountain View, CA",
          "movie": "Barbie"
        }
      }
    }\]
  }, {
    "role": "user",
    "parts": \[{
      "functionResponse": {
        "name": "find\_theaters",
        "response": {
          "name": "find\_theaters",
          "content": {
            "movie": "Barbie",
            "theaters": \[{
              "name": "AMC Mountain View 16",
              "address": "2000 W El Camino Real, Mountain View, CA 94040"
            }, {
              "name": "Regal Edwards 14",
              "address": "245 Castro St, Mountain View, CA 94040"
            }\]
          }
        }
      }
    }\]
  }\],
  "tools": \[{
    "functionDeclarations": \[{
      "name": "find\_movies",
      "description": "find movie titles currently playing in theaters based on any description, genre, title words, etc.",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "description": {
            "type": "STRING",
            "description": "Any kind of description including category or genre, title words, attributes, etc."
          }
        },
        "required": \["description"\]
      }
    }, {
      "name": "find\_theaters",
      "description": "find theaters based on location and optionally movie title which is currently playing in theaters",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "movie": {
            "type": "STRING",
            "description": "Any movie title"
          }
        },
        "required": \["location"\]
      }
    }, {
      "name": "get\_showtimes",
      "description": "Find the start times for movies playing in a specific theater",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "movie": {
            "type": "STRING",
            "description": "Any movie title"
          },
          "theater": {
            "type": "STRING",
            "description": "Name of the theater"
          },
          "date": {
            "type": "STRING",
            "description": "Date for requested showtime"
          }
        },
        "required": \["location", "movie", "theater", "date"\]
      }
    }\]
  }\]
}'
    

The response to this curl example includes the result of calling the `find_theaters` method. The response might be similar to the following:

#### Multi-turn function calling curl example response

{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "text": " OK. Barbie is showing in two theaters in Mountain View, CA: AMC Mountain View 16 and Regal Edwards 14."
          }
        \]
      }
    }
  \],
  "usageMetadata": {
    "promptTokenCount": 9,
    "candidatesTokenCount": 27,
    "totalTokenCount": 36
  }
}
    

#### Call the model multiple times

The following cURL example calls the generative AI model multiple times to call a function. Each time the model calls the function, it can use a different function to answer a different user query in the request.

#### Multi-turn function calling curl example request

curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\_KEY \\
  -H 'Content-Type: application/json' \\
  -d '{
    "contents": \[{
      "role": "user",
      "parts": \[{
        "text": "Which theaters in Mountain View show Barbie movie?"
    }\]
  }, {
    "role": "model",
    "parts": \[{
      "functionCall": {
        "name": "find\_theaters",
        "args": {
          "location": "Mountain View, CA",
          "movie": "Barbie"
        }
      }
    }\]
  }, {
    "role": "user",
    "parts": \[{
      "functionResponse": {
        "name": "find\_theaters",
        "response": {
          "name": "find\_theaters",
          "content": {
            "movie": "Barbie",
            "theaters": \[{
              "name": "AMC Mountain View 16",
              "address": "2000 W El Camino Real, Mountain View, CA 94040"
            }, {
              "name": "Regal Edwards 14",
              "address": "245 Castro St, Mountain View, CA 94040"
            }\]
          }
        }
      }
    }\]
  },
  {
    "role": "model",
    "parts": \[{
      "text": " OK. Barbie is showing in two theaters in Mountain View, CA: AMC Mountain View 16 and Regal Edwards 14."
    }\]
  },{
    "role": "user",
    "parts": \[{
      "text": "Can we recommend some comedy movies on show in Mountain View?"
    }\]
  }\],
  "tools": \[{
    "functionDeclarations": \[{
      "name": "find\_movies",
      "description": "find movie titles currently playing in theaters based on any description, genre, title words, etc.",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "description": {
            "type": "STRING",
            "description": "Any kind of description including category or genre, title words, attributes, etc."
          }
        },
        "required": \["description"\]
      }
    }, {
      "name": "find\_theaters",
      "description": "find theaters based on location and optionally movie title which is currently playing in theaters",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "movie": {
            "type": "STRING",
            "description": "Any movie title"
          }
        },
        "required": \["location"\]
      }
    }, {
      "name": "get\_showtimes",
      "description": "Find the start times for movies playing in a specific theater",
      "parameters": {
        "type": "OBJECT",
        "properties": {
          "location": {
            "type": "STRING",
            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
          },
          "movie": {
            "type": "STRING",
            "description": "Any movie title"
          },
          "theater": {
            "type": "STRING",
            "description": "Name of the theater"
          },
          "date": {
            "type": "STRING",
            "description": "Date for requested showtime"
          }
        },
        "required": \["location", "movie", "theater", "date"\]
      }
    }\]
  }\]
}'
    

#### Multi-turn function calling curl example response

\[{
  "candidates": \[
    {
      "content": {
        "parts": \[
          {
            "functionCall": {
              "name": "find\_movies",
              "args": {
                "description": "comedy",
                "location": "Mountain View, CA"
              }
            }
          }
        \]
      },
      "finishReason": "STOP",
      "safetyRatings": \[
        {
          "category": "HARM\_CATEGORY\_HARASSMENT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_HATE\_SPEECH",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_SEXUALLY\_EXPLICIT",
          "probability": "NEGLIGIBLE"
        },
        {
          "category": "HARM\_CATEGORY\_DANGEROUS\_CONTENT",
          "probability": "NEGLIGIBLE"
        }
      \]
    }
  \],
  "usageMetadata": {
    "promptTokenCount": 48,
    "totalTokenCount": 48
  }
}
\]
    

Best practices
--------------

Follow these best practices to improve the accuracy and reliability of your function calls.

### User prompt

For best results, prepend the user query with the following details:

*   Additional context for the model. For example, ```
    You are a movie API assistant
    to help users find movies and showtimes based on their preferences.
    ```
*   Details or instructions on how and when to use the functions. For example, `Don't make assumptions on showtimes. Always use a future date for showtimes.`
*   Instructions to ask clarifying questions if user queries are ambiguous. For example, ```
    Ask clarifying questions if not enough information is available to
    complete the request.
    ```

### Sampling parameters

For the temperature parameter, use `0` or another low value. This instructs the model to generate more confident results and reduces hallucinations.

### API invocation

If the model proposes the invocation of a function that would send an order, update a database, or otherwise have significant consequences, validate the function call with the user before executing it.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-11 UTC.

## Metadata

```json
{
  "title": "Intro to function calling with the Gemini API",
  "description": "",
  "url": "https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..",
  "content": "*   [Models](https://ai.google.dev/gemini-api/docs)\n    *   [Gemini API docs](https://ai.google.dev/gemini-api/docs)\n    *   [API Reference](https://ai.google.dev/api)\n    *   [SDKs](https://ai.google.dev/gemini-api/docs/sdks)\n    *   [Pricing](https://ai.google.dev/pricing)\n    *   [Cookbook](https://github.com/google-gemini/cookbook)\n*   Solutions\n*   Code assistance\n*   Showcase\n*   Community\n\n*   [Overview](https://ai.google.dev/gemini-api/docs)\n*   Get started\n    \n*   [Quickstart](https://ai.google.dev/gemini-api/docs/quickstart)\n*   [API keys](https://ai.google.dev/gemini-api/docs/api-key)\n*   [Libraries](https://ai.google.dev/gemini-api/docs/downloads)\n*   [Release notes](https://ai.google.dev/gemini-api/docs/changelog)\n*   [Developer forum](https://discuss.ai.google.dev/c/gemini-api/)\n*   Models\n    \n*   [Gemini](https://ai.google.dev/gemini-api/docs/models/gemini)\n\n*   [Experimental models](https://ai.google.dev/gemini-api/docs/models/experimental-models)\n*   Capabilities\n    \n*   [Text generation](https://ai.google.dev/gemini-api/docs/text-generation)\n*   [Vision](https://ai.google.dev/gemini-api/docs/vision)\n*   [Audio understanding](https://ai.google.dev/gemini-api/docs/audio)\n*   [Long context](https://ai.google.dev/gemini-api/docs/long-context)\n*   [Code execution](https://ai.google.dev/gemini-api/docs/code-execution)\n*   [Structured output](https://ai.google.dev/gemini-api/docs/structured-output)\n\n*   [Document understanding](https://ai.google.dev/gemini-api/docs/document-processing)\n\n*   [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings)\n*   Guides\n    \n*   [Context caching](https://ai.google.dev/gemini-api/docs/caching)\n\n*   [Token counting](https://ai.google.dev/gemini-api/docs/tokens)\n*   [OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai)\n*   [Billing info](https://ai.google.dev/gemini-api/docs/billing)\n\n*   Gemini for Research\n    \n*   [Gemini Academic Program](https://ai.google.dev/gemini-api/docs/gemini-for-research)\n*   Use cases\n    \n\n*   Troubleshooting\n    \n*   [API troubleshooting](https://ai.google.dev/gemini-api/docs/troubleshooting)\n*   [AI Studio troubleshooting](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio)\n*   [Google Workspace](https://ai.google.dev/gemini-api/docs/workspace)\n*   [Request more quota](https://ai.google.dev/gemini-api/docs/quota)\n*   Legal\n    \n*   [Terms of service](https://ai.google.dev/gemini-api/terms)\n*   [Available regions](https://ai.google.dev/gemini-api/docs/available-regions)\n*   [Abuse monitoring](https://ai.google.dev/gemini-api/docs/abuse-monitoring)\n\nUsing the Gemini API function calling feature, you can provide custom function definitions to the model. The model doesn't directly invoke these functions, but instead generates structured output that specifies a function name and suggested arguments. You can then use the function name and arguments to call an external API, and you can incorporate the resulting API output into a further query to the model, enabling the model to provide a more comprehensive response and take additional actions.\n\nFunction calling empowers users to interact with real-time information and services like databases, customer relationship management systems, and document repositories. The feature also enhances the model's ability to provide relevant and contextual answers. Function calling is best for interacting with external systems. If your use case requires the model to perform computation but doesn't involve external systems or APIs, you should consider using [code execution](https://ai.google.dev/gemini-api/docs/code-execution) instead.\n\nFor a working example of function calling, see the [\"light bot\" notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Function_calling_config.ipynb).\n\nHow function calling works\n--------------------------\n\nYou use the function calling feature by adding structured query data describing programing interfaces, called _function declarations_, to a model prompt. The function declarations provide the name of the API function, explain its purpose, any parameters it supports, and descriptions of those parameters. After you pass a list of function declarations in a query to the model, it analyzes function declarations and the rest of the query to determine how to use the declared API in response to the request.\n\nThe model then returns an object in an [OpenAPI compatible schema](https://spec.openapis.org/oas/v3.0.3#schema) specifying how to call one or more of the declared functions in order to respond to the user's question. You can then take the recommended function call parameters, call the actual API, get a response, and provide that response to the user or take further action. Note that the model doesn't actually call the declared functions. Instead, you use the returned schema object parameters to call the function. The Gemini API also supports parallel function calling, where the model recommends multiple API function calls based on a single request.\n\nFunction declarations\n---------------------\n\nWhen you implement function calling in a prompt, you create a `tools` object, which contains one or more _`function declarations`_. You define functions using JSON, specifically with a [select subset](https://ai.google.dev/api/caching#schema) of the [OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schemawr) format. A single function declaration can include the following parameters:\n\n*   **`name`** (string): The unique identifier for the function within the API call.\n*   **`description`** (string): A comprehensive explanation of the function's purpose and capabilities.\n*   **`parameters`** (object): Defines the input data required by the function.\n    *   **`type`** (string): Specifies the overall data type, such as `object`.\n    *   **`properties`** (object): Lists individual parameters, each with:\n        *   **`type`** (string): The data type of the parameter, such as `string`, `integer`, `boolean`.\n        *   **`description`** (string): A clear explanation of the parameter's purpose and expected format.\n    *   **`required`** (array): An array of strings listing the parameter names that are mandatory for the function to operate.\n\nFor code examples of a function declaration using cURL commands, see the [Function calling examples](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#function-calling-curl-samples). For examples of creating function declarations using the Gemini API SDKs, see the [Function calling tutorial](https://ai.google.dev/gemini-api/docs/function-calling/tutorial).\n\n### Best practices for function declarations\n\nAccurately defining your functions is essential when integrating them into your requests. Each function relies on specific parameters that guide its behavior and interaction with the model. The following listing provides guidance on defining the parameters of an individual function in a `functions_declarations` array.\n\n*   **`name`**: Use clear, descriptive names without space, period (`.`), or dash (`-`) characters. Instead, use underscore (`_`) characters or camel case.\n    \n*   **`description`**: Provide detailed, clear, and specific function descriptions, providing examples if necessary. For example, instead of `find theaters`, use ```\n    find theaters based on location and optionally movie\n    title that is currently playing in theaters.\n    ``` Avoid overly broad or ambiguous descriptions.\n    \n*   **`properties` \\> `type`**: Use strongly typed parameters to reduce model hallucinations. For example, if the parameter values are from a finite set, use an `enum` field instead of listing the values in the description (e.g., `\"type\": \"enum\", \"values\": [\"now_playing\", \"upcoming\"]`). If the parameter value is always an integer, set the type to `integer` rather than `number`.\n    \n*   **`properties` \\> `description`**: Provide concrete examples and constraints. For example, instead of `the location to search`, use ```\n    The city and state,\n    e.g. San Francisco, CA or a zip code e.g. 95616\n    ```.\n    \n\nFor more best practices when using function calling, see the [Best Practices](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#best-practices) section.\n\nFunction calling mode\n---------------------\n\nYou can use the function calling _`mode`_ parameter to modify the execution behavior of the feature. There are three modes available:\n\n*   **`AUTO`**: The default model behavior. The model decides to predict either a function call or a natural language response.\n*   **`ANY`**: The model is constrained to always predict a function call. If `allowed_function_names` is _not_ provided, the model picks from all of the available function declarations. If `allowed_function_names` _is_ provided, the model picks from the set of allowed functions.\n*   **`NONE`**: The model won't predict a function call. In this case, the model behavior is the same as if you don't pass any function declarations.\n\nThe usage of the `ANY` mode (\"forced function calling\") is supported for **`Gemini 1.5 Pro`** and **`Gemini 1.5 Flash`** models only.\n\nYou can also pass a set of `allowed_function_names` that, when provided, limits the functions that the model will call. You should only include `allowed_function_names` when the mode is `ANY`. Function names should match function declaration names. With the mode set to `ANY` and the `allowed_function_names` set, the model will predict a function call from the set of function names provided.\n\nThe following code snippet from an [example request](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#single-turn-using-mode-and-allowed-functions) shows how to set the `mode` to `ANY` and specify a list of allowed functions:\n\n```\n\"tool_config\": {\n  \"function_calling_config\": {\n    \"mode\": \"ANY\",\n    \"allowed_function_names\": [\"find_theaters\", \"get_showtimes\"]\n  },\n}\n```\n\nFunction calling examples\n-------------------------\n\nThis section provides example prompts for function calling using cURL commands. The examples include single turn and multiple-turn scenarios, and enabling different function calling modes.\n\nWhen using cURL commands with this feature, the function and parameter information is included in the `tools` element. Each function declaration in the `tools` element contains the function name, and you specify the parameters using an [OpenAPI compatible schema](https://spec.openapis.org/oas/v3.0.3#schema), and a function description.\n\n### Single-turn example\n\nSingle-turn is when you call the language model one time. With function calling, a single-turn use case might be when you provide the model a natural language query and a list of functions. In this case, the model uses the function declaration, which includes the function name, parameters, and description, to predict which function to call and the arguments to call it with.\n\nThe following curl sample is an example of passing in a description of a function that returns information about where a movie is playing. Several function declarations are included in the request, such as `find_movies` and `find_theaters`.\n\n#### Single-turn function calling example request\n\ncurl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\\_KEY \\\\\n  -H 'Content-Type: application/json' \\\\\n  -d '{\n    \"contents\": {\n      \"role\": \"user\",\n      \"parts\": {\n        \"text\": \"Which theaters in Mountain View show Barbie movie?\"\n    }\n  },\n  \"tools\": \\[\n    {\n      \"function\\_declarations\": \\[\n        {\n          \"name\": \"find\\_movies\",\n          \"description\": \"find movie titles currently playing in theaters based on any description, genre, title words, etc.\",\n          \"parameters\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"location\": {\n                \"type\": \"string\",\n                \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n              },\n              \"description\": {\n                \"type\": \"string\",\n                \"description\": \"Any kind of description including category or genre, title words, attributes, etc.\"\n              }\n            },\n            \"required\": \\[\n              \"description\"\n            \\]\n          }\n        },\n        {\n          \"name\": \"find\\_theaters\",\n          \"description\": \"find theaters based on location and optionally movie title which is currently playing in theaters\",\n          \"parameters\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"location\": {\n                \"type\": \"string\",\n                \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n              },\n              \"movie\": {\n                \"type\": \"string\",\n                \"description\": \"Any movie title\"\n              }\n            },\n            \"required\": \\[\n              \"location\"\n            \\]\n          }\n        },\n        {\n          \"name\": \"get\\_showtimes\",\n          \"description\": \"Find the start times for movies playing in a specific theater\",\n          \"parameters\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"location\": {\n                \"type\": \"string\",\n                \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n              },\n              \"movie\": {\n                \"type\": \"string\",\n                \"description\": \"Any movie title\"\n              },\n              \"theater\": {\n                \"type\": \"string\",\n                \"description\": \"Name of the theater\"\n              },\n              \"date\": {\n                \"type\": \"string\",\n                \"description\": \"Date for requested showtime\"\n              }\n            },\n            \"required\": \\[\n              \"location\",\n              \"movie\",\n              \"theater\",\n              \"date\"\n            \\]\n          }\n        }\n      \\]\n    }\n  \\]\n}'\n    \n\nThe response to this curl example might be similar to the following.\n\n#### Single-turn function calling curl example response\n\n\\[{\n  \"candidates\": \\[\n    {\n      \"content\": {\n        \"parts\": \\[\n          {\n            \"functionCall\": {\n              \"name\": \"find\\_theaters\",\n              \"args\": {\n                \"movie\": \"Barbie\",\n                \"location\": \"Mountain View, CA\"\n              }\n            }\n          }\n        \\]\n      },\n      \"finishReason\": \"STOP\",\n      \"safetyRatings\": \\[\n        {\n          \"category\": \"HARM\\_CATEGORY\\_HARASSMENT\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_HATE\\_SPEECH\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_SEXUALLY\\_EXPLICIT\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_DANGEROUS\\_CONTENT\",\n          \"probability\": \"NEGLIGIBLE\"\n        }\n      \\]\n    }\n  \\],\n  \"usageMetadata\": {\n    \"promptTokenCount\": 9,\n    \"totalTokenCount\": 9\n  }\n}\\]\n    \n\n### Single-turn example using ANY mode\n\nThe following curl example is similar to the [single-turn example](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#function-calling-single-turn-curl-sample), but it sets the [mode](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#function_calling_mode) to `ANY`:\n\n```\n\"tool_config\": {\n  \"function_calling_config\": {\n    \"mode\": \"ANY\"\n  },\n}\n```\n\n#### Single-turn function calling using ANY mode (request)\n\ncurl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\\_KEY \\\\\n  -H 'Content-Type: application/json' \\\\\n  -d '{\n    \"contents\": {\n      \"role\": \"user\",\n      \"parts\": {\n        \"text\": \"What movies are showing in North Seattle tonight?\"\n    }\n  },\n  \"tools\": \\[\n    {\n      \"function\\_declarations\": \\[\n        {\n          \"name\": \"find\\_movies\",\n          \"description\": \"find movie titles currently playing in theaters based on any description, genre, title words, etc.\",\n          \"parameters\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"location\": {\n                \"type\": \"string\",\n                \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n              },\n              \"description\": {\n                \"type\": \"string\",\n                \"description\": \"Any kind of description including category or genre, title words, attributes, etc.\"\n              }\n            },\n            \"required\": \\[\n              \"description\"\n            \\]\n          }\n        },\n        {\n          \"name\": \"find\\_theaters\",\n          \"description\": \"find theaters based on location and optionally movie title which is currently playing in theaters\",\n          \"parameters\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"location\": {\n                \"type\": \"string\",\n                \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n              },\n              \"movie\": {\n                \"type\": \"string\",\n                \"description\": \"Any movie title\"\n              }\n            },\n            \"required\": \\[\n              \"location\"\n            \\]\n          }\n        },\n        {\n          \"name\": \"get\\_showtimes\",\n          \"description\": \"Find the start times for movies playing in a specific theater\",\n          \"parameters\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"location\": {\n                \"type\": \"string\",\n                \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n              },\n              \"movie\": {\n                \"type\": \"string\",\n                \"description\": \"Any movie title\"\n              },\n              \"theater\": {\n                \"type\": \"string\",\n                \"description\": \"Name of the theater\"\n              },\n              \"date\": {\n                \"type\": \"string\",\n                \"description\": \"Date for requested showtime\"\n              }\n            },\n            \"required\": \\[\n              \"location\",\n              \"movie\",\n              \"theater\",\n              \"date\"\n            \\]\n          }\n        }\n      \\]\n    }\n  \\],\n  \"tool\\_config\": {\n    \"function\\_calling\\_config\": {\n      \"mode\": \"ANY\"\n    },\n  }\n}'\n    \n\nThe response might be similar to the following:\n\n#### Single-turn function calling using ANY mode (response)\n\n{\n  \"candidates\": \\[\n    {\n      \"content\": {\n        \"parts\": \\[\n          {\n            \"functionCall\": {\n              \"name\": \"find\\_movies\",\n              \"args\": {\n                \"description\": \"\",\n                \"location\": \"North Seattle, WA\"\n              }\n            }\n          }\n        \\],\n        \"role\": \"model\"\n      },\n      \"finishReason\": \"STOP\",\n      \"index\": 0,\n      \"safetyRatings\": \\[\n        {\n          \"category\": \"HARM\\_CATEGORY\\_DANGEROUS\\_CONTENT\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_HARASSMENT\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_HATE\\_SPEECH\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_SEXUALLY\\_EXPLICIT\",\n          \"probability\": \"NEGLIGIBLE\"\n        }\n      \\]\n    }\n  \\],\n  \"promptFeedback\": {\n    \"safetyRatings\": \\[\n      {\n        \"category\": \"HARM\\_CATEGORY\\_SEXUALLY\\_EXPLICIT\",\n        \"probability\": \"NEGLIGIBLE\"\n      },\n      {\n        \"category\": \"HARM\\_CATEGORY\\_HATE\\_SPEECH\",\n        \"probability\": \"NEGLIGIBLE\"\n      },\n      {\n        \"category\": \"HARM\\_CATEGORY\\_HARASSMENT\",\n        \"probability\": \"NEGLIGIBLE\"\n      },\n      {\n        \"category\": \"HARM\\_CATEGORY\\_DANGEROUS\\_CONTENT\",\n        \"probability\": \"NEGLIGIBLE\"\n      }\n    \\]\n  }\n}\n    \n\n### Single-turn example using ANY mode and allowed functions\n\nThe following curl example is similar to the [single-turn example](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#function-calling-single-turn-curl-sample), but it sets the [mode](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#function_calling_mode) to `ANY` and includes a list of allowed functions:\n\n```\n\"tool_config\": {\n  \"function_calling_config\": {\n    \"mode\": \"ANY\",\n    \"allowed_function_names\": [\"find_theaters\", \"get_showtimes\"]\n  },\n}\n```\n\n#### Single-turn function calling using ANY mode and allowed functions (request)\n\ncurl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\\_KEY \\\\\n  -H 'Content-Type: application/json' \\\\\n  -d '{\n    \"contents\": {\n      \"role\": \"user\",\n      \"parts\": {\n        \"text\": \"What movies are showing in North Seattle tonight?\"\n    }\n  },\n  \"tools\": \\[\n    {\n      \"function\\_declarations\": \\[\n        {\n          \"name\": \"find\\_movies\",\n          \"description\": \"find movie titles currently playing in theaters based on any description, genre, title words, etc.\",\n          \"parameters\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"location\": {\n                \"type\": \"string\",\n                \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n              },\n              \"description\": {\n                \"type\": \"string\",\n                \"description\": \"Any kind of description including category or genre, title words, attributes, etc.\"\n              }\n            },\n            \"required\": \\[\n              \"description\"\n            \\]\n          }\n        },\n        {\n          \"name\": \"find\\_theaters\",\n          \"description\": \"find theaters based on location and optionally movie title which is currently playing in theaters\",\n          \"parameters\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"location\": {\n                \"type\": \"string\",\n                \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n              },\n              \"movie\": {\n                \"type\": \"string\",\n                \"description\": \"Any movie title\"\n              }\n            },\n            \"required\": \\[\n              \"location\"\n            \\]\n          }\n        },\n        {\n          \"name\": \"get\\_showtimes\",\n          \"description\": \"Find the start times for movies playing in a specific theater\",\n          \"parameters\": {\n            \"type\": \"object\",\n            \"properties\": {\n              \"location\": {\n                \"type\": \"string\",\n                \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n              },\n              \"movie\": {\n                \"type\": \"string\",\n                \"description\": \"Any movie title\"\n              },\n              \"theater\": {\n                \"type\": \"string\",\n                \"description\": \"Name of the theater\"\n              },\n              \"date\": {\n                \"type\": \"string\",\n                \"description\": \"Date for requested showtime\"\n              }\n            },\n            \"required\": \\[\n              \"location\",\n              \"movie\",\n              \"theater\",\n              \"date\"\n            \\]\n          }\n        }\n      \\]\n    }\n  \\],\n  \"tool\\_config\": {\n    \"function\\_calling\\_config\": {\n      \"mode\": \"ANY\",\n      \"allowed\\_function\\_names\": \\[\"find\\_theaters\", \"get\\_showtimes\"\\]\n    },\n  }\n}'\n    \n\nThe model can't predict the `find_movies` function, because it's not on the list of allowed functions, so it predicts a different function instead. The response might be similar to the following:\n\n#### Single-turn function calling using ANY mode and allowed functions (response)\n\n{\n  \"candidates\": \\[\n    {\n      \"content\": {\n        \"parts\": \\[\n          {\n            \"functionCall\": {\n              \"name\": \"find\\_theaters\",\n              \"args\": {\n                \"location\": \"North Seattle, WA\",\n                \"movie\": null\n              }\n            }\n          }\n        \\],\n        \"role\": \"model\"\n      },\n      \"finishReason\": \"STOP\",\n      \"index\": 0,\n      \"safetyRatings\": \\[\n        {\n          \"category\": \"HARM\\_CATEGORY\\_SEXUALLY\\_EXPLICIT\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_HARASSMENT\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_HATE\\_SPEECH\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_DANGEROUS\\_CONTENT\",\n          \"probability\": \"NEGLIGIBLE\"\n        }\n      \\]\n    }\n  \\],\n  \"promptFeedback\": {\n    \"safetyRatings\": \\[\n      {\n        \"category\": \"HARM\\_CATEGORY\\_SEXUALLY\\_EXPLICIT\",\n        \"probability\": \"NEGLIGIBLE\"\n      },\n      {\n        \"category\": \"HARM\\_CATEGORY\\_HATE\\_SPEECH\",\n        \"probability\": \"NEGLIGIBLE\"\n      },\n      {\n        \"category\": \"HARM\\_CATEGORY\\_HARASSMENT\",\n        \"probability\": \"NEGLIGIBLE\"\n      },\n      {\n        \"category\": \"HARM\\_CATEGORY\\_DANGEROUS\\_CONTENT\",\n        \"probability\": \"NEGLIGIBLE\"\n      }\n    \\]\n  }\n}\n    \n\n### Multi-turn examples\n\nYou can implement a multi-turn function calling scenario by doing the following:\n\n1.  Get a function call response by calling the language model. This is the first turn.\n2.  Call the language model using the function call response from the first turn and the function response you get from calling that function. This is the second turn.\n\nThe response from the second turn either summarizes the results to answer your query in the first turn, or contains a second function call you can use to get more information for your query.\n\nThis topic includes two multi-turn curl examples:\n\n*   [Curl example that uses a function response from a previous turn](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#multi-turn-example-1)\n*   [Curl example that calls a language model multiple times](https://ai.google.dev/gemini-api/docs/function-calling?_gl=1*1pt6il2*_ga*MTI4NDAwNzIyNi4xNzMzODY0OTY1*_ga_P1DBVKWT6V*MTczNDAyMjIyMC44LjEuMTczNDAyMjYwMy42MC4wLjkxMjQyOTI0Mg..#multi-turn-example-2)\n\n#### Use a response from a previous turn\n\nThe following curl sample calls the function and arguments returned by the previous single-turn example to get a response. The method and parameters returned by the single-turn example are in this JSON.\n\n```\n\"functionCall\": {\n  \"name\": \"find_theaters\",\n  \"args\": {\n    \"movie\": \"Barbie\",\n    \"location\": \"Mountain View, CA\"\n  }\n}\n```\n\n#### Multi-turn function calling curl example request\n\ncurl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\\_KEY \\\\\n  -H 'Content-Type: application/json' \\\\\n  -d '{\n    \"contents\": \\[{\n      \"role\": \"user\",\n      \"parts\": \\[{\n        \"text\": \"Which theaters in Mountain View show Barbie movie?\"\n    }\\]\n  }, {\n    \"role\": \"model\",\n    \"parts\": \\[{\n      \"functionCall\": {\n        \"name\": \"find\\_theaters\",\n        \"args\": {\n          \"location\": \"Mountain View, CA\",\n          \"movie\": \"Barbie\"\n        }\n      }\n    }\\]\n  }, {\n    \"role\": \"user\",\n    \"parts\": \\[{\n      \"functionResponse\": {\n        \"name\": \"find\\_theaters\",\n        \"response\": {\n          \"name\": \"find\\_theaters\",\n          \"content\": {\n            \"movie\": \"Barbie\",\n            \"theaters\": \\[{\n              \"name\": \"AMC Mountain View 16\",\n              \"address\": \"2000 W El Camino Real, Mountain View, CA 94040\"\n            }, {\n              \"name\": \"Regal Edwards 14\",\n              \"address\": \"245 Castro St, Mountain View, CA 94040\"\n            }\\]\n          }\n        }\n      }\n    }\\]\n  }\\],\n  \"tools\": \\[{\n    \"functionDeclarations\": \\[{\n      \"name\": \"find\\_movies\",\n      \"description\": \"find movie titles currently playing in theaters based on any description, genre, title words, etc.\",\n      \"parameters\": {\n        \"type\": \"OBJECT\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"STRING\",\n            \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n          },\n          \"description\": {\n            \"type\": \"STRING\",\n            \"description\": \"Any kind of description including category or genre, title words, attributes, etc.\"\n          }\n        },\n        \"required\": \\[\"description\"\\]\n      }\n    }, {\n      \"name\": \"find\\_theaters\",\n      \"description\": \"find theaters based on location and optionally movie title which is currently playing in theaters\",\n      \"parameters\": {\n        \"type\": \"OBJECT\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"STRING\",\n            \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n          },\n          \"movie\": {\n            \"type\": \"STRING\",\n            \"description\": \"Any movie title\"\n          }\n        },\n        \"required\": \\[\"location\"\\]\n      }\n    }, {\n      \"name\": \"get\\_showtimes\",\n      \"description\": \"Find the start times for movies playing in a specific theater\",\n      \"parameters\": {\n        \"type\": \"OBJECT\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"STRING\",\n            \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n          },\n          \"movie\": {\n            \"type\": \"STRING\",\n            \"description\": \"Any movie title\"\n          },\n          \"theater\": {\n            \"type\": \"STRING\",\n            \"description\": \"Name of the theater\"\n          },\n          \"date\": {\n            \"type\": \"STRING\",\n            \"description\": \"Date for requested showtime\"\n          }\n        },\n        \"required\": \\[\"location\", \"movie\", \"theater\", \"date\"\\]\n      }\n    }\\]\n  }\\]\n}'\n    \n\nThe response to this curl example includes the result of calling the `find_theaters` method. The response might be similar to the following:\n\n#### Multi-turn function calling curl example response\n\n{\n  \"candidates\": \\[\n    {\n      \"content\": {\n        \"parts\": \\[\n          {\n            \"text\": \" OK. Barbie is showing in two theaters in Mountain View, CA: AMC Mountain View 16 and Regal Edwards 14.\"\n          }\n        \\]\n      }\n    }\n  \\],\n  \"usageMetadata\": {\n    \"promptTokenCount\": 9,\n    \"candidatesTokenCount\": 27,\n    \"totalTokenCount\": 36\n  }\n}\n    \n\n#### Call the model multiple times\n\nThe following cURL example calls the generative AI model multiple times to call a function. Each time the model calls the function, it can use a different function to answer a different user query in the request.\n\n#### Multi-turn function calling curl example request\n\ncurl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=$API\\_KEY \\\\\n  -H 'Content-Type: application/json' \\\\\n  -d '{\n    \"contents\": \\[{\n      \"role\": \"user\",\n      \"parts\": \\[{\n        \"text\": \"Which theaters in Mountain View show Barbie movie?\"\n    }\\]\n  }, {\n    \"role\": \"model\",\n    \"parts\": \\[{\n      \"functionCall\": {\n        \"name\": \"find\\_theaters\",\n        \"args\": {\n          \"location\": \"Mountain View, CA\",\n          \"movie\": \"Barbie\"\n        }\n      }\n    }\\]\n  }, {\n    \"role\": \"user\",\n    \"parts\": \\[{\n      \"functionResponse\": {\n        \"name\": \"find\\_theaters\",\n        \"response\": {\n          \"name\": \"find\\_theaters\",\n          \"content\": {\n            \"movie\": \"Barbie\",\n            \"theaters\": \\[{\n              \"name\": \"AMC Mountain View 16\",\n              \"address\": \"2000 W El Camino Real, Mountain View, CA 94040\"\n            }, {\n              \"name\": \"Regal Edwards 14\",\n              \"address\": \"245 Castro St, Mountain View, CA 94040\"\n            }\\]\n          }\n        }\n      }\n    }\\]\n  },\n  {\n    \"role\": \"model\",\n    \"parts\": \\[{\n      \"text\": \" OK. Barbie is showing in two theaters in Mountain View, CA: AMC Mountain View 16 and Regal Edwards 14.\"\n    }\\]\n  },{\n    \"role\": \"user\",\n    \"parts\": \\[{\n      \"text\": \"Can we recommend some comedy movies on show in Mountain View?\"\n    }\\]\n  }\\],\n  \"tools\": \\[{\n    \"functionDeclarations\": \\[{\n      \"name\": \"find\\_movies\",\n      \"description\": \"find movie titles currently playing in theaters based on any description, genre, title words, etc.\",\n      \"parameters\": {\n        \"type\": \"OBJECT\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"STRING\",\n            \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n          },\n          \"description\": {\n            \"type\": \"STRING\",\n            \"description\": \"Any kind of description including category or genre, title words, attributes, etc.\"\n          }\n        },\n        \"required\": \\[\"description\"\\]\n      }\n    }, {\n      \"name\": \"find\\_theaters\",\n      \"description\": \"find theaters based on location and optionally movie title which is currently playing in theaters\",\n      \"parameters\": {\n        \"type\": \"OBJECT\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"STRING\",\n            \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n          },\n          \"movie\": {\n            \"type\": \"STRING\",\n            \"description\": \"Any movie title\"\n          }\n        },\n        \"required\": \\[\"location\"\\]\n      }\n    }, {\n      \"name\": \"get\\_showtimes\",\n      \"description\": \"Find the start times for movies playing in a specific theater\",\n      \"parameters\": {\n        \"type\": \"OBJECT\",\n        \"properties\": {\n          \"location\": {\n            \"type\": \"STRING\",\n            \"description\": \"The city and state, e.g. San Francisco, CA or a zip code e.g. 95616\"\n          },\n          \"movie\": {\n            \"type\": \"STRING\",\n            \"description\": \"Any movie title\"\n          },\n          \"theater\": {\n            \"type\": \"STRING\",\n            \"description\": \"Name of the theater\"\n          },\n          \"date\": {\n            \"type\": \"STRING\",\n            \"description\": \"Date for requested showtime\"\n          }\n        },\n        \"required\": \\[\"location\", \"movie\", \"theater\", \"date\"\\]\n      }\n    }\\]\n  }\\]\n}'\n    \n\n#### Multi-turn function calling curl example response\n\n\\[{\n  \"candidates\": \\[\n    {\n      \"content\": {\n        \"parts\": \\[\n          {\n            \"functionCall\": {\n              \"name\": \"find\\_movies\",\n              \"args\": {\n                \"description\": \"comedy\",\n                \"location\": \"Mountain View, CA\"\n              }\n            }\n          }\n        \\]\n      },\n      \"finishReason\": \"STOP\",\n      \"safetyRatings\": \\[\n        {\n          \"category\": \"HARM\\_CATEGORY\\_HARASSMENT\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_HATE\\_SPEECH\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_SEXUALLY\\_EXPLICIT\",\n          \"probability\": \"NEGLIGIBLE\"\n        },\n        {\n          \"category\": \"HARM\\_CATEGORY\\_DANGEROUS\\_CONTENT\",\n          \"probability\": \"NEGLIGIBLE\"\n        }\n      \\]\n    }\n  \\],\n  \"usageMetadata\": {\n    \"promptTokenCount\": 48,\n    \"totalTokenCount\": 48\n  }\n}\n\\]\n    \n\nBest practices\n--------------\n\nFollow these best practices to improve the accuracy and reliability of your function calls.\n\n### User prompt\n\nFor best results, prepend the user query with the following details:\n\n*   Additional context for the model. For example, ```\n    You are a movie API assistant\n    to help users find movies and showtimes based on their preferences.\n    ```\n*   Details or instructions on how and when to use the functions. For example, `Don't make assumptions on showtimes. Always use a future date for showtimes.`\n*   Instructions to ask clarifying questions if user queries are ambiguous. For example, ```\n    Ask clarifying questions if not enough information is available to\n    complete the request.\n    ```\n\n### Sampling parameters\n\nFor the temperature parameter, use `0` or another low value. This instructs the model to generate more confident results and reduces hallucinations.\n\n### API invocation\n\nIf the model proposes the invocation of a function that would send an order, update a database, or otherwise have significant consequences, validate the function call with the user before executing it.\n\nExcept as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.\n\nLast updated 2024-12-11 UTC.",
  "usage": {
    "tokens": 9114
  }
}
```
