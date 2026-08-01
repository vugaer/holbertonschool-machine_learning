#!/usr/bin/env python3
"""Load and prepare translation datasets."""

import tensorflow as tf
import transformers
from setup import load_pt2en


class Dataset:
    """Prepare datasets and train subword tokenizers."""

    def __init__(self, batch_size, max_len):
        """Initialize datasets and processing pipeline."""
        self.data_train = load_pt2en('train')
        self.data_valid = load_pt2en('validation')

        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train
        )

        self.data_train = self.data_train.map(self.tf_encode)
        self.data_valid = self.data_valid.map(self.tf_encode)

        self.data_train = (
            self.data_train
            .filter(lambda pt, en: self.filter_max_length(
                pt, en, max_len
            ))
            .cache()
            .shuffle(20000)
            .padded_batch(batch_size)
            .prefetch(tf.data.experimental.AUTOTUNE)
        )

        self.data_valid = (
            self.data_valid
            .filter(lambda pt, en: self.filter_max_length(
                pt, en, max_len
            ))
            .padded_batch(batch_size)
        )

    def tokenize_dataset(self, data):
        """Train tokenizers from translation pairs."""

        def pt_iterator():
            for pt, _ in data:
                yield pt.numpy().decode("utf-8")

        def en_iterator():
            for _, en in data:
                yield en.numpy().decode("utf-8")

        tokenizer_pt = transformers.AutoTokenizer.from_pretrained(
            "neuralmind/bert-base-portuguese-cased"
        )
        tokenizer_en = transformers.AutoTokenizer.from_pretrained(
            "bert-base-uncased"
        )

        tokenizer_pt = tokenizer_pt.train_new_from_iterator(
            pt_iterator(),
            vocab_size=2 ** 13
        )
        tokenizer_en = tokenizer_en.train_new_from_iterator(
            en_iterator(),
            vocab_size=2 ** 13
        )

        return tokenizer_pt, tokenizer_en

    def encode(self, pt, en):
        """Encode translation sentence pairs."""
        pt = (
            [self.tokenizer_pt.vocab_size]
            + self.tokenizer_pt.encode(
                pt.numpy().decode("utf-8"),
                add_special_tokens=False
            )
            + [self.tokenizer_pt.vocab_size + 1]
        )

        en = (
            [self.tokenizer_en.vocab_size]
            + self.tokenizer_en.encode(
                en.numpy().decode("utf-8"),
                add_special_tokens=False
            )
            + [self.tokenizer_en.vocab_size + 1]
        )

        return pt, en

    def tf_encode(self, pt, en):
        """Wrap encoding for TensorFlow datasets."""
        pt, en = tf.py_function(
            self.encode,
            [pt, en],
            [tf.int64, tf.int64]
        )

        pt.set_shape([None])
        en.set_shape([None])

        return pt, en

    def filter_max_length(self, pt, en, max_len):
        """Filter sentence pairs exceeding maximum length."""
        return tf.logical_and(
            tf.size(pt) <= max_len,
            tf.size(en) <= max_len
        )
