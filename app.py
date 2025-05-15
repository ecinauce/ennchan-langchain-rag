from src.modelLoader import vector_store
from src.docsLoader import load_documents
from src.QAModel import QAModel


def inquire(question, model):
    # Execute chat
    answer = model.graph.invoke({"question": question})
    return answer["answer"]

# Load docs
load_documents(vector_store)
model = QAModel(vector_store=vector_store)

question = "Can you tell me in detail what Hitler's last moments were like?"
answer = inquire(question, model)
print(answer)