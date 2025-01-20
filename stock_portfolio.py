import yfinance as yf
import random

# List of stock tickers (for example purposes)
stock_tickers = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA', 'FB', 'NVDA', 'NFLX']

# Randomly pick 5 stocks
selected_stocks = random.sample(stock_tickers, 5)

# Fetch real-time data for selected stocks
stock_data = {}
for ticker in selected_stocks:
    stock = yf.Ticker(ticker)
    stock_info = stock.history(period="1d")  # Get latest stock data
    stock_data[ticker] = stock_info['Close'][0]  # Get the closing price

# Calculate portfolio value (assuming 1 share per stock)
total_value = sum(stock_data.values())

print("Selected Stocks and Prices:", stock_data)
print("Total Portfolio Value:", total_value)
