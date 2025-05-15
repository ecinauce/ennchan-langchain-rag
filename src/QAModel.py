
print("Invoking model...")
from langchain import hub
from langgraph.graph import START, StateGraph
from typing import Optional

from src.interfaces import LLMInterface, VectorStoreInterface, RetrievalStrategy
from src.modelState import State
from src.modelLoader import llm, vector_store
from src.configLoader import prompt_source, context_scope
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
    def retrieve(self, state: State):
        retrieved_docs = self.retrieval_strategy.retrieve(
            state["question"],
            self.vector_store
        ) # self.vector_store.similarity_search(state["question"])
        return {"context": retrieved_docs}


    def generate(self, state: State):
        max_chars = self.context_scope
        docs = state["context"]
        docs_content = ""

        for doc in docs:
            if len(doc.page_content) + len(docs_content) < max_chars:
                docs_content += doc.page_content + "\n\n"
            else:
                break

        if not docs_content and docs:
            docs_content = docs[0].page_content[:1000]

        # docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = self.prompt.invoke({"question": state["question"], "context": docs_content})
        response = self.llm.invoke(messages)

        return {"answer": response}
