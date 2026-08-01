#!/usr/bin/env python3
"""
9. Transformer Encoder

This module implements the complete encoder component of the Transformer
architecture introduced in the paper "Attention Is All You Need"
(Vaswani et al., 2017).

The encoder is responsible for converting an input sequence of token IDs
into a sequence of contextualized vector representations. Unlike traditional
RNNs or LSTMs, every token is processed simultaneously while self-attention
allows each token to gather information from every other token in the
sequence.

The encoder performs the following operations:

1. Convert token IDs into dense embedding vectors.
2. Scale the embeddings by sqrt(dm) to stabilize the variance of the
   embedding vectors before positional information is added.
3. Add positional encodings so the model can distinguish the order of
   tokens, since self-attention itself is permutation invariant.
4. Apply dropout as a regularization technique.
5. Pass the sequence through N identical encoder blocks.
6. Return the final contextualized representation of every token.

Each EncoderBlock consists of:
    • Multi-head self-attention
    • Residual connection
    • Layer normalization
    • Position-wise feed-forward network
    • Residual connection
    • Layer normalization

The output produced by this encoder is later consumed by the decoder during
encoder-decoder attention.
"""

import tensorflow as tf

positional_encoding = __import__(
    '4-positional_encoding'
).positional_encoding
EncoderBlock = __import__(
    '7-transformer_encoder_block'
).EncoderBlock


class Encoder(tf.keras.layers.Layer):
    """
    Implements the Transformer Encoder.

    The encoder is composed of an embedding layer followed by positional
    encodings and a stack of identical EncoderBlocks.

    Parameters
    ----------
    N : int
        Number of encoder blocks.

    dm : int
        Dimensionality of the model.

    h : int
        Number of attention heads.

    hidden : int
        Number of neurons inside the feed-forward network.

    input_vocab : int
        Size of the input vocabulary.

    max_seq_len : int
        Maximum sequence length supported by the model.

    drop_rate : float
        Dropout probability.
    """

    def __init__(self, N, dm, h, hidden,
                 input_vocab, max_seq_len,
                 drop_rate=0.1):
        """Initialize the Transformer encoder."""
        super().__init__()

        self.N = N
        self.dm = dm

        self.embedding = tf.keras.layers.Embedding(
            input_vocab,
            dm
        )

        self.positional_encoding = positional_encoding(
            max_seq_len,
            dm
        )

        self.blocks = [
            EncoderBlock(dm, h, hidden, drop_rate)
            for _ in range(N)
        ]

        self.dropout = tf.keras.layers.Dropout(
            drop_rate
        )

    def call(self, x, training, mask):
        """
        Execute a complete forward pass through the Transformer encoder.

        The encoder first converts every token index into a dense embedding
        vector. These embeddings are multiplied by sqrt(dm), which is the
        scaling factor proposed in the original Transformer paper to prevent
        positional encodings from dominating the embeddings.

        Next, positional encodings are added so the network knows the
        absolute position of each token within the sequence.

        After dropout regularization, the sequence is passed sequentially
        through every encoder block. Each block progressively enriches the
        token representations by allowing every token to attend to every
        other token.

        Parameters
        ----------
        x : Tensor
            Shape:
                (batch_size, input_seq_len)

            Contains integer token IDs.

        training : bool
            Determines whether dropout layers should be active.

        mask : Tensor
            Optional padding mask used by the attention layers.

        Returns
        -------
        Tensor
            Shape:
                (batch_size, input_seq_len, dm)

            Contextualized representations for every input token.
        """
        seq_len = tf.shape(x)[1]

        x = self.embedding(x)
        x *= tf.math.sqrt(tf.cast(self.dm, tf.float32))

        x += self.positional_encoding[:seq_len]

        x = self.dropout(
            x,
            training=training
        )

        for block in self.blocks:
            x = block(
                x,
                training,
                mask
            )

        return x
