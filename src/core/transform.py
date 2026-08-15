# import yfinance as yf
import numpy as np


from .data_loader import fetch_data


def calc_log_returns(prices):
    """
    Receives the historical close data and transforms it to log returns

    Parameter:
    prices (DataFrame): The historical close price data with their corresponding market sectors

    Returns:
    log_returns (DataFrame): The log returns of the price data after removing any missing rows
    """

    log_returns = np.log(prices/prices.shift(1)).dropna()

    return log_returns