from src.modelLoader import vector_store, llm
from src.docsLoader import load_documents
from src.QAModel import QAModel
from src.config import config  # Import the config object directly


def inquire(question, model):
    # Execute chat
    answer = model.graph.invoke({"question": question})
    return answer["answer"]


# Load docs
load_documents(vector_store)
model = QAModel(
    llm=llm,
    vector_store=vector_store,
    prompt_source=config.prompt_source,  # Use config.prompt_source
    context_scope=config.context_scope  # Use config.context_scope
    )

question = "What was Stalin's relationship with Hitler?"
answer = inquire(question, model)
print(answer)
