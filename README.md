# FP16 Image and LoRA Loader

This package provides separate classes for loading images in FP16 format and applying LoRA weights in FP16 to PyTorch models. It is designed for optimized performance when working with large images and deep learning models, especially on systems with limited memory.

## Features

- **FP16 Image Loader**: Load images as FP16 tensors compatible with PyTorch, reducing memory usage and improving processing speed.
- **LoRA Loader**: Load LoRA (Low-Rank Adaptation) weights in FP16 format and apply them to PyTorch models, useful for fine-tuning large models efficiently.

## Installation

To use this package, you need Python 3.7 or higher and pip installed on your system.

1. **Clone or Download the Repository**

   Clone this repository or download the code files to your local machine.

   ```bash
   git clone https://github.com/JesseBrown1980/fp16_image_lora_loader.git
   cd fp16_image_lora_loader
Build the Package

Open a terminal in the fp16_image_lora_loader directory and run the following command to build the package:

bash
Copy code
python setup.py sdist bdist_wheel
Install the Package Locally

After building, you can install the package by running:

bash
Copy code
pip install .
This will install the package and its dependencies (torch, opencv-python, numpy, and safetensors).

Usage
Once installed, you can import and use the FP16ImageLoader and LoRALoader classes in your Python code.

Loading an FP16 Image
Use the FP16ImageLoader to load an image in FP16 format as a PyTorch tensor:

python
Copy code
from fp16_image_lora_loader import FP16ImageLoader

# Initialize the image loader
image_loader = FP16ImageLoader()

# Load an image as an FP16 tensor
tensor_image = image_loader.load_fp16_image("path/to/your/image.png")

# tensor_image is now a PyTorch tensor in FP16 format
Make sure that the image path (path/to/your/image.png) is valid.

Loading LoRA Weights
Use the LoRALoader to load LoRA weights in FP16 format into a PyTorch model:

python
Copy code
from fp16_image_lora_loader import LoRALoader

# Initialize the LoRA loader
lora_loader = LoRALoader()

# Load the LoRA weights into the model
model = ...  # replace with your PyTorch model instance
lora_loader.load_lora_weights(model, "path/to/lora_weights.safetensors")

# The model now has LoRA weights applied in FP16 format
Ensure that the path to the LoRA weights file (path/to/lora_weights.safetensors) is valid.

Requirements
Python 3.7 or higher
torch (PyTorch)
opencv-python
numpy
safetensors
These dependencies are listed in the setup.py file and will be installed automatically.

Project Structure
fp16_image_loader.py: Contains the FP16ImageLoader class for loading images in FP16 format.
lora_loader.py: Contains the LoRALoader class for loading LoRA weights in FP16 format.
__init__.py: Imports both classes to make them accessible at the package level.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue to discuss what you would like to change.

Contact
For questions or further information, please contact:

Author: Jesse Daniel Brown
Email: plasmatoid@gmail.com
GitHub: JesseBrown1980
Linkedin: https://www.linkedin.com/in/jessedanielbrown1980/
ResearchGate: https://www.researchgate.net/profile/Jesse-Brown-21
