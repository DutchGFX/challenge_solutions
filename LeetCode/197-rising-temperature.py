import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    return weather[weather["temperature"].diff() > 0]["id"].to_frame()
