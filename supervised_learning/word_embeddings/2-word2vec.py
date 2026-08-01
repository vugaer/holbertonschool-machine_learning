#!/usr/bin/env python3
"""Train a Word2Vec model."""

from gensim.models import Word2Vec # import gensim


def word2vec_model(sentences, vector_size=100, min_count=5,
                   window=5, negative=5, cbow=True,
                   epochs=5, seed=0, workers=1):
    """
    Create, build and train a Word2Vec model.

    Args:
        sentences: list of tokenized sentences.
        vector_size: embedding dimension.
        min_count: minimum word frequency.
        window: context window size.
        negative: number of negative samples.
        cbow: True for CBOW, False for Skip-gram.
        epochs: number of training epochs.
        seed: random seed.
        workers: number of worker threads.

    Returns:
        Trained gensim Word2Vec model.
    """
    model = Word2Vec(
        vector_size=vector_size,
        min_count=min_count,
        window=window,
        negative=negative,
        sg=0 if cbow else 1,
        seed=seed,
        workers=workers,
    )

    model.build_vocab(sentences)

    model.train(
        sentences,
        total_examples=model.corpus_count,
        epochs=epochs,
    )

    return model
