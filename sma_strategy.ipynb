import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. Data download
ticker = "AAPL"
data = yf.download(ticker, start="2020-01-01", end="2023-01-01")

# 2. SMA20 and SMA50 calculation
data["SMA20"] = data["Close"].rolling(window=20).mean()
data["SMA50"] = data["Close"].rolling(window=50).mean()

# 3. Signals generation (1 = long, 0 = out)
data["Signal"] = 0
data["Signal"][20:] = (data["SMA20"][20:] > data["SMA50"][20:]).astype(int)
data["Position"] = data["Signal"].shift(1)  # posizione effettiva dal giorno dopo

# 4. Daily returns
data["Return"] = data["Close"].pct_change()
data["Strategy_Return"] = data["Position"] * data["Return"]

# 5. Cumulative returns
data["Cumulative_BuyHold"] = (1 + data["Return"]).cumprod()
data["Cumulative_Strategy"] = (1 + data["Strategy_Return"]).cumprod()

# 6. Price plot + signals
plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Close Price", alpha=0.5)
plt.plot(data["SMA20"], label="SMA20", linewidth=1.2)
plt.plot(data["SMA50"], label="SMA50", linewidth=1.2)

# BUY signals
plt.plot(data[data["Position"] == 1].index, 
         data["SMA20"][data["Position"] == 1], 
         "^", markersize=8, color="g", label="Buy")

# SELL signals
plt.plot(data[data["Position"] == 0].index, 
         data["SMA20"][data["Position"] == 0], 
         "v", markersize=8, color="r", label="Sell")

plt.title(f"SMA Crossover Strategy on {ticker}")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# 7. Plot performance
plt.figure(figsize=(12,6))
plt.plot(data["Cumulative_BuyHold"], label="Buy & Hold", color="blue")
plt.plot(data["Cumulative_Strategy"], label="SMA Strategy", color="orange")
plt.title("Cumulative Returns")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.legend()
plt.show()
