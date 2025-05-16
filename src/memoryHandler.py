from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from src.config import config


embeddings = HuggingFaceEmbeddings(model_name=config.embeddings_model)  # Use config.embeddings_model
vector_store = InMemoryVectorStore(embeddings)
