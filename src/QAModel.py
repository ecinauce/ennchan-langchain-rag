
print("Invoking model...")
from langchain import hub
from langchain_core.documents import Document
from langchain_huggingface import HuggingFacePipeline
from langgraph.graph import START, StateGraph
from typing import Optional, Dict

from src.contextProcessor import ContextProcessor
from src.interfaces import LLMInterface, VectorStoreInterface, RetrievalStrategy
from src.modelState import State
from src.modelLoader import llm
from src.memoryHandler import vector_store
from src.config import config  # Import the config object directly
from src.similaritySearchRetrieval import SimilaritySearchRetrieval


class QAModel:
    def __init__(self, 
                 llm: LLMInterface, 
                 vector_store: VectorStoreInterface, 
                 prompt_source: str,
                 context_scope: int,
                 retrieval_strategy: RetrievalStrategy = SimilaritySearchRetrieval()):
        self.prompt = hub.pull(prompt_source)
        self.context_scope = context_scope
        self.llm = llm
        self.vector_store = vector_store
        self.retrieval_strategy = retrieval_strategy

        # Compile application and test
        self.graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        self.graph_builder.add_edge(START, "retrieve")
        self.graph = self.graph_builder.compile()


    # Define application steps
    def retrieve(self, state: State) -> Dict[str, list[Document]]:
        query = state["question"]
        retrieved_docs = self.retrieval_strategy.retrieve(query, self.vector_store) 
        return {"context": retrieved_docs}


    def generate(self, state: State) -> Dict[str, HuggingFacePipeline]:
        context = ContextProcessor()
        messages = self.prompt.invoke({"question": state["question"], "context": context.process(state, self.context_scope)})
        response = self.llm.invoke(messages)

        return {"answer": response}
