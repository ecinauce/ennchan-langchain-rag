# Ennchan RAG (Placeholder)

This is a placeholder implementation of the Ennchan RAG module. It provides the same API as the full implementation but returns simulated responses.

## Installation

```bash
pip install ennchan-rag

# USAGE

from ennchan_rag import inquire

## Simple usage
answer = inquire("What is artificial intelligence?")

## Using a config file
answer = inquire("What is artificial intelligence?", "config.json")

## Using a config dictionary
config = {
    "model_name": "mistralai/Mistral-7B-Instruct-v0.2",
    "docs_source": "https://en.wikipedia.org/wiki/Artificial_intelligence"
}
answer = inquire("What is artificial intelligence?", config)
