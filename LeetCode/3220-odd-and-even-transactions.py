import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    # insert columns for odd and even amounts
    transactions['odd_sum'] = transactions['amount'] * (transactions['amount'] % 2)
    transactions['even_sum'] = transactions['amount'] * (1 - transactions['amount'] % 2)
    
    # groupby and return
    df = transactions.groupby('transaction_date').sum()[['odd_sum', 'even_sum']].reset_index()
    return df