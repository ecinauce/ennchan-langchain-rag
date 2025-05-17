from src.modelLoader import llm
from src.memoryHandler import vector_store
from src.docsLoader import load_documents
from src.QAModel import QAModel
from src.config import config  # Import the config object directly


def inquire(question):
    load_documents(vector_store)
    model = QAModel(
        llm=llm,
        vector_store=vector_store,
        prompt_source=config.prompt_source,  # Use config.prompt_source
        context_scope=config.context_scope  # Use config.context_scope
    )

    # Execute chat
    answer = model.graph.invoke({"question": question})
    return answer["answer"]


# Load docs
question = "Did Jesus write the 10 commandments?"
answer = inquire(question)
print(answer)
