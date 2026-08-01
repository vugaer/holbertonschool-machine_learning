#!/usr/bin/env python3
"""RNN Encoder for machine translation."""

import tensorflow as tf


class RNNEncoder(tf.keras.layers.Layer):
    """Encodes input sequences using a GRU."""

    def __init__(self, vocab, embedding, units, batch):
        """Initialize the encoder."""
        super().__init__()
        self.batch = batch
        self.units = units

        self.embedding = tf.keras.layers.Embedding(
            input_dim=vocab,
            output_dim=embedding
        )

        self.gru = tf.keras.layers.GRU(
            units,
            return_sequences=True,
            return_state=True,
            recurrent_initializer='glorot_uniform'
        )

    def initialize_hidden_state(self):
        """Initialize the hidden state with zeros."""
        return tf.zeros((self.batch, self.units))

    def call(self, x, initial):
        """Forward pass of the encoder."""
        x = self.embedding(x)
        outputs, hidden = self.gru(x, initial_state=initial)
        return outputs, hidden
