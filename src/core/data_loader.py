import yfinance as yf
import numpy as np


def fetch_data(asset, period):
    """
    Ingests historical close data and transforms it to log returns.

    Parameters:
    asset (dictionary): The asset symbols and their corresponding market sectors
    period (string): The length of past time to download from Yahoo Finance

    Returns:
    log_returns (DataFrame): The log returns of the asset by the period 
    """
    tickers = list(asset.keys())
    raw_data = yf.download(tickers, period=period)['Close']
    log_returns = np.log(raw_data/raw_data.shift(1)).dropna()

    return log_returns




if __name__ == "__main__":


    # Define asset universe across 5 distinct economic classes
    ASSET_UNIVERSE = {
        'BTC-USD': 'Crypto', 
        'ETH-USD': 'Crypto', 
        'SOL-USD': 'Crypto',
        'AAPL': 'Tech', 
        'MSFT': 'Tech',
        'JPM': 'Finance', 
        'BAC': 'Finance',
        'XOM': 'Energy', 
        'CVX': 'Energy',
        'WMT': 'Retail'
        }


    print()
    data = fetch_data(ASSET_UNIVERSE, "6mo")
    print(data)