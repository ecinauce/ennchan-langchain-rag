from abc import ABC, abstractmethod

class RetrievalStrategy(ABC):
    """Abstract base class for document retrieval strategies."""
    
    @abstractmethod
    def retrieve(self, query: str, vector_store):
        """Retrieve relevant documents based on the query."""
        pass
