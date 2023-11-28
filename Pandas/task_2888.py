# SOLUTION
#
# 2888. Reshape Data: Concatenate
# https://leetcode.com/problems/reshape-data-concatenate

import pandas as pd


def concatenate_tables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat(objs=[df1, df2], ignore_index=True)
