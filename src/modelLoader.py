print("Loading model...")
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEmbeddings
from src.configLoader import model_name, embeddings_model, quantization

import torch
from src.quantizationLoader import quantization_config

p_quantization = {}
if quantization and torch.cuda.is_available():
    print("Loading quantized model...")
    from src.quantizationLoader import quantization_config
    p_quantization = {"quantization_config": quantization_config}
else:
    if quantization:
        print("Quantization requested but CUDA not available. My guy, either CUDA isn't installed or you're honestly too poor to run this thing. Here's the backup implementation. Good luck!")
    else:
        print("Loading full model...")

llm = HuggingFacePipeline.from_model_id(
    model_id=model_name,
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
        return_full_text=False,
    ),
    model_kwargs=p_quantization,
)

embeddings = HuggingFaceEmbeddings(model_name=embeddings_model)
vector_store = InMemoryVectorStore(embeddings)
