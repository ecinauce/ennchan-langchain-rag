# from src.modelLoader import llm
# from src.memoryHandler import vector_store
# from src.docsLoader import load_documents
# from src.QAModel import QAModel
# from src.config import config  # Import the config object directly
# # from pprint import pprint as pr

# # from ennchan_search import search, load_config


# # load_config("config.json")
# # pr(search("World War II"))

# def inquire(question):
#     load_documents(vector_store)
#     model = QAModel(
#         llm=llm,
#         vector_store=vector_store,
#         prompt_source=config.prompt_source,  # Use config.prompt_source
#         context_scope=config.context_scope  # Use config.context_scope
#     )

#     # Execute chat
#     output = model.graph.invoke({"question": question})
#     return output["answer"]


# # Load docs
# inquiry = "Did Jesus write the 10 commandments?"
# answer = inquire(inquiry)
# print(answer)

from ennchan_rag import ask


# Load docs
inquiry = "What are the 3 laws of robotics?"
answer = ask(inquiry, "config.json")
print(answer)
