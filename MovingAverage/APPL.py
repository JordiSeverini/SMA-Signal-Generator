import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Download historical market data for AAPL
df = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

# Focus on adjusted closing price for signal generation
df = df[["Close"]]

# Calculate short-term and long-term moving averages
# Used to identify trend direction and crossover points
df["SMA_SHORT"] = df["Close"].rolling(window=20).mean()
df["SMA_LONG"] = df["Close"].rolling(window=50).mean()

# Generate trading signals based on moving average crossover strategy
# Signal = 1 → bullish trend (short-term MA above long-term MA)
# Signal = 0 → bearish trend (short-term MA below long-term MA)
df["Signal"] = np.where(df["SMA_SHORT"] > df["SMA_LONG"], 1, 0)

# Identify changes in signal state to determine entry/exit points
# 1 → buy signal, -1 → sell signal
df["Position"] = df["Signal"].diff()

# Output latest computed values for validation
print(df.tail())