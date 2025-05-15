from abc import ABC, abstractmethod
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore
from langchain_community.document_loaders.base import BaseLoader
from typing import Any, Dict, List


class RetrievalStrategy(ABC):
    """Abstract base class for document retrieval strategies."""
    
    @abstractmethod
    def retrieve(self, query: str, vector_store: VectorStore) -> list[Document]:
        """Retrieve relevant documents based on the query."""
        pass


class LLMInterface(ABC):
    """Abstract base class for LLM interfaces."""
    
    @abstractmethod
    def invoke(self, messages: Any) -> Any:
        """Invoke the LLM with the given messages."""
        pass


class VectorStoreInterface(ABC):
    @abstractmethod
    def similarity_search(self, query: str) -> List[Any]:
        """Perform a similarity search in the vector store."""
        pass


class DocLoader(BaseLoader):
    """Abstract base class for document loaders."""
    
    @abstractmethod
    def load(self) -> Any:
        """Load documents from a web source."""
        pass