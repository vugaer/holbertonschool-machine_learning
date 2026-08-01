#!/usr/bin/env python3
"""Word2Vec model."""

import gensim


def word2vec_model(sentences, vector_size=100, min_count=5,
                   window=5, negative=5, cbow=True,
                   epochs=5, seed=0, workers=1):
    """
    Creates and trains a Word2Vec model.

    Args:
        sentences: List of tokenized sentences.
        vector_size: Dimensionality of the word vectors.
        min_count: Minimum number of occurrences for a word.
        window: Maximum distance between the current and predicted word.
        negative: Number of negative samples.
        cbow: True for CBOW, False for Skip-gram.
        epochs: Number of training epochs.
        seed: Seed for the random number generator.
        workers: Number of worker threads.

    Returns:
        A trained gensim.models.Word2Vec model.
    """
    return gensim.models.Word2Vec(
        sentences=sentences,
        vector_size=vector_size,
        min_count=min_count,
        window=window,
        negative=negative,
        sg=0 if cbow else 1,
        epochs=epochs,
        seed=seed,
        workers=workers
    )
