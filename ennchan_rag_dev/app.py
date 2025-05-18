from ennchan_rag.ask import ask


# Load docs
inquiry = "What are RAGs?"
answer = ask(inquiry, "..\\config.json")
print(answer)
