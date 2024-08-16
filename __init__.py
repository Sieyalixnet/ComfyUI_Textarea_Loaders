from .lib import LoraLoaderText,CheckpointLoaderText

NODE_CLASS_MAPPINGS = {
    "LoRALoader_Text": LoraLoaderText,
    "CheckPointLoader_Text": CheckpointLoaderText
}

NODE_DISPLAY_NAMES_MAPPINGS = {
    "LoRALoader_Text": "LoRA Loader(Text)",
    "CheckPointLoader_Text": "Checkpoint Loader(Text)"
}

__all__ = ['NODE_CLASS_MAPPINGS']