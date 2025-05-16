print("Loading model...")
from langchain_huggingface import HuggingFacePipeline
import torch

from src.config import config  # Import the config object directly
from src.quantizationHandler import load_quantization

p_quantization = load_quantization()

llm = HuggingFacePipeline.from_model_id(
    model_id=config.model_name,  # Use config.model_name
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.03,
        return_full_text=False,
    ),
    model_kwargs=p_quantization,
)