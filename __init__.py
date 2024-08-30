from .lib import LoraLoaderText,CheckpointLoaderText, EmptyLatentImageText,LoadImageText

NODE_CLASS_MAPPINGS = {
    "LoRALoader_Text": LoraLoaderText,
    "CheckPointLoader_Text": CheckpointLoaderText,
    "EmptyLatentImage_Text": EmptyLatentImageText,
    "LoadImage_Text": LoadImageText
}

NODE_DISPLAY_NAMES_MAPPINGS = {
    "LoRALoader_Text": "LoRA Loader(Text)",
    "CheckPointLoader_Text": "Checkpoint Loader(Text)",
    "EmptyLatentImage_Text": "Empty Latent Image(Text)",
    "LoadImage_Text": "Load Image(Text)"
}

__all__ = ['NODE_CLASS_MAPPINGS']