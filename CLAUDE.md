
Okay, here is a Python code block demonstrating how you could implement the Open Deep Research system within your deltaload project, using the programmatic approach outlined in the documentation you provided.

This example assumes:

You have followed the setup instructions (Docker running, .env file configured with API keys).

You have a way within your deltaload project to define or retrieve the data you want to research (e.g., summarizing recent bookmarks, analyzing specific GitHub repos from your list, etc.). This part is represented by a placeholder function get_topic_and_context_from_deltaload().

You'll run this Python script from an environment where it can connect to the Docker container (e.g., potentially within the deltaload project structure itself, ensuring network access to localhost:2024).

import asyncio
import uuid
import json # For potentially handling structured output

# Imports from Open Deep Research / LangGraph
# Ensure these packages are installed in your deltaload environment
# (potentially via requirements.txt or similar)
try:
    from langgraph.checkpoint.memory import MemorySaver
    from langgraph.errors import GraphRecursionError
    from langgraph.graph.graph import CompiledGraph # Specific import for type hinting if needed
    from langgraph.types import Command
    # Assuming 'open_deep_research' is importable because it's a submodule
    # or correctly added to the PYTHONPATH
    from open_deep_research.graph import builder
except ImportError as e:
    print(f"Import Error: {e}")
    print("Please ensure 'langgraph' and 'open_deep_research' components are installed and accessible.")
    # You might need to adjust PYTHONPATH or install dependencies
    exit(1)

# --- Placeholder for Deltaload Integration ---
def get_topic_and_context_from_deltaload():
    """
    Placeholder function to simulate getting research topic/context from deltaload.
    Replace this with your actual logic to interact with your bookmarks,
    twitter data, github readmes etc. managed by deltaload.
    """
    # Example: Maybe you want to research the latest trends in AI based on recent bookmarks
    # 1. Query your deltaload storage for bookmarks tagged 'AI' in the last month
    # 2. Extract key themes or URLs
    # 3. Formulate a research topic

    topic = "Emerging trends in Generative AI development tools based on recent GitHub READMEs and tech blogs"

    # You could potentially pass more structured context if needed,
    # although Open Deep Research primarily takes a 'topic' string.
    # context_data = [...] # List of URLs, summaries, etc.

    print(f"--- Deltaload: Generated Research Topic ---")
    print(topic)
    print("-" * 40)
    return topic
# --- End Placeholder ---

