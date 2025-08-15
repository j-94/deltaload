FROM python:3.11-slim

WORKDIR /app

# Copy the repository content first
COPY . /app/

# Install the package in development mode and dependencies
RUN pip install --no-cache-dir "langgraph-cli[inmem]" && \
    pip install --no-cache-dir \
    langgraph>=0.2.55 \
    langchain-community>=0.3.9 \
    langchain-openai>=0.3.7 \
    langchain-anthropic>=0.3.9 \
    openai>=1.61.0 \
    tavily-python>=0.5.0 \
    langchain-groq>=0.2.4 \
    arxiv>=2.1.3 \
    pymupdf>=1.25.3 \
    xmltodict>=0.14.2 \
    linkup-sdk>=0.2.3 \
    duckduckgo-search>=3.0.0 \
    exa-py>=1.8.8 \
    requests>=2.32.3 \
    beautifulsoup4==4.13.3 \
    langchain-deepseek>=0.1.2 \
    python-dotenv==1.0.1

# Create a symlink for the open_deep_research package
RUN ln -s /app/src/open_deep_research /app/open_deep_research

# Create .env file with API keys
RUN echo "TAVILY_API_KEY=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" > .env

# Expose the LangGraph server port
EXPOSE 2024

# Start the LangGraph server
CMD ["langgraph", "dev", "--host", "0.0.0.0"]