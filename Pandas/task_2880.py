# SOLUTION
#
# 2880. Select Data
# https://leetcode.com/problems/select-data

import pandas as pd


def select_data(students: pd.DataFrame) -> pd.DataFrame:
    return students[students.student_id == 101][['name', 'age']]