async def run_deep_research_with_deltaload_topic():
    """
    Runs the Open Deep Research graph with a topic derived from deltaload data.
    """
    print("--- Initializing Open Deep Research ---")
    # 1. Load the Open Deep Research graph
    # Uses in-memory saving for checkpoints in this example
    memory = MemorySaver()
    try:
        graph: CompiledGraph = builder.compile(checkpointer=memory)
        print("Graph compiled successfully.")
    except Exception as e:
        print(f"Error compiling graph: {e}")
        return

    # 2. Get the research topic from your deltaload data source
    topic = get_topic_and_context_from_deltaload()
    if not topic:
        print("Error: Could not determine research topic from deltaload data.")
        return

    # 3. Configure the research parameters (thread)
    # Adjust models, search tools, depth etc. based on your needs and API keys
    thread_id = str(uuid.uuid4())
    thread = {
        "configurable": {
            "thread_id": thread_id,
            "search_api": "tavily",      # Or "exa", "perplexity" - ensure you have the key in .env
            "planner_provider": "anthropic", # Or "openai", "groq"
            "planner_model": "claude-3-5-sonnet-latest", # Or "gpt-4o", specific Groq model etc.
            "writer_provider": "anthropic",
            "writer_model": "claude-3-5-sonnet-latest", # Use the strongest model available for writing
            "max_search_depth": 1,        # How many search cycles per section (1 is often sufficient)
            # Add other relevant configurations if needed
        }
    }
    print(f"Research Thread ID: {thread_id}")
    print(f"Configuration: {json.dumps(thread['configurable'], indent=2)}")
    print("-" * 40)

    # 4. Run the graph to get the research plan
    print("--- Starting Research - Generating Plan ---")
    final_report = None
    try:
        async for event in graph.astream({"topic": topic}, thread, stream_mode="updates"):
            # Print events to see the progress (planning stage)
            # The key event to look for signals the plan is ready for review
            print(f"Event: {event.keys()}") # Show which node/step is running
            # You would typically check the event data here to find the plan
            # and decide whether to approve or provide feedback.
            # For this example, we will automatically approve after the stream ends.
            # Look for the specific output structure that contains the plan.

        print("-" * 40)
        print("--- Plan Generation Phase Complete ---")
        # !!! IMPORTANT: Human Review Step Simulation !!!
        # In a real application, you would pause here, present the plan
        # (extracted from the 'event' stream above) to the user,
        # and get their feedback ("true" to approve, or text feedback).
        user_feedback = "true" # Simulating automatic approval
        print(f"Simulating User Feedback: '{user_feedback}'")
        print("-" * 40)

        # 5. Resume the graph to generate the report based on the plan
        print("--- Resuming Research - Generating Report ---")
        if user_feedback.lower() == "true":
            async for event in graph.astream(Command(resume=True), thread, stream_mode="values"):
                # stream_mode="values" returns the full state after each step
                print(f"Report Generation Step Output Keys: {event.keys()}")
                # The final report is typically under a key like 'report' or 'final_report'
                # in the output of the final node ('compile_report' or similar)
                if "final_report" in event:
                     final_report = event.get("final_report")
                     print("Final Report potentially found!")
                elif "report" in event: # Check alternative key
                     final_report = event.get("report")
                     print("Final Report potentially found!")


        else:
            # Handle feedback (This part needs more logic based on how ODR handles feedback)
            # async for event in graph.astream({"feedback": user_feedback}, thread):
            #     print(event)
            print("Feedback handling not fully implemented in this example.")

        print("-" * 40)
        print("--- Research Process Complete ---")

        # 6. Process the final report
        if final_report:
            print("\n--- Generated Report ---")
            print(final_report)
            # --- Deltaload Integration: Save/Use Report ---
            # Here you would save the report back into your deltaload system,
            # associate it with the source data, or trigger other workflows.
            # Example: save_report_to_deltaload(topic, final_report, thread_id)
            # --- End Deltaload Integration ---
        else:
            print("Error: Could not retrieve the final report from the graph state.")
            print("Check the event stream details and final graph state for potential issues.")
            # You might want to inspect the graph state for the last successful step
            # state = await graph.aget_state(thread)
            # print("Last graph state:", state)

    except GraphRecursionError:
        print("Error: Graph entered a loop. Check planning/feedback logic.")
    except Exception as e:
        print(f"An error occurred during the research process: {e}")
        # You might want to inspect the last known state
        try:
            state = await graph.aget_state(thread)
            print("Last known graph state:", state.values)
        except Exception as state_e:
            print(f"Could not retrieve graph state: {state_e}")


if __name__ == "__main__":
    # Ensure Docker container 'open-deep-research' is running on port 2024
    print("Starting Deltaload <> Open Deep Research Integration Script")
    print("Ensure the Open Deep Research Docker container is running via:")
    print("`docker-compose up -d open-deep-research` in the deltaload root.")
    print("Ensure localhost:2024 is accessible from where this script runs.")
    print("-" * 40)
    asyncio.run(run_deep_research_with_deltaload_topic())


Explanation and How to Use:

Placeholder Function: Replace the get_topic_and_context_from_deltaload() function with your actual code that interacts with your deltaload data sources (bookmarks, Twitter data, GitHub README content) to formulate a meaningful research topic.

Dependencies: Make sure langgraph and potentially other dependencies of open_deep_research are installed in the Python environment where you run this script. You might need to adjust your requirements.txt or pyproject.toml for the deltaload project.

Configuration (thread): Modify the configurable dictionary to select the specific LLMs (OpenAI, Anthropic, Groq) and search tools (Tavily, Exa, Perplexity) you want to use, ensuring you have the corresponding API keys in your env_files/open_deep_research.env. Choose models appropriate for planning and writing (e.g., stronger models like claude-3-5-sonnet-latest or gpt-4o are often better for writing).

Plan Review: The code currently simulates accepting the plan (user_feedback = "true"). In a real interactive application, you'd need to:

Parse the event stream during the first graph.astream call to extract the generated plan.

Present this plan to the user.

Wait for user input ("true" or feedback text).

Use that input to either resume (Command(resume=True)) or potentially send feedback (which requires understanding how the specific open_deep_research graph handles feedback messages).

Report Handling: The code attempts to find the final report in the event stream of the second astream call (keys final_report or report). Replace the comment # save_report_to_deltaload(...) with your logic to store or use the generated Markdown report within your deltaload system.

Error Handling: Basic error handling is included, but you might want to add more robust logging or state inspection if issues occur.

Run: Execute this Python script. It will connect to the running open-deep-research Docker container on localhost:2024, generate a topic (using the placeholder), run the research process, simulate plan approval, and print the final report.