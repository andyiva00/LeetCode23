# SOLUTION
#
# 2886. Change Data Type
# https://leetcode.com/problems/change-data-type

import pandas as pd


def change_datatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade': 'int'})
