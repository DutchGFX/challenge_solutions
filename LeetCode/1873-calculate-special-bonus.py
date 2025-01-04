import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # sort by employee ID
    employees.sort_values("employee_id", inplace=True)
    # figure out who gets a bonus
    get_bonus = (employees.employee_id % 2 == 1) & (~employees.name.str.startswith("M"))
    # calculate the bonus
    bonus = employees["salary"] * get_bonus
    # return the new DataFrame
    return pd.DataFrame({"employee_id": employees.employee_id, "bonus": bonus})
