from src.modelLoader import vector_store, llm
from src.docsLoader import load_documents
from src.QAModel import QAModel
from src.configLoader import prompt_source, context_scope


def inquire(question, model):
    # Execute chat
    answer = model.graph.invoke({"question": question})
    return answer["answer"]


# Load docs
load_documents(vector_store)
model = QAModel(
    llm=llm,
    vector_store=vector_store,
    prompt_source=prompt_source,
    context_scope=context_scope
    )

question = "Who was Jesus Christ?"
answer = inquire(question, model)
print(answer)