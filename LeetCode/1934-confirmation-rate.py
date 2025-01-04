import pandas as pd


def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    # replace with 1/0
    confirmations.replace({"timeout": 0, "confirmed": 1}, inplace=True)
    # calculate rates for each user, round to 2 decimals
    rates = confirmations.groupby("user_id").mean()[["action"]].round(2)
    # merge, rename, replace null
    out = signups[["user_id"]].merge(rates, on="user_id", how="outer")
    return out.rename(columns={"action": "confirmation_rate"}).fillna(0)
