# SOLUTION
#
# 2879. Display the First Three Rows
# https://leetcode.com/problems/display-the-first-three-rows

import pandas as pd


def select_first_rows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
