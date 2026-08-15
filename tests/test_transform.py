import numpy as np
import pandas as pd


from src.core.transform import calc_log_returns


def test_calc_log_returns():
    """Log returns should be calculated correctly from price data."""

    prices = pd.DataFrame({
        "AAPL": [100, 110, 121],
        "BTC-USD": [1000, 1100, 1210],
    })

    result = calc_log_returns(prices)

    print(result)

    expected_return = np.log(1.10)

    assert result.shape == (2, 2)
    assert np.isclose(result.iloc[0]["AAPL"], expected_return)
    assert np.isclose(result.iloc[1]["AAPL"], expected_return)
    assert np.isclose(result.iloc[0]["BTC-USD"], expected_return)
    assert np.isclose(result.iloc[1]["BTC-USD"], expected_return)







# from data_loader import fetch_data


# def calc_log_returns(prices):
#     """
#     Receives the historical close data and transforms it to log returns

#     Parameter:
#     prices (DataFrame): The historical close price data with their corresponding market sectors

#     Returns:
#     log_returns (DataFrame): The log returns of the price data after removing any missing rows
#     """

#     log_returns = np.log(prices/prices.shift(1)).dropna()

#     return log_returns


# if __name__ == "__main__":


#     # Define asset universe across 5 distinct economic classes
#     ASSET_UNIVERSE = {
#         'BTC-USD': 'Crypto', 
#         'ETH-USD': 'Crypto', 
#         'SOL-USD': 'Crypto',
#         'AAPL': 'Tech', 
#         'MSFT': 'Tech',
#         'JPM': 'Finance', 
#         'BAC': 'Finance',
#         'XOM': 'Energy', 
#         'CVX': 'Energy',
#         'WMT': 'Retail'
#         }


#     print()
#     # data = fetch_data(ASSET_UNIVERSE, "6mo")
#     # transformed_data = calc_log_returns(data)
#     # print(transformed_data)

#     test_calculate_log_returns()