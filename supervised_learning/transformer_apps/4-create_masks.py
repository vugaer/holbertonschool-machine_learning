#!/usr/bin/env python3
"""Create attention masks for transformer training."""

import tensorflow as tf


def create_masks(inputs, target):
    """Create encoder and decoder attention masks."""
    encoder_mask = tf.cast(tf.math.equal(inputs, 0), tf.float32)
    encoder_mask = encoder_mask[:, tf.newaxis, tf.newaxis, :]

    decoder_mask = tf.cast(tf.math.equal(inputs, 0), tf.float32)
    decoder_mask = decoder_mask[:, tf.newaxis, tf.newaxis, :]

    seq_len = tf.shape(target)[1]
    look_ahead_mask = 1 - tf.linalg.band_part(
        tf.ones((seq_len, seq_len)),
        -1,
        0
    )

    target_padding_mask = tf.cast(
        tf.math.equal(target, 0),
        tf.float32
    )
    target_padding_mask = target_padding_mask[
        :, tf.newaxis, tf.newaxis, :
    ]

    combined_mask = tf.maximum(
        target_padding_mask,
        look_ahead_mask
    )

    return encoder_mask, combined_mask, decoder_mask
