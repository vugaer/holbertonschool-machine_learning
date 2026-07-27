# Time Series Forecasting

This directory contains a small time series project for predicting the
closing price of Bitcoin from historical Coinbase USD minute-level data.
The workflow preprocesses the raw data, creates fixed-width time windows,
and trains an LSTM model with TensorFlow/Keras.

## Learning Objectives

By the end of this project, you should be able to explain:

- What time series data is
- Why time series data must be split chronologically
- How to normalize train, validation, and test data without data leakage
- How sliding windows are used for sequence prediction
- How an LSTM can be used for one-step forecasting
- How to build a `tf.data.Dataset` from a pandas DataFrame

## Files

- `preprocess_data.py`: Loads the Bitcoin CSV file, removes missing values,
  splits the data into training, validation, and test sets, and normalizes all
  splits with the training set statistics.
- `forecast_btc.py`: Defines the `WindowGenerator` class, builds TensorFlow
  datasets, compiles an LSTM model, trains it, and evaluates it on validation
  and test data.

## Dataset

The preprocessing script expects the following CSV file:

```text
coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv
```

The file should contain Coinbase BTC/USD minute-level market data. The model
uses all numeric columns as input features and predicts the `Close` column.

Expected workflow:

1. Place the CSV file in the directory where the script will be executed.
2. Run the forecasting script from that same location, or update the CSV path
   in `preprocess_data.py`.

## Requirements

- Python 3
- pandas
- NumPy
- TensorFlow

Install the Python dependencies with:

```bash
pip install pandas numpy tensorflow
```

## Usage

From this directory, run:

```bash
python forecast_btc.py
```

The script will:

1. Load and clean the Bitcoin data.
2. Split the data into 70% training, 20% validation, and 10% testing sets.
3. Normalize the validation and test sets using only the training set mean and
   standard deviation.
4. Create 24-step input windows to predict the next `Close` value.
5. Train a small LSTM model.
6. Evaluate the model on validation and test datasets.

## Model Summary

The forecasting model is a simple sequential Keras model:

```text
LSTM(24) -> Dense(1)
```

It is trained with:

- Mean Squared Error loss
- Adam optimizer
- Mean Absolute Error metric
- Early stopping on validation loss

## Notes

- The project is educational and intentionally minimal.
- The data is split in chronological order to preserve the structure of the
  time series.
- Normalization statistics are computed only from the training data to avoid
  leaking information from the validation or test sets.
- Plotting code is included as comments in `preprocess_data.py` for optional
  data exploration.
