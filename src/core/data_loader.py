import yfinance as yf


from src.config.assets import ASSET


def fetch_data(period):
    """
    Ingests historical close data

    Parameters:
    period (string): The length of past time to download from Yahoo Finance

    Returns:
    raw_data (DataFrame): The data of the asset by the period 
    """

    tickers = list(ASSET.keys())
    raw_data = yf.download(tickers, period=period)['Close']

    return raw_data