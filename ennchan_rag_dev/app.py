from ennchan_rag import ask


# Load docs
inquiry = "What are RAGs?"
answer = ask(inquiry, "..\\config.json")
print(answer)
