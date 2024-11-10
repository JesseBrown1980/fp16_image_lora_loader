# fp16_image_lora_loader/fp16_image_loader.py
import torch
import cv2
import numpy as np
import os

class FP16ImageLoader:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_path": ("STRING", {"default": "path/to/image.png"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "load_fp16_image"
    CATEGORY = "ImageProcessing"
    TITLE = "Load FP16 Image"

    def load_fp16_image(self, image_path):
        # Validate image path
        if not image_path or not os.path.isfile(image_path):
            print("Invalid image path.")
            return None

        # Load the image with OpenCV
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

        if image is None:
            print("Image could not be loaded.")
            return None

        # Convert to FP16 if necessary
        if image.dtype != np.float16:
            image = image.astype(np.float16) / 255.0  # Convert 8-bit to FP16

        # Convert from BGR to RGB if required by your model
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Convert to a torch tensor
        tensor_image = torch.from_numpy(image).permute(2, 0, 1).unsqueeze(0)  # CHW format for PyTorch

        # Ensure the tensor is in FP16 format for efficient processing
        tensor_image = tensor_image.to(torch.float16)

        return (tensor_image,)

NODE_CLASS_MAPPINGS = {
    "FP16ImageLoader": FP16ImageLoader,
}
