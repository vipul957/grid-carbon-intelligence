"""Carbon-aware workload placement primitives."""
from __future__ import annotations
import pandas as pd

def choose_low_carbon_window(intensity: pd.Series, duration_hours: int) -> pd.Timestamp:
    """Return the start of the contiguous window with lowest mean intensity."""
    if duration_hours < 1 or duration_hours > len(intensity):
        raise ValueError("duration_hours must fit inside intensity")
    means = intensity.rolling(duration_hours).mean().dropna()
    end = means.idxmin()
    return intensity.index[intensity.index.get_loc(end) - duration_hours + 1]

def avoided_emissions(kwh: float, baseline_g_per_kwh: float, scheduled_g_per_kwh: float) -> float:
    """Compute avoided grams of CO2-equivalent."""
    return max(0.0, kwh * (baseline_g_per_kwh - scheduled_g_per_kwh))
