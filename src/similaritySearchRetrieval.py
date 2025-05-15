from src.interfaces import RetrievalStrategy

class SimilaritySearchRetrieval(RetrievalStrategy):
    """Retrieval strategy using vector similarity search."""
    
    def retrieve(self, query: str, vector_store):
        """Retrieve documents using similarity search."""
        return vector_store.similarity_search(query)
