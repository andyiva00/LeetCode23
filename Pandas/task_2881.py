# SOLUTION
#
# 2881. Create a New Column
# https://leetcode.com/problems/create-a-new-column

import pandas as pd


def create_bonus_column(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda row: row.salary * 2,
        axis=1
    )
    return employees
