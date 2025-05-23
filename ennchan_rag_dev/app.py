"""
Example application demonstrating the use of the ennchan_rag module.

This script shows how to use the RAG system to answer a question,
and measures the runtime of the operation.
"""

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