#!/usr/bin/env python3
"""Positional encoding for a Transformer."""

import numpy as np


def positional_encoding(max_seq_len, dm):
    """Calculate the positional encoding."""
    pos = np.arange(max_seq_len)[:, np.newaxis]
    i = np.arange(dm)[np.newaxis, :]

    angles = pos / np.power(10000, (2 * (i // 2)) / dm)

    pe = np.zeros((max_seq_len, dm))
    pe[:, 0::2] = np.sin(angles[:, 0::2])
    pe[:, 1::2] = np.cos(angles[:, 1::2])

    return pe
