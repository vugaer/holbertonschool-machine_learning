CNN From Scratch + LeNet-5 (NumPy & Keras)
Project Summary

This repository implements the fundamental building blocks of Convolutional Neural Networks (CNNs) from scratch using NumPy, including both forward and backward propagation, and extends this understanding by building a production-ready implementation of the LeNet-5 architecture using Keras.

The project is designed to bridge the gap between low-level mathematical operations and high-level deep learning frameworks.

Objectives
Implement convolution and pooling layers without using deep learning libraries
Derive and code backpropagation for CNN layers
Understand gradient flow and parameter updates
Build a classical CNN architecture (LeNet-5) using Keras
Strengthen deep learning system design intuition
    Implemented Modules
🔹 Convolutional Layer (Forward)
Manual convolution using sliding windows
Supports:
same and valid padding
arbitrary strides
multi-channel inputs and filters
Integrated activation pipeline
🔹 Pooling Layer (Forward)
Max Pooling
Average Pooling
Configurable kernel size and stride
🔹 Convolutional Backpropagation
Computes:
dA_prev (input gradients)
dW (filter gradients)
db (bias gradients)
Handles padding & stride correctly
Implements full gradient propagation pipeline
🔹 Pooling Backpropagation
Max pooling → gradient masking
Average pooling → gradient distribution
Channel-wise gradient handling
🔹 LeNet-5 (Keras Implementation)

A modernized implementation of LeNet-5 with:

He initialization (he_normal, seed=0)
ReLU activations
Adam optimizer
Architecture:
Input (28x28x1)
↓
Conv2D (6 filters, 5x5, same)
↓
MaxPool (2x2)
↓
Conv2D (16 filters, 5x5, valid)
↓
MaxPool (2x2)
↓
Dense (120)
↓
Dense (84)
↓
Dense (10, Softmax)
🧮 Core Concepts
Convolution as a linear operator
Padding strategies and output dimensionality
Stride impact on spatial resolution
Feature map generation
Gradient propagation in CNNs
Parameter sharing and locality
Pooling as downsampling
🛠 Tech Stack
Python
NumPy (low-level implementation)
TensorFlow / Keras (model building)

📁 Repository Structure
.
├── cnn/
│   ├── conv_forward.py
│   ├── conv_backward.py
│   ├── pool_forward.py
│   ├── pool_backward.py
│
├── models/
│   └── lenet5.py
│
└── README.md

Why This Project Matters

Most deep learning workflows rely heavily on frameworks like TensorFlow or PyTorch, abstracting away critical internal mechanics.

This project:

Exposes the mathematical foundations of CNNs
Demonstrates ability to implement backpropagation from scratch
Shows understanding beyond API-level usage
Highlights readiness for:
ML Engineering roles
Deep Learning research
Technical interviews


Potential Extensions
Add vectorized implementation (performance optimization)
Implement CNN training loop from scratch
Compare NumPy vs Keras performance
Extend to CIFAR-10 / real datasets
Add BatchNorm / Dropout layers
GPU acceleration (CuPy / PyTorch reimplementation)

Author
Fidan Baghirova AI / Machine Learning Engineer

Final Note

This repository is not just an implementation — it is a demonstration of deep understanding of neural network internals, which is critical for building scalable and efficient AI systems.