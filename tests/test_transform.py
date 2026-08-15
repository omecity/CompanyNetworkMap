import numpy as np
import pandas as pd


from src.core.transform import calc_log_returns


def test_calc_log_returns():
    """Log returns should be calculated correctly from price data."""

    prices = pd.DataFrame({
        "AAPL": [100, 110, 121],
        "BTC-USD": [1000, 1100, 1210]
    })

    result = calc_log_returns(prices)

    print(result)

    expected_return = np.log(1.10)

    assert result.shape == (2, 2)
    assert np.isclose(result.iloc[0]["AAPL"], expected_return)
    assert np.isclose(result.iloc[1]["AAPL"], expected_return)
    assert np.isclose(result.iloc[0]["BTC-USD"], expected_return)
    assert np.isclose(result.iloc[1]["BTC-USD"], expected_return)


def test_calc_log_returns_removes_first_row():
    """The first row should be removed because it has no previous price."""

    prices = pd.DataFrame({
        "AAPL": [100, 110, 120]
    })

    result = calc_log_returns(prices)

    assert len(result) == 2
    assert result.index.tolist() == [1, 2]