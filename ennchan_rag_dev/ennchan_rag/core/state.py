from typing_extensions import List, TypedDict, Optional, Dict
from langchain_core.documents import Document


# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str
    search_queries: Optional[List[str]]  # Added for query tracking
    search_results: Optional[List[Dict]]  # Added for raw search results
    processed_results: Optional[List[Dict]]  # Added for individual summaries
    reference_document: Optional[str]  # Added for compiled document

