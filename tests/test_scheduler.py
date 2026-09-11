import pandas as pd
from grid_carbon_intelligence.scheduler import choose_low_carbon_window, avoided_emissions

def test_window():
    idx = pd.date_range("2025-01-01", periods=4, freq="h")
    assert choose_low_carbon_window(pd.Series([400, 100, 120, 500], index=idx), 2) == idx[1]

def test_emissions():
    assert avoided_emissions(10, 500, 300) == 2000
