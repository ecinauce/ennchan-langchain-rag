# src/configLoader.py
from src.config import config

# For backward compatibility, expose the config values as individual variables
USER_AGENT = config.USER_AGENT
LANGSMITH_TRACING = config.LANGSMITH_TRACING
LANGSMITH_API_KEY = config.LANGSMITH_API_KEY
HUGGINGFACEHUB_API_TOKEN = config.HUGGINGFACEHUB_API_TOKEN
model_name = config.model_name
embeddings_model = config.embeddings_model
quantization = config.quantization
docs_source = config.docs_source
prompt_source = config.prompt_source
context_scope = config.context_scope
