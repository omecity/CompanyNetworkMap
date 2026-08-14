import yfinance as yf


def fetch_data(asset, period):
    """
    Ingests historical close data

    Parameters:
    asset (dictionary): The asset symbols and their corresponding market sectors
    period (string): The length of past time to download from Yahoo Finance

    Returns:
    raw_data (DataFrame): The data of the asset by the period 
    """

    tickers = list(asset.keys())
    raw_data = yf.download(tickers, period=period)['Close']

    return raw_data