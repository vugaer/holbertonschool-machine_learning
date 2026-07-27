# Autoencoders

This project covers the implementation of different types of autoencoders using TensorFlow/Keras as part of the Machine Learning curriculum.

## Learning Objectives

By completing this project, I learned:

* What an autoencoder is and how it works
* The architecture of encoder and decoder networks
* How latent space representations are learned
* The difference between vanilla, sparse, convolutional, and variational autoencoders
* How regularization can be applied to autoencoders
* How convolutional layers can be used for image reconstruction
* How variational autoencoders generate probabilistic latent representations

## Requirements

* Python 3.9+
* TensorFlow / Keras
* NumPy

## Tasks

### 0. Vanilla Autoencoder

Implemented a basic autoencoder consisting of:

* Encoder network
* Latent space representation
* Decoder network

The model is trained using binary cross-entropy loss and Adam optimization.

### 1. Sparse Autoencoder

Implemented a sparse autoencoder by applying L1 activity regularization on the latent representation to encourage sparse feature learning.

### 2. Convolutional Autoencoder

Implemented a convolutional autoencoder designed for image data using:

* Conv2D layers
* MaxPooling2D layers
* UpSampling2D layers

This architecture enables efficient image compression and reconstruction.

### 3. Variational Autoencoder (VAE)

Implemented a variational autoencoder that learns a probabilistic latent space using:

* Mean vector (μ)
* Log variance vector (log σ²)
* Reparameterization trick

The model can be used as a generative model capable of producing new samples from the learned latent distribution.

## Files

| File               | Description               |
| ------------------ | ------------------------- |
| 0-vanilla.py       | Vanilla autoencoder       |
| 1-sparse.py        | Sparse autoencoder        |
| 2-convolutional.py | Convolutional autoencoder |
| 3-variational.py   | Variational autoencoder   |

## Author

Fidan Baghirova