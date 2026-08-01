#!/usr/bin/env python3
"""Extract Word2Vec embeddings into a Keras Embedding layer."""
import tensorflow as tf


def gensim_to_keras(model):
    """
    Converts a trained gensim Word2Vec model to a trainable
    Keras Embedding layer.

    Args:
        model: A trained gensim Word2Vec model.

    Returns:
        A trainable tf.keras.layers.Embedding layer initialized
        with the Word2Vec vectors.
    """
    weights = model.wv.vectors

    embedding = tf.keras.layers.Embedding(
        input_dim=weights.shape[0],
        output_dim=weights.shape[1],
        trainable=True,
    )

    embedding.build((None,))
    embedding.set_weights([weights])

    return embedding
