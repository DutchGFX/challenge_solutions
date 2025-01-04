import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the number of salaries in each category

    Notes
    -----
    Approach is to calculate LOW and HIGH, since they use a single logical,
    and then use the total count to deduce the number of entries in the AVG
    category
    """
    L = sum(accounts["income"] < 20000)
    H = sum(accounts["income"] > 50000)
    A = len(accounts) - L - H
    return pd.DataFrame({"category": ["Low Salary", "Average Salary", "High Salary"], "accounts_count": [L, A, H]})
