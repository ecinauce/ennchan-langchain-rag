# Move this to a config file
print("Loading configuration...")
import os, json
from src.fallbackClass import FallbackLoader

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(os.path.dirname(script_dir), "config.json")
try:
    with open(config_path, "r") as f:
        config = json.load(f)
except FileNotFoundError:
    print(f"Configuration file not found at {config_path}.")
    exit(1)

os.environ["BRAVE_API_KEY"] = config["BRAVE_API_KEY"]
os.environ["USER_AGENT"] = config["USER_AGENT"]
os.environ["LANGSMITH_TRACING"] = config["LANGSMITH_TRACING"]
os.environ["LANGSMITH_API_KEY"] = config["LANGSMITH_API_KEY"]
os.environ["HUGGINGFACEHUB_API_TOKEN"] = config["HUGGINGFACEHUB_API_TOKEN"]

quantization = FallbackLoader.load(config["quantization"], False)
model_name = FallbackLoader.load(config["model_name"],"deepseek-ai/DeepSeek-R1-Distill-Llama-8B")
embeddings_model = FallbackLoader.load(config["embeddings_model"], "sentence-transformers/all-MiniLM-L6-v2")
docs_source = FallbackLoader.load(config["docs_source"], "https://en.wikipedia.org/wiki/World_War_II")
prompt_source = FallbackLoader.load(config["prompt_source"], "rlm/rag-prompt")
context_scope = FallbackLoader.load(config["context_scope"], 1000)