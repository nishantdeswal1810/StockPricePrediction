import yfinance as yf
import os

# Define the stock ticker for Reliance Industries
ticker = "RELIANCE.NS"

# Download the stock price data for the last year
data = yf.download(ticker, period="1y", interval="1d")

# Create the data directory if it doesn't exist
data_dir = 'data/'
os.makedirs(data_dir, exist_ok=True)

# Save the data to a CSV file
data_file_path = os.path.join(data_dir, 'reliance_stock_data.csv')
data.to_csv(data_file_path)

print(f"Data collected and saved to {data_file_path}")
