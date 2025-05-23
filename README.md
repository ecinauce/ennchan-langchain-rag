# Ennchan LangChain RAG

A locally-hosted chatbot system that answers questions using information from the internet, designed for offline and resource-conscious environments.

## Project Components

This repository contains three main components:

### 1. [Ennchan RAG](./ennchan_rag_dev/)

The core RAG (Retrieval-Augmented Generation) module that:
- Processes user questions
- Integrates with search functionality
- Applies various retrieval strategies
- Generates answers using local LLM models

### 2. [Ennchan Search](./ennchan_search_dev/)

A robust search module that:
- Handles web search queries via the Brave Search API
- Extracts content from web pages
- Processes search results in parallel
- Implements error handling with automatic retries

### 3. [Ennchan Interface CMD](./ennchan_interface_cmd/)

A command-line interface that:
- Provides a user-friendly way to interact with the system
- Supports verbose mode for debugging
- Displays formatted responses with timing information

## Quick Start

```bash
# Clone the repository
git clone https://github.com/ecinauce/ennchan-langchain-rag.git
cd ennchan-langchain-rag

# Install dependencies for all modules
pip install -r ennchan_rag_dev/requirements.txt
pip install -r ennchan_search_dev/requirements.txt

# Create a config.json file in the root directory
# (See configuration section in the module READMEs)

# Run the command-line interface
python -m ennchan_interface_cmd.app
```

## Features

- **Fully Local Operation**: Runs entirely on your machine
- **Flexible Model Selection**: Choose your own LLM models
- **Multiple Retrieval Strategies**: Semantic search, keyword matching, MMR, and hybrid approaches
- **Performance Optimizations**: Parallel processing, model caching, and automatic retries
- **Robust Error Handling**: Comprehensive exception handling throughout the system

## System Requirements

- Python >= 3.8
- CUDA-capable GPU (optional, for model quantization)
- Internet connection for search functionality

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [LangChain](https://github.com/langchain-ai/langchain)
- Uses [Brave Search](https://brave.com/search/) for web queries
- Inspired by the need for accessible, offline LLM solutions