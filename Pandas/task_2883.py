# SOLUTION
#
# 2883. Drop Missing Data
# https://leetcode.com/problems/drop-missing-data

import pandas as pd


def drop_missing_data(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])
