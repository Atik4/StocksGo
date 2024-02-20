import pandas as pd

# Read the CSV file
df = pd.read_csv('/Users/atik.agarwal/Projects/personal/trading/stock_utils/all_stocks_list.csv', nrows=1500)

filtered_df = df[df['MarketCap'] > 100000]

# Get the list of symbols
symbols_list = filtered_df['Symbol'].tolist()

print(f"Symbols with MarketCap > 100000: {symbols_list}")
