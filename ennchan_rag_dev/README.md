# Ennchan RAG

A locally-hosted chatbot that answers questions using information from the internet, designed for offline and resource-conscious environments.

## Overview

Ennchan RAG is a proof-of-concept Q&A system that:
- Processes user questions
- Searches the internet for relevant information
- Summarizes findings into coherent answers
- Runs entirely on local hardware

The project aims to provide a self-hosted alternative to cloud-based LLMs, offering more control over resources and avoiding service limitations.

## Features

- **Local Operation**: Runs entirely on your machine
- **Flexible Model Selection**: Choose your own LLM models
- **Intelligent Search**: Converts questions into optimized search queries
- **Advanced Retrieval**: Multiple strategies for context selection:
  - Semantic Search
  - Keyword Matching
  - Maximum Marginal Relevance (MMR)
  - Hybrid Approach
- **Performance Optimizations**:
  - Parallel content processing
  - Model caching
  - Automatic retries for network operations
  - Configurable quantization for GPU optimization

## Installation

```bash
# Clone the repository
git clone https://github.com/ecinauce/ennchan-rag01.git
cd ennchan-rag01

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install -r requirements.txt[dev]
```

## Configuration

Create a `config.json` file in the project root:

```json
{
    "BRAVE_API_KEY": "your_api_key",
    "USER_AGENT": "your_user_agent",
    "model_name": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
    "embeddings_model": "sentence-transformers/all-MiniLM-L6-v2",
    "quantization": true,
    "context_scope": 1000
}
```

## Usage

### Command Line Interface

```python
from ennchan_rag import ask

# Ask a question
answer = ask("What's the story behind Niccolo Machiaveli's 'The Prince'?")
print(answer)
```

### With Verbose Output

```bash
python app.py -v
```

## System Requirements

- Python >= 3.8
- CUDA-capable GPU (optional, for model quantization)
- Internet connection for search functionality

## Project Structure

```
ennchan_rag/
├── core/           # Core RAG functionality
├── loaders/        # Document loading utilities
├── retrievers/     # Retrieval strategies
└── utils/          # Helper functions and utilities
```

## Future Plans

- Web App API interface
- Additional search engine integrations
- Enhanced offline capabilities

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [LangChain](https://github.com/langchain-ai/langchain)
- Uses [Brave Search](https://brave.com/search/) for web queries
- Inspired by the need for accessible, offline LLM solutions