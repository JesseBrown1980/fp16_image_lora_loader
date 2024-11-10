# setup.py
from setuptools import setup, find_packages

setup(
    name="fp16_image_lora_loader",
    version="0.1.0",
    description="A package for loading FP16 images and LoRA weights for PyTorch models.",
    author="Jesse Daniel Brown",
    author_email="plasmatoid@gmail.com",
    url="https://github.com/JesseBrown1980/fp16_image_lora_loader",
    packages=find_packages(),
    install_requires=[
        "torch>=1.0.0",
        "opencv-python",
        "numpy",
        "safetensors"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
    keywords="fp16 image lora loader pytorch",
    python_requires=">=3.7",
)
