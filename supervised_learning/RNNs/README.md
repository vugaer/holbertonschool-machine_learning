# Recurrent Neural Networks (RNNs)

This folder contains implementations and examples related to Recurrent Neural
Networks (RNNs) used in the unsupervised learning section of the
holbertonschool-machine_learning project.

Contents
- models/: RNN model implementations (vanilla RNN, LSTM, GRU) and
	utility functions for forward/backward passes.
- examples/: small scripts demonstrating usage, toy datasets, and
	training loops.
- tests/: unit tests validating shapes and basic numerical
	correctness of implementations.
- utils.py: helper functions for sequence batching, gradient clipping,
	and loss computation.

Quick start
1. Inspect an example in examples/ to see how datasets are prepared and
	 how models are instantiated.
2. Run a training script (Python 3.8+ recommended):

	 python examples/train_rnn.py

Notes
- Code is intentionally educational and minimal — not production tuned.
- Check tests/ for expected behaviors and small examples to validate
	changes after editing code.

References
- Goodfellow, Bengio, and Courville — "Deep Learning" (chapter on
	sequence modelling)
- PyTorch/TensorFlow official docs for production-ready RNN APIs

If you add or modify files here, update this README to reflect the change.
