# Ennchan Search

A robust search module designed to support RAG (Retrieval-Augmented Generation) systems with efficient web content retrieval and processing.

## Overview

Ennchan Search is a component of the Ennchan RAG system that handles:
- Web search queries via the Brave Search API
- Content extraction from web pages
- Parallel processing of search results
- Error handling with automatic retries

## Features

- **Robust Error Handling**: Comprehensive exception handling with exponential backoff retries
- **Parallel Processing**: Concurrent extraction of content from multiple URLs
- **Content Extraction**: Intelligent parsing of HTML to extract meaningful content
- **Clean API**: Simple interface for integration with other systems

## Installation

```bash
# Clone the repository
git clone https://github.com/ecinauce/ennchan-search01.git
cd ennchan-search01

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install -e ".[dev]"
```

## Configuration

Create a `config.json` file:

```json
{
    "BRAVE_API_KEY": "your_api_key",
    "USER_AGENT": "your_user_agent"
}
```

## Usage

```python
from ennchan_search import search

# Simple search
results = search("quantum computing")

# With custom configuration
config = {
    "BRAVE_API_KEY": "your_api_key"
}
results = search("quantum computing", config)

# Process results
for result in results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Content snippet: {result['content'][:100]}...")
    print()
```

## System Requirements

- Python >= 3.8
- Internet connection for search functionality

## Project Structure

```
ennchan_search/
├── core/           # Core search functionality
├── extractor/      # Content extraction utilities
└── utils/          # Helper functions and utilities
```

## Testing

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Uses [Brave Search](https://brave.com/search/) for web queries
- Built to support the Ennchan RAG system