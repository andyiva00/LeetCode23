# SOLUTION
#
# 1873. Calculate Special Bonus
# https://leetcode.com/problems/calculate-special-bonus

import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda row: row.salary if row.employee_id % 2 != 0 and row['name'][:1] != 'M' else 0,
        axis=1
    )

    employees.sort_values(
        by='employee_id',
        inplace=True
    )

    return employees[['employee_id', 'bonus']]
