# SOLUTION
#
# 2884. Modify Columns
# https://leetcode.com/problems/modify-columns

import pandas as pd


def modify_salary_column(employees: pd.DataFrame) -> pd.DataFrame:
    return_data_frame = employees
    return_data_frame['salary'] = return_data_frame['salary'].multiply(2)
    return return_data_frame
