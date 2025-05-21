from ennchan_rag import ask
import time

start_time = time.time()
# Load docs
inquiry = "What's the story behind Niccolo Machiaveli's 'The Prince'?"
answer = ask(inquiry, "..\\config.json")
print(answer)
end_time = time.time()
runtime = end_time - start_time
print(f"Runtime: {runtime:.2f} seconds")