from src.interfaces import RetrievalStrategy
from langchain_core.documents import Document
from typing import List

class SimilaritySearchRetrieval(RetrievalStrategy):
    """Retrieval strategy using vector similarity search."""
    
    def retrieve(self, query: str, vector_store) -> List[Document]:
        """Retrieve documents using similarity search."""
        return vector_store.similarity_search(query)
