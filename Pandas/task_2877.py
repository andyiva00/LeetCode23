# SOLUTION - DONE
#
# 2877. Create a DataFrame from List
# https://leetcode.com/problems/create-a-dataframe-from-list

import pandas as pd
from typing import List


def create_dataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])
