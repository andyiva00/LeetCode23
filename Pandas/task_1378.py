# SOLUTION
#
# 1378. Replace Employee ID With The Unique Identifier
# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier

import pandas as pd


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    tmp_table_1 = employees.merge(
        employee_uni,
        left_on='id',
        right_on='id',
        how='left'
    )

    tmp_table_1 = tmp_table_1[['unique_id', 'name']]

    return tmp_table_1
