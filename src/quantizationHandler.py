import torch
from src.config import config
from src.quantizationLoader import quantization_config

def load_quantization():
    if config.quantization and torch.cuda.is_available():
        print("Loading quantized model...")
        from src.quantizationLoader import quantization_config
        return {"quantization_config": quantization_config}
    else:
        if config.quantization:
            print("Quantization requested but CUDA not available. My guy, either CUDA isn't installed or you're honestly too poor to run this thing. Here's the backup implementation. Good luck!")
        else:
            print("Loading full model...")
        return {}
